from app.models import Producto
from mongoengine.errors import DoesNotExist
from app.alertas import stock_min
import json

def all_productos(sku):
    productos = []
    try:
        if sku:
            producto_db = Producto.objects(sku=sku).first()
            producto = Producto(sku=producto_db.sku, name=producto_db.name, stock=producto_db.stock, price=producto_db.price)
            productos.append(producto)
        else:
            productos_db = Producto.objects.all()
            for producto_db in productos_db:
                producto = Producto(sku=producto_db.sku, name=producto_db.name, stock=producto_db.stock, price=producto_db.price)
                productos.append(producto)
        return productos
    except DoesNotExist as e:
        return e
    
def new_producto(productos_data_list):
    ids = []
    for registro in productos_data_list:
        sku = registro.get("sku",None)
        name = registro.get("name",None)
        stock = registro.get("stock",100)
        price = registro.get("price",0.0)
        try:
            producto = Producto(sku=sku, name=name, stock=stock, price=price)
            producto.save()
            id = str(producto.id)
            ids.append({"storage":"SUCCESS", "_id":id})
        except Exception as e:
            ids.append({"storage":"ERROR", "sku":registro.sku})
    result = json.dumps(ids)  
    return {"result": result}

def update_producto(sku, data):
    try:
        producto = Producto.objects(sku=sku).first()
        if producto:
            nuevo_stock = producto.stock + data.stock
            producto.stock = nuevo_stock
            producto.save()
            id = str(producto.id)
            return {"update":"SUCCESS","_id":id} 
        else:
            return {"update":"ERROR","sku":sku} 
    except Exception as e:
            return {"update":"ERROR","error":e}

def sell_productos(sell_productos_list):
    ids = []
    for registro in sell_productos_list:
        #sku = registro.get("sku",None)
        sku = registro.sku
        #cantidad = registro.get("cantidad",0)
        cantidad = registro.cantidad
        try:
            producto = Producto.objects(sku=sku).first()
            if producto:
                nuevo_stock = producto.stock - cantidad
                if nuevo_stock < 0 :
                    ids.append({"update":"ERROR", "error": f"STOCK insuficiente en sku {sku}"})
                else:
                    producto.stock = nuevo_stock
                    producto.save()
                    id = str(producto.id)
                    if nuevo_stock < 10:
                        ids.append({"update":"SUCCESS", "_id":id, "alert": f"STOCK minimo en sku {sku}"})
                        stock_min(sku, nuevo_stock)
                    else:
                        ids.append({"update":"SUCCESS", "_id":id})
        except Exception as e:
            #ids.append({"update":"ERROR", "error":e})
            raise ValueError("Ha ocurrido un error") from e
    result = json.dumps(ids)  
    return {"result": result}
 
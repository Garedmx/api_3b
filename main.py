from fastapi import FastAPI, Query
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from app.controllers import all_productos, new_producto, update_producto, sell_productos
from app.connection import conectar

app = FastAPI()

conectar()

class ProductosData(BaseModel):
    sku: str
    name: str
    stock: Optional[int]
    price: Optional[float]

class ProductosStock(BaseModel):
    stock: int

class ProductosSell(BaseModel):
    sku: str
    cantidad: int


@app.get("/")
async def index():
    """
    Esta funcion da la bienvenida a la API, mostrando un pequeño resumen de que se puede hacer con la API_3B
    """
    steps= {
        "Paso 1": "Para ver la lista de productos, proporcione una consulta GET a la URL http://127.0.0.1:8000/api/products",
        "Paso 2": "Para crear un nuevo producto, proporcione una consulta POST a la URL http://127.0.0.1:8000/api/products",
        "Paso 3": "Para modificar el STOCK de un producto, proporcione una consulta PATCH a la URL http://127.0.0.1:8000/api/inventories/product/{sku} y en formanto JSON los atributos a actualizar",
        "Paso 4": "Para generar una orden de compra, proporcione una consulta POST a la URL http://127.0.0.1:8000/api/orders y en formato JSON los atributos de sku y cantidad"                                           
    }
    return {f"Hola Mundo": "Este es un sistema desarrollado como ejercicio para 3B por el puesto de Backend Developer", "Instrucciones": steps}


@app.get("/api/products", response_model=List[ProductosData])
async def get_productos(sku: str = Query(None, description="SKU especifico a consultar")):
    """
    Este endpoint regresa todo los productos almacenados en la Base de Datos.
    """
    result = all_productos(sku)
    return result

@app.post("/api/products")
async def post_productos(productos_data_list: List[Dict[Any, Optional[Any]]]):
    """
    Este endpoint crea un nuevo producto en la Base de Datos recibiendo una lisat de los nuevos productos:
    [
        {
            'sku':'SKU01', (requiered) 
            'name': 'Producto 1', (requiered)
            'stock': 100, (optional)
            'price': 10.25 (optional)
        },
        {
            'sku':'SKU02', (requiered) 
            'name': 'Producto 2', (requiered)
            'stock': 100, (optional)
            'price': 10.25 (optional)
        }
    ]
    """
    result = new_producto(productos_data_list)
    return result

@app.post("/api/inventroies/products/{sku}")
async def patch_producto(sku:str, data: ProductosStock):
    """
    Este endpoint nos permite agregar stock a un sku
    """
    result = update_producto(sku, data)
    return result

@app.post("/api/orders")
async def update_productos(sell_productos_list: List[ProductosSell]):
    """
    Este endpoint nos permite simular compras de productos restando el stock y detonando un JOB como alerta cuando el STOCK sea menor a 10
    """
    result = sell_productos(sell_productos_list)
    return result
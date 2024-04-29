from fastapi import FastAPI, Query
from typing import Optional, List, Dict
from pydantic import BaseModel
from app.controller import all_productos
import json

app = FastAPI()

class ProductosData(BaseModel):
    sku: str
    name: str
    stock:Optional[float]
    price: Optional[float]


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


@app.get("/api/products")
async def get_productos():
    result = all_productos()
    return result
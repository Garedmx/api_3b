from datetime import datetime, timedelta
from models import Producto
from mongoengine.errors import DoesNotExist
import requests
import json

def all_productos():
    try:
        productos = Producto.objects.get()
        return productos
    except DoesNotExist as e:
        return e
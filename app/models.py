from mongoengine import Document, StringField, IntField, FloatField

class Producto(Document):
    sku = StringField(required=True, unique=True)
    name = StringField(required=True)
    stock = IntField(required=False, default=100)
    price = FloatField(required=False, default=0.0)
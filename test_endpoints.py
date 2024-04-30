import requests

BASE_URL = "http://localhost:8000"

def test_post_productos():
    data = [
        {
            "sku": "SKU01",
            "name": "Producto_1",
            "stock": 100,
            "price": 10.5
        },
        {
            "sku": "SKU02",
            "name": "Producto_2",
            "price": 10.5
        },
        {
            "sku": "SKU03",
            "name": "Producto_3",
            "stock": 100
        },
        {
            "sku": "SKU04",
            "name": "Producto_4"
        }
    ]
    response = requests.post(f"{BASE_URL}/api/products", json=data)
    assert response.status_code == 200

def test_get_all_productos():
    response = requests.get(f"{BASE_URL}/api/products")
    assert response.status_code == 200

def test_get_productos():
    response = requests.get(f"{BASE_URL}/api/products?sku=SKU01")
    assert response.status_code == 200

def test_patch_producto():
    data = {
        "stock": 10
        }
    response = requests.post(f"{BASE_URL}/api/inventroies/products/SKU01", json=data)
    assert response.status_code == 200

def test_update_productos():
    data = [
        {
            "sku": "SKU01",
            "cantidad": 95
        },
        {
            "sku": "SKU02",
            "cantidad": 101
        },
        {
            "sku": "SKU03",
            "cantidad": 20
        }
    ]
    response = requests.post(f"{BASE_URL}/api/orders", json=data)
    assert response.status_code == 200
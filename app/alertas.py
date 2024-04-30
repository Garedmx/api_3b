from datetime import datetime
import os
import json

def stock_min(sku, nuevo_stock):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = "alertas.json"
    folder_path = "Log"
    
    json_data = {
         'fecha' : timestamp,
         'sku' : sku,
         'stock' : nuevo_stock
    }

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, filename)

    existing_data = {}

    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            existing_data = json.load(json_file)

    existing_data[timestamp] = json_data
 
    with open(file_path, "w") as json_file:
        json.dump(existing_data, json_file, indent=4)

    print(f"NUEVO REGISTRO EN LOG {timestamp}")
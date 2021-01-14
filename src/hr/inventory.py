import json

def inventory_read(filename):
    with open(filename, 'r') as f:
        return json.load(f)

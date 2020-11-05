import json


def ReadData(path = 'data/categories.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def get_product_by_id(product_id):
    products = ReadData('data/product.json')
    for p in products:
        if p['id'] == product_id:
            return p


def read_product(cat_id=None):
    products = ReadData('data/product.json')
    if cat_id:
        cat_id = int(cat_id)
        products = [p for p in products if p['category_id'] == cat_id]
    return products

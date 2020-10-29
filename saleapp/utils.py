import json


def ReadData(path = 'data/categories.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)
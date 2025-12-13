import json

def load_list(filename: str) -> list:
    with open(filename, 'r') as file:
        data = [line.strip() for line in file.readlines()]
        return json.loads(data[0])

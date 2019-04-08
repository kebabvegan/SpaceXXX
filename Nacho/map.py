import json


def serialization_map():
    with open("map.json", "w") as f:
        str = json.dumps(map_as)
        f.write(str)

def deserialization_map():
    with open("map.json", "r") as f:
        data = json.loads(f.read())
    return data

def desererialization_ressources():
    with open("ress.json", "r") as f:
        data = json.loads(f.read())
    return data

def serialization_ressources():
    with open("ress.json", "w") as f:
        str = json.dumps(ressources)

def get_ress(user):
    if user in ressources.keys():
        list = ressources[user]
    else:
        list = []
    return list

# def

map_as = deserialization_map()
ressources = desererialization_ressources()
print(ressources)
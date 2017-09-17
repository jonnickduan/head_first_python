import json


def entity2json(my_dict):
    my_json = json.dumps(my_dict)
    return my_json


def json2entity(json_data):
    my_dict = json.load(json_data)
    return my_dict

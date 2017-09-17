from suds.client import Client

from src.utils.data_transfer import entity2json

CRM_URL = "http://114.255.45.138:8896/JinYuanCRMInterface/CRMService?wsdl"  # CRM系统Services地址


def call_register_member(request_data):
    client = Client(CRM_URL)
    my_json = entity2json(request_data)
    client.service.RegisterMember(my_json)
    request_json = str(client.last_sent())
    response_json = str(client.last_received())
    return request_json,response_json


def call_other():
    pass

import requests
from typing import List
from models import GrowattUser, StringPVData
import os

BASE_URL = os.getenv('POWER_TRACK_API_URL', 'http://go_app:8080/api/v1')

def fetch_users() -> List[GrowattUser]:
    #enviar token para autenticar parser
    response = requests.get(f"{BASE_URL}/user-parser/growatt")
    response.raise_for_status()
    data = response.json()
    
    # Converte os dados brutos em objetos GrowattUser
    users = [GrowattUser(**user) for user in data]
    return users

def post_stringpv_data(data: List[StringPVData]):
    #Envia um lote de dados StringPV para a API.

    # Converte os objetos StringPVData para dicionários antes de enviar
    payload = [item.dict() for item in data]
    #enviar token para autenticar parser
    response = requests.post(f"{BASE_URL}/strings/batch", json=payload)
    response.raise_for_status()
    return response.json()
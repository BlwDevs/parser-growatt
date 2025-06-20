import requests
from typing import List
from models import GrowattUser, StringPVData
import os

BASE_URL = os.getenv('POWER_TRACK_API_URL', 'http://go_app:8080/api/v1')
HEADERS = {
    'Authorization': f"{os.getenv('POWER_TRACK_API_TOKEN', '0f64e10f9c29903fa6d08583a0f9711b2314351aa5cd35fe93e34a9656d70f67')}" # Inserir 'Bearer' Depois
}

def fetch_users() -> List[GrowattUser]:
    response = requests.get(f"{BASE_URL}/auth/growatt",headers=HEADERS)
    response.raise_for_status()
    data = response.json()
    
    # Converte os dados brutos em objetos GrowattUser
    users = [GrowattUser(**user) for user in data]
    print(f"Usuários obtidos: {users}")
    return users

def post_stringpv_data(data: List[StringPVData]):
    #Envia um lote de dados StringPV para a API.

    # Converte os objetos StringPVData para dicionários antes de enviar
    payload = [item.dict() for item in data]
    response = requests.post(f"{BASE_URL}/auth/batch", json=payload, headers=HEADERS)
    response.raise_for_status()
    return response.json()
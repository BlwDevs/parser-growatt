import requests
from typing import List
from models import GrowattUser, StringPVData
import os

BASE_URL = os.getenv('POWER_TRACK_API_URL', 'http://localhost:8080')

def fetch_users() -> List[GrowattUser]:
    response = requests.get(f"{BASE_URL}/userparser/growatt")
    response.raise_for_status()
    data = response.json()
    
    # Converte os dados brutos em objetos GrowattUser
    users = [GrowattUser(**user) for user in data["data"]]
    return users

def post_stringpv_data(user_id: int, data: List[StringPVData]):
    """
    Envia um lote de dados StringPV para a API.
    Args:
        user_id: ID do usuário
        data: Lista de dados StringPV para enviar em lote
    """
    # Converte os objetos StringPVData para dicionários antes de enviar
    payload = {
        "user_id": user_id,
        "batch": [pv_data.dict() for pv_data in data]
    }
    
    response = requests.post(f"{BASE_URL}/stringpv/batch", json=payload)
    response.raise_for_status()
    return response.json()
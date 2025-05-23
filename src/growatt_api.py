import requests
import hashlib
import time
import json
from typing import List
from models import GrowattUser, StringPVData
from datetime import datetime
import os

API_URL = os.getenv('GROWATT_API_URL', 'https://openapi.growatt.com/v4/new-api/queryLastData')

def sign_request(params: dict, secret: str):
    """
    Gera o hash 'sign' para autenticação.
    """
    # Exemplo simplificado
    payload = json.dumps(params, separators=(',', ':'))
    timestamp = int(time.time() * 1000)
    sign_str = f"{secret}{payload}{timestamp}"
    sign = hashlib.md5(sign_str.encode()).hexdigest()
    return sign, timestamp

def get_last_data(user: GrowattUser) -> List[StringPVData]:
    """
    Faz a requisição à Growatt e converte a resposta para objetos StringPVData.
    Processa os dados das strings fotovoltaicas do inversor.
    """
    string_data = []

    params = {
        "deviceSn": user.sn,
        "deviceType": user.device_type,
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': user.api_token,
    }

    response = requests.post(API_URL, headers=headers, data=params)
    response.raise_for_status()
    
    # Obtém os dados do primeiro inversor da lista
    raw_data = response.json()["data"][user.device_type][0]
    timestamp = datetime.strptime(raw_data["time"], "%Y-%m-%d %H:%M:%S")

    # Processa os dados das strings (considerando até 4 strings possíveis)
    for i in range(1, user.stringsNum+1):
        vpv = raw_data.get(f"vpv{i}", 0.0)
        ipv = raw_data.get(f"ipv{i}", 0.0)
        ppv = raw_data.get(f"ppv{i}", 0.0)
        
        # Só adiciona se houver dados válidos na string
        if vpv > 0 or ipv > 0 or ppv > 0:
            string_data.append(
                StringPVData(
                    timestamp=timestamp,
                    index=1, # índice fixo para o inversor *por enquanto*
                    string_number=i,
                    ppv=float(ppv),
                    ipv=float(ipv),
                    vpv=float(vpv),
                    inverter_id=user.inverter_id
                )
            )
    
    return string_data
    
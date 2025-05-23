from pydantic import BaseModel
from datetime import datetime

from typing import Optional


class StringPVData(BaseModel):
    timestamp: datetime
    index: int
    string_number: int
    ppv: float
    ipv: float
    vpv: float
    inverter_id: int

class GrowattUser(BaseModel):
    id: int #id do UserParserInverter
    api_token: str # token para acessar a API da Growatt
    sn: str # serial number do inversor
    device_type: str # tipo do dispositivo
    inverter_id: int  # mapeado previamente
    growatt_token: str  # token para acessar a API da Growatt
    stringsNum: int  # número de strings do inversor
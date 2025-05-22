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
    id: int
    api_token: str
    sn: str
    device_type: str
    inverter_id: int  # mapeado previamente
    growatt_token: str  # token para acessar a API da Growatt
import schedule
import time
from src.power_track_api import fetch_users, post_stringpv_data
from src.growatt_api import get_last_data
from models import GrowattUser, StringPVData
from typing import List

def job():
    users: List[GrowattUser] = fetch_users()

    for user in users:
        try:
            growatt_data: List[StringPVData] = get_last_data(user)
            post_stringpv_data(growatt_data)
        except Exception as e:
            print(f"Erro com o usuário {user.id}: {str(e)}")

def schedule_job():
    schedule.every(5).minutes.do(job)
    print("Worker iniciado, executando a cada 5 minutos...")

    while True:
        schedule.run_pending()
        time.sleep(1)
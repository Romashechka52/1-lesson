import logging
from datetime import date

logging.basicConfig(level=logging.INFO)

today = date.today()
logging.info(f"Поточна дата: {today}")

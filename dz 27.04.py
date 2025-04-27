import sqlite3
import requests
from datetime import datetime

conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime TEXT,
    temperature REAL
)
''')

latitude = 50.4501
longitude = 30.5234
url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'

response = requests.get(url)
data = response.json()

temperature = data['current_weather']['temperature']
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

cursor.execute('INSERT INTO weather_data (datetime, temperature) VALUES (?, ?)', (now, temperature))
conn.commit()
conn.close()

print(f"Дані збережено: {now} - {temperature}°C")

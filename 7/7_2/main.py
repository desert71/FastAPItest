from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()
# Внешний API URL
EXTERNAL_API_URL = 'https://catfact.ninja/fact'

# Функция для получения данных из внешнего API
def fetch_data_from_api():
    response = requests.get(EXTERNAL_API_URL)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        raise HTTPException(status_code=418, detail="Не подлючилося")

# Функция для обработки данных
def process_data(data:dict):
    # какая-то логика обработки данных
    new_data = {}
    # for key, value in data.items():
    #     new_data[key.upper()] = value.upper()
    return data #new_data

# Путь, который извлекает и обратывает данные от внешнего API
@app.get('/data/')
async def get_and_process_data():
    data: dict = fetch_data_from_api()
    if data:
        return process_data(data)
    else:
        return {"error": "Не получилось подключиться к внешнему API"}
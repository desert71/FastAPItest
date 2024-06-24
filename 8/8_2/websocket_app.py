import logfire
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()
logfire.configure()
logfire.instrument_fastapi(app)

# Список для хранения подключенных WebSocket клиентов
connection_clients: List[WebSocket] = []

# WebSocket путь для обработки WebSocket подключений
@app.websocket('/ws/')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connection_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        connection_clients.remove(websocket)

@app.get('/broadcast/')
async def broadcast_message(message: str):
    for client in connection_clients:
        await client.send_text(f"Broadcast message: {message}")
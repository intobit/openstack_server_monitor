import asyncio
from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect
from backend.api.datacollection import DataCollection


server_app = FastAPI()


async def send_server_data_list(websocket: WebSocket):
    while True:
        data = DataCollection()
        server_data = data.get_server_data()
        await websocket.send_json(server_data)
        await asyncio.sleep(5)


@server_app.websocket("/ws_server")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        await send_server_data_list(websocket)
    except WebSocketDisconnect:
        print("Server WebSocket disconnected")
    except Exception as e:
        print(f"Unexpected error: {e}")




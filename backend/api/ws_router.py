import asyncio
from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect
from backend.api.datacollection import DataCollection


router_app = FastAPI()


async def send_router_data_list(websocket: WebSocket):
    while True:
        data = DataCollection()
        router_data = data.get_router_data()
        await websocket.send_json(router_data)
        await asyncio.sleep(5)


@router_app.websocket("/ws_router")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        await send_router_data_list(websocket)
    except WebSocketDisconnect:
        print("Router WebSocket disconnected")
    except Exception as e:
        print(f"Unexpected error: {e}")

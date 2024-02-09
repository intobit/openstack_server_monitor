import multiprocessing
import os


def run_server(script_name, app_name, port):
    os.system(f"uvicorn {script_name}:{app_name} --host 0.0.0.0 --port {port} --log-level info --reload")


if __name__ == "__main__":

    processes = [multiprocessing.Process(target=run_server, args=("backend.api.ws_server", "server_app", 8000)),
                 multiprocessing.Process(target=run_server, args=("backend.api.ws_router", "router_app", 8001))]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

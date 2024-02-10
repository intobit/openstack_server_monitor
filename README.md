# Openstack Server Monitor
Little project for university. The main goal was to request data from the servers and router by calling different endpoint routes. 
[FastAPI](https://fastapi.tiangolo.com/advanced/websockets/) websockets were used to send data to two different localhost ports (8000, 8001). The websockets running 
simultaneously by using multiprocessing. The framework [React](https://react.dev/) was used to present the data at [localhost:3000](http://localhost:3000). For the Accordion to display server and router data,
[React Bootstrap](https://react-bootstrap.netlify.app/) was used. With [React MaterialUI](https://mui.com/) the active status as a chart was implemented.

## Usage
Configure your vpn for connecting to network where servers are running.

### Backend
Install dependencies:
```
pip install -r requirements.txt
```

Add your credentials for openstack api in `credentialsdata.py`

```
cd ../backend/authentication/

class CredentialData(Enum):
    ID = ""
    NAME = ""
    SECRET = ""
```

Start the backend to fetch data from servers and router, as well as the [Uvicorn](https://www.uvicorn.org/) servers, which runs the websocket at port 8000 and 8001.

```
python3 main.py
```

If you have no [Uvicorn](https://www.uvicorn.org/) on your machine, or [FastAPI](https://fastapi.tiangolo.com/advanced/websockets/) is missing the websockets, run the following command.

```
pip install fastapi uvicorn websockets
```

### Frontend

Switch to `frontend` directory and install dependencies.

```
cd frontend

npm install
```

Start the frontend with:

```
npm start
```

The frontend will be available at [http://localhost:3000](http://localhost:3000).


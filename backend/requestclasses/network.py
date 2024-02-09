import requests as req
from backend.requestclasses.endpoints import EndPoints


class Network:
    def __init__(self, auth_headers: dict):
        self.headers = auth_headers
        self.network_url = EndPoints.NETWORK.value
        self.ports = EndPoints.N_PORTS.value
        self.floatingips = EndPoints.N_FLOATINGIPS.value
        self.routers = EndPoints.N_ROUTERS.value
        self.subnets = EndPoints.N_SUBNETS.value
        self.networks = EndPoints.N_NETWORKS.value

    def _make_request(self, endpoint) -> dict:
        try:
            resp = req.request('GET', self.network_url + endpoint, headers=self.headers)
            resp.raise_for_status()
            data = resp.json()
            return data
        except req.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return {}

    def all_ports(self) -> dict:
        return self._make_request(self.ports)["ports"]

    def all_floatingips(self) -> dict:
        return self._make_request(self.floatingips)["floatingips"]

    def all_routers(self) -> dict:
        return self._make_request(self.routers)["routers"]

    def all_subnets(self) -> dict:
        return self._make_request(self.subnets)["subnets"]

    def all_networks(self) -> dict:
        return self._make_request(self.networks)["networks"]

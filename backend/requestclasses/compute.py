import requests as req
from backend.requestclasses.endpoints import EndPoints


class Compute:
    def __init__(self, auth_headers: dict):
        self.headers = auth_headers
        self.compute_url = EndPoints.COMPUTE.value
        self.servers = EndPoints.C_SERVERS.value
        self.flavors = EndPoints.C_FLAVORS.value

    def _make_request(self, endpoint) -> dict:
        try:
            resp = req.request('GET', self.compute_url + endpoint, headers=self.headers)
            resp.raise_for_status()
            data = resp.json()
            return data
        except req.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return {}

    def all_servers(self) -> dict:
        return self._make_request(self.servers)["servers"]

    def all_servers_detail(self) -> dict:
        return self._make_request(self.servers + EndPoints.C_SERVERS_DETAIL.value)["servers"]

    def all_flavors(self) -> dict:
        return self._make_request(self.flavors)["flavor"]

    def set_id_flavors(self, value_id) -> dict:
        id_url = "/" + str(value_id)
        return self._make_request(self.flavors + id_url)["flavor"]

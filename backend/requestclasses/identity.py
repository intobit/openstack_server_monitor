import requests as req
from backend.requestclasses.endpoints import EndPoints


class Identity:
    def __init__(self, json: dict):
        self.end_id = EndPoints.IDENTITY.value
        self.token_url = EndPoints.TOKEN_URL.value
        self.json = json
        self.headers = EndPoints.HEADERS.value

    def auth_token(self) -> dict:
        try:
            resp = req.request('POST', self.end_id + self.token_url, json=self.json, headers=self.headers)
            auth_token = resp.headers["x-subject-token"]
            auth_headers = { "X-Auth-Token" : auth_token }
            return auth_headers
        except req.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return {}

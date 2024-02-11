class Credentials:
    def __init__(self, set_id: str, name: str, secret: str, json: dict):
        self._id = set_id
        self._name = name
        self._secret = secret
        self._json = json

    @property
    def json(self) -> dict:
        return self._json

    @json.setter
    def json(self, value):
        set_id, name, secret = value
        self._json = {
            "auth": {
                "identity": {
                    "methods": [
                        "application_credential"
                    ],
                    "application_credential": {
                        "id": set_id,
                        "name": name,
                        "secret": secret
                    }
                }
            }
        }

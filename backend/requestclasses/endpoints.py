from enum import Enum


class EndPoints(Enum):
    IDENTITY = 'https://os2020.fh-joanneum.at:5000/v3'
    TOKEN_URL = '/auth/tokens'
    HEADERS = {"Content-Type": "application/json"}

    COMPUTE = "https://os2020.fh-joanneum.at:8774/v2.1"
    C_SERVERS = "/servers"
    C_SERVERS_DETAIL = "/detail"
    C_FLAVORS = "/flavors"

    NETWORK = " https://os2020.fh-joanneum.at:9696/v2.0"
    N_PORTS = "/ports"
    N_FLOATINGIPS = "/floatingips"
    N_ROUTERS = "/routers"
    N_SUBNETS = "/subnets"
    N_NETWORKS = "/networks"

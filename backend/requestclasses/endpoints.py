from enum import Enum


class EndPoints(Enum):
    IDENTITY = ""
    TOKEN_URL = "/auth/tokens"
    HEADERS = {"Content-Type": "application/json"}

    COMPUTE = ""
    C_SERVERS = "/servers"
    C_SERVERS_DETAIL = "/detail"
    C_FLAVORS = "/flavors"

    NETWORK = ""
    N_PORTS = "/ports"
    N_FLOATINGIPS = "/floatingips"
    N_ROUTERS = "/routers"
    N_SUBNETS = "/subnets"
    N_NETWORKS = "/networks"

import json

from backend.authentication.credentials import Credentials
from backend.authentication.credentialsdata import CredentialData
from backend.requestclasses.compute import Compute
from backend.requestclasses.identity import Identity
from backend.requestclasses.network import Network


class DataCollection:
    def __init__(self):
        self.credentials = Credentials(set_id="", name="", secret="", json={})
        self.credentials.json = (CredentialData.ID.value, CredentialData.NAME.value, CredentialData.SECRET.value)
        self.identity = Identity(self.credentials.json)
        self.compute = Compute(self.identity.auth_token())
        self.network = Network(self.identity.auth_token())

    def get_server_data(self) -> list[dict]:
        get_servers_detail = self.compute.all_servers_detail()
        get_flavor_ids = self.compute.set_id_flavors
        return self._process_server_data(get_servers_detail, get_flavor_ids)

    def get_router_data(self) -> list[dict]:
        get_routers = self.network.all_routers()
        get_ports = self.network.all_ports()
        get_networks = self.network.all_networks()
        get_subnets = self.network.all_subnets()
        return self._process_router_data(get_routers, get_ports, get_networks, get_subnets)

    @staticmethod
    def _process_server_data(all_servers, all_flavor_ids):

        lst_server_data = []

        for server in all_servers:
            server_data = {}
            server_data["id"] = server["id"]
            server_data["name"] = server["name"]
            if server["status"] == 'ACTIVE':
                server_data["active_status"] = True
            else:
                server_data["active_status"] = False
            if isinstance(server["image"], dict):
                server_data["image_id"] = server["image"]["id"]
            else:
                server_data["image_id"] = server["image"]
            server_data["flavor_id"] = next(iter(server["flavor"].values()))
            server_data["flavor_info"] = {"ram": "", "vcpus": "", "disk": ""}
            server_data["networkname"] = next(iter(server["addresses"]))
            server_data["address"] = server["addresses"][server_data["networkname"]][0].get("addr")
            server_data["created_at"] = server["created"]
            server_data["updated_at"] = server["updated"]

            # Add flavor information based on flavor id to every server
            flavor_id = all_flavor_ids(server_data["flavor_id"])
            server_data["flavor_info"]["ram"] = flavor_id["ram"]
            server_data["flavor_info"]["vcpus"] = flavor_id["vcpus"]
            server_data["flavor_info"]["disk"] = flavor_id["disk"]

            json.dumps(server_data)
            lst_server_data.append(server_data)

        return lst_server_data

    @staticmethod
    def _process_router_data(all_routers, all_ports, all_networks, all_subnets):

        lst_router_data = []

        for router in all_routers:
            router_data = {}
            router_data["id"] = router["id"]
            router_data["name"] = router["name"]
            if router["status"] == 'ACTIVE':
                router_data["active_status"] = True
            else:
                router_data["active_status"] = False
            router_data["created_at"] = router["created_at"]
            router_data["updated_at"] = router["updated_at"]

            # Add port information
            ports = all_ports
            router_data_ports = []
            for port in ports:
                if port["device_id"] == router_data["id"]:
                    port_data = {
                        "id": port["id"],
                        "name": port["name"],
                        "active_status": port["status"],
                        "network_id": port["network_id"],
                        "fixed_ips": port["fixed_ips"][0]["ip_address"],
                    }
                    if port_data["active_status"] == 'ACTIVE':
                        port_data["active_status"] = True
                    else:
                        port_data["active_status"] = False
                    router_data_ports.append(port_data)
            router_data["ports"] = router_data_ports

            # Add network information
            networks = all_networks
            for port in router_data["ports"]:
                for network in networks:
                    if port["network_id"] == network["id"]:
                        port["subnet_id"] = network["subnets"][0]
                        port["network_name"] = network["name"]

            # Add subnet information
            subnets = all_subnets
            for port in router_data["ports"]:
                for subnet in subnets:
                    if port["subnet_id"] == subnet["id"]:
                        port["cidr"] = subnet["cidr"]

            json.dumps(router_data)
            lst_router_data.append(router_data)

        return lst_router_data

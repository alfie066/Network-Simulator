import random

from port import Port


class NetworkDevice:

    def __init__(self, name, number_of_ports):
        if number_of_ports < 1:
            raise ValueError("A network device must have at least one port.")

        self.name = name
        self.mac_address = self.generate_mac_address()

        self.ports = []

        for port_number in range(number_of_ports):
            port = Port(self, f"eth{port_number}")
            self.ports.append(port)

    def generate_mac_address(self):
        return ":".join(
            f"{random.randint(0, 255):02x}"
            for _ in range(6)
        )

    def get_port(self, port_name):
        for port in self.ports:
            if port.name == port_name:
                return port

        raise ValueError(
            f"{self.name} does not have a port named {port_name}."
        )

    def show_ports(self):
        for port in self.ports:
            print(port)

    def __str__(self):
        return (
            f"{self.__class__.__name__}: {self.name}, "
            f"MAC address: {self.mac_address}, "
            f"Ports: {len(self.ports)}"
        )
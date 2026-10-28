from network_device import NetworkDevice


class Switch(NetworkDevice):

    def __init__(self, name, number_of_ports):
        super().__init__(name, number_of_ports)
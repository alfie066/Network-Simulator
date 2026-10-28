from network_device import NetworkDevice


class EndDevice(NetworkDevice):

    def __init__(self, name, number_of_ports):
        super().__init__(name, number_of_ports)
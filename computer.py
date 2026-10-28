from end_device import EndDevice


class Computer(EndDevice):

    def __init__(self, name, number_of_ports=1):
        super().__init__(name, number_of_ports)
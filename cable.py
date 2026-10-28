class Cable:

    next_cable_number = 1

    def __init__(self):
        self.cable_id = f"cable{Cable.next_cable_number}"
        Cable.next_cable_number += 1

        self.port1 = None
        self.port2 = None

    def connect(self, port1, port2):
        if port1 is port2:
            raise ValueError("A cable cannot connect a port to itself.")

        if port1.is_connected():
            raise ValueError(
                f"{port1.device.name}:{port1.name} is already connected."
            )

        if port2.is_connected():
            raise ValueError(
                f"{port2.device.name}:{port2.name} is already connected."
            )

        self.port1 = port1
        self.port2 = port2

        port1.cable = self
        port2.cable = self

    def disconnect(self):
        if self.port1 is not None:
            self.port1.cable = None

        if self.port2 is not None:
            self.port2.cable = None

        self.port1 = None
        self.port2 = None

    def get_other_port(self, current_port):
        if current_port is self.port1:
            return self.port2

        if current_port is self.port2:
            return self.port1

        raise ValueError("The specified port is not connected to this cable.")

    def __str__(self):
        if self.port1 is None or self.port2 is None:
            return f"{self.cable_id} - disconnected"

        return (
            f"{self.cable_id}: "
            f"{self.port1.device.name}:{self.port1.name} <--> "
            f"{self.port2.device.name}:{self.port2.name}"
        )
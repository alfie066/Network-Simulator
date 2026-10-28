class Port:

    def __init__(self, device, name):
        self.device = device
        self.name = name
        self.cable = None

    def is_connected(self):
        return self.cable is not None

    def __str__(self):
        if self.cable is None:
            return f"{self.device.name}:{self.name} - disconnected"

        return f"{self.device.name}:{self.name} - connected to {self.cable.cable_id}"
from computer import Computer
from switch import Switch
from ethernet_cable import EthernetCable


computer1 = Computer("PC1")
computer2 = Computer("PC2")

switch1 = Switch("SW1", 4)

cable1 = EthernetCable()
cable2 = EthernetCable()

cable1.connect(
    computer1.get_port("eth0"),
    switch1.get_port("eth0")
)

cable2.connect(
    computer2.get_port("eth0"),
    switch1.get_port("eth1")
)

print(computer1)
print(computer2)
print(switch1)

print()

print(cable1)
print(cable2)

print()

computer1.show_ports()
computer2.show_ports()
switch1.show_ports()
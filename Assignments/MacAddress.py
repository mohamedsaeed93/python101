class MacAddress:
    def __init__(self, mac_address):
        if isinstance(mac_address, str):
            self.address = int(mac_address.replace(':', ''), 16)
        elif isinstance(mac_address, int):
            self.address = mac_address
        else:
            self.address = mac_address.address

    def __add__(self, address_value):
        return MacAddress(self.address + MacAddress(address_value).address)

    def __str__(self):
        return ':'.join(
            [str(hex(self.address)[2:])[i:i + 2] for i, j in enumerate(str(hex(self.address))[2:]) if not (i % 2)])
        # works only with python2
        # return ':'.join(s.encode('hex') for s in str(hex(self.address))[2:].decode('hex'))


address1 = MacAddress("A6:C2:D5:C6:89:AB")
address2 = MacAddress(0xa6c2d5c689ab)
address3 = MacAddress(183355740424619)

print("Address 1 : {}".format(address1))
print("Address 2 : {}".format(address2))
print("Address 3 : {}".format(address3))
print("-------------------------------------------")
address1new = address1 + 10
print("Address 1 after addition : {}".format(address1new))

address2new = address2 + 10
print("Address 2 after addition : {}".format(address2new))

address3new = address3 + 10
print("Address 3 after addition : {}".format(address3new))

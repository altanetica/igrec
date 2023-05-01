import netaddr


class IpAddr(object):
    def __init__(self, address):
        try:
            self._ip = netaddr.IPAddress(address, 4)
        except netaddr.AddrFormatError:
            raise ValueError

    def to_int(self):
        return self._ip.__int__()

    def to_str(self):
        return str(self._ip)

    def __int__(self):
        return self.to_int()

import netaddr


class MacAddr(object):
    def __init__(self, address):
        try:
            self._mac = netaddr.EUI(address)
            self._mac.dialect = netaddr.mac_unix_expanded
            self._mac.__str__()
            if self._mac.__str__() == '00:00:00:00:00:00' or self._mac.__str__() == 'ff:ff:ff:ff:ff:ff':
                raise ValueError
        except (netaddr.AddrFormatError, netaddr.AddrConversionError, IndexError):
            raise ValueError

    def to_str(self):
        return self._mac.__str__()

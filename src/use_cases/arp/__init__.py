from pyroute2.iproute.linux import IPRoute
from src.settings import GlobalConfig

ipr = IPRoute()
config = GlobalConfig()
iface = ipr.link_lookup(ifname=config.get_config('local.interfaces.internal'))[0]

_STATES_ = {'None': 0,
            'INCOMPLETE': 1,
            'REACHABLE': 2,
            'STALE': 4,
            'DELAY': 8,
            'PROBE': 16,
            'FAILED': 32,
            'NOARP': 64,
            'PERMANENT': 128,
            }

VALID_MAC_STATES = (2, 4, 8, 128)

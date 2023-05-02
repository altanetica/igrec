from pyroute2.ipset import IPSet
from src.settings import GlobalConfig

ips = IPSet()
config = GlobalConfig()

from . import add, remove, flush, enable, disable, load, check, list, status, counters, test, save

from pyroute2.ipset import IPSet
from src.settings import GlobalConfig


config = GlobalConfig()
ips = IPSet()

from . import add, remove, flush, enable, disable, load, check, list, status, counters, test, save

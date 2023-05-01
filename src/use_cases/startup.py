def load_arp(ifname, fn):
    import json
    from pyroute2.iproute import IPRoute
    ipr = IPRoute()
    iface = ipr.link_lookup(ifname=ifname)[0]
    with open(fn) as f:
        try:
            data = json.load(f)
            for obj in data:
                ipr.neigh('append', ifindex=iface,
                          lladdr=obj['mac'],
                          dst=obj['ip'],
                          nud='permanent')
        except (IOError, ValueError):
            pass
        finally:
            f.close()

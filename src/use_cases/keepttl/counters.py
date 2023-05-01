from src.interfaces.zeromq.shared.dataobject import DataObject
import subprocess


def ipset_read():
    from . import config
    try:
        proc = subprocess.Popen(['/usr/sbin/ipset', 'list', config.get_config('ipset.keepttl'), '--terse'], shell=False, stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if line != '':
                if ': ' in line:
                    key, value = line.split(': ')
                    if key == 'Number of entries':
                        return int(value.strip())
            else:
                break
        return 0
    except OSError:
        return 0


def process_request():
    resp = DataObject()
    count = ipset_read()
    resp.add_data({'count': count})
    return resp


def execute(data):
    """
    :param data:
    :type data: DataObject
    """
    if not isinstance(data, DataObject):
        raise ValueError
    resp = process_request()
    for err in data.errors:
        resp.add_error(err.param, err.message)
    return resp


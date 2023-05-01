from src.interfaces.zeromq.shared.dataobject import DataObject


def process_request():
    from . import config
    import subprocess
    resp = DataObject()
    fn = '/etc/ipset.keepttl'
    try:
        process = subprocess.Popen(["/sbin/ipset", "save", config.get_config('ipset.keepttl')],
                                   universal_newlines=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
        (output, err) = process.communicate()
        with open(fn, 'w') as f:
            try:
                f.writelines(output)
            finally:
                f.close()
    except (subprocess.CalledProcessError, OSError, ValueError, IOError), e:
        pass
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

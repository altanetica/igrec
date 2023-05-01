import logging
import threading
import importlib
from src.settings import GlobalConfig
from zeromq import zeromq_push_pull as pp
from zeromq import zeromq_request_response as rr
from rabbitmq.rabbitmqasynchronous import RabbitMQAsynchronous
from src.interfaces.zeromq.shared.requestobject import RequestObject
from src.interfaces.zeromq.shared.responseobject import ResponseSuccess, ResponseFail


MODULES = ('app', 'whitelist', 'auth', 'keepttl', 'arp',
           'shaper', 'ratelimit', 'dhcp', 'dnat')
ACTIONS = ('add', 'remove', 'flush', 'enable', 'disable', 'load',
           'check', 'list', 'status', 'counters', 'test', 'save')


# calling use case without answer needed
def controller(req):
    """
    :param req:
    :type req: RequestObject
    """
    if not isinstance(req, RequestObject):
        logging.warn("Request is invalid")
        return

    if req.module_ not in MODULES:
        logging.warn(req.module_ + " not in module list")
        return

    if req.action not in ACTIONS:
        logging.warn(req.action + " not in action list")
        return

    use_case = "." + req.action
    pkg = "src.use_cases." + req.module_
    try:
        m = importlib.import_module(use_case, pkg)
        getattr(m, "execute")(req.data)
    except (ImportError, AttributeError, TypeError, ValueError), e:
        logging.warn(e)
    except NotImplementedError, e:
        logging.warn(e)
    # other Exceptions
    # todo: add excepts
    pass


# calling use case and return answer
def informer(req):
    """
    :param req:
    :type req: RequestObject
    """
    if not isinstance(req, RequestObject):
        logging.warn("Request is invalid")
        return ResponseFail(req, "Request is invalid")

    if req.module_ not in MODULES:
        logging.warn(req.module_ + " not in module list")
        return ResponseFail(req.module_, "Not in module list")

    if req.action not in ACTIONS:
        return ResponseFail(req.action, "Not in action list")

    use_case = "." + req.action
    pkg = "src.use_cases." + req.module_
    try:
        m = importlib.import_module(use_case, pkg)
        resp = getattr(m, "execute")(req.data)
    except (ImportError, AttributeError, TypeError, ValueError), e:
        logging.warn(e)
        return ResponseFail(req.module_ + "." + req.action, e)
    except NotImplementedError, e:
        logging.warn(e)
        return ResponseFail(req.module_ + "." + req.action, "Not implement")
    # other Exceptions
    # todo: add excepts

    return ResponseSuccess(resp)


# start listeners as threads
def run():
    threads = []
    config = GlobalConfig()
    if config.get_config('rpc.zeromq.enabled'):
        thread = threading.Thread(target=pp.run, args=[controller])
        thread.setDaemon(True)
        threads.append(thread)
        thread = threading.Thread(target=rr.run, args=[informer])
        thread.setDaemon(True)
        threads.append(thread)
    if config.get_config('rpc.rabbitmq.enabled'):
        rt = RabbitMQAsynchronous(cb=informer)
        threads.append(rt)
    try:
        for thread in threads:
            logging.error('start thread')
            thread.start()
        logging.warn("RPC threads started")
        return threads
    except Exception, e:
        logging.exception(e)

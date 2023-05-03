import logging
import threading
import importlib
from src.settings import GlobalConfig
from src.interfaces.zeromq import zeromq_push_pull as pp
from src.interfaces.zeromq import zeromq_request_response as rr

from src.interfaces.zeromq.shared.requestobject import RequestObject
from src.interfaces.zeromq.shared.responseobject import ResponseSuccess, ResponseFail

import src.use_cases.arp as arp
import src.use_cases.auth as auth
import src.use_cases.app as app
import src.use_cases.whitelist as whitelist

MODULES = ('arp', 'auth', 'self', 'whitelist')
ACTIONS = ('add', 'remove', 'flush', 'enable', 'disable', 'load',
           'check', 'list', 'status', 'counters', 'test', 'save')

FN = {
    'arp': {
        'add': arp.add.execute,
        'remove': arp.remove.execute,
        'flush': arp.flush.execute,
        'enable': arp.enable.execute,
        'disable': arp.disable.execute,
        'load': arp.load.execute,
        'check': arp.check.execute,
        'list': arp.list.execute,
        'status': arp.status.execute,
        'counters': arp.counters.execute,
        'test': arp.test.execute,
        'save': arp.save.execute,
    },
    'auth': {
        'add': auth.add.execute,
        'remove': auth.remove.execute,
        'flush': auth.flush.execute,
        'enable': auth.enable.execute,
        'disable': auth.disable.execute,
        'load': auth.load.execute,
        'check': auth.check.execute,
        'list': auth.list.execute,
        'status': auth.status.execute,
        'counters': auth.counters.execute,
        'test': auth.test.execute,
        'save': auth.save.execute,
    },
    'whitelist': {
        'add': whitelist.add.execute,
        'remove': whitelist.remove.execute,
        'flush': whitelist.flush.execute,
        'enable': whitelist.enable.execute,
        'disable': whitelist.disable.execute,
        'load': whitelist.load.execute,
        'check': whitelist.check.execute,
        'list': whitelist.list.execute,
        'status': whitelist.status.execute,
        'counters': whitelist.counters.execute,
        'test': whitelist.test.execute,
        'save': whitelist.save.execute,
    },
    'app': {
        'add': app.add.execute,
        'remove': app.remove.execute,
        'flush': app.flush.execute,
        'enable': app.enable.execute,
        'disable': app.disable.execute,
        'load': app.load.execute,
        'check': app.check.execute,
        'list': app.list.execute,
        'status': app.status.execute,
        'counters': app.counters.execute,
        'test': app.test.execute,
        'save': app.save.execute,
    },
}


'''
def load_modules():
    loaded_modules = dict()
    for module in MODULES:
        pkg = "src.use_cases." + module
        use_cases = dict()
        print(pkg)
        for use_case in ACTIONS:
            try:
                m = importlib.import_module(use_case, pkg)
                use_cases[use_case] = m
            except ImportError as e:
                logging.warning("Import Error:", e)
            except Exception as e:
                logging.warning("Unexpected error:", e)
        loaded_modules[module] = use_cases
    return loaded_modules
'''


# calling use case without answer needed
def controller(req):
    """
    :param req:
    :type req: RequestObject
    """
    global FN

    if not isinstance(req, RequestObject):
        logging.warning("Request is invalid")
        return

    if req.module_ not in MODULES:
        logging.warning(req.module_ + " not in module list")
        return ResponseFail(req.module_, "Not in module list")

    module = FN.get('app', None) if req.module_ == 'self' else FN.get(req.module_, None)
    if module is None:
        return ResponseFail(req.module_ + "." + req.action, "Fail to execute")

    if req.action not in ACTIONS:
        logging.warning(req.action + " not in action list")
        return

    func = module.get(req.action, None)
    if func is not None:
        try:
            func(req.data)
        except (AttributeError, TypeError, ValueError) as e:
            logging.warning(e)
        except NotImplementedError as e:
            logging.warning(e)
        except Exception as e:
            logging.warning("Unexpected error:", e)


# calling use case and return answer
def informer(req):
    """
    :param req:
    :type req: RequestObject
    """
    global FN

    if not isinstance(req, RequestObject):
        logging.warning("Request is invalid")
        return ResponseFail(req, "Request is invalid")

    if req.module_ not in MODULES:
        logging.warning(req.module_ + " not in module list")
        return ResponseFail(req.module_, "Not in module list")

    module = FN.get('app', None) if req.module_ == 'self' else FN.get(req.module_, None)
    if module is None:
        return ResponseFail(req.module_ + "." + req.action, "Fail to execute")

    if req.action not in ACTIONS:
        return ResponseFail(req.action, "Not in action list")

    func = module.get(req.action, None)
    if func is not None:
        try:
            resp = func(req.data)
            return ResponseSuccess(resp)
            #getattr(m, "execute")(req.data)
        except (AttributeError, TypeError, ValueError) as e:
            logging.warning(e)
        except NotImplementedError as e:
            logging.warning(e)
            return ResponseFail(req.module_ + "." + req.action, "Not implement")
        except Exception as e:
            logging.warning("Unexpected error:", e)
    return ResponseFail(req.module_ + "." + req.action, "Fail to execute")


# start listeners as threads
def run():
    threads = []
    config = GlobalConfig()
    if config.get_config('rpc.zeromq.enabled'):
        threads.append({'name': 'ZeroMQ PuspPull', 'thread': threading.Thread(target=pp.run, args=[controller], daemon=True)})
        threads.append({'name': 'ZeroMQ RequestResponse', 'thread': threading.Thread(target=rr.run, args=[informer], daemon=True)})
    try:
        for thread in threads:
            thread['thread'].start()
            logging.warning(f"RPC thread {thread['name']} started")
        return [t['thread'] for t in threads]
    except Exception as e:
        logging.exception(e)

import logging
import threading
import importlib
from src.settings import GlobalConfig
from src.interfaces.zeromq import zeromq_push_pull as pp
from src.interfaces.zeromq import zeromq_request_response as rr

from src.interfaces.zeromq.shared.requestobject import RequestObject
from src.interfaces.zeromq.shared.responseobject import ResponseSuccess, ResponseFail


MODULES = ('arp', 'auth', 'self', 'whitelist')
ACTIONS = ('add', 'remove', 'flush', 'enable', 'disable', 'load',
           'check', 'list', 'status', 'counters', 'test', 'save')


def load_modules():
    loaded_modules = dict()
    for module in MODULES:
        pkg = "src.use_cases." + module
        use_cases = dict()
        for use_case in ACTIONS:
            try:
                m = importlib.import_module(use_case, pkg)
                use_cases[use_case] = m
            except ImportError as e:
                logging.warning(e)
            except Exception as e:
                logging.warning("Unexpected error:", e)
        loaded_modules[module] = use_cases
    return loaded_modules


LOADED_MODULES = load_modules()


# calling use case without answer needed
def controller(req):
    """
    :param req:
    :type req: RequestObject
    """
    global LOADED_MODULES
    if not isinstance(req, RequestObject):
        logging.warning("Request is invalid")
        return

    if req.module_ not in MODULES:
        logging.warning(req.module_ + " not in module list")
        return

    if req.action not in ACTIONS:
        logging.warning(req.action + " not in action list")
        return

    module = LOADED_MODULES.get(req.module_, None).get(req.action, None)
    if module is not None:
        try:
            module.execute(req.data)
            #getattr(m, "execute")(req.data)
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
    global LOADED_MODULES
    if not isinstance(req, RequestObject):
        logging.warning("Request is invalid")
        return ResponseFail(req, "Request is invalid")

    if req.module_ not in MODULES:
        logging.warning(req.module_ + " not in module list")
        return ResponseFail(req.module_, "Not in module list")

    if req.action not in ACTIONS:
        return ResponseFail(req.action, "Not in action list")

    module = LOADED_MODULES.get(req.module_, None).get(req.action, None)
    if module is not None:
        try:
            resp = module.execute(req.data)
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
        thread = threading.Thread(target=pp.run, args=[controller], daemon=True)
        threads.append(thread)
        thread = threading.Thread(target=rr.run, args=[informer], daemon=True)
        threads.append(thread)
    try:
        for thread in threads:
            thread.start()
        logging.warning("RPC threads started")
        return threads
    except Exception as e:
        logging.exception(e)

import logging
import zmq

from src.interfaces.zeromq.shared.requestobject import RequestObject
from src.settings import GlobalConfig


def run(cb):
    config = GlobalConfig()
    context = zmq.Context()
    socket = context.socket(zmq.PULL)  # pylint: disable=E1101
    try:
        socket.bind(config.get_config('rpc.zeromq.ports.push_pull'))
        while True:
            try:
                # time.sleep(1)
                # msg = socket.recv_json(flags=zmq.NOBLOCK)
                msg = str(socket.recv_string())
                req = RequestObject.from_json(msg)
                cb(req)
            except ValueError as e:
                logging.warning("Request value error: " + str(e))
            except zmq.ZMQError:
                # normal state for NOBLOCK
                pass
            except Exception as e:
                logging.exception(e)
    except Exception as e:
        logging.exception(e)
    finally:
        socket.close()
        context.term()

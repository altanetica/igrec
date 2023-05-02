import zmq
import logging

from src.interfaces.zeromq.shared.requestobject import RequestObject
from src.settings import GlobalConfig


def run(cb):
    config = GlobalConfig()
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # pylint: disable=E1101
    try:
        socket.bind(config.get_config('rpc.zeromq.ports.req_resp'))
        while True:
            try:
                # time.sleep(1)
                # msg = socket.recv_json(flags=zmq.NOBLOCK)
                # msg = socket.recv_json()
                msg = str(socket.recv())
                req = RequestObject.from_json(msg)
                reply = cb(req)
                socket.send(reply.to_json())
            except ValueError as e:
                logging.warning("Request value error: " + str(e))
                reply = {'code': -1, 'models': None, 'errors': [{'param': 'ValidateError', 'message': str(e)}]}
                socket.send_json(reply)
            except zmq.ZMQError:
                # normal state for NOBLOCK
                pass
            except Exception as e:
                logging.exception(e)
                reply = {'code': -1, 'models': None, 'errors': [{'param': 'Exception', 'message': str(e)}]}
                socket.send_json(reply)
    except Exception as e:
        logging.exception(e)
    finally:
        socket.close()
        context.term()

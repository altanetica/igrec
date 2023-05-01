from src.interfaces import rpc
from src.interfaces.zeromq.shared.requestobject import RequestObject
from src.interfaces.zeromq.shared.responseobject import ResponseObject


# todo: add check resp object

def test_rpc_informer_valid_request():
    req = RequestObject("app", "test", [])
    resp = rpc.informer(req)
    assert isinstance(resp, ResponseObject)


def test_rpc_informer_invalid_target(caplog):
    req = RequestObject("invalid", "test", [])
    resp = rpc.informer(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'


def test_rpc_informer_invalid_action(caplog):
    req = RequestObject("test", "invalid", [])
    resp = rpc.informer(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'


def test_rpc_informer_invalid_both(caplog):
    req = RequestObject("invalid", "invalid", [])
    resp = rpc.informer(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'


def test_rpc_informer_file_not_exist(caplog):
    req = RequestObject("test", "test", [])
    resp = rpc.informer(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'


def test_rpc_informer_run_not_exist(caplog):
    req = RequestObject("test", "flush", [])
    resp = rpc.informer(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'


def test_rpc_informer_argument_not_exist(caplog):
    req = RequestObject("test", "status", [])
    resp = rpc.informer(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'

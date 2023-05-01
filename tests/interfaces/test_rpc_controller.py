from src.interfaces import rpc
from src.interfaces.zeromq.shared.requestobject import RequestObject


def test_rpc_controller_valid_request():
    req = RequestObject("app", "test", None)
    rpc.controller(req)


def test_rpc_controller_invalid_request(caplog):
    req = 1
    rpc.controller(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'


def test_rpc_controller_invalid_target(caplog):
    req = RequestObject("invalid", "test", None)
    rpc.controller(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'


def test_rpc_controller_invalid_action(caplog):
    req = RequestObject("test", "invalid", None)
    rpc.controller(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'


def test_rpc_controller_invalid_both(caplog):
    req = RequestObject("invalid", "invalid", [])
    rpc.controller(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'


def test_rpc_controller_file_not_exist(caplog):
    req = RequestObject("test", "test", [])
    rpc.controller(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'


def test_rpc_controller_run_not_exist(caplog):
    req = RequestObject("test", "flush", [])
    rpc.controller(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'


def test_rpc_controller_argument_not_exist(caplog):
    req = RequestObject("test", "status", [])
    rpc.controller(req)
    assert len(caplog.records) == 1
    for record in caplog.records:
        assert record.levelname == 'WARNING'

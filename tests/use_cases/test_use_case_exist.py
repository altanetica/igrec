import sys
import pytest
import importlib
from src.interfaces import rpc

# skip if not module pyroute2
# pytest.importorskip('pyroute2')


@pytest.mark.skipif(sys.platform is not 'Linux', reason='Run only on Linux for module dependencies')
def test_use_case_exist():
    for target in rpc.MODULES:
        for action in rpc.ACTIONS:
            use_case = "." + action
            pkg = "src.use_cases." + target
            importlib.import_module(use_case, pkg)


@pytest.mark.skipif(sys.platform is not 'Linux', reason='Run only on Linux for module dependencies')
def test_use_case_have_execute():
    for target in rpc.MODULES:
        for action in rpc.ACTIONS:
            use_case = "." + action
            pkg = "src.use_cases." + target
            m = importlib.import_module(use_case, pkg)
            getattr(m, "execute")


@pytest.mark.skipif(sys.platform is not 'Linux', reason='Run only on Linux for module dependencies')
def test_use_case_have_process_request():
    for target in rpc.MODULES:
        for action in rpc.ACTIONS:
            use_case = "." + action
            pkg = "src.use_cases." + target
            m = importlib.import_module(use_case, pkg)
            getattr(m, "process_request")

import pytest
from python_package_template import PythonPackageTemplate as p

def test_unicode():
    instance = p()
    assert instance.__unicode__() == 'just a template'

def test_ping():
    assert p.ping() is "pong"

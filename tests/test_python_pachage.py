import pytest
from random import randint
from python_package_template import PythonPackageTemplate as p

def test_unicode():
    instance = p()
    assert instance.__unicode__() == 'just a template!'

def test_other():
    instance = p()
    assert instance.other() is False

def test_ping():
    assert p.ping() == "pong"

def test_this_gonna_be_flaky():
    assert randint(0,9) < 8

import pytest

@pytest.fixture()
def before_after():
    print('before test')
def test_demo1():
    assert 1 == 1
def test_demo2():
    assert 2 == 3
import pytest  # pip install pytest


def test_upper():
    # pytest 파이썬_파일.py 명령어로 실행
    assert 'foo'.upper() == 'FOO'


def test_upper_fail():
    assert 'foo'.upper() == 'Foo'
    

@pytest.mark.parametrize("obj", ['1', '2', 'Foo'])
def test_isdigit(obj):
    assert obj.isdigit()
    
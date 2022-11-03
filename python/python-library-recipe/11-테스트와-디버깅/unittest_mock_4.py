import unittest
from unittest.mock import MagicMock, patch


"""
mock이란, 테스트가 의존하고 있는 객체를 인터페이스가 동일한 의사 객체로 대체하는 것이다.
mock를 이용하면 외부 API를 사용하고 있거나 데이터베이스에 접속해야 해서 테스트가 어려울 때도,
외부에 의존하지 않고 테스트를 실행할 수 있다.
"""
# 어떤 외부 API
class OutsideAPI:
    def do_something(self):
        return '외부 API로 어떠한 처리를 실행한 결과'


# 단위 테스트를 하려는 처리
def my_processing():
    api = OutsideAPI()
    return api.do_something() + '를 사용하여 무엇인가를 하고 있다.'


def main():
    """mock 객체를 생성하여 반환값과 예외 설정하기 - MagicMock 
    MagicMock은 Mock의 서브클래스로 정의되어 있다. MagicMock은 Mock 클래스의 모든 기능뿐만 아니라 파이썬이 갖는 모든 특수 메소드를 지원한다.
    특별한 이유가 없다면 일단 MagicMock을 사용
    """
    # 외부 API의 do_something() 함수를 대체하는 mock 객체 생성
    api = OutsideAPI()
    api.do_something = MagicMock()
    print(api.do_something)

    # do_something() 함수의 반환값 설정
    api.do_something.return_value = 'mock 객체로 대체된 결과'
    print(api.do_something())

    # 함수에 예외를 설정할 수 있음
    # api.do_something.side_effect = Exception('예외를 설정')
    # print(api.do_something())

    # mock 객체가 호출되었는지 확인
    print(api.do_something.assert_called_with())  # 1회 이상 호출되지 않았으면 AssertionError 발생
    print(api.do_something())
    print(api.do_something.assert_called_once_with())  # 1회 이상이기 때문에 에러 발생


if __name__ == "__main__":
    print(my_processing())
    main()

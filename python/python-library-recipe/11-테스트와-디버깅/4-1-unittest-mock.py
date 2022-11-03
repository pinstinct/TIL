import unittest
from unittest.mock import patch

from unittest_mock_4 import my_processing


class TestMyClass(unittest.TestCase):
    """클래스와 메서드를 mock으로 대체하기 - patch """
    # patch 데코레이터를 이용해 OutsideAPI를 APIMock으로 대체
    @patch('unittest_mock_4.OutsideAPI')
    def test_my_processing(self, APIMock):
        api = APIMock()
        api.do_something.return_value = 'mock 객체로 대체된 결과'
        assert my_processing() == 'mock 객체로 대체된 결과를 사용하여 무엇인가를 하고 있다.'

    # 컨텍스트 매니저를 이용하여 OutsideAPI를 APIMock으로 대체
    def test_my_processing_2(self):
        with patch('unittest_mock_4.OutsideAPI') as APIMock:
            api = APIMock()
            api.do_something.return_value = 'mock 객체로 대체된 결과'
            # 의존하던 처리를 mock으로 대체하고 my_processing() 처리를 실행
            assert my_processing() == 'mock 객체로 대체된 결과를 사용하여 무엇인가를 하고 있다.'  # with 문의 불록 내에서만 적용
        assert my_processing() == '외부 API로 어떠한 처리를 실행한 결과를 사용하여 무엇인가를 하고 있다.'        


if __name__ == "__main__":
    unittest.main()

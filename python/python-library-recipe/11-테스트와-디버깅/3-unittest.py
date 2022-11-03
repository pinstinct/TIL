import unittest


"""테스트를 작성하여 실행하기 """
class TestSample(unittest.TestCase):
    """unittest.TestCase 클래스에서는 테스트 러너가 테스트를 실행하는 인터페이스 뿐만 아니라
    각종 검사 및 테스트 실패를 보고하는 메서드를 지원한다.

    다음 메소드를 이용하면 테스트 전후 처리(setUp/tearDown)를 작성할 수 있다.
    setUp(): test fixture를 준비하는 메서드, 테스트 메서드 실행하기 직전에 호출
    tearDown(): 테스트 메소드를 실행하고 나서 호출, 테스트 결과에 상관없이 setUp()이 성공한 경우에만 호출
    """
    def setUp(self) -> None:
        self.target = 'foo'

    def test_upper(self):
        self.assertEqual(self.target.upper(), 'FOO')

    @unittest.skip('이 테스트를 건너뜁니다.')    
    def test_pass(self):
        # 실패 케이스
        self.assertEqual('foo'.upper(), 'Foo')
        

if __name__ == "__main__":
    unittest.main()

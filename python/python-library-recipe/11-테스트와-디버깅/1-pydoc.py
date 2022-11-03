"""소스 코드에 작성한 주석으로부터 문서를 자동으로 생성하는 pydoc
커맨드 라인에서 다음의 명령어로 확인
$ pydoc 1-pydoc
$ pydoc -w 1-pydoc
$ pydoc -p 1234
"""


__author__ = "Python Freelec <sample@sample.com>"
__version__ = "0.0.1"


class SampleClass(object):
    """클래스에 관한 주석을 작성합니다. """
    def sample_method(self, sample_param):
        """메서드에 관한 주석을 작성합니다.
        :param str sample_param: 인수에 관한 주석을 작성합니다.
        """
        pass

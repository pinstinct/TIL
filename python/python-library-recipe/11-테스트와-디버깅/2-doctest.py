"""주어진 인수에 대해 a / b를 실행하는 함수
>>> div(5, 2)
2.5
"""


"""docstring 내에 작성한 테스트 코드를 실행하는 기능을 제공하는 doctest
파이썬 대화모드와 비슷한 형식으로 실행 내용과 기대하는 결과를 적는다.
>>> 파이썬 코드
기대하는 출력

자세한 로그를 확인하려면 다음 명령을 실행한다.
$ python 2-doctest.py -v 
"""
def div(a, b):
    """답은 소수로 반환
    >>> [div(n , 2) for n in range(5)]
    [0.0, 0.5, 1.0, 1.5, 2.0]

    >>> div(1, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return a / b
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

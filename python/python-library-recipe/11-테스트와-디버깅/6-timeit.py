import timeit


"""timeit은 너무 크지 않은 코드들을 처리하는데 사용
코드 실행 시간을 측정하면 구현 성능을 분석할 수 있기 때문에 병목 구간 발견에 도움

명령줄에서 코드의 실행 시간 측정하기
$ python -m timeit [-n N] [-r N] [-s S] [-p] [-v] ...
-n N: 파이썬 코드를 실행하는 횟수를 지정(생략하면 10회부터 시작해 소요시간이 0.2초가 되도록 반복 횟수가 자동으로 계산)
-r N: 실행 시간 측정을 반복할 횟수 지정(기본값 3)
-s S: 맨 처음 1회만 실행되는 명령문 지정(기본값 pass)
-p: 지정하면 실시간이 아닌 프로세스 시간 측정
-v: 지정하면 결과를 자세한 수치로 반복하여 표시

예) 지정된 파이썬 코드를 20000000 실행할 때 실행시간을 측정하며, 이를 5회 반복한다. 최종적으로 가장 실행 속도가 빨랐던 것을 선택한다.
$ python -m timeit '"test" in "This is a test."'
20000000 loops, best of 5: 18.5 nsec per loop
"""
def main():
    # Timer 인스턴스를 생성하여, 파이썬 코드를 number회(기본값 1000000) 실행
    print(timeit.timeit('"test" in "This is a test."'))
    # Timer 인스턴스를 생성하여, 파이썬 코드를 number회 실행하는 것을 repeat(기본값 5)회 반복
    print(timeit.repeat('"test" in "This is a test."'))

    # Timer 클래스를 이용하여 셋업문을 지정
    t = timeit.Timer('char in text', setup='text="This is a test"; char="test"')
    print(t.timeit())


if __name__ == "__main__":
    main()

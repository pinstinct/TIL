import traceback
import logging


logging.basicConfig(filename='python/python-library-recipe/11-테스트와-디버깅/example.log', format='%(asctime)s %(levelname)s %(message)s')


"""traceback 모듈은 프로그램을 정지시키지 않고 스택 트레이스를 표시하거나
콘솔이외(로그파일 등)에 스택 트레이스를 출력한다.
"""
def main():
    """스택 트레이스 표시하기 """
    # print_exc()는 스택 트레이스를 파이썬 인터프리터와 같은 서식으로 출력
    # 기본으로 콘솔에 출력하지만, 인수 file을 지정하면 파일에도 출력할 수 있음
    # 인수: limit(지정한 수까지 스택 트레이스 출력), file(출력 위치가 될 file-like 객체 지정, 기본값 sys.stderr), chain(True면 연쇄적인 예외도 동일하게 출력)
    tuple()[0]


if __name__ == "__main__":
    try:
        main()
    except IndexError:
        print('--- Exception occurred ---')
        traceback.print_exc(limit=1)

    """스택 트레이스 문자열로 취급하기 """
    # format_exc는 스택 트레이스를 파이썬 인터프리터와 같은 서식으로 맞춘 문자열을 반환
    try:
        tuple()[0]
    except IndexError:
        logging.error(traceback.format_exc())
        raise    

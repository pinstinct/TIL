from pprint import pprint
import sys


def main():
    """명령줄의 인수 얻기 - sys.argv """
    # sys.argv[0]은 실행된 스크립트 자신의 파일 이름
    print(sys.argv)

    """라이브러리의 import path 조작하기 - sys.path """
    # sys.path는 import 대상 모듈이나 패키지를 탐색하는 위치가 되는 여러 개의 파일 경로를 저장한 리스트
    # sys.path에 파일 경로를 추가하면 해당 파일 경로에 있는 파이썬 패키지나 모듈을 import문으로 import 할 수 있음
    pprint(sys.path)

    """콘솔 입출력 - sys.stdin, stdout, stderr """
    # 다음 세 개의 객체는 모두 파일 객체
    # sys.stdin(표준 입력 객체, 읽기 전용), sys.stdout(표준 출력 객체, 쓰기 전용), sys.stderr(표준 오류 출력 객체, 쓰기 전용)
    sys.stdout.write('standard output message\n')
    sys.stderr.write('standard error message\n')
    print(sys.stdin.read())  # 콘솔의 임의의 문자열을 입력하고 Ctrl + D 입력하면 입력을 반환


if __name__ == "__main__":
    main()

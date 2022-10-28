import os


def main():
    """실행 중인 프로세스 속성 조작하기 """
    # 환경변수 접근
    print(os.environ['HOME'])  # os.envrion은 환경변수를 저장하는 맵 형식 객체

    """파일과 디렉토리 조작하기 """
    # 기본적인 파일 조작
    print(os.getcwd())  # 현재 작업 디렉토리 구함
    os.mkdir('test')  # 디렉토리 생성
    print(os.listdir('.'))  # 현재 디렉토리 안의 파일과 디렉토리의 리스트를 생성
    os.rmdir('test')  # 디렉토리 삭제

    """무작위 문자열 생성하기 """
    # 2장의 random 모듈의 생성하는 난수는 의사 난수, 보안상의 용도로는 적합하지 않음
    # 보안이 필요할 때는 os.urandom, radnom.SystemRandom 클래스를 이용할 것을 추천
    print(os.urandom(10))  # 10바이트의 무작위 문자열을 생성


if __name__ == "__main__":
    main()

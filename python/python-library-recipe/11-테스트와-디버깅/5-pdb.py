import pdb


"""파이썬 프로그램용 대화 모드 디버거인 pdb 
pdb를 이용하면 프로그램 실행 도중의 변수값과 오류 발생 시 원인 등을 조사할 수 있다.

대표적인 디버거 명령어
h: 도움말 명령어
w: stack trace 출력
n: 다음 행 실행
l: 지정한 범위의 소스코드 표시
c: break point에 도달할 때까지 실행
q: 디버거 종료
"""
def add(a, b):
    """중단점 삽입하기 """
    pdb.set_trace()  # 이 위치에서 디버그 모드로 전환
    return a + b


def div(a, b):
    # 프로그램이 비정산적으로 종료할 때 자동으로 디버그 모드 전환
    return a / b


def main():
    add(1, 2)
    div(1, 0)
    

if __name__ == "__main__":
    main()

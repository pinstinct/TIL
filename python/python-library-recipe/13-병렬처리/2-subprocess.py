import subprocess
from subprocess import Popen, PIPE


def main():
    """자식 프로세스 실행하기 """
    result = subprocess.call(['echo', 'hello world'])  # 실행하려는 명령어와 인수를 리스트로 넘김
    print(result)  # 0: 정상 종료

    r = subprocess.call(['exit 1'], shell=True)  # shell=True라고 지정하면 셸을 거쳐 명령어가 실행(특별히 필요한 경우가 아니라면 지정하지 않는 것이 좋음)
    print(r)  # exit 1을 지정하여 셸을 비정상 종료

    # subprocess.check_call(['exit 1'], shell=True)  # 정상 종료하지 않았을 때 예외 발생시키려면 check_call() 메서드 사용

    """자식 프로세스를 실행하여 표준 출력 결과 얻기 """
    # 표준 입출력/오류 출력과 값을 주고받고 싶을 때는 subprocess.Popen 클래스 사용
    # 인수: args(실행할 프로그램 문자열 또는 시퀀스), stdin, stdout, stderr(파일 핸들러 지정), shell
    cmd = 'echo Hello World!'
    # 자식 프로세스 생성
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)  # PIPE:표준 스트림에 대해 파이프 여는 것을 지정하기 위한 특별한 값
    # 실행한 결과를 표준 출력으로 얻음
    stdout_data, stderr_data = p.communicate()  # stdout.read(), stderr.read()와 같은 메서드를 제공하지만, communicate를 사용하자(데이터 양이 매우 클 때, 운영체제의 파이프 버퍼가 대기 상태가 되어 데드락이 발생하는 문제가 있음, 데드락을 피하기 위해 communicate() 이용)
    print(stdout_data)

    # 자식 프로세스 출력을 다시 다른 자식 프로세스 입력으로 전달하기
    p1 = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    cmd2 = 'tr "[:upper:]" "[:lower:]"'
    p2 = Popen(cmd2, shell=True, stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
    stdout_data, stderr_data = p2.communicate()
    print(stdout_data)


if __name__ == "__main__":
    main()

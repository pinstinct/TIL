import paramiko  # pip install paramiko


"""SSH 모듈 기능을 제공하는 paramiko 패키지
주로 다음 목적으로 이용
- SSH 접속과 명령어 실행
- SFTP 접속을 통한 파일 전송
"""
def main():
    """SSH 명령어 실행하기 """
    # 리눅스 서버에 접속하여 명령어 ls -l /home을 실행하는 샘플 코드
    ssh = paramiko.SSHClient()
    # 모르는 서버 호스트에 접속할 경우 정책 설정(known_hosts에 없을 경우 정책 지정)
    # known_hosts: 접속할 서버 호스트의 진위 여부를 확인하기 위하여 서버 호스트 이름과 호스트 공개키 한 쌍을 기록해두는 파일을 가리킴
    # 보통은 ~/.ssh/known_hosts에 저장
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # AutoAddPolicy() 자동으로 추가
    # SSH 서버에 대한 접속 및 인증을 실행
    ssh.connect('hamegg.com', 22, 'your_user', key_filename='/home/your_user/.ssh/id_rsa')
    # SSH 서버상에서 명령어를 실행
    stdin, stdout, stderr = ssh.exec_command('ls -l /home')  # 표준 입력, 표준 출력, 표준 오류 출력
    for line in stdout:
        print(line, end="")
    ssh.close()

    """SFTP 파일 전송하기 """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('hamegg.com', 22, 'your_user', key_filename='/home/your_user/.ssh/id_rsa')
    sftp = client.open_sftp()
    # 올리기
    # subprocess로 SCP 명령어를 사용할 수 있으나, pramiko를 쓰는 편이 오류처리가 쉬움
    sftp.put('local_file', 'remote_file')
    # 권한을 0755로 지정
    # mode를 다룰 때 주의사항: 리눅스 명령어 chmod 644와 같은 동작을 기대하고 mode=644라고 지정하면, chomod 1204라는 권한이 설정됨
    # mode는 받는 값을 10진수라고 인식하기 때문임
    # 따라서 8진수 644를 10진수로 변환한 mode=420이라고 지정하거나, 맨앞에 0o(zero, o)를 붙여 0o644와 같이 8진수로 지정
    sftp.chmod('remote_file', mode=0o0755)
    # 내려받기
    sftp.get('remote_file', 'local_file')
    sftp.close()
    client.close()


if __name__ == "__main__":
    main()

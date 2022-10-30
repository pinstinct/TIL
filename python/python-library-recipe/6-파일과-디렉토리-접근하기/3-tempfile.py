import tempfile


"""tempfile은 사용자만 읽고 쓸 수 있도록 권한이 설정되고, 생성할 때 경합하지 않는 등 안전한 방법으로 구현
TemporaryFile(): 파일 이름이 없는 임시 파일을 생성(디스크)
NamedTemporaryFile(): 파일 이름이 있는 임시 파일을 생성(디스크)
SpooledTemporaryFile(): 일정 크기의 데이터까지 메모리에 쓰고, 이를 넘어서면 디스크에 임시 파일 생성(메모리 -> 디스크)
TemporaryDirectory(): 임시 디렉토리 생성
"""
def main():
    """임시 파일 생성하기 """
    with tempfile.TemporaryFile() as tmp:  # with 블록을 빠져나오면 암묵적으로 .close가 호출 -> 파일을 닫음과 동시에 삭세
        tmp.write(b'test test test\n')
        tmp.seek(0)
        print(tmp.read())

    # 명시적으로 임시 파일 삭제
    tmp1 = tempfile.TemporaryFile()
    tmp1.close()

    # 이름을 가진 임시 파일 생성
    tmp2 = tempfile.NamedTemporaryFile()
    print(tmp2.name)
    tmp2.close()

    # 명시적으로 임시 디렉토리 삭제
    tmpdir = tempfile.TemporaryDirectory()
    tmpdir.cleanup()


if __name__ == "__main__":
    main()

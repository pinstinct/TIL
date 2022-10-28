import io


def main():
    """I/O를 다루는 스트림 객체를 살펴 본다.
    스트림 객체 또는 file-like 객체라고 불리는 것들, 문자열, 바이트열 등의 객체를 파일과 같이 취급할 수 있다.

    - 문자열을 파일과 같은 인터페이스로 다루는 StringsIO 클래스
    - 바이트열을 파일과 같은 인터페이스로 다루는 BytesIO 클래스
    - 기타, 스트림 객체의 추상 기반 클래스 군

    내장 함수 open()에 의해 생성되는 파일 객체도 스트림 객체이다.
    """
    # 인메모리 텍스트 스트림 다루기 - StringIO
    # 파일 객체와 달리 데이터를 메모리상에서 취급
    stream = io.StringIO("this is test\n")
    print(stream.read(10))  # 지정한 크기만큼 읽기
    print(stream.tell())  # 현재 오프셋 반환
    print(stream.seek(0, io.SEEK_END))  # 오프셋을 맨 끝으로 변경(https://docs.python.org/3/library/io.html#io.IOBase.seek)
    print(stream.write('test'))  # 스트림에 문자열을 쓰기
    print(stream.getvalue())  # 스트림이 가진 모든 내용을 반환
    stream.close()  # 스트림을 닫음


if __name__ == "__main__":
    main()

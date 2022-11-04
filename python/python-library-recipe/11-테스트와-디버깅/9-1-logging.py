import logging


def main():
    # logging.basicConfig()로 로깅 동작 변경하기
    # 출력 위치나 메시지 출력 포맷, 로그 레벨 등의 로깅 동작을 변경하고 싶을 때 사용
    # 인수: filename(출력 파일 이름 지정), filemode(파일 열 때 모드 지정), format(지정한 로그 포맷으로 출력), level(로그 레벨의 임계 값을 지정), stream(지정한 스트림 사용, filename과 동시 사용 불가), handlers(사용할 핸들러 지정, filename, stream과 동시 사용 불가)
    # format: https://docs.python.org/3/library/logging.html#logrecord-attributes
    logformat = '%(asctime)s %(levelname)s %(message)s'
    logging.basicConfig(filename='./test.log', level=logging.DEBUG, format=logformat)
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')


if __name__ == "__main__":
    main()

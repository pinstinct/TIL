import bz2


def main():
    """bzip2 형식의 파일 압축과 해제를 실행하는 bz2 모듈 """
    # bz2로 압축된 파일을 열어 파일 객체를 반환
    # 압축률이 높아지면 시간이 오래 걸림
    with bz2.open('sample.bz2', 'wt') as f:
        f.write('한국어 텍스트를 bz2 압축 파일로 쓰기')

    with bz2.open('sample.bz2', 'rt') as f:
        content = f.read()
    print(content)

    text = '한국어 텍스트'
    b = text.encode('utf-8')
    # 지정된 데이터(bytes 형식)를 bz2로 압축
    gzipped_data = bz2.compress(b)
    print(len(b))
    print(len(gzipped_data))  # 압축 대상 데이터가 작을 때는 압축 후의 데이터가 더 커지는 경우도 있음

    long_text = b'A' * 1000
    gzipped_data = bz2.compress(long_text)
    print(f'{len(long_text)}, {len(gzipped_data)}')

    gunzipped_data = bz2.decompress(gzipped_data)
    print(len(gunzipped_data))
    print(long_text == gunzipped_data)


if __name__ == "__main__":
    main()

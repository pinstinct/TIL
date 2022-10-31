import zlib


def main():
    """zlib 라이브러리에는 gzip 파일에 이용하는 압축 알고리즘 제공 """
    text = '한국어 텍스트'
    b = text.encode('utf-8')
    # 지정한 데이터(bytes 형식)의 압축 결과 반환 (압축률이 높으면 시간이 오래 걸림)
    compressed_data = zlib.compress(b)  
    print(len(b))
    print(len(compressed_data))  # 압축 대상 데이터가 작을 때는 압축 후의 데이터가 더 커지는 경우도 있음

    long_text = b'A' * 10000
    compressed_data = zlib.compress(long_text)
    print(f"{len(long_text)}, {len(compressed_data)}")

    # 압축 해제 결과 반환
    decompressed_data = zlib.decompress(compressed_data) 
    print(len(decompressed_data))
    print(long_text == decompressed_data)  # 데이터 확인


if __name__ == "__main__":
    main()

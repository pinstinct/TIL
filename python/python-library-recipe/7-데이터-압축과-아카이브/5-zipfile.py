import zipfile


def main():
    """zip 형식으로 압축된 파일을 다루는 zipfile 모듈 
    https://docs.python.org/3/download.html 페이지에서 plain text 형식 문서 zip과 tar.bz2를 내려받아 사용
    """
    directory = './python/python-library-recipe/7-데이터-압축과-아카이브'
    f = f'{directory}/python-3.11.0-docs-text.zip'
    # ZIP 파일인지 여부를 반환
    print(zipfile.is_zipfile(f))
    print(zipfile.is_zipfile(f'{directory}/python-3.11.0-docs-text.tar.bz2'))

    # ZIP 파일을 읽고 쓰기 위한 객체 생성
    zip = zipfile.ZipFile(f)
    # ZIP 파일 내에 압축된 파일 이름 리스트를 반환
    print(len(zip.namelist()))
    print(zip.namelist()[:2])
    # ZIP 파일 안의 지정된 파일을 열기
    file = zip.open(zip.namelist()[1])
    contents = file.read()
    print(contents[:60])

    for name in zip.namelist():  # zipfile 매뉴얼 찾기
        if 'zipfile' in name:
            zipfile_doc = name
    print(zipfile_doc)
    # 지정된 파일의 ZipInfo 객체 취득
    zipinfo = zip.getinfo(zipfile_doc)
    print(zipinfo.filename)  # 파일 이름
    print(zipinfo.date_time)  # 파일의 최종 갱신 일시를 튜플로 반환
    print(zipinfo.compress_size)  # 압축 후 파일 크기
    print(zipinfo.file_size)  # 압축 전 파일 크기

    # 지정된 ZIP 파일 안의 파일을 지정한 경로에 압축 해제
    zip.extract(zipinfo)
    # ZIP 파일 안의 모든 파일을 지정한 경로에 압축 해제
    zip.extractall()
    # ZipFile을 닫음
    zip.close()

    wzip = zipfile.ZipFile('example.zip', mode='w')
    # 지정한 파일을 ZIP 파일로 쓰기
    wzip.write('./python-3.11.0-docs-text/library/zipfile.txt', 'zipfile.txt')
    print(wzip.namelist())
    # 지정한 bytes 데이터를 ZIP 파일로 쓰기
    wzip.writestr('test.txt', b'test text')
    print(wzip.namelist())
    wzip.close()
    print(zipfile.is_zipfile('example.zip'))


if __name__ == "__main__":
    main()

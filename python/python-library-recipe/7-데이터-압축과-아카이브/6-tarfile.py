from importlib.resources import contents
import tarfile


def main():
    """tar 형식으로 압축된 파일을 다루기 위한 tarfile 모듈
    gzip, bz2, lzma 형식으로 압축된 파일을 다룰 수 있다.
    https://docs.python.org/3/download.html 페이지에서 plain text 형식 문서 zip과 tar.bz2를 내려받아 사용
    """
    directory = './python/python-library-recipe/7-데이터-압축과-아카이브'
    python_zip = f'{directory}/python-3.11.0-docs-text.zip'
    python_tar = f'{directory}/python-3.11.0-docs-text.tar.bz2'
    # tar 파일인지 여부를 반환
    print(tarfile.is_tarfile(python_zip))
    print(tarfile.is_tarfile(python_tar))

    # tar 파일 열기
    tar = tarfile.open(python_tar)
    # tar 파일 내에 압축된 파일 이름 리스트 반환
    print(len(tar.getnames()))
    print(tar.getnames()[:2])

    # 지정된 파일의 파일 객체 반환
    f = tar.extractfile(tar.getnames()[1])
    contents = f.read()
    print(contents[:60])

    for name in tar.getnames():  # tarfile 매뉴얼 찾기
        if 'tarfile' in name:
            tarfile_doc = name
    print(tarfile_doc)
    # 지정한 파일 이름의 TarInfo 객체 취득
    tarinfo = tar.getmember(tarfile_doc)
    print(f'파일이름: {tarinfo.name}, 파일크기: {tarinfo.size}, 최종 갱신 시각: {tarinfo.mtime}, 허가 비트: {tarinfo.mode}')
    # 압축 안의 지정된 파일을 지정된 경로에 압축 해제
    tar.extract(tarinfo)
    # 압축 안의 모든 파일을 지정된 경로에 압축 해제
    tar.extractall()
    # TarFile 닫기
    tar.close()

    wtar = tarfile.open('example.tar.gz', mode='w:gz')
    # 지정된 파일을 tar 압축에 추가
    wtar.add('./python-3.11.0-docs-text/library/tarfile.txt', 'tarfile.txt')
    print(wtar.getnames())
    wtar.close()
    print(tarfile.is_tarfile('example.tar.gz'))


if __name__ == "__main__":
    main()

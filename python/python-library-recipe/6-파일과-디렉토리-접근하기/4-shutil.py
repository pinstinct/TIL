import shutil


def main():
    """파일 복사하기 """
    # copymode(src, dst): 권한을 src에서 dst로 복사
    # copystat(src, dst): 권한, 최종접근시간, 최종변경시간 및 기타 파일정보를 src에서 dst로 복사
    # copy(src, dst): 파일 src를 dst로 복사
    # copy2(src, dst): copy()와 같은 기능에 추가로 모든 메타 데이터를 복사

    """재귀적으로 디렉토리와 파일 조작하기 """
    # rmtree(): 지정한 디렉토리 삭제
    # move(): 디렉토리 이동
    # copytree(): 디렉토리 통째로 복사
    ignore = shutil.ignore_patterns("*.pyc", "*.swp")  # 확장자가 .pyc, .swp 파일을 제외
    print(ignore)
    shutil.copytree('./ETC', './tmp', ignore=ignore)
    shutil.move('./tmp', './abc')
    shutil.rmtree('./abc')

    """압축 파일의 생성과 압축 해제 """
    shutil.make_archive(base_name='example', format='gztar', base_dir='./python/python-library-recipe/6-파일과-디렉토리-접근하기/example')
    shutil.unpack_archive(filename='example.tar.gz')


if __name__ == "__main__":
    main()

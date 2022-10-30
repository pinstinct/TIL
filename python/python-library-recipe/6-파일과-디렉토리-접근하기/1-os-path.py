import os.path


def main():
    """파일 경로 조작하기 """
    print(os.path.abspath('.'))  # 절대 경로 반환
    print(os.path.join('hoge', 'fuga', 'piyo'))  # 여러개의 파일 경로 경합
    path = os.path.abspath('.')
    print(os.path.basename(path))  # 맨 끝 파일 이름을 반환
    print(os.path.dirname(path))  # 파일이름을 제외한 디렉토리 부분을 반환
    print(os.path.exists(path))  # 파일 경로 존재 확인
    print(os.path.split(path))  # 디렉토리 부분(dirname() 과 같음)과 파일이름 부분(basename()과 같음)으로 분해한 두 요소의 튜플 반환




if __name__ == "__main__":
    main()

from pathlib import Path, PurePath


"""파일 경로 조작이나 파일 자체의 조작을 객체지향 스타일의 직관적인 인터페이스로 제공하는 pathlib
- I/O를 수반하지 않는 기능을 제공하는 "순수 경로(pure path)"
- I/O를 수반하는 기능을 제공하는 "구상 경로(concrete path)"
"""
def main():
    """클래스 구성 """
    # 어떤 클래스를 선택할지 모를 때는 대부분 Path를 사용하면 문제가 없음
    # 구상 경로 클래스인 Path는 순수 경로 클래스인 PurePath의 서브클래스이므로,
    # 순수 경로 클래스와 구상 경로 클래스 양쪽의 기능을 모두 사용할 수 있음
    print(Path('.'))
    print(type(Path('.')))

    """연산자로 경로 결합하기 """
    p = PurePath('/hoge/fuga/')
    p = p / 'piyo.txt'
    print(p)

    """순수경로 다루기 - PurePath """
    # 순수 경로의 기능은 파일 시스템에 접근하지 않기 때문에
    # 운영체제 상에 존재하지 않는 파일 경로를 다룰 수 있음
    print(p.drive)  # WindowsPath일 때 드라이브 문자, PosixPath일 때 빈 문자 반환
    print(p.root)  # 루트를 나타내는 문자 반환
    print(p.anchor)  # 드라이브와 루트를 결합한 문자 반환
    print(list(p.parents))  # 상위 경로에 접속할 수 있는 시퀀스 객체 반환
    print(p.parent)  # 바로 위 경로 반환
    print(p.name)  # 경로 요소의 맨 끝을 나타내는 문자열 반환
    print(p.suffix)  # 경로 요소의 맨 끝에 확장자가 있으면 반환
    print(p.stem)  # 경로 요소의 맨 끝에 확장자를 빼고 반환
    print(p.is_absolute())  # 경로가 절대 경로이면 True 반환
    print(p.joinpath('foo', 'bar', 'baz'))  # 경로 연결
    print(p.match('piyo.*'))  # 패턴과 일치하면 True 반환

    """구상경로 다루기 - Path"""
    print('=====')
    # 구상 경로의 기능은 파일 시스템에 접근하기 때문에
    # 운영체제제 상에 조작 대상 파일 경로가 존재해야 함
    p1 = Path.cwd() / 'newfile.txt'  # 현재 디렉토리 경로 반환
    print(p1.exists())  # 경로가 존재하면 True
    f = p1.open('w+')
    print(p1.exists)
    print(p1.resolve())  # 경로를 절대 경로로 하고, 심볼릭 링크를 해제

    p2 = Path('.')
    print(p2.iterdir())  # 경로 아래 존재하는 파일이나 디렉토리를 반환
    print(sorted(p2.iterdir()))
    print(p2.glob('**/*.txt'))  # 패턴에 일치하는 파일을 경로 객체 발생자(generator) 반환
    print(sorted(p2.glob('**/*.txt')))  # **/로 시작하는 패턴을 지정하면, 이 디렉토리와 서브 디렉토리를 재귀적으로 스캔


if __name__ == "__main__":
    main()

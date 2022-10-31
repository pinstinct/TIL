from configparser import ConfigParser, ExtendedInterpolation


def main():
    """INI 파일 읽어오기 """
    path = './python/python-library-recipe/8-특정-데이터-포맷-다루기'
    file = f'{path}/config.ini'
    config = ConfigParser()
    print(config.read(file))  # INI 읽기(여러개의 INI 파일 리스트도 지정 가능)
    print(config.sections())  # 섹션 리스트 얻기(DEFAULT 섹션은 포함되지 않음, 기타 모든 섹션의 기본 값으로 채택, 섹션 이름은 대소문자 구별)
    print(config.options('USER_A'))  # 옵션 리스트 얻기(대소문자 구별 안 함)
    print('USER_B' in config)  # 섹션 존재 확인
    print(config.get('USER_A', 'group'))  # 옵션 값 얻기
    print(config.get('USER_A', 'limit'))  # DEFAULT 값 얻기

    """INI 파일의 추가 활용법 
    반복해서 같은 문자열을 적다 보면 복잡하기 쉽다.
    이 같은 경우에 값 삽입(interpolation) 기능을 이용할 수 있다.
    """
    file1 = f'{path}/config_interp.ini'
    # ConfigParser 클래스의 인스턴스를 생성할 때 아무것도 지정하지 않을 경우, 기본으로 값 삽입 기능을 이용할 수 있음
    config1 = ConfigParser()  
    print(config1.read(file1))
    print(config1.get('USER_A', 'mail_dir'))  # INI 파일의 %(home_dir)s -> 같은 섹션(또는 DEFAULT 섹션 내)의 옵션이름 home_dir값으로 치환

    # ExtendedInterpolation 이용하면 더 고도의 값 삽입 가능
    config2 = ConfigParser(interpolation=ExtendedInterpolation())
    config2.read(file1)
    print(config2.get('USER_B', 'group'))  # ${섹션:옵션이름} 혹은 같은 섹션인 경우 ${옵션이름} 형식 -> 해당 값 치환

    """configparser와 자료형
    configparser로 읽어온 데이터는 모두 문자열이다.
    """
    print(config.getint('USER_A', 'limit'))
    print(int(config.get('USER_A', 'limit')))


if __name__ == "__main__":
    main()

import re


def main():
    """기본 함수 """
    # 지정된 문자열이 정규 표현에 일치하는지 확인
    # 인수: 정규 표현 문자열, 확인할 문자열, 정규 표현을 컴파일 할 때 동작을 변경하는 플래그
    # 반환: 일치하면 매치 객체, 일치하지 않으면 None
    print(re.search('a.c', 'abc'))

    # 지정된 문자열이 정규 표현에 일치하는지 확인, search()와는 다르게 문자열의 맨 앞 글자부터 일치하는지 확인
    # 인수: 정규 표현 문자열, 확인할 문자열, 정규 표현을 컴파일 할 때 동작을 변경하는 플래그
    print(re.match('a.c', 'abc'))
    print(re.match('b', 'abc'))
    print(re.search('b', 'abc'))

    """re 모듈의 상수(플래그) """
    # A 또는 ASCII: \w 등의 매치 처리에서 ASCII 문자만 매치
    # I 또는 IGNORECASE: 대소문자를 구별하지 않고 매치
    # M 또는 MULTILINE: ^와 $를 각 행의 맨 처음과 맨 끝에 매치
    # S 또는 DOTALL: 점(.)을 줄바꿈까지 포함해 매치
    print(re.search('\w', '가나다라마ABC'))
    print(re.search('\w', '가나다라마ABC', flags=re.A))
    print(re.search('[abc]+', 'ABC'))
    print(re.search('[abc]+', 'ABC', re.I))
    print(re.match('a.c', 'A\nC', re.I))
    print(re.match('a.c', 'A\nC', re.I | re.S))

    """정규 표현 객체 """
    # 지정된 정규 표현을 컴파일하여 정규 표현 객체를 반환
    regex = re.compile('[a-n]+')  # a-n 범위의 영어 소문자 매치
    print(type(regex))

    # 정규 표현 객체 메서드
    print(regex.search('python'))
    print(regex.match('python'))  # 맨 앞글자가 일치하지 않으므로 None
    print(regex.fullmatch('eggs'))  # 문자열 전체와 일치하는지 검사
    print(regex.fullmatch('egg'))
    regex2 = re.compile('[-+()]')  # 전화번호에 사용되는 기호 패턴 정의
    print(regex2.split('(080)1234-5678'))
    print(regex2.sub('', '+81-80-1234-5678'))
    regex3 = re.compile('\d+')  # 문자 한 개 이상으로 된 숫자의 정규 표현
    print(regex3.findall('080-1234-5678'))
    for m in regex3.finditer('+82-80-1234-5678'):
        print(m)

    """매치 객체 """
    # 정규 표현에 일치한 문자열에 관한 정보를 저장하는 객체
    regex4 = re.compile('(\d+)-(\d+)-(\d+)')
    m = regex4.match('080-1234-5678')
    print(m.group())
    print(m.group(1), m.group(2), m.group(3))

    regex5 = re.compile(r'(?P<first>\w+) (?P<last>\w+)')  # Named Capturing Group을 사용하는 방법은 (?P<그룹명>정규식)와 같이 정규식 표현 앞에 ?P<그룹명>을 사용
    m2 = regex5.match('Abc def: Pycon Chair')
    print(m2.group())
    print(m2.group('first'), m2.group('last'))

    # 매치 객체의 메서드
    print(m2.groups())  # 일치한 문자열 모두 tuple로 얻음 
    print(m2.groupdict())  # 일치한 문자열을 사전 형식으로 얻음
    print(m2.expand(r'last: \2, first: \1'))  # 일치한 문자열을 반환
    print(m2.expand(r'last: \g<last>, first: \g<first>'))


if __name__ == "__main__":
    main()

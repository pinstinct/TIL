def main():
    """문자열 검사 메서드 """
    # 문자와 숫자일 때, True
    print('123abc'.isalnum())
    print('가나다'.isalnum())

    # 문자 only
    print('abcd'.isalpha())
    print('가나다라가한국어'.isalpha())

    # 문자열이 모두 소문자일 때, True
    print('lower'.islower())

    # 문자열이 모두 대문자일 때, True
    print('UPPER'.isupper())

    # 맨 처음만 대문자고 뒤는 소문자인 문자열인 경우 True
    print('Title'.istitle())

    # 문자열이 숫자로 구성될 때, True
    print('1234'.isdigit())

    # 문자열이 십진수 숫자일 때, True
    print('123'.isdigit())

    """문자열 변환 메서드 """
    text = 'HELLO world!'
    print(text.upper())
    print(text.lower())
    print(text.swapcase())  # 대문자는 소문자로, 소문자는 대문자로
    print(text.capitalize())  # 맨 처음 한 글잘만 대문자로, 그 외에는 소문자로
    print(text.title())  # 단어마다 대문자+소문자 형식으로 변환
    print(text.replace('world', 'python'))

    """서식화 메서드 """
    print('{} is better than {}'.format('Beautiful', 'ugly'))
    print('{1} is better than {0}'.format('implicit', 'Explicit'))
    print('My name is {name}'.format(name='tester'))
    person = {
        'name': 'tester',
        'twitter': 'abc',
    }
    print('My twitter id is {twitter}'.format_map(person))

    """기타 문자열 메서드 """
    # 문자열에서 존재하는 위치를 반환, 없으면 -1
    print('python'.find('th'))
    print('python'.find('TH'))

    # 문자열 분할, 기본으로 공백 문자로 분할
    words = 'Beautiful is better than ugly. Explicit is better than implicit.'
    words = words.split()
    print(words)

    # 문자열 결합
    print('-'.join(words[:5]))

    # 접두사를 가진 문자열 검색
    print('python'.startswith('py'))

    # 접미사를 가진 문자열 검색
    image_suffix = ('jpg', 'png', 'gif')
    print('image.png'.endswith(image_suffix))

    # 문자열을 지정한 인코딩 형식으로 변환
    encoding = '가abc나'
    print(encoding.encode('utf-8'))
    print(encoding.encode('ascii', 'ignore'))  # 에러가 발생할 경우 무시 (한국어를 무시)
    print(encoding.encode('ascii', 'replace'))  # 에러가 발생할 경우 변환 (한국어를 ?로 변환)

if __name__ == "__main__":
    main()

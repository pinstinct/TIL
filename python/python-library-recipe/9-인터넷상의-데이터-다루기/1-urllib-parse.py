from urllib import parse


def main():
    """URL 해석하기 - urlparse() """
    # URL을 해석해 결과를 반환
    # 반환: ParseResult 클래스(튜플의 서브클래스) 인스턴스
    result = parse.urlparse('https://www.python.org/doc/;parameter?q=example#hoge')
    print(result)
    print(result.geturl())  # parse 결과로부터 URL 취득
    print(result.scheme)  # 튜플 요소에 이름으로 접근
    print(result[0])  # 튜플 요소에 인덱스로 접근
    print(result.hostname)  # 튜플 이외에도 몇 개의 속성을 가짐

    """쿼리 문자열 해석하기 - parse_qs() """
    # 쿼리 문자열을 해석하여 파이썬 자료구조로 변환
    result1 = parse.urlparse('https://www.google.co.kr/search?q=python&oq=python&sourceid=chrome&ie=UTF-8')
    print(result1.query)
    print(parse.parse_qs(result1.query))  # 사전으로 반환
    print(parse.parse_qs('key=1&key=2'))  # 하나의 키에 대한 값이 여럿일 때
    print(parse.parse_qsl(result1.query))  # 튜플 리스트로 반환
    print(parse.parse_qsl('key=1&key=2'))  # 하나의 키에 대한 값이 여럿일 때

    print(parse.parse_qs('key1=&key2=hoge'))  # 빈 값이 있는 쿼리는 해석 결과에서 제외
    print(parse.parse_qs('key1=&key2=hoge', keep_blank_values=True))  # 빈 문자로 취급

    """쿼리 문자열 조합하기 - urlencode() """
    # 파이썬 자료구조로부터 application/x-www-form-urlencoded와 같은 폼 데이터나 URL 쿼리 문자열로 사용할 수 있는 문자열을 조합
    # 인수: query, doseq(True: 시퀀스로 해석, False: 문자열로 해석), encoding, errors
    # 반환: str
    print(parse.urlencode({'key1': 1, 'key2': 2, 'key3': '파이썬'}))
    print(parse.urlencode([('key1', 1), ('key2', 2), ('key3', '파이썬')]))
    query = {'key1': 'hoge', 'key2': ['fuga', 'piyo']}
    print(parse.urlencode(query))  # 결과 디코딩: key1=hoge&key2=['fuga',+'piyo']
    print(parse.urlencode(query, doseq=True))


if __name__ == "__main__":
    main()

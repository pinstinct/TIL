from urllib import request


def main():
    """지정한 URL 열기 """
    # URL을 열어 콘텐츠를 취득
    # 반환: http.client.HTTPResponse
    # GET, POST 메서드만 직접 URL과 데이터 요청 가능
    # 그 외 메서드는 HTTP 요청을 추상화한 urllib.request.Request 클래스 인스턴스를 지정
    res = request.urlopen('http://httpbin.org/get')
    print(res.code)  # 반환값은 응답 정보를 저장한 file-like 객체이기 때문에, read() 메서드로 데이터 읽기 가능
    print(res.read())
    # 매개변수 붙여 요청하기
    res1 = request.urlopen('http://httpbin.org/get?key1=value')
    print(res1.read())
    # 사용자 정의 헤더 설정하기
    headers = {'Accept': 'application/json'}
    req = request.Request('http://httpbin.org/get', headers=headers)
    res2 = request.urlopen(req)
    print(res2.read())
    # POST 요청하기
    data = 'key1=value1&key2=value2'  # urllib.parse 모듈을 이용할 수 있음
    res3 = request.urlopen('http://httpbin.org/post', data=data.encode())  # data는 bytes형 데이터를 전달해야하므로 encode()를 사용해 변환
    print(res3.code)

    """GET, POST 이외의 HTTP 메서드 다루기 """
    req = request.Request('http://httpbin.org/get', method='HEAD')
    res4 = request.urlopen(req)
    print(res4.code)
    print(res4.read())  # HEAD 메서드는 응답 본문(body)은 비어 있음  


if __name__ == "__main__":
    main()

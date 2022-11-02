import requests  # pip install requests         


def main():
    """지정한 URL 열기 """
    url = 'http://httpbin.org/get'
    r = requests.get(url)
    print(r)
    print(r.text)  # 문자열로 인코딩 완료된 응답 본문
    # 매개변수 붙여 GET 요청하기
    r = requests.get(url, params='example')
    print(r.url)  # 요청한 URL 문자열
    r = requests.get(url, params={'key': 'value'})
    print(r.url)
    # HTTP 헤더 지정하기
    headers = {'Accept': 'application/json'}
    r = requests.get(url, headers=headers)
    # requests.models.Response 객체의 대표적 속성
    print(r.cookies)  # 응답에 포함된 Cookie 정보 객체
    print(r.headers)  # 사전 형식의 응답 헤더
    print(r.status_code)  # 응답의 HTTP 상태 코드
    print(r.ok)  # 응답의 HTTP 상태 코드가 정상이면 True, 그렇지 않으면 False 반환
    print(r.iter_lines())  # 응답 본문을 한 줄씩 반환하는 반복자 반환(문자열이 아닌 바이트열로 반환)
    for l in r.iter_lines():
        print(l)
    print(r.json())  # 응답 본문을 JSON 포맷으로 해석하고 사전으로 변환하여 반환
    
    # POST 요청하기
    payload = {'hoge': 'fuga'}
    r = requests.post('http://httpbin.org/post', data=payload)  # data 인수에 사전을 지정하면, application/x-www-form-urlencoded 형식의 인수로 변환
    print(r.request.body)


if __name__ == "__main__":
    main()

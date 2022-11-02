import base64


"""Base64로 인코딩과 디코딩하는 모듈 base64
이들 인코딩 방식은 알파벳과 숫자 등 취급할 수 있는 문자 종류가 한정된 환경에서
그 외의 문자(예를 들면 멀티 바이트 문자나 이진 데이터)를 사용하기 위한 것
Base64는 주로 Basic 인증이나 이메일 등에 이용
"""
def main():
    """Base64로 인코딩 """
    s = 'Python은 간단히 습득할 수 있으며 이와 동시에 강력한 언어 중의 하나입니다.'
    # 바이트 문자열을 Base64로 인코딩
    print(base64.b64encode(s.encode()))
    print(base64.b64encode(s.encode(), altchars=b'@*'))  # + -> @, / -> * 치환
    # urlsafe_b64encode()는 URL의 일부로 안전히 이용할 수 있는 알파벳만 사용한 인코딩 결과 반환

    b = 'UHl0aG9u7J2AIOqwhOuLqO2eiCDsirXrk53tlaAg7IiYIOyeiOycvOupsCDsnbTsmYAg64+Z7Iuc7JeQIOqwleugpe2VnCDslrjslrQg7KSR7J2YIO2VmOuCmOyeheuLiOuLpC4='
    # Base64로 인코딩된 바이트 문자열을 디코딩
    print(base64.b64decode(b))
    print(base64.b64decode(b).decode())


if __name__ == "__main__":
    main()

import email


"""이메일 메시지나 헤더 해석과 작성을 위한 기능을 제공하는 email
이메일에는 텍스트 외에도 이미지나 첨부 파일 등의 다양한 데이터가 포함
이는 MIME(Multipurpose Internet Mail Extensions)라는 사양에 의해 구현되지만, MIME 형식의 데이터는 복잡
email 모듈을 사용하면 MIME 형식의 데이터를 해석하고 생성할 수 있다.
"""
def main():
    """이메일 해석하기 - email.parser """
    # 메일을 해석하기 위한 parser를 생성하는 생성자
    path = './python/python-library-recipe/9-인터넷상의-데이터-다루기/email.txt'
    parser = email.parser.Parser()  # Parser 생성
    # Parser 객체의 메서드
    # parse() = email.message_from_file(fp)
    # parsestr() = email.message_from_string(s)
    with open(path) as f:
        m = parser.parse(f)  # 파일 내용을 해석
        print(type(m))
        print(m.items())  # 헤더 필드 이름과 값을 튜플 리스트로 반환

    with open(path) as f:
        s = f.read()
        m = email.message_from_string(s)
        print(m.items())

    """메시지 데이터 관리학 - email.message """
    # email.message 모듈은 메일의 데이터를 관리하는 클래스 제공
    # 메일을 표시하는 객체 email.message.Message는 보통 email.parser나 email.mime로 생성
    f = open(path)
    msg = email.message_from_file(f)
    print(type(msg))
    print(msg.is_multipart())  # 메일이 멀티파트(여러 가지 데이터를 포함)일 때 True 반환
    print(msg.get_payload())  # 페이로드(본문)을 얻음
    print(msg.keys())  # 헤더의 필드 이름을 리스트로 반환
    print(msg.get('From'))
    print(msg.as_string())  # 메시지 전체를 문자열로 반환
    f.close()


if __name__ == "__main__":
    main()

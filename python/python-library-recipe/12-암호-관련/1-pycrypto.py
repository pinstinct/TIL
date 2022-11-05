from Crypto.Hash import MD5, SHA512  # pip install PyCryptodome
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP


"""pycrypto는 AES, DES, RSA 등 다양한 암호 알고리즘 지원
암호화/복호화와 SSH 통신 공개키, 비밀키를 생성하는 목적으로 이용한다.
또한, MD5와 SHA-512등의 해시 알고리즘도 갖추고 있어 부호화와 암호화를 폭넓게 지원한다.
"""
def main():
    """"해시값 생성하기 """
    # MD5의 알고리즘 해시값 생성
    hash_md5 = MD5.new()
    hash_md5.update(b'hamegg')  # 문자열은 바이트 문자열로 전달
    print(hash_md5.hexdigest())
    # SHA-512 알고리즘 해시값 생성
    hash_sha512 = SHA512.new()
    hash_sha512.update(b'ham')
    print(hash_sha512.hexdigest())
    # 인스턴스를 생성할 때, 데이터도 전달할 수 있다
    hash_md5_1 = MD5.new(b'ham')
    print(hash_md5_1.hexdigest())
    hash_md5_1.update(b'egg')
    print(hash_md5_1.hexdigest())  # b'ham'과 b'egg'가 연결되어 b'hamegg'가 됨
    # 표준 라이브러리 hashlib를 사용한 MD5 해시값 생성
    import hashlib
    hash_md5_2 = hashlib.md5(b'hamegg')
    print(hash_md5_2.hexdigest())

    """RSA 암호화 알고리즘 이용하기 """
    # 암호화 방식에는 크게 공통키 암호화와 공개키 암호화가 있음
    # 공통키 암호 방식 알고리즘: DES, 3DES, AES
    # 공개키 암호 방식 알고리즘: RSA
    # 비밀키와 공개키 한 쌍을 생성
    rsa = RSA.generate(2048)  # RSA 키를 무작위로 생성
    private_pem = rsa.exportKey(format='PEM', passphrase='password')  # RSA 키를 작성
    with open('private.pem', 'wb') as f:
        f.write(private_pem)
    public_pem = rsa.publickey().exportKey()
    with open('public.pem', 'wb') as f:
        f.write(public_pem)


if __name__ == "__main__":
    main()

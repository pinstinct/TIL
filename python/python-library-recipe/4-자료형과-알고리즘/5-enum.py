import enum


class Dynasty(enum.Enum):
    """상수값 정의하기 """
    # 열거형은 상수값의 이름을 정의할 때 사용
    GOGURYEO = 1
    BAEKJE = 2
    SILLA = 3
    GAYA = 4
    DUPULICATED = 4


@enum.unique  # 같은 값을 지정할 수 없음
class Spam(enum.Enum):
    HAM = 1
    # EGG = 1  # ValueError


def main():
    d = Dynasty.SILLA
    print(d)
    print(d.name)
    print(d.value)

    print(list(Dynasty))  # 중복되는 열거 값은 하나만 반환


if __name__ == "__main__":
    main()

from decimal import ROUND_05UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN, Decimal, getcontext, ROUND_UP


# 정밀도 지정, 반올림, 버림 등 엄격한 규칙이 요구되는 금액 계산 등에 주로 이용
def main():
    """정밀도를 지정하여 계산하기 """
    # 지정한 값을 바탕으로 Decimal 객체를 생성
    print(Decimal('1'))
    print(type(Decimal('1')))
    print(Decimal('3.14'))
    print(Decimal((0, (3, 1, 4), -2)))  # 부호, 숫자 튜플, 지수
    print(Decimal((1, (4, 1, 4), -3)))

    print(Decimal('1.1') - Decimal('0.1'))
    x = Decimal('1.2')
    y = Decimal('0.25')
    print(x + y)
    # print(x + 1.0)  # TypeError
    x1 = Decimal('10')
    y1 = Decimal('3')
    print(x1 / y1)  # 기본 28자리
    getcontext().prec = 8  # 8자리로 변경
    print(x1 / y1)

    """숫자 반올림 방법 지정하기 """
    # 인수: 자릿수, 반올림 방법
    # 반환: Decimal 객체
    # ROUND_UP: 올림
    # ROUND_DOWN: 버림
    # ROUND_CEILING: 양의 무한대로 올림
    # ROUND_FLOOR: 음의 무한대로 내림
    # ROUND_HARF_UP: 반올림(사사오입)
    # ROUND_HALF_DOWN: 오사육입
    # ROUND_HALF_EVEN: 바로 앞 자리수가 홀수면 사사오입, 짝수면 오사육입
    # ROUND_05UP: 바로 앞 한자리수가 0 또는 5이면 올림, 그렇지 않으면 버림
    exp = Decimal((0, (1, 0), -1))
    print(Decimal('1.04').quantize(exp, rounding=ROUND_UP))
    print(Decimal('1.06').quantize(exp, ROUND_HALF_DOWN))
    print(Decimal('1.15').quantize(exp, ROUND_HALF_EVEN))
    print(Decimal('1.25').quantize(exp, ROUND_HALF_EVEN))
    print(Decimal('1.55').quantize(exp, ROUND_05UP))
    print(Decimal('1.75').quantize(exp, ROUND_05UP))


if __name__ == "__main__":
    main()

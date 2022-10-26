import random


def main():
    """난수 생성하기
    Mersenne Twister 알고리즘을 채택, 난수 생성기로 높은 평가를 받는 알고리즘 
    """
    # 0.0 ~ 1.0 사이의 float형
    print(random.random())

    # x ~ y 사이의 int형
    print(random.randint(1, 5))

    # x ~ y 사이의 float형
    print(random.uniform(1, 5))

    # 시드 고정: 실험이나 기능 테스트를 수행할 때 수치는 난수로 취득하고 싶으나 재현성이 필요한 경우
    random.seed(10)
    print(random.random())

    random.seed(10)
    print(random.random())

    print(random.random())  # 시드를 지정하지 않으면 시스템 시각이 사용

    """특정 분포를 따르는 난수 생성하기 """
    # 평균, 표준편차 정규분포를 따르는 난수 생성
    print(random.normalvariate(0, 1))

    # 형상모수, 척도모수의 감마분포를 따르는 난수 생성
    print(random.gammavariate(3, 1))

    """무작위로 선택하기 """
    l = [1, 2, 3, 4, 5]
    # 시퀀스 요소를 하나 반환
    print(random.choice(l))

    # 모집단의 샘플 k개를 구하여 새롭게 리스트를 작성
    print(random.sample(l, 2))

    # 시퀀스의 요소 순서를 셔플
    random.shuffle(l)
    print(l)
    

if __name__ == "__main__":
    main()

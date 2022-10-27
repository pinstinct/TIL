import itertools


def spam(left, right):
    return left * right


def main():
    """반복자 값을 합치기 """
    # 인수: iterable 객체, 함수(생략하면 operator.add())
    for v in itertools.accumulate([1, 2, 3], spam):
        print(v)
    
    print('=====')
    it = itertools.accumulate([1, 2, 3, 4], spam)
    print(next(it))  # 맨 처음 값
    print(next(it))  # 처음 값 * 2
    print(next(it))
    print(next(it))

    """iterable 객체 연결하기 """
    print('=====')
    it1 = itertools.chain([1, 2, 3], {'a', 'b', 'c'})
    for v in it1:
        print(v)

    """값의 순열, 조합, 직적 구하기 """
    print('=====')
    # 지정한 길이의 순열을 만드는 반복자 생성
    for v in itertools.permutations('ABC', 2):
        print(v)

    # 조합
    print('=====')
    for v in itertools.combinations('ABC', 2):
        print(v)

    # 같은 값의 중복까지 포함한 조합
    print('=====')
    for v in itertools.combinations_with_replacement('ABC', 2):
        print(v)

    # 직적(direct product, 두 집합의 원소를 뽑아 하나씩 짝짓는 것)
    print('=====')
    for v in itertools.product('ABC', [1, 2, 3]):
        print(v)

    """iterable 객체의 필터링 """
    def is_even(n):
        return n % 2 == 0
    # iterable 객체에서 특정 조건만 추출
    for v in filter(is_even, [1, 2, 3, 4, 5, 6]):
        print(v)
    # filter()와는 반대로, 지정한 함수가 거짓인 값만을 반환하는 반복자 생성
    for v in itertools.filterfalse(is_even, [1, 2, 3, 4, 5, 6]):
        print(v)
    # 두 iteralbe 객체를 지정하며, selectors에서 얻은 값이 참이면 data에서 얻은 같은 순번의 값을 반환하는 반복자 생성
    for v in itertools.compress(['spam', 'egg', 'ham'], [1, 0, 1]):
        print(v)

    """등차수열 만들기 """
    # 인수: 초기값, 증가분
    for v in itertools.count(1, 2):
        if v > 5: break
        print(v)

    """반복자에서 범위를 지정하여 값 구하기 """
    # islice()
    print(list(itertools.islice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5)))
    print(list(itertools.islice(itertools.count(1, 1), 3, 8, 2)))  # count 함수에서 1부터 1씩 증가하는 수를 생성하고, islice 함수에서 8까지 생성하도록 제한
    print(dict(itertools.islice({"a": 1, "b": 2, "c": 3}.items(), 2)))

    """같은 값을 반복하기 """
    # 지정한 값을 반복하는 반복자 생성
    print(list(itertools.repeat('a', 5)))

    # iterable 객체의 모든 값을 반복하는 반복자 생성
    for c in itertools.islice(itertools.cycle('abc'), 1, 5):
        print(c)

    """연속 값 구하기 """
    print('=====')
    # iterable 객체로부터 값을 얻어 연속하는 같은 값을 그룹으로 취합
    for value, group in itertools.groupby(['a', 'b', 'b', 'c', 'c', 'c', 'a']):
        print(value, group, tuple(group))

    """여러 iterable 객체의 요소로 튜플 만들기 """
    for v in zip((1, 2, 3), ('a', 'b', 'c'), ('가', '나')):
        print(v)
    
    for v in zip([1, 2, 3]):
        print(v)

    # 행과 열 교환
    matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    transformed = list(zip(*matrix))
    print(transformed)
    print(list(zip(*transformed)))

    # 모든 iterable 객체의 모든 값으로부터 튜플을 생성
    for v in itertools.zip_longest('abcdefg', '123', '가나다라마', fillvalue='-'):
        print(v)

    """반복자의 값 변환하기 """
    # 인수: 함수, iterable 객체
    for v in map(chr, [0x40, 0x41, 0x42, 0x43]):
        print(v)
    
    for v in map(min, 'spam', 'ham', 'egg'):
        print(v)


if __name__ == "__main__":
    main()

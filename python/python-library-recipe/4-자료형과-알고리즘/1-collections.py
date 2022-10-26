import collections


def main():
    """데이터의 횟수 세기 """
    # 사전형에서 파생된 클래스로, 사전에 데이터 건수를 카운트하는 기능을 추가한 것
    # 반환: Counter 객체
    c = collections.Counter()
    c['spam'] += 1
    c[100] += 1
    c[200] += 1
    c[200] += 4
    print(c)
    print(c.get(200))
    print(c['egg'])  # 존재하지 않는 요소를 참조해도 오류가 발생하지 않음
    print(c.most_common(2))  # 값이 큰 순서대로 키와 값 한 쌍을 list로 반환

    counter = collections.Counter(
        [1, 2, 3, 1, 2, 1, 2, 1]
    )
    print(counter)
    
    counter1 = collections.Counter(spam=1, ham=2)
    counter2 = collections.Counter(ham=3, egg=4)
    print(counter1 + counter2)  
    print(counter1 - counter2)  # 음수가 되는 요소는 포함되지 않음
    print(counter1 & counter2)  # 양쪽에 동시에 존재하는 키는 작은 쪽 값
    print(counter1 | counter2)  # 양쪽에 동시에 존재하는 키는 큰 쪽 값

    counter3 = collections.Counter(spam=-1, ham=2)
    counter4 = collections.Counter(ham=2, egg=-3)
    print(counter3 + counter4)
    print(counter3 - counter4)
    print(+counter3)
    print(-counter3)

    """여러 개의 사전 요소를 모아서 하나의 사전으로 만들기 """
    print('=====')
    d1 = {'spam': 1}
    d2 = {'ham': 2}
    c = collections.ChainMap(d1, d2)
    print(c['spam'])
    print(c['ham'])
    print(c)

    # 맨 앞에 등록한 매핑 객체에 반영
    c['bacon'] = 3
    print(d1)
    c.clear()
    print(d1)
    print(c)

    """기본값이 있는 사전 """
    # 보통 사전 객체는 등록되어 있지 않은 키를 참조하면 KeyError 예외 발생
    # collections.defaultdict는 사전에서 파생된 클래스지만, 등록되지 않은 키를 참조해도 예외가 발생하지 않음
    d = {'spam': 100}
    # print(d['ham'])  KeyError 발생

    def value():
        return 'default-value'
    d = collections.defaultdict(value, spam=100)
    print(d)
    print(d['ham'])

    # 초기 값으로 형 객체 지정
    c1 = collections.defaultdict(int)
    print(c1['spam'])
    c1['spam'] += 100
    print(c1)

    c1 = collections.defaultdict(list)
    c1['spam'].append(100)
    c1['spam'].append(200)
    print(c1)

    """등록 순서를 저장하는 사전 """
    print('=====')
    d3 = collections.OrderedDict()
    d3['spam'] = 100
    d3['ham'] = 200
    for key in d:
        print(key)

    d4 = collections.OrderedDict([('spam', 100), ('ham', 200)])
    print(d4)  # 인덱스 순서대로 기록
    d4 = collections.OrderedDict({'spam': 100, "ham": 200})
    print(d4)  # 순서가 없음
    d4 = collections.OrderedDict(spam=100, ham=200)
    print(d4)  # 순서가 없음

    """튜플을 구조체로 활용하기 """
    print('=====')
    # 메모리 사용량은 일반 튜플과 같으며, 일반 클래스 인스턴스나 사전보다 효율적으로 데이터 관리를 할 수 있음
    # 인수: 생성할 튜플형의 이름 지정, 튜플 요소 이름 지정
    Coordinate = collections.namedtuple('Coordinate', ['X', 'Y', 'Z'])
    c2 = Coordinate(100, -50, 200)
    print(c2)

    """deque(양끝 리스트) 이용하기 """
    # 큐의 맨 앞과 맨 끝에서 데이터 추가와 삭제를 등록된 데이터 수와 관계없이 일정한 속도로 수행
    # 인수: 초기값, 최대 요소 수(지정한 값 이상이 되면 요소를 맨 앞에 추가할 때는 끝에서 부터 요소를 삭제하고, 끝에 추가할 때는 맨 앞부터 요소를 삭제)
    # 반환: deque 객체(시퀀스 객체, 인덱스 사용 가능)
    deq = collections.deque('spam')
    print(deq)
    print(deq[1])
    deq[1] = 'P'
    print(deq)

    # 인덱스를 사용하여 deque 객체 중간에 있는 요소에 접근하면, 요소 수에 따라 처리에 시간이 걸리게 됨
    # 이런 처리는 리스트 객체를 사용하는 편이 빠름
    # 요소의 추가나 삭제가 큐의 맨 처음과 끝에서만 이루어지는 처리일 때 deque의 특징을 활용할 수 있음
    deq1 = collections.deque(maxlen=5)
    for v in range(10):
        deq1.append(v)  # 끝에 추가
        if len(deq1) >= 5:
            print(list(deq1), sum(deq1) / 5)

    deq2 = collections.deque('12345')
    print(deq2)
    deq2.rotate(3)  # 양의 정수를 지정하면 deque 객체 요소가 오른쪽으로 회전
    print(deq2)
    deq2.rotate(-3)  # 음의 정수를 지정하면 deque 객체 요소가 왼쪽으로 회전
    print(deq2)

    # 맨 앞 요소와 두 번째 요소를 교환하는 예
    first = deq2.popleft()  # 맨 앞 요소를 가져옴
    print(first)
    deq2.rotate(-1)  # 맨 앞 요소가 맨 뒤로 이동
    print(deq2)
    deq2.appendleft(first)  # 맨 앞에 추가
    print(deq2)
    deq2.rotate(1)  # 오른쪽을 회전해 다시 제자리로 돌림
    print(deq2)


if __name__ == "__main__":
    main()

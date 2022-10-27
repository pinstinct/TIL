import heapq


def main():
    """리스트의 요소를 작은 값부터 순서대로 가져오기 """
    # 힙큐는 우선순위 큐라고도 불리며, 리스트 중의 최소 값이 항상 리스트의 맨 앞 요소가 되는 성질이 있음
    queue = []  # heapq로 이용하는 리스트 객체
    heapq.heappush(queue, 2)  # 리스트 heap 객체에 아이템 추가
    heapq.heappush(queue, 1)
    heapq.heappush(queue, 0)
    print(heapq.heappop(queue))  # 최소값을 삭제하고 그 값을 반환 
    print(queue[0])  # 참조할 때
    print(heapq.heappop(queue))
    print(heapq.heappop(queue))
    
    """시퀀스에서 상위 n건의 리스트 작성하기 """
    q = [1, 2, 3, 4, 5]
    heapq.heapify(q)  # 요소를 heapq로 정렬
    heapq.heappushpop(q, 6)  # 값을 추가하고 최소 값을 제거
    heapq.heappushpop(q, 7)
    print(q)


if __name__ == '__main__':
    main()

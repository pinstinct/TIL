import bisect


def main():
    """이진 탐색으로 리스트에서 값 검색하기 """
    # 정렬된 시퀀스(리스트, 튜플)에서 값을 검색하여 해당 인덱스 반환
    seq = [0, 1, 2, 2, 3, 4, 5]  # 오름차순으로 정렬된 리스트
    print(bisect.bisect_left(seq, 2))  # 검색한 값의 맨 처음 인덱스
    print(bisect.bisect_right(seq, 2))  # 검색한 값의 마지막 인덱스

    """리스트를 항상 정렬 완료 상태로 유지하기 """
    bisect.insort_left(seq, 3)  # bisect_left()로 구한 위치에 삽입
    print(seq)


if __name__ == "__main__":
    main()

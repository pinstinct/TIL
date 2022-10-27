import array


def main():
    """array.array에 수치 저장하기 """
    # array.array는 요소를 파이썬 객체가 아니라 이진(binary) 데이터로 저장하기 때문에, 리스트나 튜플 등과 비교해 메모리 효율이 뛰어남
    arr = array.array('f', [1, 2, 3, 4])  # typecode: https://docs.python.org/3/library/array.html
    print(arr)
    arr.append(100.0)
    arr[2] = 200
    print(arr)
    del arr[-1]
    print(arr)
    print(sum(arr))

    """이진 데이터의 입출력 """
    arr1 = array.array('i', (1, 2, 3, 4, 5))
    with open('bin-int', 'wb') as f:
        arr1.tofile(f)


if __name__ == "__main__":
    main()

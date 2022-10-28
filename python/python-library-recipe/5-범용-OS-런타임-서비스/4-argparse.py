import argparse


def main():
    """명령줄 옵션 다루기"""
    # 두 개의 명령줄 인수를 갖는 스크립트(하나는 문자열, 하나는 정수)
    parser = argparse.ArgumentParser(description='Example command')
    parser.add_argument('-s', '--string', type=str, help='string to display', required=True)
    parser.add_argument('-n', '--num', type=int, help='number of times repeatedly display the string', default=2)
    args = parser.parse_args()  # 인수를 해석(parse)하여 얻어진 값을 변수에 저장
    print(args.string * args.num)  # 해석으로 얻은 값 다루기


if __name__ == "__main__":
    main()

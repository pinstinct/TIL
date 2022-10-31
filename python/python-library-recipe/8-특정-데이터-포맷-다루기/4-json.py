import json

from decimal import Decimal


def main():
    """JSON 인코딩과 디코딩 """
    data = [{'id': 123, 'entities': {'url': 'python.org', 'hashtags': ['#python', '#pythonkor']}}]
    # JSON 인코딩
    print(json.dumps(data, indent=2))  # JSON 형식의 str 객체 반환

    json_str = '["ham", 1.0, {"a": false, "b": null}]'
    # JSON 디코딩
    print(json.loads(json_str))  # 파이썬 객체 반환
    print(json.loads(json_str, parse_float=Decimal))  # 부동소수점 수의 취급 지정

    """JSON 인코딩과 디코딩(파일 객체) """
    # 문자열을 다루는 함수는 loads(), dumps()
    # 파일을 다루는 함수는 load(), dump()
    path = './python/python-library-recipe/8-특정-데이터-포맷-다루기/sample.json'
    # 파일 객체 중 JSON 데이터를 디코딩
    with open(path, mode='r') as f:
        json_string = json.load(f)  # 파이썬 객체 반환
    print(json.dumps(json_string, indent=2))
    
    json_string[0]['entities']['hashtags'].append('#pyhack')
    # 데이터를 JSON 포맷으로 인코딩하여 파일에 출력
    with open('dump.json', mode='w') as f:
        json.dump(json_string, f, indent=2)


if __name__ == "__main__":
    main()

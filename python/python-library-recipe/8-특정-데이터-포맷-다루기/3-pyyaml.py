import yaml  # pip install PyYAML


"""YAML 포맷의 데이터를 다루는 기능을 제공하는 PyYAML 패키지 """
def main():
    """YAML 파일 읽어오기 """
    path = './python/python-library-recipe/8-특정-데이터-포맷-다루기'
    sample = f'{path}/sample1.yml'
    file = open(sample, 'r')
    # YAML 포맷으로 작성된 파일을 읽기
    # 인수: stream(텍스트 스트림)
    # 반환: 해석한 결과의 파이썬 객체
    conf = yaml.safe_load(file)
    print(conf)  # 사전형 반환
    print(conf['database']['port'])
    file.close()

    sample2 = f'{path}/sample2.yml'
    with open(sample2, 'r') as f:
        for data in yaml.safe_load_all(f):
            print(data)

    """YAML 파일 쓰기 """
    # yaml.dump()
    # YAML 포맷 관련 인수: indent, explicit_start, default_flow_style
    hosts = {'web_server': ['192.168.0.2', '192.168.0.3'], 'db_server': ['192.168.10.7']}
    with open('dump.yml', 'w') as f:
        f.write(yaml.dump(hosts, default_flow_style=False))


if __name__ == "__main__":
    main()

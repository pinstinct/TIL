import xml.etree.ElementTree as et


def main():
    """XML 해석하기 """
    path = './python/python-library-recipe/10-HTML과-XML-다루기/sample.xml'
    # XML을 해석해 트리를 작성
    tree = et.parse(path)  
    # 요소를 트리에서 탐색하고 발견되면 Element 인스턴스를 반환(맨 처음 하나가 발견된 시점에서 탐색 종료)
    # 인수: match(트리 탐색 경로 지정, Xpath의 일부 표현 사용)
    # Xpath(http://www.w3.org/TR/xpath)
    tokyo = tree.find('./local_weather')  
    print(tokyo.tag)
    print(tokyo.attrib)
    print(tokyo.get('name'))
    tokyo_condition = tokyo.find('./condition')
    print(tokyo_condition.tag)
    print(tokyo_condition.text)
    # 한 번에 더 깊은 경로 탐색
    kanagawa_condition = tree.find('./local_weather[@name="Kanagawa"]/condition')
    print(kanagawa_condition.text)
    # 요소를 트리에서 탐색하고 발견되면 Element 인스턴스 리스트 반환
    elements = tree.findall('./local_weather')
    for element in elements:
        print(element.attrib)


if __name__ == "__main__":
    main()
    
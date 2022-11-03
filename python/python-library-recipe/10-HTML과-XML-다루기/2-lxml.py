import urllib.request

from lxml import etree, html  # pip install lxml


"""XML을 해석하는 기능을 제공하는 lxml 패키지
lxml은 처리 속도가 빠르므로 크기가 큰 파일, 많은 파일을 다룰 때 사용하기 편리
"""
def main():
    """올바른 형식이 아닌(non well-formed) XML 해석하기 """
    path = './python/python-library-recipe/10-HTML과-XML-다루기/broken.xml'
    # tree = etree.parse(path)  # 올바르지 않은 xml 파일이므로 XMLSyntaxError가 발생
    parser = etree.XMLParser(recover=True)  # XML을 해석(올바른 형식이 아닌 XML도 다룰 수 있음)
    tree = etree.parse(path, parser)
    print(tree.find('./local_weather').attrib)

    """HTML 해석하기 """
    # lxml에는 HTML 해석에 적합한 lxml.etree.HTMLParser도 있음
    url = 'https://docs.python.org/3/library/index.html'
    source = urllib.request.urlopen(url).read()
    tree = etree.fromstring(source, etree.HTMLParser())
    elements = tree.findall('.//li[@class="toctree-l1"]/a')
    for element in elements:
        print(element.text, element.attrib['href'])    

    """HTML 수정하기 """
    tree = html.parse(urllib.request.urlopen(url)).getroot()
    div_toctree = tree.find('.//div[@class="toctree-wrapper compound"]/')
    print(html.tostring(div_toctree, pretty_print=True, encoding='unicode'))

    # 각 요소의 class 속성 삭제
    for tag in div_toctree.xpath('//*[@class]'):
        tag.attrib.pop('class')

    # a 요소의 href 속성값을 절대 경로로 변경
    absolute_url = html.make_links_absolute(div_toctree, base_url="https://docs.python.org/3/library")  
    print(html.tostring(absolute_url, pretty_print=True, encoding='unicode'))


if __name__ == "__main__":
    main()

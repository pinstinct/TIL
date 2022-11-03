import re
from urllib import request

from bs4 import BeautifulSoup  # pip install beautifulsoup4


def main():
    """HTML 내 요소 정보 구하기 """
    # HTML을 해석
    # 인수: markup(해석 대상 HTML), features(parser를 지정)
    html = BeautifulSoup(request.urlopen('https://www.python.org'), features="lxml")
    print(html.title)  # title 요소 얻기
    print(html.title.text)  # title "요소 내용 얻기"
    print(html.h1)  # h1 요소 얻기
    # 요소를 탐색하여 맨 처음 발견된 하나를 반환
    # 반환: Tag 객체
    print(html.find('h1'))  # h1 요소 얻기
    print(html.h1.img)  # h1 요소의 자식요소 img 얻기
    print(html.h1.img.attrs)  # img "요소의 속성과 값 얻기"(Tag 객체에 사전으로 존재)
    print(html.h1.img['src'])  # img 요소의 src 속성 값 값 얻기
    print(html.find(id='back-to-top-1'))  # id 속성 값으로 요소 검색
    print(html.find('li', attrs={'class': 'shop-meta'}))  # 속성 이름과 값 사전으로 지정하여 검색

    """HTML 내의 링크 URL을 모두 추출하기 """
    url_list = html.find_all('a')  # 모든 a 요소 얻기
    for url in url_list:
        print(url['href'])
    docs_list = html.find_all(href=re.compile('^http(s)?://docs'), limit=2)  # limit 만큼 요소가 발견되면 검색 종료
    for doc in docs_list:
        print(doc['href'])

    """텍스트만 추출하기 """
    tag = html.find('div', attrs={'id': 'nojs'})
    print(tag)
    # 트리로부터 텍스트 부분을 추출
    # 인수: seperator(태그로 잘려있던 위치에 지정한 문자열 삽입), strip(True를 지정하면 빈 행을 제외)
    print(tag.get_text(strip=True))
    print(tag.get_text(separator='-- '))

    """HTML을 정형화하여 출력하기 """
    print(html.h1)
    print(html.h1.prettify())
    print(html.h1.prettify(formatter='html'))

    """HTML 수정하기 """
    h1 = html.h1
    h1.insert(0, 'ham')  # 0 위치에 ham 내용을 삽입
    print(h1)
    new_tag = html.new_tag('span')
    new_tag.string = 'ham egg'
    # 태그를 new_tag로 대체
    h1.img.replace_with(new_tag)  # img 태그를 대체함
    print(h1)
    # 요소의 내용을 삭제, 태그는 남음
    h1.span.clear()
    print(h1)
    # 트리에서 태그를 제거(태그의 자식 요소도 제거)
    h1.span.decompose()
    print(h1)
    # 태그를 트리에서 추출하고 제거
    h1.a.extract()
    print(h1)


if __name__ == "__main__":
    main()

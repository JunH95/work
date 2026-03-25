# Beautifulsoup 객체 method 활용
from bs4 import BeautifulSoup

html_page = """
<html><body>
<h1>제목 태그</h1>
<p>웹문서 연습</p>
<p>원하는 자료 확인</p>
</body></html>
"""

print(type(html_page))
soup = BeautifulSoup(html_page, "html.parser")
print(type(soup))
print()
h1 = soup.html.body.h1
print("h1 :", h1.string)
p1 = soup.html.body.p
print("p1 :", p1.string)
p2 = p1.next_sibling.next_sibling    # DOM 을 이용한 자료 접근 (복잡할 경우 문제 있음)
print("p2 :", p2.string)

# find method 사용
html_page2 = """
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹문서 연습</p>
<p id="my" class="our">원하는 자료 확인</p>
</body></html>
"""
soup2 = BeautifulSoup(html_page2, "html.parser")
# find(tag명, attrs, recursive, string)
print(soup2.p," ", soup2.p.string)
print(soup2.find("p").string)
print(soup2.find("p", id="my").string)
print(soup2.find(id="title").string)
print(soup2.find(id="my").string)
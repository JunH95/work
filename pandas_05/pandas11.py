# css selector이용
from bs4 import BeautifulSoup
html_page = """
<html>
<body>
<div id="hello">
    <a href="https://www.naver.com">naver</a><br>
    <span>
    <a href="https://www.daum.net">daum</a><br>
    </span>
    <ul class="world">
        <li>안녕</li>
        <li>반가워</li>
    </ul>
</div>
<div id="hi" class="good">
    두번째 div
</div>
</body>
</html>
"""
soup = BeautifulSoup(html_page, "lxml")
aa = soup.select_one("div")
print("aa :", aa, " ", aa.string)
import sys
sys.stdout.reconfigure(encoding='utf-8')

s1 = '자료1'
s2 = '두번째 자료'

print('Content-Type:text/html;charset=utf-8')

print(f"""
    <!DOCTYPE html>
    <html lang="kr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>메인</title>
    </head>
    <body>
        <h1>world 페이지</h1>
        자료출력 : {s1}, {s2}
        <br/>
        <img src="../images/dog.jpeg" />
        <br/>
        <a href="../index.html">메인으로</a>
    </body>
    </html>        
""")

# 템플레이트 엔진, 파일 
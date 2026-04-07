import MySQLdb
import pickle
import sys

# 표준 출력 인코딩을 UTF-8로 설정 (웹 브라우저 한글 깨짐 방지)
sys.stdout.reconfigure(encoding='utf-8')

# 1. DB 접속 정보 로드 (하드코딩 방지)
with open("cgi-bin/mydb.dat", mode="rb") as obj:
    config = pickle.load(obj)

# 2. HTTP 헤더 전송 (CGI 스크립트 필수 규약, 출력 후 반드시 빈 줄 필요)
print("Content-Type: text/html; charset=utf-8")
print() 

# 3. HTML 렌더링 시작
print("<html><body><b>**상품 정보**</b><br/>")
print("<table border='1'>")
print("<tr><td>코드</td><td>상품명</td><td>수량</td><td>단가</td></tr>")

try:
    # 4. DB 연결 및 작업용 커서(Cursor) 생성
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor() 
    
    # 5. SQL 쿼리 실행 및 전체 데이터 로드
    cursor.execute("select * from sangdata order by code desc")
    datas = cursor.fetchall() 
    
    # 6. 조회된 데이터를 반복하여 HTML 테이블 행(Row)으로 출력
    for code, sang, su, dan in datas:
        print('''
            <tr>
                <td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td>
            </tr>
        '''.format(code, sang, su, dan))

except Exception as e:
    # 에러 발생 시 웹 화면에 에러 내용 출력
    print("err : ", e)

finally:
    # 7. 예외 발생 여부와 상관없이 DB 연결 자원 반드시 반납
    cursor.close() 
    conn.close()

# 8. HTML 문서 종료
print("</table>")
print("</body></html>")
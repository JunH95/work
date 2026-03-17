# http.server: 파이썬에 기본 내장된 웹 서버 모듈
from http.server import HTTPServer, CGIHTTPRequestHandler

# 1. 서버가 요청을 대기할 포트(Port) 번호 설정
PORT = 8888

# 2. 요청 처리기(Handler) 클래스 정의
# CGIHTTPRequestHandler를 상속받아 정적 파일(HTML)뿐만 아니라 동적 스크립트(Python)도 실행할 수 있도록 합니다.
class Handler(CGIHTTPRequestHandler):
    # 클라이언트(웹 브라우저)가 접근할 수 있는 CGI 스크립트 폴더 경로를 지정합니다.
    # 앞서 만든 DB 연동 파이썬 파일이 바로 이 'cgi-bin' 폴더 안에 있어야 정상 실행됩니다.
    cgi_directories = ['/cgi-bin']

# 3. 웹 서버 구동 함수
def run():
    # 서버 객체 생성: ('IP주소', 포트번호)와 처리기(Handler)를 연결합니다.
    # 127.0.0.1은 내 컴퓨터(Localhost)를 의미합니다.
    serv = HTTPServer(('127.0.0.1', PORT), Handler)
    
    print('웹 서비스 진행중...... (종료하려면 Ctrl+C)')
    
    try:
        # 서버를 무한루프로 대기시키며 클라이언트의 요청을 계속 받습니다.
        serv.serve_forever()
    except Exception as e:
        # 사용자가 강제 종료(Ctrl+C)하거나 에러가 발생하면 서버를 중단합니다.
        print('서버종료')
    finally:
        # 4. 자원 반납
        # DB 연결과 마찬가지로, 웹 서버 점유를 해제하여 포트 충돌을 방지합니다.
        serv.server_close()
        
# 5. 메인 실행 블록
# 이 스크립트가 직접 실행될 때만 run() 함수를 호출합니다.
if __name__ == '__main__':
    run()
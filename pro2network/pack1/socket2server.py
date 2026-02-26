import socket
import sys

# HOST를 ''(빈 문자열)로 설정하면 현재 컴퓨터의 모든 네트워크 인터페이스에서 접속을 허용합니다.
HOST = ''
PORT = 7788

# 1. 서버 소켓 객체 생성 (IPv4 체계, TCP 통신 방식 지정)
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 2. 소켓에 IP 주소와 포트 번호를 연결 (바인딩)
    serversock.bind((HOST, PORT))
    
    # 3. 클라이언트의 접속 요청을 대기 (최대 5개의 대기열 생성)
    serversock.listen(5)
    print('서버(무한 루핑) 서비스 중...')

    # 4. 무한 루프: 서버를 끄지 않는 한 계속해서 클라이언트를 받음
    while True:
        # 5. 접속 수락 (통신을 위한 '새로운 소켓(conn)'과 '클라이언트 정보(addr)' 반환)
        conn, addr = serversock.accept()
        print('client info : ', addr[0], ' ', addr[1]) # addr[0]: IP, addr[1]: Port
        
        # 6. 클라이언트가 보낸 데이터 수신 (최대 1024바이트) 후 문자열로 해독(decode)
        print(conn.recv(1024).decode()) 
        
        # 7. 클라이언트에게 응답 메시지를 바이트(byte) 형태로 변환(encode)하여 송신
        conn.send(('from server :' + str(addr[1]) + '너도 잘지내라').encode('utf_8'))

except Exception as e:
    print('err : ', e)
    sys.exit()

finally:
    # 8. 통신이 종료되면 반드시 소켓 자원 반납
    conn.close()        # 개별 클라이언트와의 통신 소켓 닫기
    serversock.close()  # 접속을 대기하는 메인 서버 소켓 닫기
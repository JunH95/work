# socket : 소켓(Socket)은 프로세스가 네트워크 세계로 데이터를 내보내거나 혹은 그 세계로부터 데이터를 받기 위한 실제적인 창구 역할을 한다. 
# 그러므로 프로세스가 데이터를 보내거나 받기 위해서는 반드시 소켓을 열어서 소켓에 데이터를 써보내거나 소켓으로부터 데이터를 읽어들여야 한다.
# socket 이란 TCP/IP의 프로그래머 인터페이스 
# 통신 기기간 대화 가능하도록 하는 통신방식으로 클라이언트/서버 모델의 기초한다
# 연결지향 : TCP/IP
# 비연결지향 : 

# socket 통신 확인
import socket

print(socket.getservbyname('http', 'tcp'))      # www(world wide web)환경 전송 규약
print(socket.getservbyname('ssh', 'tcp'))       # 원격 컴 접속 프로토콜
print(socket.getservbyname('ftp', 'tcp'))       # 파일 전송 프로토콜
print(socket.getservbyname('smtp', 'tcp'))      # 메일 송수신 프로토콜
print(socket.getservbyname('pop3', 'tcp'))      # 이메일 프로토콜

# 0 ~ 65535 까지 있음
# 0 ~ 1024 포트번호는 사용하지 않음

# 특정 웹서버의 ipaddress 확인
print(socket.getaddrinfo('www.daum.net', 80, proto=socket.SOL_TCP))
print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))

# 도메인 네임(Domain Name)은 숫자로 된 복잡한 IP 주소(192.0.2.1 등) 대신 사람들이 기억하기 쉽게 만든 google.com 같은 웹사이트 주소


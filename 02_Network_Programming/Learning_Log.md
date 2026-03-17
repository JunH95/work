# Network Programming — 학습 노트

## 1. TCP/UDP 소켓 통신

### OSI 7계층과 소켓의 위치
```
응용 계층 (L7)  ← HTTP, FTP, SMTP
전송 계층 (L4)  ← TCP / UDP  ← 소켓이 동작하는 계층
네트워크 계층(L3) ← IP 라우팅
```

### TCP vs UDP
| 항목 | TCP | UDP |
|------|-----|-----|
| 연결 | 연결 지향 (3-way handshake) | 비연결 |
| 신뢰성 | 보장 (재전송) | 미보장 |
| 속도 | 상대적으로 느림 | 빠름 |
| 사용 | HTTP, 파일 전송 | 스트리밍, DNS |

### 소켓 기본 패턴

**서버 (Server)**
```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
server.bind(("0.0.0.0", 8080))
server.listen(5)  # 대기열 최대 5개

conn, addr = server.accept()  # 클라이언트 연결 수락 (블로킹)
data = conn.recv(1024)        # 최대 1024 bytes 수신
conn.send(b"Hello")
conn.close()
```

**클라이언트 (Client)**
```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))
client.send(b"Hello Server")
response = client.recv(1024)
client.close()
```

---

## 2. HTTP 프로토콜 구조

### HTTP 요청 구조
```
GET /index.html HTTP/1.1          ← 요청 라인
Host: www.example.com             ← 헤더
Accept: text/html                 ← 헤더
                                  ← 빈 줄 (헤더 끝)
[body - POST일 경우만]
```

### HTTP 응답 구조
```
HTTP/1.1 200 OK                   ← 상태 라인
Content-Type: text/html           ← 헤더
Content-Length: 1234              ← 헤더
                                  ← 빈 줄
<html>...</html>                  ← 바디
```

### 주요 상태 코드
| 코드 | 의미 |
|------|------|
| 200 | OK - 성공 |
| 301/302 | Redirect |
| 400 | Bad Request - 클라이언트 오류 |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## 3. CGI (Common Gateway Interface)

```
브라우저 → HTTP 요청 → 웹서버 → CGI 스크립트 실행 → 결과 → 브라우저
```

- CGI: 웹서버가 외부 프로그램(Python 스크립트)을 실행하여 동적 응답을 생성하는 초기 방식
- 단점: 요청마다 새 프로세스 생성 → 성능 저하 → 현재는 WSGI/ASGI로 대체됨
- Flask는 WSGI 기반으로 프로세스를 재사용하여 성능 개선

```python
# CGI 스크립트 예시
import cgi
print("Content-Type: text/html")
print()  # 헤더와 바디 구분 빈 줄
form = cgi.FieldStorage()
name = form.getvalue("name", "Guest")
print(f"<h1>Hello, {name}!</h1>")
```

---

## 트러블슈팅 기록

- **Address already in use**: `server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)` 추가
- **한글 깨짐**: 소켓 송수신 시 `.encode("utf-8")` / `.decode("utf-8")` 명시 필요

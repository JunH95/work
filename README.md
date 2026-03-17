# 현대로템 AI 과정 학습 포트폴리오

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?logo=mariadb&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)

> 현대로템 AI 과정에서 진행한 학습 실습 코드를 단계별로 정리한 포트폴리오 저장소입니다.
> 이론 → 구현 → 심화 순서로 구성되어 있습니다.

---

## 학습 경로 (Learning Path)

```
01_Python_Foundation/          ← Python 기초 / OOP / DB 연동
│   ├── 01_OOP_Basics/         클래스, 상속, 클로저, 모듈
│   ├── 01b_Extra_Modules/     추가 Python 모듈 실습
│   ├── 02_Database_FileIO/    파일 I/O, SQLite, MariaDB
│   └── 03_Exception_Handling/ 예외처리, 디버깅
│
02_Network_Programming/        ← 소켓 / HTTP 서버 구현
│   ├── 01_Socket_Programming/ TCP/UDP 소켓 통신
│   ├── 02_HTTP_Server/        기본 HTTP 서버 구현
│   └── 03_CGI_Advanced_HTTP/  CGI 스크립팅, 고급 HTTP
│
03_Web_Frontend/               ← HTML / CSS / JavaScript
│   ├── 01_HTML_CSS/           시맨틱 HTML, CSS 레이아웃
│   └── 02_JavaScript/         DOM 조작, 이벤트, JSON
│
04_Backend_Flask/              ← Flask 백엔드 전체
│   ├── 01_Flask_Basics/       WSGI, 라우팅 기초
│   ├── 02_Request_Response/   요청/응답 객체, 쿠키 설정
│   ├── 03_Jinja2_Templates/   Jinja2 템플릿 엔진
│   ├── 04_Template_Control/   조건/반복 템플릿
│   ├── 05_Forms_GET/          폼 데이터 수신 (GET)
│   ├── 06_Cookie_Basics/      쿠키 생성·읽기·삭제
│   ├── 07_Cookie_Auth/        쿠키 기반 로그인
│   ├── 08_Session_Basics/     세션 기초
│   ├── 09_Session_Advanced/   세션 응용 (상품 목록)
│   ├── 10_Session_Cookie/     세션+쿠키 심화
│   ├── 11_Database/           MariaDB 연동 ★
│   ├── 12_File_Upload/        이미지 업로드 처리 ★
│   ├── 13_AJAX/               AJAX 기초 (fetch API)
│   ├── 14_AJAX_Advanced/      AJAX 심화
│   ├── 15_JS_Integration/     JavaScript + Flask 연동
│   ├── 16_Advanced_DB/        고급 DB 쿼리
│   └── 17_Advanced_DB_Ajax/   DB + AJAX 통합 ★
│
archive/                       ← 기타 스크립트 보관
```

---

## 주요 프로젝트 하이라이트

| 폴더 | 주제 | 핵심 기술 |
|------|------|-----------|
| `04_Backend_Flask/11_Database` | Flask + MariaDB CRUD | SQLAlchemy, .env 환경변수 |
| `04_Backend_Flask/12_File_Upload` | 이미지 업로드 & 썸네일 | Pillow, Werkzeug |
| `04_Backend_Flask/17_Advanced_DB_Ajax` | AJAX + DB 통합 실습 | fetch API, JSON REST |

---

## 기술 스택 요약

| 분야 | 기술 |
|------|------|
| 언어 | Python 3.x, JavaScript ES6+ |
| 백엔드 | Flask, Waitress (WSGI) |
| DB | MariaDB, SQLite |
| 프론트엔드 | HTML5, CSS3, Vanilla JS |
| 보안/환경 | python-dotenv, .env 분리 |

---

## 학습 문서

각 폴더의 `Learning_Log.md`에서 해당 단계의 핵심 이론을 확인할 수 있습니다.

- [Python 기초 학습 노트](01_Python_Foundation/Learning_Log.md)
- [네트워크 프로그래밍 학습 노트](02_Network_Programming/Learning_Log.md)
- [웹 프론트엔드 학습 노트](03_Web_Frontend/Learning_Log.md)
- [Flask 백엔드 학습 노트](04_Backend_Flask/Learning_Log.md)

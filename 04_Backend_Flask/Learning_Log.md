# Backend Flask — 학습 노트

## 1. Flask 동작 원리 (WSGI)

```
클라이언트 (브라우저)
    ↓ HTTP 요청
WSGI 서버 (waitress / gunicorn)
    ↓ WSGI 인터페이스 호출
Flask Application
    ↓ URL 라우터 → 뷰 함수 호출
    ↓ Jinja2 렌더링 / JSON 직렬화
WSGI 서버
    ↑ HTTP 응답
클라이언트
```

**WSGI (Web Server Gateway Interface)**
- Python 웹 앱과 웹 서버를 연결하는 표준 인터페이스 (PEP 3333)
- `app(environ, start_response)` 형태의 콜러블(callable)
- Flask 기본 서버는 학습용, 실무에는 `waitress`(Windows) 또는 `gunicorn`(Linux) 사용

---

## 2. 라우팅 & 뷰 함수

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# 기본 라우트
@app.route("/")
def index():
    return "<h1>Hello</h1>"

# URL 변수 (Path Parameter)
@app.route("/user/<int:user_id>")
def get_user(user_id):
    return jsonify({"id": user_id})

# HTTP 메서드 지정
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        data = request.form.get("username")
```

---

## 3. Jinja2 템플릿 엔진

```html
<!-- 변수 출력 -->
<h1>{{ user.name }}</h1>

<!-- 조건문 -->
{% if user.is_admin %}
  <span>관리자</span>
{% else %}
  <span>일반 사용자</span>
{% endif %}

<!-- 반복문 -->
{% for item in items %}
  <li>{{ loop.index }}. {{ item.name }}</li>
{% endfor %}

<!-- 템플릿 상속 -->
{% extends "base.html" %}
{% block content %}
  <!-- 페이지별 내용 -->
{% endblock %}
```

---

## 4. 쿠키 (Cookie)

```python
from flask import make_response, request

# 쿠키 설정
@app.route("/set_cookie")
def set_cookie():
    resp = make_response("쿠키 설정 완료")
    resp.set_cookie("username", "홍길동",
                    max_age=60*60*24*7,  # 7일
                    httponly=True,        # JS 접근 차단
                    samesite="Lax")       # CSRF 방지
    return resp

# 쿠키 읽기
@app.route("/get_cookie")
def get_cookie():
    username = request.cookies.get("username", "Guest")
    return f"안녕하세요, {username}!"
```

**쿠키 보안 속성**
| 속성 | 역할 |
|------|------|
| `httponly=True` | JS에서 document.cookie 접근 차단 (XSS 방지) |
| `secure=True` | HTTPS에서만 전송 |
| `samesite="Lax"` | 외부 사이트 요청 시 쿠키 미전송 (CSRF 방지) |

---

## 5. 세션 (Session)

```python
from flask import session
from datetime import timedelta

app.secret_key = "강력한_비밀키_여기에"  # 세션 암호화 키
app.permanent_session_lifetime = timedelta(hours=1)

@app.route("/login", methods=["POST"])
def login():
    session.permanent = True
    session["user_id"] = 123
    session["username"] = "홍길동"
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
```

**쿠키 vs 세션 비교**
| 항목 | 쿠키 | 세션 |
|------|------|------|
| 저장 위치 | 브라우저 | 서버 |
| 보안성 | 낮음 (노출 가능) | 높음 |
| 크기 제한 | 4KB | 서버 메모리 허용 범위 |
| 용도 | 로그인 유지, 설정 | 민감한 사용자 상태 |

---

## 6. REST API 개념

| HTTP 메서드 | 의미 | 예시 URL |
|------------|------|---------|
| GET | 조회 | `GET /api/users` |
| POST | 생성 | `POST /api/users` |
| PUT | 전체 수정 | `PUT /api/users/1` |
| PATCH | 부분 수정 | `PATCH /api/users/1` |
| DELETE | 삭제 | `DELETE /api/users/1` |

```python
@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({"users": [...]})

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    # DB에 삽입
    return jsonify({"message": "생성됨"}), 201
```

---

## 7. 파일 업로드

```python
from flask import request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("image")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # 경로 탐색 공격 방지
        file.save(os.path.join(UPLOAD_FOLDER, filename))
```

**보안 포인트**
- `secure_filename()`: `../` 같은 경로 탐색 문자 제거
- 파일 타입 화이트리스트: 확장자 + MIME 타입 검증
- 업로드 폴더는 `.gitignore`에 추가하여 실제 이미지를 저장소에 포함하지 않음

---

## 8. AJAX 통신 패턴 (Flask + JavaScript)

**Flask 서버측**
```python
@app.route("/api/search")
def search():
    keyword = request.args.get("q", "")
    results = db_search(keyword)  # DB 조회
    return jsonify(results)       # JSON 응답
```

**JavaScript 클라이언트측**
```javascript
document.querySelector("#search").addEventListener("input", async (e) => {
  const res = await fetch(`/api/search?q=${e.target.value}`);
  const data = await res.json();
  renderResults(data);  // DOM 업데이트
});
```

---

## 트러블슈팅 기록

- **`RuntimeError: Working outside of application context`**: `with app.app_context():` 블록 안에서 DB 접근
- **세션이 저장 안됨**: `app.secret_key` 미설정 → 세션 암호화 불가
- **파일 업로드 500 오류**: `uploads/` 폴더 미존재 → `os.makedirs(UPLOAD_FOLDER, exist_ok=True)` 추가
- **AJAX 응답이 HTML로 옴**: 뷰 함수에서 `jsonify()` 대신 `return dict` → `jsonify()` 명시 필요

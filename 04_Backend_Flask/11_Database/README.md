# Flask + MariaDB CRUD 실습

## 프로젝트 개요

직원 정보 관리 시스템. Flask와 MariaDB를 연동하여 로그인 인증 및 직원 데이터를 조회하는 CRUD 구현 실습.

## 기술 스택

| 분류 | 기술 |
|------|------|
| 백엔드 | Flask, pymysql |
| DB | MariaDB |
| 보안 | python-dotenv (.env 환경변수 분리) |
| 세션 | Flask session + flash 메시지 |

## 핵심 구현 로직

### 1. 환경변수로 DB 접속 정보 분리
```python
from dotenv import load_dotenv
load_dotenv()  # .env 파일에서 환경변수 로드

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
```
- `.env` 파일은 `.gitignore`에 포함 → GitHub에 DB 비밀번호 노출 방지
- 팀 협업 시 `.env.example` 파일로 필요한 변수 목록만 공유

### 2. DB 연결 함수 패턴
```python
def get_conn():
    return pymysql.connect(
        charset="utf8mb4",              # 한글 + 이모지 처리
        cursorclass=pymysql.cursors.DictCursor,  # 결과를 dict로 반환
        autocommit=False                # 명시적 commit 필요
    )
```

### 3. 로그인 검증 + 세션 저장
- 폼 입력값 검증 (`.strip()`, `.isdigit()`)
- DB 조회 후 일치 시 `session["user"]`에 저장
- `flash()` 메시지로 오류 피드백 전달

## 실행 방법

```bash
# 1. 의존성 설치
pip install flask pymysql python-dotenv

# 2. .env 파일 생성 (예시)
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=mydb

# 3. 서버 실행
python app.py
```

## 학습 포인트

- `pymysql.cursors.DictCursor` 사용으로 컬럼명 키 접근 가능
- `autocommit=False` → INSERT/UPDATE/DELETE 후 반드시 `conn.commit()` 호출
- SQL Injection 방지: `%s` 플레이스홀더 사용, 절대 f-string으로 쿼리 직접 조합 금지

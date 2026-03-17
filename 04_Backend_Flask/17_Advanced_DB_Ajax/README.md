# Flask REST API + AJAX 통합 실습

## 프로젝트 개요

직원 정보 관리 시스템의 완성형 구현. Flask로 REST API 엔드포인트를 구축하고, 프론트엔드에서 JavaScript fetch API로 비동기 통신하여 페이지 새로고침 없이 CRUD를 수행.

## 기술 스택

| 분류 | 기술 |
|------|------|
| 백엔드 | Flask, pymysql |
| API 방식 | REST (JSON 응답) |
| 프론트엔드 | Vanilla JavaScript (fetch API) |
| DB | MariaDB (JOIN 쿼리) |

## 핵심 구현 로직

### 1. REST API 구조
```
GET    /api/jikwon         ← 전체 직원 목록
GET    /api/jikwon/<id>    ← 직원 1명 조회
POST   /api/jikwon         ← 직원 추가
PUT    /api/jikwon/<id>    ← 직원 수정
DELETE /api/jikwon/<id>    ← 직원 삭제
```

### 2. DB 모듈 분리
```python
# db.py — 연결 로직을 모듈로 분리
def get_connFunc():
    return pymysql.connect(...)
```
- `app.py`에서 `from db import get_connFunc`로 임포트
- DB 설정 변경 시 `db.py` 한 곳만 수정

### 3. JOIN 쿼리로 관련 테이블 데이터 통합
```sql
SELECT jikwonno, jikwonname, busername, jikwonjik, jikwonpay,
       YEAR(jikwonibsail) AS ibsayear
FROM jikwon
INNER JOIN buser ON jikwon.busernum = buser.buserno
ORDER BY jikwonno
```

### 4. AJAX 프론트엔드 패턴
```javascript
// 전체 목록 로드
async function loadList() {
    const res = await fetch("/api/jikwon");
    const json = await res.json();
    if (json.ok) renderTable(json.data);
}

// 삭제
async function deleteItem(id) {
    await fetch(`/api/jikwon/${id}`, { method: "DELETE" });
    loadList();  // 목록 갱신
}
```

### 5. 일관된 JSON 응답 형식
```python
return jsonify({"ok": True, "data": rows})       # 성공
return jsonify({"ok": False, "error": str(e)}), 500  # 실패
```

## 실행 방법

```bash
pip install flask pymysql python-dotenv

# .env 파일에 DB 접속 정보 설정 후:
python app.py
```

## 학습 포인트

- SPA(Single Page Application) 패턴: HTML은 한 번만 로드, 데이터는 AJAX로 동적 갱신
- `jsonify()` 반환 시 `Content-Type: application/json` 자동 설정
- REST 설계 원칙: URL은 명사(자원), HTTP 메서드로 동작 표현
- `with conn.cursor() as cur:` 패턴으로 커서 자동 close

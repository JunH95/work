# Python Foundation — 학습 노트

## 1. 객체지향 프로그래밍 (OOP)

### 핵심 개념
| 개념 | 설명 |
|------|------|
| 클래스 (Class) | 객체를 만들기 위한 설계도. 속성(데이터)과 메서드(행동)를 묶음 |
| 인스턴스 | 클래스로부터 생성된 실제 객체 |
| 상속 (Inheritance) | 부모 클래스의 속성·메서드를 자식 클래스가 물려받음 |
| 다형성 (Polymorphism) | 같은 메서드 이름이 클래스마다 다르게 동작 |
| 캡슐화 (Encapsulation) | 내부 구현을 숨기고 인터페이스만 노출 (`_`, `__` prefix 활용) |

### 클로저 (Closure)
```python
# 외부 함수의 변수를 내부 함수가 기억하는 패턴
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c())  # 1
print(c())  # 2  ← count 상태가 유지됨
```
- 클로저는 상태를 캡슐화하는 경량 객체처럼 활용 가능
- 데코레이터 패턴의 기반이 됨

---

## 2. 파일 I/O

```python
# 텍스트 파일 읽기 (권장 방식)
with open("data.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

# 바이너리 파일 읽기
with open("image.jpg", "rb") as f:
    content = f.read()
```

**핵심 포인트**
- `with` 블록을 사용하면 파일이 자동으로 닫힘 (`__enter__`/`__exit__` 프로토콜)
- `encoding="utf-8"` 명시가 Windows 환경에서 필수
- `csv` 모듈, `json` 모듈로 구조화 데이터 처리

---

## 3. 데이터베이스 연동

### SQLite (파일 기반, 로컬 테스트용)
```python
import sqlite3
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()
conn.close()
```

### MariaDB (실서버, pymysql 사용)
```python
import pymysql
conn = pymysql.connect(host="localhost", user="root", password="pw",
                       db="testdb", charset="utf8mb4")
```

**SQL 핵심 문법**
```sql
SELECT * FROM table WHERE condition;
INSERT INTO table (col1, col2) VALUES (val1, val2);
UPDATE table SET col = val WHERE id = ?;
DELETE FROM table WHERE id = ?;
```

---

## 4. 예외처리

```python
try:
    result = int(input("숫자 입력: "))
except ValueError as e:
    print(f"잘못된 입력: {e}")
except Exception as e:
    print(f"예상치 못한 오류: {e}")
finally:
    print("항상 실행됨")  # 파일/DB 연결 해제에 활용
```

**커스텀 예외 클래스**
```python
class ValidationError(Exception):
    def __init__(self, message, field):
        super().__init__(message)
        self.field = field
```

---

## 트러블슈팅 기록

- **UnicodeDecodeError**: `open()` 시 `encoding="utf-8"` 추가로 해결
- **DB 연결 오류**: `.dat` 파일 경로 오타, 상대경로 → 절대경로로 수정

# CLAUDE.md — 프로젝트 작업 가이드라인

현대로템 AI 과정 학습 포트폴리오 저장소의 자동화 규칙 및 작업 지침.

---

## 1. 커밋 메시지 컨벤션

모든 커밋은 아래 접두사(prefix)를 사용한다:

| 접두사 | 사용 시점 | 예시 |
|--------|-----------|------|
| `feat` | 새로운 학습 예제 추가 | `feat: AJAX 파일 업로드 예제 추가` |
| `docs` | 이론 주석·README·Learning_Log 수정 | `docs: Flask 세션 관리 이론 주석 추가` |
| `refactor` | 코드 구조 변경, 폴더 재구조화 | `refactor: pro4flask → 04_Backend_Flask 폴더 이름 변경` |
| `fix` | 버그 수정 | `fix: DB 연결 인코딩 오류 수정` |
| `chore` | .gitignore 업데이트, 의존성 변경 | `chore: .gitignore에 static/uploads 추가` |

**형식:** `<접두사>: <한글 설명> (<영어 키워드 선택>)`

---

## 2. 폴더 명명 규칙

```
<두자리_번호>_<영어_주제명>/
```

예시:
- `01_Python_Foundation/`
- `04_Backend_Flask/`
- `11_Database/`

- 번호는 학습 순서를 나타냄
- 영어 사용 (GitHub URL 호환성)
- 단어 구분은 언더스코어 `_`

---

## 3. Learning_Log.md 작성 가이드

각 주요 폴더에 `Learning_Log.md` 생성. 아래 섹션을 포함:

```markdown
# <폴더명> — 학습 노트

## 1. 핵심 개념
- 이론 설명 (표, 다이어그램 활용)

## 2. 핵심 코드 패턴
- 코드 블록 + 한글 주석

## 3. 트러블슈팅 기록
- 문제 상황 → 원인 → 해결 방법
```

---

## 4. .gitignore 자동 점검 체크리스트

새 폴더/파일 추가 시 커밋 전 반드시 확인:

- [ ] `.env` 파일이 포함되지 않았는가?
- [ ] `__pycache__/` 가 추적되지 않는가?
- [ ] `*.dat` (로컬 DB 파일) 이 추적되지 않는가?
- [ ] `static/uploads/` 업로드 이미지가 포함되지 않았는가?
- [ ] `.claude/` 폴더가 제외되어 있는가?
- [ ] `.venv/` 가상환경 폴더가 제외되어 있는가?

확인 명령어:
```bash
git check-ignore -v <파일경로>   # 특정 파일의 gitignore 적용 여부
git status --short               # 전체 변경 파일 목록
```

---

## 5. 보안 규칙

### .env 파일 처리
- `.env` 파일은 **절대 커밋하지 않는다**
- `.env.example` 파일에 필요한 환경변수 이름(값 없이)만 기록
- 팀 협업 시 `.env.example`을 참조하여 로컬에서 `.env` 직접 생성

```bash
# .env.example 예시
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=
FLASK_SECRET_KEY=
```

### SQL Injection 방지
- 쿼리에 f-string 직접 조합 금지
- pymysql의 `%s` 플레이스홀더 항상 사용:

```python
# ❌ 금지
cur.execute(f"SELECT * FROM users WHERE id = {user_id}")

# ✅ 올바른 방법
cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

### 파일 업로드 보안
- `secure_filename()` 항상 적용
- 파일 타입 화이트리스트 검증 (확장자)
- 업로드 폴더는 `.gitignore`에 포함

---

## 6. 프로젝트 추가 시 체크리스트

새로운 학습 폴더 추가 시:

1. [ ] 폴더명 규칙 준수 (`<번호>_<주제>/`)
2. [ ] 폴더 내 `README.md` 생성 (기획 의도, 실행 방법, 학습 포인트)
3. [ ] 루트 `README.md` 폴더 트리에 항목 추가
4. [ ] `.env` 사용 시 `.env.example` 함께 생성
5. [ ] `.gitignore` 체크리스트 확인 후 커밋

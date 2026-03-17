# Web Frontend — 학습 노트

## 1. HTML 구조와 시맨틱 태그

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>페이지 제목</title>
</head>
<body>
  <header>  ← 헤더 (로고, 네비게이션)
  <main>    ← 주요 콘텐츠
    <article>  ← 독립적 콘텐츠 블록
    <section>  ← 주제별 섹션
  </main>
  <footer>  ← 푸터
</body>
```

**시맨틱 vs 비시맨틱**
- 시맨틱 태그(`<header>`, `<nav>`, `<main>`, `<footer>`)는 의미를 명확히 함
- SEO 최적화와 접근성(Accessibility) 향상에 기여

---

## 2. CSS 레이아웃

### Box Model
```
[ margin ]
  [ border ]
    [ padding ]
      [ content ]
```
- `box-sizing: border-box` → padding/border를 width에 포함 (권장)

### Flexbox 핵심
```css
.container {
  display: flex;
  justify-content: center;  /* 가로 정렬 */
  align-items: center;       /* 세로 정렬 */
  flex-wrap: wrap;           /* 줄 바꿈 허용 */
}
.item {
  flex: 1;  /* 남은 공간 균등 분배 */
}
```

### CSS 선택자 우선순위
```
인라인 style (1000) > #id (100) > .class (10) > tag (1)
```

---

## 3. JavaScript DOM 조작

### 요소 선택
```javascript
const el = document.querySelector("#id");       // CSS 선택자
const els = document.querySelectorAll(".class"); // 여러 개
```

### 이벤트 처리
```javascript
el.addEventListener("click", function(event) {
  event.preventDefault();  // 기본 동작 방지 (폼 제출 등)
  console.log(event.target);  // 클릭된 요소
});
```

### fetch API (비동기 HTTP 요청)
```javascript
fetch("/api/data", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ key: "value" })
})
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

---

## 4. JSON / CSV 데이터 처리

### JSON
```javascript
// 직렬화 (객체 → 문자열)
const json = JSON.stringify({ name: "홍길동", age: 30 });

// 역직렬화 (문자열 → 객체)
const obj = JSON.parse(json);
```

### 동적 테이블 렌더링 (CSV 데이터)
```javascript
const rows = csvText.split("\n").map(line => line.split(","));
rows.forEach(row => {
  const tr = document.createElement("tr");
  row.forEach(cell => {
    const td = document.createElement("td");
    td.textContent = cell;
    tr.appendChild(td);
  });
  tbody.appendChild(tr);
});
```

---

## 트러블슈팅 기록

- **CORS 오류**: 브라우저가 다른 Origin의 요청을 차단 → Flask에서 `flask-cors` 설정으로 해결
- **`undefined` 출력**: `querySelector` 실패 (잘못된 선택자 또는 DOM 로드 전 실행) → `DOMContentLoaded` 이벤트 내부로 이동

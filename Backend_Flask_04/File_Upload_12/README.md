# Flask 이미지 업로드 & 썸네일 생성

## 프로젝트 개요

사용자가 이미지를 업로드하면 서버에서 UUID 기반 파일명으로 저장하고, Pillow 라이브러리로 썸네일을 자동 생성하여 DB에 메타데이터를 관리하는 실습.

## 기술 스택

| 분류 | 기술 |
|------|------|
| 백엔드 | Flask, pymysql |
| 이미지 처리 | Pillow (PIL) |
| 파일 보안 | Werkzeug `secure_filename`, UUID |
| DB | MariaDB |

## 핵심 구현 로직

### 1. UUID 파일명으로 보안 강화
```python
import uuid
from werkzeug.utils import secure_filename

filename = secure_filename(file.filename)           # ../../../ 등 경로 탐색 제거
ext = filename.rsplit(".", 1)[1].lower()
unique_name = f"{uuid.uuid4().hex}.{ext}"           # 충돌 없는 고유 파일명
```
- 원본 파일명을 그대로 사용하면 충돌 및 경로 탐색 공격 위험
- UUID로 완전 랜덤한 이름 생성

### 2. 썸네일 경로를 DB에 저장하지 않는 설계
```python
def thumb_rel_from_file_path(file_path: str) -> str:
    base = os.path.basename(file_path)
    return f"uploads/thumbs/{base}"
```
- 원본 경로(`uploads/xxxx.jpg`)만 DB에 저장
- 썸네일 경로는 규칙으로 항상 계산 → DB 컬럼 절약

### 3. Pillow 썸네일 생성
```python
from PIL import Image

img = Image.open(원본_경로)
img.thumbnail((240, 240))   # 비율 유지하며 최대 240×240 축소
img.save(썸네일_경로)
```
- `thumbnail()`: 원본 비율 유지, 지정 크기를 넘지 않도록 축소
- 원본 파일은 별도 보존

### 4. 파일 타입 검증
```python
ALLOWED_EXT = {"jpg", "jpeg", "png", "gif", "webp"}

def allowed_file(filename: str) -> bool:
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT
```

## 실행 방법

```bash
pip install flask pymysql pillow python-dotenv

python app.py
```

## 디렉토리 구조

```
12_File_Upload/
├── app.py
├── static/
│   └── uploads/           ← 원본 이미지 (.gitignore 처리됨)
│       └── thumbs/        ← 썸네일 이미지
└── templates/
    ├── list.html
    └── upload.html
```

## 학습 포인트

- `request.files`로 멀티파트 폼 데이터 수신
- Pillow `thumbnail()` vs `resize()` 차이: thumbnail은 비율 유지
- 업로드된 실제 파일은 `.gitignore`(`**/static/uploads/`)로 저장소에서 제외

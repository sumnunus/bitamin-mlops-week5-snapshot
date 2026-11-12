# BITAmin MLOps — Week 5 Snapshot

**5조: Docker + GitHub Actions CI/CD** · 2026-11-18 세션

4주차에 완성한 고객 이탈 예측 FastAPI를 Docker 이미지로 만들고, 코드 push 시 테스트 → 빌드 → Docker Hub 업로드까지 자동화합니다. 실제 학습 모델이 포함되어 있으며 W&B 로그인·재학습은 필요 없습니다.

> `main`은 **실습 출발 코드**입니다. API는 실행되지만 `test_main.py`의 TODO 세 개와 Dockerfile은 직접 완성해야 합니다. 출발 코드에서 pytest가 세 개 실패하는 것은 의도된 상태입니다. 완성본은 [`solution`](https://github.com/sumnunus/bitamin-mlops-week5-snapshot/tree/solution)입니다.

## 참가자 시작 순서

1. **각 조의 기존 저장소에 가져오기:** [가져오기 가이드](docs/IMPORT.md)를 따릅니다. 이 스냅샷 저장소에 직접 push하지 않습니다.
2. **로컬 실습:** [50분 실습 가이드](week5/README.md)의 STEP 0~4를 진행합니다.
3. **제출:** 각 조 저장소의 `week5/README.md`에 체크포인트 캡처·Actions 링크·Docker Hub 이미지 링크를 기록합니다.

개인 연습 저장소에 등록한 Secrets는 조별 저장소로 이전되지 않습니다. 조별 Secrets를 다시 등록해야 합니다. 공개 조별 저장소를 권장하며, 비공개 저장소는 Actions 사용 한도와 결제 상태를 먼저 확인하세요.

## 혼자 출발 코드 실행해보기

```bash
git clone https://github.com/sumnunus/bitamin-mlops-week5-snapshot.git
cd bitamin-mlops-week5-snapshot
```

Python **3.13.x**로 가상환경을 만듭니다. 이후 명령은 저장소 루트에서 실행합니다.

macOS:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r week5/requirements-dev.txt
python -m uvicorn week4.main:app --reload
```

Windows PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r week5/requirements-dev.txt
.\.venv\Scripts\python.exe -m uvicorn week4.main:app --reload
```

<http://127.0.0.1:8000/docs>에서 `POST /predict` → Try it out → Execute. 실제 모델의 예측 결과가 나오면 준비 완료입니다. 이 터미널은 `Ctrl+C`로 종료할 수 있습니다.

## 구조

```text
.github/workflows/verify-snapshot.yml  # 배포본 자체 검증용, 참가자가 가져갈 필요 없음
.dockerignore                        # 빌드 컨텍스트는 저장소 루트
docs/IMPORT.md                       # 각 조 저장소로 가져오기
docs/INSTRUCTOR.md                   # 발표조 리허설·범위·체크포인트
docs/PROVENANCE.md                   # 원본 코드·모델 출처와 SHA256
week4/                               # 공통 FastAPI·입력 스키마·학습 모델·의존성
week5/
  Dockerfile                         # STEP 2에서 완성
  test_main.py                       # STEP 1에서 완성
  requirements-dev.txt               # pytest·httpx2
  sample_request.json                # 19개 입력 필드 예시
  smoke.py                           # 실제 HTTP 예측 확인 도구
  templates/                         # Actions 워크플로 템플릿
  README.md                          # 실습과 결과 기록 양식
```

실습 중 `.github/workflows/ci.yml`을 **루트에** 만듭니다. `week5/.github/workflows/`에서는 GitHub Actions가 인식하지 못합니다.

## 단계별 코드

| 태그 | 상태 |
| --- | --- |
| `week5-start` | API·모델 제공, 테스트·Dockerfile은 TODO |
| `week5-step1` | API 테스트 세 개 완성 |
| `week5-step2` | Docker 이미지 빌드·실행 완성 |
| `week5-step3` | 자동 테스트·빌드·컨테이너 HTTP 검증 |
| `week5-final` | Docker Hub 멀티 아키텍처 자동 업로드 포함 |

태그별 복구는 [실습 가이드](week5/README.md#막혔을-때-단계별-복구)를 따릅니다. 태그는 파일 복구용이며 체크아웃한 태그에 직접 작업하지 않습니다.

## 이번 실습의 배포 범위

`git push → pytest → Docker Build → Docker Hub Push`까지 자동화합니다. Docker Hub의 이미지를 PC에서 `pull`·`run`하여 서비스 실행을 확인합니다. 원격 운영 서버의 컨테이너를 자동 교체하는 단계는 선택 확장입니다.

출발 모델은 5조의 4주차 결과물로 통일합니다. 각 조 모델을 쓰는 확장은 공통 모델로 전 과정을 통과한 뒤 진행하세요. 모델마다 학습 환경·스키마가 달라질 수 있습니다.

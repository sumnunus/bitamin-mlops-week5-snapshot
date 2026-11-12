# 발표조 운영·리허설

## 범위와 운영 원칙

- 5조 기존 저장소는 주차별 결과물용으로 유지하고, 이 저장소는 참가자 배포용으로 사용합니다.
- `main`은 출발 코드, `solution`은 완성 코드입니다. `week5-*` 태그는 복구 가능한 고정 기준점입니다.
- 공통 모델로 먼저 진행하여 4주차 조별 모델·스키마 차이가 CI/CD 실습을 막지 않게 합니다.
- 기본 실습은 Test → Build → Registry Push입니다. 원격 서버 자동 교체는 선택 확장입니다. 운영진이 서버 자동 배포를 필수로 요구하면 별도 서버·인증·복구 절차를 추가합니다.
- 사전 세팅의 개인 연습 저장소와 세션의 조별 제출 저장소를 구분합니다. 조별 Secrets를 다시 등록하고 업로드 활성화 Variable 하나를 추가합니다.

## 세션 전 준비

1. `Verify snapshot (instructor)` Actions에서 amd64·arm64 두 러너 모두 테스트·Docker 빌드·실제 HTTP 예측이 성공했는지 확인합니다.
2. 아래 Docker Hub 리허설을 실행합니다.
3. 참가자와 동일하게 기존 조별 저장소의 복사본에 `week5-start`를 가져와 봅니다. 4주차 캡처·이전 주차 파일 보존을 확인합니다.
4. 50분 안에 도달하도록 대표자·파일 담당을 정하고, 모델 추론과 pytest부터 실행합니다.
5. 문제가 생기면 공통 모델·새 가상환경으로 돌아오고 단계별 태그에서 파일만 복구합니다.

## Docker Hub 리허설

발표조 대상 이미지: **`sumnunus/bitamin-mlops-week5`**.

Secret 값은 GitHub 웹 Settings에서 등록합니다. GitHub의 기존 Secret 값은 읽어올 수 없으며 다른 저장소로 자동 이전되지 않습니다.

이 배포용 저장소는 기본 브랜치가 starter인 `main`이므로, 별도 `Rehearse Docker Hub (instructor)` 워크플로가 solution 코드로 테스트·양쪽 CPU Docker 검증 후 업로드합니다. 일반 참가자용 ci.yml의 기본 브랜치 조건을 바꾸지 않고 검증하기 위한 것입니다.

| 종류 | 이름 | 값 |
| --- | --- | --- |
| Secret | `DOCKERHUB_USERNAME` | `sumnunus` |
| Secret | `DOCKERHUB_TOKEN` | 본인 Read & Write 토큰 |
| Variable | `ENABLE_DOCKERHUB_PUSH` | `true` |
| Variable | `DOCKERHUB_IMAGE` | `bitamin-mlops-week5` |

Docker Hub 공개 저장소를 먼저 만든 뒤 Actions → **Rehearse Docker Hub (instructor)** → Run workflow (`main`)를 실행합니다. `verify`의 운영체제·CPU별 검증, `publish`, 두 CPU의 `verify-published`까지 모두 성공했는지 확인합니다. 마지막 단계는 업로드된 SHA 태그 이미지를 각 CPU에서 실제로 pull하고 예측 API를 호출합니다. 운영 증거는 [검증 기록](VALIDATION.md)에 연결합니다.

## 실패 시 차단 시연

발표 중 3분 시연을 권장합니다. 리허설용 작업 브랜치에서 `test_root`의 예상 메시지를 틀리게 바꾸고 push합니다. test 실패 → build가 skipped인 것을 확인합니다. 테스트를 올바르게 돌리고 다시 push해 성공을 확인합니다. 참가자 제출 브랜치나 고정 태그를 수정하지 않습니다.

## 채점 체크포인트

CP1 API → CP2 pytest → CP3 Docker 실행 → CP4 자동 테스트·빌드 → CP5 자동 업로드와 pull 실행. CP5는 publish가 skipped이면 통과가 아닙니다. 자기 조 저장소 이름·실행 커밋·Docker Hub 이미지가 연결되어 있어야 합니다.

## 일정

- 2026-11-13 23:59 KST: Snapshot repository 제출
- 2026-11-16 23:59 KST: 발표자료·체크포인트 리스트 제출
- 2026-11-18: 발표 50분 + 실습 50분

스냅샷 제출 안내 예시:

> 5조 Docker + GitHub Actions CI/CD 실습 스냅샷입니다. main은 출발 코드, solution은 완성 코드이며 week5-start~week5-final 태그로 단계별 복구가 가능합니다. README의 가져오기 가이드에 따라 각 조 기존 저장소에서 진행합니다. 모델 파일이 포함되어 재학습·W&B 인증 없이 시작할 수 있습니다. 워크플로는 루트 .github/workflows/ci.yml에 작성합니다.

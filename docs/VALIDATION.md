# 배포 검증 기록

이 문서는 발표조의 검증 기록입니다. 참가자의 CP 캡처를 대신하지 않습니다.

## 확인 대상

- Python 3.13 가상환경의 공통 모델 로드·실제 예측
- 완성 테스트 세 개 통과 / 출발 테스트 세 개는 안내된 TODO로 실패
- Linux amd64·arm64 각각의 패키지 설치, Docker 빌드, 컨테이너 HTTP 예측
- 기존 조별 저장소로 가져올 때 이전 주차·4주차 캡처 보존
- Docker Hub 멀티 플랫폼 업로드와 업로드 이미지의 실제 API 실행

## 확인 결과 — 2026-11-12 KST

| 항목 | 결과·증거 |
| --- | --- |
| macOS 로컬 Python 3.13.12 | 실제 모델 추론·API 테스트 3 passed, 경고를 오류로 처리해도 통과 |
| Windows 2025·macOS 15 / Python 3.13 | 테스트·기존 week4 실행 위치 호환성 모두 성공 |
| Linux amd64·arm64 / Python 3.13 | 테스트·Docker 빌드·컨테이너 실제 HTTP 예측·starter TODO 확인 모두 성공 |
| 출발 상태 | 실제 API 실행 가능, pytest는 의도된 TODO 세 개만 실패 |
| 기존 조별 저장소 가져오기 | 5조 원본 복사본에서 이전 주차와 4주차 증거 44개 파일의 SHA256 일치, 모델 추적·단계별 복구 확인 |
| 테스트 실패 시 중단 | 의도적으로 test 실패 → build·publish 모두 skipped |
| 워크플로 구문 | actionlint 1.7.12 통과 |
| 서버 시작 대기 | 초기 connection reset·disconnected·refused 상태 재시도 후 예측 확인 |

- [4개 운영체제·CPU 러너 검증 성공](https://github.com/sumnunus/bitamin-mlops-week5-snapshot/actions/runs/43163952232)
- [참가자 완성 워크플로 test·build 성공](https://github.com/sumnunus/bitamin-mlops-week5-snapshot/actions/runs/43163952525) — solution은 기본 브랜치가 아니므로 publish는 의도적으로 skipped.
- [실패 시 차단 시연](https://github.com/sumnunus/bitamin-mlops-week5-snapshot/actions/runs/43163791202) — 이 실행의 failure는 의도된 테스트이며, 임시 시연 브랜치는 정리했습니다.

## Docker Hub 전체 리허설 — 성공

- [전체 리허설 실행](https://github.com/sumnunus/bitamin-mlops-week5-snapshot/actions/runs/43165450034): 7개 job 모두 성공.
- Windows·macOS API 테스트, Linux 두 CPU의 테스트·Docker 검증 후 레지스트리 업로드까지 연결했습니다.
- [공개 Docker Hub 이미지](https://hub.docker.com/r/sumnunus/bitamin-mlops-week5/tags): `latest`와 `4177575ea01f20b6ee6d973b79c2a56f9009b220` 태그.
- Manifest digest: `sha256:5eda4e67e1ab70663ef7fa4bddb66fd97e58f9a4dc8b64f4b949bb9afe9cbe81`.
- 플랫폼: `linux/amd64`, `linux/arm64`.
- 업로드 후 두 CPU의 별도 러너가 SHA 태그 이미지를 실제로 pull·run하고 GET `/`·POST `/predict`를 검증했습니다.
- 양쪽 CPU의 응답: `{"churn": 1, "churn_probability": 0.80412358901082}`.
- 첫 멀티 플랫폼 빌드·업로드는 약 4분 35초, 전체 검증은 약 7분이 걸렸습니다. 네트워크·러너 대기 시간에 따라 달라질 수 있습니다.

단순 빌드 성공이나 skipped 업로드를 성공으로 대체하지 않았습니다. 이번 범위는 이미지 자동 전달과 실제 실행 확인이며, 원격 운영 서버의 컨테이너 자동 교체는 포함하지 않습니다.

발표 준비 중 발견한 Docker 시작 직후 연결 초기화 문제는 공통 `smoke.py`에 시작 대기를 추가해 수정했습니다. `week5-*` 태그에도 배포 전 수정을 반영했습니다. 최종 배포 이후 태그를 이동하지 않고 새 버전으로 수정합니다.

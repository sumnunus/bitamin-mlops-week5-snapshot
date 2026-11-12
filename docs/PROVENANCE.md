# 코드·모델 출처

- 원본: <https://github.com/sumnunus/bitamin-mlops-5>
- 원본 커밋: `0f177d111f79126f78e26c7cb7b0c25c82e88234`
- 기준 파일: `week4/main.py`, `schema.py`, `requirements.txt`, `churn_model.joblib`
- 모델 SHA256: `c12cc04bb6efb544301b76111f02f416bd1e6da38c1ba0bf534883feb3081964`
- 모델 크기: 1,944,891 bytes

모델과 스키마는 원본에서 가져왔습니다. main.py는 파일 위치 기준 모델 로드와 패키지 import를 지원하도록 정리했습니다. GET `/`, POST `/predict`와 19개 입력 필드는 유지합니다. 런타임 주요 패키지 버전은 원본 4주차에 맞춥니다. 테스트 의존성 pytest와 httpx2는 별도로 제공합니다.

학습·데이터 수집은 이 실습의 범위가 아닙니다. 원본 모델은 신뢰할 수 있는 발표조 제공 파일로 사용합니다. 모델 파일이 없는 상태의 모의 API나 빈 모델로 대체하지 않습니다.

참고 구조: [3조 스냅샷](https://github.com/0jin03/bitamin-mlops-week3-snapshot)의 출발 코드·solution·단계별 복구 방식. W&B 기능이나 API 키는 이번 코드에 포함하지 않습니다.

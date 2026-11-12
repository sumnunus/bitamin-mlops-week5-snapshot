# 각 조의 기존 저장소로 가져오기

조별 대표자 한 명이 공통 출발 코드를 가져와 push하고, 다른 조원들은 그 코드를 pull합니다. 각 조의 기존 `week1`~`week3`와 4주차 캡처는 보존합니다.

## 1. 기존 작업 저장

각 조의 로컬 `bitamin-mlops-{조번호}` 폴더로 이동한 뒤:

```bash
git status
git branch --show-current
```

변경 파일이 있으면 먼저 검토하여 커밋합니다. 아직 커밋할 수 없는 변경은 별도로 백업한 뒤 진행하세요. **아래 가져오기는 공통 API 코드·모델을 덮어씁니다.** 기존 4주차 코드는 현재 커밋에 남겨두고, 새 브랜치에서 작업합니다.

```bash
git switch -c feature/week5-cicd
git remote add week5-snapshot https://github.com/sumnunus/bitamin-mlops-week5-snapshot.git
git fetch week5-snapshot --tags
```

이미 remote가 있으면 `git remote get-url week5-snapshot`으로 주소를 확인하고 `remote add`를 생략합니다. 이미 작업 브랜치가 있다면 새 이름으로 만드세요.

## 2. 출발 파일 가져오기

아래 명령은 macOS 터미널·PowerShell에서 동일합니다. 캡처 폴더를 지우지 않도록 `week4/` 전체 대신 파일을 개별 지정합니다.

```bash
git restore --source week5-start -- week4/__init__.py week4/main.py week4/schema.py week4/churn_model.joblib week4/requirements.txt week5 .dockerignore
git add week4/__init__.py week4/main.py week4/schema.py week4/requirements.txt week5 .dockerignore
git add -f week4/churn_model.joblib
git diff --cached --stat
git commit -m "Add week5 common starter"
git push -u origin feature/week5-cicd
```

기존 `.gitignore`에 `*.joblib`가 있을 수 있어 공통 모델은 `git add -f`로 포함합니다. 기존 루트 Dockerfile·requirements.txt는 이전 주차용이므로 그대로 두고, 이번에는 **반드시 `-f week5/Dockerfile`과 주차별 requirements 경로**를 사용합니다. 루트 `.dockerignore`는 이번 공통 파일로 교체됩니다.

`week5`가 이미 존재하거나 `.github/workflows/ci.yml`이 이미 있다면 덮어쓰기 전에 기존 파일을 검토하고 백업하세요. 기존 CI가 있다면 이번 파일 이름을 `week5-ci.yml`로 바꿔도 됩니다.

다른 조원은 원격 작업 브랜치를 가져옵니다.

```bash
git fetch origin
git switch --track origin/feature/week5-cicd
```

## 3. 실습·기본 브랜치 반영

[실습 가이드](../week5/README.md)를 진행합니다. 대표자가 변경을 모아 작업 브랜치에 push하고, PR로 조별 저장소의 **기본 브랜치**에 병합합니다. 기본 브랜치 이름은 `main`·`master` 중 실제 설정을 사용하세요. Docker Hub publish는 기본 브랜치에서 실행됩니다.

충돌 방지를 위해 Dockerfile·테스트·워크플로 담당을 나누고 같은 파일의 동시 편집은 피하세요. 각 조의 스크린샷과 결과 링크는 자기 조 저장소에 기록합니다.

## 4. 조별 계정 설정

1. 자기 조 저장소의 **Settings → Secrets and variables → Actions → Secrets**에서 `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`을 등록합니다.
2. 같은 화면의 **Variables** 탭에 `ENABLE_DOCKERHUB_PUSH`를 값 `true`로 등록합니다.
3. Docker Hub에 팀 계정 소유의 **공개** 저장소 `bitamin-mlops-week5`를 만듭니다.
4. 다른 이름을 쓸 때만 Variable `DOCKERHUB_IMAGE`에 **저장소 이름만** 입력합니다. 예: `bitamin-mlops-week5-team2` (Docker ID와 `/`는 제외).

`DOCKERHUB_USERNAME`은 표시 이름·이메일이 아닌 Docker ID입니다. 토큰은 해당 계정의 Read & Write 권한이 필요합니다. GitHub 저장소 Secrets는 개인 연습 저장소나 원본 스냅샷에서 자동 복사되지 않습니다.

### 토큰 값을 기억하지 못할 때

기존 토큰이 활성 상태이고 만료되지 않았으며 팀 Docker ID의 Read & Write 권한이라면 재사용할 수 있습니다. 단, Docker Hub와 GitHub Secrets에서는 이미 저장한 토큰 값을 다시 조회할 수 없습니다. 값을 보관하지 않았다면 새로 발급합니다.

1. Docker Hub에 팀 계정으로 로그인 → 프로필 → Account settings → Personal access tokens를 엽니다.
2. Generate new token → 설명은 `week5-github-actions`, 만료일은 발표·제출 기간을 포함하도록 정합니다. 예: 30일.
3. 이미지 저장소 권한을 **Read & Write**로 선택하고 Generate를 누릅니다.
4. 생성 직후 표시되는 값을 복사하여 자기 조 GitHub 저장소의 `DOCKERHUB_TOKEN` Secret에 붙여넣습니다.
5. Secret 이름 목록에 등록된 것을 확인합니다. 토큰 값은 채팅·README·캡처에 넣지 않습니다.

발급 화면을 닫으면 값을 다시 볼 수 없으므로 필요한 경우 자격 증명 관리자에 보관합니다. [Docker 공식 발급 안내](https://docs.docker.com/security/access-tokens/personal-access-tokens/)

`ENABLE_DOCKERHUB_PUSH`가 없으면 `publish` job은 **skipped**입니다. 이 상태는 이미지 업로드 체크포인트 통과가 아닙니다. 두 Secret과 Variable을 등록한 뒤 기본 브랜치에 새 커밋을 push하거나 Actions의 **Run workflow**를 기본 브랜치에서 실행하세요.

기존 저장소에서 Actions가 꺼져 있으면 Actions 탭 또는 Settings → Actions에서 활성화합니다. Fork를 사용하는 경우에도 Actions 활성화와 자기 저장소 Secrets 등록은 직접 해야 합니다.

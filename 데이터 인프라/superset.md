# Dashboard Tool
- 구글 시트, 엑셀 - 여전히 가장 많이 쓰는 시각화 도구
- Tableau, Power BI, Redash, Looker ,Apache Superset(오픈소스)
- 유료이지만 마켓리더인 Tableau, 구글이 인수한 Looker,오픈소스인 superset, 윈도우 Power BI
- 그 외에 python, mode analyics와 같은 '개발자' 친화적 도구도 있음

## SuperSet 설치
- SuperSet을 사용하는 방법은 2가지가 있음
- Docker를 활용한 오픈소스 사용
- 웹 방식으로 접속(유료, 일부 무료 제공)하는 것 - https://preset.io/

### Docker를 통해 Superset을 설치하여 사용함
- Docker를 설치(운영체제에 맞게 다운로드) - https://docs.docker.com/desktop/
- Docker를 실행(=엔진 Start)
- 여기까지는 Docker 인터넷 검색, 다운로드 & 더블클릭
- 다음으로는 git에서 superset 오픈소스를 clone하여 local환경에 다운로드-- clone
- 오픈소스 폴더로 들어가서 도커 이미지 불러오기-- pull
- 도커 이미지를 도커 엔진을 활용하여 도커 컨테이너에 올리기 -- up
- localhost:8088에 접속하여 superset을 실행
- shell 명령어
```bash
# Docker를 다운로드 받고, 엔진을 실행한 상태에서 다음 작업을 진행합니다. 

# git에서 오픈소스를 다운로드 받습니다.
git clone https://github.com/apache/superset.git

# superset 폴더로 이동 - 예를들어 Desktop이 폴더인 쉘에서 위 git clone 명령을 치면 superset 폴더가 하위에 생깁니다.
# 아래 명령어는 Change Directory의 약자로 작업폴더를 superset으로 이동하는 것입니다.
cd superset

# Docker Image 끌어와줘!
docker-compose -f docker-compose-non-dev.yml pull

# Docker Image 컨테이너에 올려줘!
docker-compose -f docker-compose-non-dev.yml up
# Docker를 쓰는 목적은 프로그램이 어떤 환경에서 잘 작동할 수 있도록, 가상의 환경(컨테이너)를 제공하는 것이다.

# 이 컨테이너를 운영하기 위해서 Docker 프로그램이 있고, '컨테이너'라는 환경을 기록한 문서를 'Image'라고 부른다. 그리고 다시 'Image' 환경을 기록한 문서를 작성하기 전 파일을 Dockerfile이라고 한다.

# 그래서 개발할때는 순서가 반대로 된다. Dockerfile 생성 -> 명령어 -> Image 파일 -> Container 이런 형태로 이루어진다. 
```
 

## Superset 실습

- Database : redshift // 다만 localhost:8088에서 연결을 시도할 때 redshift database가 없기 때문에 postgresql라고 가정하고 연결한다.
- Database -> superset 시각화
- 주요 개념으로는 Dataset(이용할 Table) - chart(Dataset을 이용하여 만듬) - Dashboad(chart의 집합) 이렇게 3개가 있다.
# AWS Redshift에 관하여
Redshift는 AWS의 데이터 웨어하우스이다. 이야기 하기전에 BigQuery, Mysql, Postgresql처럼 왜 데이터관련 단어가 아닐까 궁금했다. 찾아본 결과 고민의 흔적이 보였다. "Redshift"라는 이름은 데이터의 색상 변화를 의미하며, 빠른 데이터 분석과 질의 실행 속도를 강조하기 위해 선택되었다. "Redshift"는 빛의 스펙트럼에서 붉은색은 더 낮은 주파수 및 긴 파장을 가짐을 나타내는데, 이는 더 빠른 데이터 처리와 분석을 의미합니다. 그럼 데이터 웨어하우스의 이론과 실습 관련 내용에 대해 알아보면 좋을 것 같다.

## AWS Redshift : 이론편
특징

최대 2PB ~ 최소 160GB의 스토리지를 제공하며, 고정비용 형태이다. 다만, 최근 가변비용 형태도 나왔다. OLAP(OnLine Analytics Processing)으로 속도 보다는 대량의 데이터 처리에 목적이 있다. 그래서 빠른 처리를 요하는 프로덕션 데이터베이스와는 차이가 있다.

컬럼기반 스토리지로 컬럼별 압축이 가능하다. 벌크 업데이트 지원하는데, 벌크 업데이트란 INSERT를 통해 레코드를 저장하는 것이 COPY 명령을 통해 한번에 데이터 웨어하우스로 저장하는 것을 말한다. Primary key는 설정에 쓸 수 있지만 중복키를 막아주진 않는다. 그럼에도 Primary key로 컬럼이 쓰인 것을 알면 Join 할 때 참고가 되기 때문에 유용해보인다. '고정비용'형태에서 용량관리를 스스로 해야한다.

## 스케일링 방식

데이터 웨어하우스를 사용 하는 중에 용량이 부족하면 새로운 노드 즉, 컴퓨팅 자원을 추가해야 한다. 어떻게 해야할까? 한대의 자원을 늘리거나 동등한 두개의 자원을 엮어 이러한 문제를 해결할 수 있는데 이를 Resizing이라고 한다. 노드의 사양을 늘리는 것을 scaleup이라고 한다. 노드의 수를 추가하는 것을 Scaleout이라고 한다. 잠깐 생각해보면 scaleup 방법이 훨씬 쉬워보인다. 왜냐하면 두 대의 노드를 묶은 클러스터는 그 노드의 통신과 다른 설정 등을 처리해야하는 부분이 1대의 노드를 다룰 때 보다 많아 보이기 때문이다. 그러나 역시 문제는 '돈'이다. 그래서 무한정 Scaleup을 할 수 는 없다.

AWS에서 Redshift 고정비용 옵션에서는 이러한 문제를 누가 담당할까? 사용하는 '누군가'가 설정해야 한다. 이러한 문제를 다루고 싶지 않다면 BigQuery로 옮기는 것을 고려해볼 수 있다. 왜냐하면 BigQuery 데이터 웨어하우스는 용량이 부족할 때 알아서 '잘' 해주기 때문이다. 이것을 autoscaling이라고 한다. 물론 redshift '가변비용' 옵션에서는 'autoscaling' 옵션이 있다고 하니 이 방법도 고려해볼 수 있다.

## 레코드 분배와 저장 방식

좋은 서비스는 비싸다. 용량의 증감에 따라 자동으로 컴퓨팅 자원을 다루어주고, 쓴 만큼 돈을 내는 가변 비용은 정말 비싸다. Money가 부족하다면 Redshift 환경에서 어떻게 레코드(행)를 노드에 나누어 저장해야 하는지 알아보고 해결해야 한다. DISTSTYLE, DISTKEY, SORTKEY로 설명해볼 수 있는데, 여기서 DIST는 Distribution의 약자로 노드 별로 분산을 뜻한다. DISTSTYLE에는 3가지가 있다. default인 방식인 even과 all, key 방식이 있다. even은 3개의 노드가 있다고 할때 1행은 1번 노드에, 2행은 2번 노드에, 3행은 3번 노드에, 4행은 1번 노드에 .... 이렇게 '균등'하게 분배되는 방식이다. all 방식은 1번 에도 1행,2행,3행 을 저장, 2번 노드에도 1행,2행,3행 을 저장하는데 데이터를 복제 하는 방식이다. 마지막으로 Key 방식이 있다. 특정 Key를 기준으로 저장할 노드를 분배한다. DISTKEY와 SORTKEY는 DISTSTYLE이 key인 경우에만 쓰인다. DISTKEY는 어떤 컬럼을 기준 키로 삼을 것인지를 정하고, SORTKEY는 분배된 노드에서 어떤 컬럼을 기준으로 정렬한 것인지를 정한다.

 어떤 것이 완벽하게 좋다고 할 수 는 없다. All방식은 안정성이 다른 무엇보다 좋아보인다. even은 특정 노드에 쏠림현상이 없어 좋아보이지만 group By의 성능이 좋지 않다. key방식은 특정 노드에 데이터 쏠림현상이 있을 수 있다. 이를 skew(data 불균형)라 한다.

## Redshift 사용하기

1. S3에 CSV를 업로드 한다.

2. S3 저장소에 있는 CSV파일을 COPY 하여 redshift 저장한다. 

## AWS Redshift : 실전편 [설치]
0. S3

S3는 버킷(폴더)을 생성해두자. ex)yourid_etl_process 등

1. AWS Redshift 인스턴스 생성
AWS에 접속한 후, Redshift를 검색하여 무료로 serverless 환경을 이용하자.
기본 - 기본 등으로 누르면 큰 문제 없이 생성될 것이다.

2. AWS redshift에서 S3에 접근할 수 있도록 허용하기

I AM 설정
IAM 서비스를 검색하여 들어간다. 왼쪽 엑세스 관리 - > 역할 -> 역할 생성 -> (AWS 서비스, 다른 AWS 서비스의 사용 사례 선택 옵션에서 Redshift, Redshift - Customizable) -> AmazonS3FullAccess 검색, 체크 ->  알아보기 쉬운 이름으로 저장 ex) redshift.access.s3 등

Redshift와 IAM 설정 연결
redshift 서비스에서 default namespace를 눌러 보안 및 암호화로 들어간 다음 IAM 역할관리 누른다. IAM 역할관리 - IAM 역할 연결을 누른다. 이미 생성한 IAM 역할을 누른 후 저장버튼을 누른다.

3. redshift로 인바우드 되도록 네트워크 설정

redshift 서비스 메인으로 온다. '작업그룹' - default를 누른다. 조금 아래로 내리면 '네트워크 및 보안' - VPC 보안 그룹을 클릭한다. 인바운드규칙 - 인바운드 규칙 편집 - (사용자지정 TCP, 허용 포트 5439, ipv4, 0.0.0.0 으로 설정) 즉 모든 5439로 들어오는 모든 IP에 오픈하겠다!

## AWS Redshift : 실전편 [COPY]
1. s3에 방금 만든 버켓에 CSV파일을 넣는다.
2. colab환경에서 접속한다.
- %load_ext sql
- !pip install sqlalchemy==1.4.47
- 런타임 재실행 후 위에 명령어 다시 실행
- %sql postgresql://id:pw@주소:5439/dev    // 이 때 주소는 redshift -> 작업 그룹 클릭 후 오른쪽 endpoint 복사
3. 스키마를 만들고, 그 안에 테이블을 만들고, COPY명령어로 S3에서 데이터를 가져오자.

```sql
%%sql
 
CREATE SCHEMA raw_data;
%%sql
 
CREATE TABLE IF NOT EXISTS raw_data.session_timestamp(
sessionid varchar(32) primary key,
ts timestamp);
%%sql

COPY raw_data.session_timestamp
FROM 's3://your_bucket_name/session_timestamp.csv'
credentials 'aws_iam_role=your_access_ID'
delimiter ',' dateformat 'auto' timeformat 'auto' IGNOREHEADER 1 removequotes;
```
-- 이때 your_access_ID는 s3접근권한으로 redshift namespace -> 보안 및 암호화 -> s3접근을 허용하는 정책이름의 ARN을 복사하면 된다. credentials 옵션을 통해 다시 한번 인증을 한다고 생각하면 된다.
-- delimiter 는 CSV가 ,로 구분되어 있어서 ,를 기준으로 나누겠다는 것이다.
-- IGNOREHEADER 는 1번째 행은 데이터가 아니라서 없애겠다는 것이다. 
-- removequotes 옵션은 데이터에 ""가 있으면 삭제하겠다는 것이다.
이렇게 하면 S3에서 redshift로 벌크 업데이트를 수행할 수 있다.


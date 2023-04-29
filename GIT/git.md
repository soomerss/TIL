4/26 : 소프트웨어 개발 과정 소개
4/27 : 깃허브 소개와 깃허브 실습
4/28 : 테스트 추가와 CI/슬랙 연동

현업에서 
## HOW to plan
### 1. waterFall 모델
> 요구조건은 계속해서 변화한다.
> 디자인시 모든 문제를 미리 알 수 없다.
> water-Fall 모델은 소프트웨어 개발에 부적합
> 요구조건 - 디자인 - 개발 - 테스트 - 릴리스 - 유지보수
> 대규모 프로젝트일수록 디자인에 걸리는 시간이 길어지며 그 기간사이에 요구조건 바뀔 수 있다.

### 2. Agile 모델
> 방법론 1
* 보이는 만큼 빠르게 요구조건 - 디자인 -개발 - 테스트 -릴리스 - 유지보수 한사이클을 돌자(1주)
* 빠르게 하고 싶으면 CI/CD가 필요함

> 방법론 2 
* 작업별로 우선순위 결정 - PM이 담당하며, Grooming이라고 함, 각 작업별로 중요도와 복잡도 결정
* 사이클에 일할 작업결정
* 화이토브드에 TO do Inprogress Testing Done 그 옆(backlog)에는 우선순위별로 정렬되어잇음(이게 가장 우선)
* TO do, In progress, Testing, Done
* 스탠드업 미팅 - 10~15분씩 모여 각자 상황 공유(각자 2~3분) , 논의 더 하고 싶으면 따로, 그 후로 무엇을 했나
* Retrospective * Demo(자랑이 섞여도 좋은듯) 미팅

> 스프린트 카드 예제
* 타이틀
* 세부설명
* 포인트(숫자) - 점수를 준다음에 평균에 맞춘다. 태스크 포인트 이상하게 하지말자
* 성공의 정의 - 
* 체크리스트 - 이 작업이 성공적으로 끝나는데 필요한 세 작업 

* 스탠드업 미팅

## How To Execute
* Jira, Trello > 프로젝트 관리, Trello가 간편

## How to Manage sourcecode
* Git과 Github
* Code리뷰 하는 사람들은 테스크를 조금 덜 할당해야한다.
* 이 때도 github이다.
  
## How to Test
* Test Driven Development(TDD)
* 개발시 테스트를 어떻게 할 것인지부터 생각 - 테스트코드부터 작성
* 코드 구성자체가 테스트에 편리하게 되고, 코드를 더 잘 이해 하게 된다.

## How to Build
* 내가 개발한 소프트웨어를 배포하기 위한 형태로 만드는 것!
* 테스트가 빌드의 중요한 일부로 포함
* 참여 개발자들이 많을수록 이는 더 중요
* Jenkins -(구)Hudson의 사장화를 방지하여 다시 만든다!
* Github CI/CD - GithubActions <Travis CI < Circle CI 
* 모든 사람들에게 공개되면 무료

## Continuous Integration
* 코드 Repo는 하나만 유지 (Master)
* 코드변경을 최대한 자주 반영
* Test를 최대한 추가
  - Test Coverage
* 빌드를 계속적으로 수행
  - build 최소화해야한다. 그동안 아무것도 못 쓰기 때문에 

## 사내업무 메신저(슬랙)
* 여기서 연동이 좋음

실습/숙제
코드 10진수가 주어졌을 경우 16진수로 바꾸어 출력하기
- 파이썬 작성
- 테스트 코드 추가
- ChatGPT나 Bard(구글) 사용해보자

git repo
setting Collaborat\or
다른 사람의 리뷰를 받아봤다.

## 기능

* clone, init, add, commit, push, pull, merge, branch

## 용어
* REpo Repository로 관리된다
* Master : 한 Repo에서 기본이 되는 메인 코드를 지칭
* Branch : 원본 브랜치와 병합하려는 목적
* clone : 다른 계정에 존재하는 Repo로부터 새로운 Local reposit  roy를 만드는 것
* Commit(Check-in):
  * - 내가 만든 코드 변경을 Branch의 Local Repository에 반영 
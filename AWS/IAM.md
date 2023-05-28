# AMAZON EKS
(Amazon Elastic Kubernetes Service)

1. Docker / ECS / ECR
2. IAM
3. AWS CLI
4. AWS CLOUD9
5. VPC


1. Docker
- Code, Dependencies, Runtime
- 몇 백개?? 나 할 이유가 있나?


로드밸런싱
서비스 디스커버리
롤아웃 롤백
복구
컴포넌트??


비동기로 바라본다 -? Watch


EKS와 쿠버네티스는 조금 다름

컨테이너 만을 위한 AWS Fargate 서비스

control plane -> Data plane
API Server : 클러스터의 API를 사용할 

ELB 를 통해 붙는다???
IP나 도메인이 없기 때문에


데이터 노드 
Pod( container( nginx ) ) - ReplicaSet - Deployment


kubectl

Master Node

쿠버네티스 설정은 어렵다.

EKS가 어느 정도 이런 어려움을 해소 해줌 
그런데 과연 이게 좋은걸까?
여러가지 설정을 해줘야 하기 때문에 쉽지가 않음

EC2 - 여기 하나만 잘쓰면 된다. AWS

amazon elastic container 
Prac
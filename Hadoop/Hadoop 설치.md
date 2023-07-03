## Ubuntu Linux환경에서 Hadoop 설치
# 참고자료 : 
https://phoenixnap.com/kb/install-hadoop-ubuntu


## 설치 명령어 모음

sudo apt update
sudo apt install openjdk-8-jdk -y
sudo apt install openssh-server openssh-client -y
sudo adduser hdoop
-> 비밀번호 2번 확인 후, 그 밑에는 적지 않아도 무방

su - hdoop
-> hdoop 유저로 변경

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
ssh localhost
wget 부분에서 오류가 발생하여 버전을 수정하였다. 압축을 해제하는 코드 또한 알맞게 수정하였다.

wget https://dlcdn.apache.org/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz
tar xzf hadoop-3.2.4.tar.gz
sudo nano .bashrc를 입력하게 되면 오류가 발생하기 때문에 vi .bashrc를 사용해야 한다. 해당 파일을 열어서 다음과 같이 i를 클릭하여 편집모드로 변환한 다음에 문서의 마지막에 환경변수 관련 자료를 복사 붙여넣기 한 후에 마지막에 nativ에서 e를 입력한 후에 ESC -> :wq + Enter를 통해 최종 문서를 저장한다. 

vi .bashrc

아래에서는 sudo nano 편집기 대신 vi를 사용하기로 한다.

vi $HADOOP_HOME/etc/hadoop/hadoop-env.sh
-> JAVA_HOME 설정

vi $HADOOP_HOME/etc/hadoop/core-site.xml
vi $HADOOP_HOME/etc/hadoop/hdfs-site.xml
vi $HADOOP_HOME/etc/hadoop/mapred-site.xml
vi $HADOOP_HOME/etc/hadoop/yarn-site.xml
->Configuration 복사 붙여넣기


네임노드 초기회

hdfs namenode -format
dfs 및 yarn 실행

cd명령어를 통해 ~/hadoop-3.2.4/sbin 폴더까지 이동

./start-dfs.sh
./start-yarn.sh
jps
 


설치 완료
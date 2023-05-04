## 파일 읽기 기초

```
# 파일을 열었던 객체를 파일디스크립터라고 한다.
file_obj = open(파일명:경로까지 포함해서,mode,encoding)
file_obj.close()
```
* 파일을 열때는 open 함수를 사용하며, 리소스 및 충돌을 방지하기 위해서 open후에는 파일디스크립터를 닫아준다.
* mode는 크게 3가지 있으며, r(읽기) , w(기존의 파일이 있더라도 처음부터 다시 쓴다.) , a(추가)
* encoding은 utf-8-sig로 한다. window에서만 utf-8을 읽을 때 다른 방식으로 읽기 때문에 이를 방지하고자 utf-8-sig를 권장

## csv파일을 csv라이브러리로 다루기

* csv라이브러리를 import csv로 불러온다

* csv를 쓸 때는 다음과 같이 한다.
```
import csv

with open('test.csv','w',encoding='utf-8-sig',newline='') as f
    writer = csv.writer(f,delimiter=',')
    writer.writerow([1,2,3])
    writer.writerow([1,2,3])
```
* 만약 읽기로 하고 싶다면 csv.reader로 하면된다. 이때 reader로 읽게되면 해당 객체는 반복을 통해 각 로우를 리스트로 반환한다.
```
with open('test.csv','r',encoding='utf-8-sig',newline='') as f
    reader = csv.reader(f,delimiter=',')
    for i in reader :
        print(i)
``` 
* 또한 csv.DictWriter 그리고 csv.DictReader도 제공하는데 다음과 같이 사용할 수 있다.

```
with open('test.csv','w',encoding='utf-8-sig',newline='') as f
    writer = csv.DictWriter(f,fieldnames=(['숫자1','숫자2','숫자3'])
    writer.writeheader() # header는 필드 이름을 셀에 쓰게 한다. 만약 누락하면 csv.DictReader로 읽을 때 값만 표시될 것이다.
    writer.writerow({'숫자1':1,'숫자2':2,'숫자3':3})
    
``` 

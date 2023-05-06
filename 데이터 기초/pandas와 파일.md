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

## 데이터 포맷 : XML
- xml은 포맷은 크롤링 때 사용했던, bs4 라이브러리를 사용해 처리한다.
- 즉 xml을 트리형태로 변경시키는 BeautifulSoup 객체에 넣은 후에 select, select_one 등의 함수를 사용한다.

## 데이터 포맷 : json
- 먼저 이놈의 json이란 뭘까? 사전형태의 문자열 이다.
- python에서 사전 형태는 {"name" : "kmk"} 인데, json은 '{"name" : "kmk"}' 이런 형식이다. 
- 그렇기 때문에 json을 받았으면, 분석하기 위해서 dict형태로 변경하고, 네트워크로 내보내기 위해서는 dict로는 통신할 수 없으므로, json으로 변경하여야 한다.
- 그래서 어떤 변수에 json데이터가 있다고 할 때, dict_data = json.loads(data)를 통해 dict로 변경할 수 있다. 
- 반대로 dict_data를 json으로 변환하고 싶다면 어떻게 해야할 까? json_data = json.dumps(dict_data)
- 그렇다면 str()과 json.dumps()의 차이는 무엇일까? 일단, 표준이 다르다. str은 ''로 묶는 반면, json.dumps는 "로 문자열을 묶는다.
- 그리고 json의 표준은 문자열을 ""로 묶어야 하기 때문에 만약 str을 json파일로 하려한다면 파싱에 오류가 발생한다.
<hr>
- 파일을 열어 파일에 json을 쓰고 싶다면, json.dump(data,파일디스크립터,indent=@)를 써야한다.
- 반대로 json 파일을 열어 그 객체를 변수에 할당하고 싶다면 json.load(파일 디스크립터)를 써야한다.

## pandas
* 판다스는 데이터를 다룬다. 그 중에는 Series와 DataFrame이 있다. 전자는 엑셀의 1열만 있는 데이터를 생각하면 되고, DataFrame은 2열 이상의 데이터를 생각하면 된다.
* CRUD로 기본을 정리하고, 추가학습을 하자
* Series
* C
* series = Series([1,2,3,4])
* R 
* series.index , series.values
* U
* series.index = [4,5,6,7], series[4] = 10 , 이 때 series.values에서 직접 변경 불가능
* D
* del series[4] index가 4인 행을 삭제
<hr>
* DataFrame
* C
* df = DataFrame({"연도":[2020,2019,2018],"확진자" :[1000,2000,3000],"사망자":[10,1,3]})
* 이는 DataFrame에 컬럼이 연도, 확진자, 사망자 를 뜻하고 나머지는 행을 뜻한다.
* 이때 index는 자동으로 0부터 시작된다.
* R
* Column 읽기 df['확진자'] -> 확진자 컬럼 읽기 이때, 해당 데이터는 Series이다. 따라서 df['확진자'][0] -> 1000을 뜻한다.
* row 읽기 df.iloc[0] 또는 df.loc[사용자지정 인덱스]
* df.[[컬럼,컬럼]].copy 변수에 저장
* U
* df.set_index -> 특정 컬럼을 인덱스로 지정하여 반환한다. 따라서 특정 변수에 저장해야한다.
* df.reset_index -> 인덱스로 지정된 특정 컬럼을 본래의 자리로 돌려놓는다. 특정 변수에 저장해야한다.
* D
* 열 삭제 del df[[컬럼명,컬럼명]]
* 행 삭제 df.drop([인덱스,인덱스]) ->변수에 저장

<hr>
* EDA와 몇가지 기본 함수
* EDA란 가설을 세우고 가설을 검증하기 위해 데이터를 보지 말고, 데이터 그 자체를 살펴보자는 것이다.
* 가설을 세우고 검증하는 것이 통계의 기본이기에 이러한 개념이 나온 것 같다.
* 1. 출처, 주제가 무엇인지 파악 - 데이터의 특정열이 어디서(web,mobile 등) 어떤 정보가 얼마나 왔는지 파악하는 것이 이에 해당
* 2. 크기 - 데이터의 크기가 얼마나 큰지 작은지 유의미한지 등
* 3. 요소 - 데이터가 어떤 요소로 구성되어 있는지 파악

* EDA와 Pandas
* csv를 읽어서 pandas 데이터 프레임 내에 들어오게 한 후 작업을 시작한다.
* doc = pd.read_csv(경로,encoding='utf-8-sig',error_bad_lines=False )
* doc.head(n=50), doc.tail() 위, 아래로 기본 5개의 행을 출력한다. n속성을 사용하면 해당하는 숫자만큼 행을 출력한다.
* doc.shape -> (행,열) 의 값을 반환하는 튜플이다.
* doc.info() -> 해당 데이터의 기본적인 정보를 알려준다.
* doc.columns -> 열을 살펴볼 수 있다.
* doc.describe() -> 속성이 숫자라면 평균,최소값,최대값,표준편차 등의 정보를 요약하여 보여준다.
* doc.corr() -> 속성간의 상관관계 기본 피어슨 상관관계 이다. 수학적으로 표현하면 어렵지만 1은 양의 상관관계 한 변수가 증가하면 다른 변수도 증가, 0은 거의 관계가 없고, -1는 음의 상관관계 한 변수가 증가하면 한 변수가 줄어드는 관계를 말한다.

* 간단 시각화
* plotly 사용 예정
* matplotlib은 가장 오래되어 한번은 다루어볼만한.
* searborn은 matplotlib의 부족한 점을 보충했다.

예제
```
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(5,5)) -> 그려질 그래프의 크기이다.
sns.heatmap(data= doc.corr(), annot=True, fmt= '.2f', linewidths=0.5, cmap="Blues")
```
이때 annot은 히트맵으로 그릴 때 그 안에 숫자의 표시 여부이다.
fmt는 doc.corr()로 구한 숫자 데이터를 소수점 둘째 자리까지 표시하겠다는 것이다.
linewidths는 각 히트맵 사이의 크기이다.
cmap은 색이다.

## 들어가면서
Pandas를 다루기 전 Numpy의 기본에 관해서 다루고자 합니다. Numpy는 The fundamental package for scientific computing with Python, 즉 과학기술을 위한 필수적인 패키지 입니다. Numpy는 배열이라는 자료구조가 핵심인데, 배열과 배열의 연산이 Numpy의 핵심입니다. 이에 대해서 다루어 보겠습니다.

 

## Numpy설치
```python
pip install numpy
```

## Numpy 자료구조
### 라이브러리 불러오기 및 약어설정

다른것으로 설정하여도 무방하지만 np가 많이 약어로 쓰입니다.
```python
import numpy as np
```
### 배열 생성

배열은 정수, 문자열 등을 원소로 하는 배열을 생성할 수 있지만, Numpy의 목적은 수의 연산이기 때문에 숫자 이외에는 잘 쓰이지 않습니다. 그리고 하나의 리스트는 행으로 그리고 다시 그 행을 리스트로 감싸면 행,열의 배열이 완성됩니다. 참고로 행,열에 더해 리스트를 다시한번 감싸면 층,행,열의 구조를 가지게 되는 3차원 배열을 완성합니다. 우선 2차원 배열의 자료에 대해서 살펴보도록 하겠습니다.

```python
# 0이라는 원소를 가진 배열
arr1 = np.array(0)
# 문자열을 가진 배열
arr2 = np.array('4')

# 2개 이상의 정수 원소를 가진 배열
arr3 = np.array([1,4,2])

# 2차원 배열
arr4 = np.array([[3,4],[1,2]])

# 다음의 행렬을 나타낸다.
# 3 4
# 1 2
```

### 배열의 인덱싱

위 arr의 인덱싱은 리스트를 다루는 것처럼 살펴볼 수 있습니다. 다만 2차원 행렬의 경우 arr4[0][1]의 인덱싱 뿐만 아니라 arr4[0,1]의 인덱싱도 허용합니다.

```python
arr3[0]
>> 3

arr3[0:2]
>> array([1, 4])

arr4[0]
>> array([3, 4])

arr4[0][1]
>> 4

arr4[0,1]
>> 4
```

### 배열의 행렬 연산

만약 같은 행,열의 갯수를 갖는 배열이 2개 있다고 할 때, 이 배열의 같은 인덱스끼리 연산을 수행할 수 있습니다. 더하기,빼기,나누기,곱하기, 제곱, 정수나누기, 나머지 연산의 7가지 행렬 연산을 수행할 수 있습니다. 예시는 2차원 배열을 기준으로 설명했지만 1차원 벡터도 당연히 지원합니다.

```python
arr4 = np.array([[10,20],[30,40]])
arr5 = np.array([[3,4],[2,5]])

# 더하기
arr4+arr5
>>
array([[13, 24],
       [32, 45]])

# 빼기
arr4-arr5
>>
array([[ 7, 16],
       [28, 35]])
       
# 곱셈
arr4 * arr5
>>
array([[ 30,  80],
       [ 60, 200]])

# 나누기
arr4 / arr5
>>
array([[ 3.33333333,  5.        ],
       [15.        ,  8.        ]])

# 정수 나누기
arr4 // arr5
>>
array([[ 3,  5],
       [15,  8]])
       
# 제곱
arr4 ** arr5
>>
array([[     1000,    160000],
       [      900, 102400000]])
       
# 나머지
arr4 % arr5
>>
array([[1, 0],
       [0, 0]])
``` 

### 배열의 행렬곱

수학시간에 배운 행렬 곱의 경우 @, dot, matmul 등을 통해 수행할 수 있습니다. 
 
```python
# 이렇게 4가지의 방법은 결과가 모두 동일합니다.
# 행렬의 곱 연산인 @는 Python 3.5버전 부터 지원한다고 하니 참고바랍니다.

arr4 = np.array([[10,20],[30,40]])
arr5 = np.array([[3,4],[2,5]])

arr4 @ arr5
np.matmul(arr4,arr5)
np.dot(arr4,arr5)
arr4.dot(arr5)

# 행렬 곱 연산 결과
>>>
array([[ 70, 140],
       [170, 320]])
``` 
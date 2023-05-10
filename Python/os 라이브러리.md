# OS 라이브러리와 기능

[폴더의 생성과 삭제]
```python
import os
import shutil

# 현재 폴더에 폴더 생성
os.mkdir(folder명)

# 현재 폴더에 폴더와 그 하위 폴더 생성
os.makedirs(folder/folder명)

# 삭제 - 폴더 안이 비어있어야 한다.
os.rmdir(폴더명)

# 폴더와 그 하위 구조까지 삭제하기
shutil.rmtree(폴더명)
```

[파일 삭제 및 이름 변경 등]
```python
import os

# 파일 생성
with open("test.txt", "w", encoding="utf-8-sig") as f:
    pass

# 파일 삭제
os.remove("test.txt")

# 파일 이름 변경 및 디렉토리 변경 (11번 라인 처럼 작성하면 폴더 이동도 하면서 이름도 변경)
os.rename("test.txt", "folder/test1.txt") 
os.rename("test.txt", "test1.txt") 

# 파일 사이즈 구하기
os.path.getsize("test.txt")
``` 

[ 경로 관련 ] 
```python
import os

# 현재 파일 작업 경로
pwd = os.getcwd() 

# 작업 경로 변경
os.chdir('..')
os.chdir(pwd)

# 현재 파일의 절대경로(a/b/c/.py)
os.path.abspath(__file__) 

# 현재 파일의 마지막 파일 경로(.py)
os.path.basename(__file__)

# 현재 파일의 마지막 폴더 경로(c)
os.path.basedir(__file__)

# 만약 b가 어떤 프로젝트의 기본 경로라면
BASE_DIR = os.path.basedir(os.path.abspath(__file__))

# 그 후 어떤 폴더와 파일을 합치고 싶다면?!
os.path.join(BASE_DIR,폴더,파일)
```

[기타]
```python
import os
import glob

# 파일 목록 얻기
os.listdir(폴더) # 어떤 폴더의 폴더 및 파일 목록 얻기
glob.glob(*.형식) # 어떤 폴더의 특정 형식 목록 얻기

# 파일이나 디렉토리가 있는지 확인하는 조건
os.path.exist(파일 및 폴더명)

# 어떤 폴더나, 파일이 파일인지 폴더인지 구분하기
os.path.isdir(파일 및 폴더명)
os.path.isfile(파일 및 폴더명)
```


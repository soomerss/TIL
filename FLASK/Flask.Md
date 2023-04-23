

## Jinja 템플릿
> 기본 문법
* {{변수명}}
* {% 파이썬 코드 %}
* 사용자가 웹서버의 특정 URL에 접속한다고 가정해보자. 이 때 URL에 특정 변수가 입력되면 서버는 이 URL에 맞는 HTML을 반환하는것은
return render_template('*.html')로 표현할 수 있다. 그런데 이때 이 html파일에 user명이 정의되어 있고, 이 user명은 url을 통해서
전달된다고 하면 어떻게 처리할 수 있을까? 그것은 render_template('*.html',변수명1 = user )을 통해 *.html에 1차적으로 변수등을 매칭하고 하고, 보여지게 된다.

* 반복문
```
{% for value in values %}
{{ value }}
{% endfor %}
```

* 반복문 추가 문법
- range() : 동일, 단, len()은 불가
- range(len(values))를 사용하고 싶다면, range(values|length) 와 같이 사용하면 된다
- loop.index = 반복문 횟수 -> 1부터 시작함
- values[index] = 리스트의 인덱싱과 동일

* 조건문
  - {% if ~~ %} {% elif %} {% else %} {% endif %}

* 주석
* {# 내용 #}

* 데코레이터  
app.route()

## BluePrint
* 블루프린트 기능은 하나의 메인 앱에 라우트 함수를 작성하는 것이 아니라 앱 별로 블루프린트라는 기능을 통해 관리하는 것을 말한다. 이를 통해 앱별로 라우팅이 가능하다.
* 방법은 메인 앱의 코드에서 개별 앱이 있는 파일을 임포트한후에, register_blueprint메서드를 통해 앱에 등록한다. 이때 url_prefix인자를 넣는데, 이는 메인 앱이 '/'에서 시작되는 것처럼 등록될 앱이 시작되는 지점이라고 이해하면된다.
* 개별 앱에서는 Blueprint를 임포트 한후에, app을 생성하는 것처럼, Blueprint인스턴스를 생성한다.
* 해당 기능을 통해 많은 앱이 있다고 하더라도 각각의 앱의 라우트를 메인앱으로 통합하여 관리할 수 있다.

* 예제의 폴더 구조는 다음과같다.
최상단 폴더
 my_blog(folder)
 --blog.py
app.py

* 메인 app.py 코드
```
from flask import Flask
from my_blog import blog

app = Flask(__name__)

app.register_blueprint(blog.my_blog,url_prefix="/blog")

...생략
```

* blog.py의 코드 예제
```
from flask import Blueprint

my_blog = Blueprint('my_blog',__name__)

@my_blog.route('/blog1')
def blog_index():
  return 'hello'
```
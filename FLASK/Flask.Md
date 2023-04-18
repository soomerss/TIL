

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
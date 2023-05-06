## 기본문법
* 컨텐츠를 가지는 태그와 컨텐츠를 가지지 않는 태그로 구분
* <태그이름></태그이름> 즉, 열리는 태그, 닫히는 태그를 이용하여 사용
* <태그이름/> 단일 태그의 셀프클로징(버전에 따라 해도되고 안해도 되는 특징)
* <태그이름 속성="값">
* 주석 <!--   내용    -->
* html 속성에는 lang으로 언어 설정

## html과 lang
* <html lang="ko">
* 웹 문서의 시작을 알리는 html 태그에서 lang은 어떤 역할을 할까?
* 검색사이트에서 특정 언어별로 검색 시 ko를 우선 검색하는 효과가 있다.
* 또한 화면낭독기에서 언어에 따라 다르게 낭독하거나 하는 기능이 있다.

## HEAD
### head 태그
* 대표 : title, meta
* <title>안녕</title> -> 브라우저의 제목표시줄이야
* <meta charset="UTF-8">
* <meta name="keywords" content="html의 구조"> -> 웹 문서의 키워드
* <meta name="description" content="html의 구조를 알아봅시다."> -> 웹 문서의 설명
* <meta name="author" content="co"> -> 웹 문서의 소유자나 제작자
* 사람의 눈에는 보이지 않지만 문서의 환경설정등의 역할을 하는 것
* 메타데이터 - 인코딩
* 타이틀, 메타데이터, 링크, 스타일(CSS), 스크립트(자바스크립트)
* css - style태그를 통해 Html안에 작성, link태그를 통해 .css로 별도 작성
* 스크립트는 콘텐츠방식 - html 안에 작성, 링크방식 - 종료태그를 작성, .js별도 작성
---
## BODY
### 요소
* block, inline, inline-block
1. block(블록레벨요소)
- 레고 블록처럼 차곡차곡 쌓이고 화면 너비가 꽉차는 요소
- div
2. inline(인라인 레벨 요소)
- 블록 요소 내에 포함되는 요소
- 크기와 여백을 가지고 오른쪽으로 나열되는 요소, 위 아래 padding추가 안됌
- span,b,strong,i,em
3. inline-block
- 글자처럼 취급되나 block 태그의 성질을 가지는 요소

---
### 레이아웃 태그 - 시맨틱 의미론적인
1. 컨텐츠 분할 요소(div)
2. 레이아웃태그(header,footer,main)
* header - 블로그 글 제목, 작성일 등의 주요 정보를 담는 태그
* footer - 저작권 정보, 연락처 등의 부차적인 정보
* main - 주요 컨텐츠를 담는 태그, 무조건 한번만!
3. 레이아웃태그(section,article,aside)
   * section - 컨텐츠의 구역을 나누는 태그이며 article이 독립된 영역을 뜻한다면 section은 몇개의 컨텐츠를 조합한다.
   * article - 블로그 포스트, 뉴스 기사와 같은 독립적인 전달을 하는 태그
   * aside - 간접적인 정보를 전달하는 태그
4. why 레이아웃태그
   * div를 통한 단순 구분이 아닌 의미있는(Semantic) 문서구조를 작성하기 위함
   * 검색순위 우선이 되게 하는 장점이 있음

### 컨텐츠
1. 제목태그(h1~h6) - 구획의 순서를 잘 지켜야한다.
2. p태그 <문단 태그> 
3. b, strong : 글씨의 두께를 조절, b는 두껍게, strong은 강조의 의미를 가짐
4. i(italic), em(emphasis) : 기울기, i= 등장인물,외국어구절, em = 기울임과 내용의 강조
5. u : 밑줄, 주석을가지는 단어임을 나타낼 수 있다.
6. s, del : s는 시각적인 취소선, del은 제거된 택스트를 나타낼 수 있음ins를 옆에 두면 추가된 텍스틀를 옆에 둘 수 있음
7. hr - horizontal line 
8. blockquote - 인용문, 들여쓰기함, 낭독기로 읽을 때 구분

### 그 외 텍스트 관련
1. abbr = 줄일말 표시 및 타이틀 속성 사용하여, 무엇의 약자인지 
### 링크 이동
1. a태그의 속성 href="연결될 곳", target="새창(_blank), 기존창 등등"
2. a태그 사이에 텍스트를 사용하면 텍스트 링크, img를 사용하면 img링크

### 멀티미디어
1. img : 단일태그 src속성 ㅣ 이미지 경로, alt 속성 | 이미지 로딩이 문제가 있을 때 띄우는 속성
* <img src="이미지 파일 경로" alt="대체용 텍스트">
   * svg : 그래픽이자 코드(xml)로 만들어진 이미지로, 해상도의 영향을 받지 않아 확대/축소 자유롭다.
2. figure, figcaption - 태그를 사용해 컨텐츠의 설명 혹은 범례추가
3. video : 재생은 | autoplay, 문서 내에 영상을 첨부할 수 있는 태그, src= 속성 비디오를 문서내에 첨부, Poster속성(로드전 포스터)
   * 재생하고 싶다면
4. audio : 재생은 | controls, src속성을 사용하여 소리를 문서 내에 첨부할 수 있다. 
5. object : 오디오 비디오, pdf 등 삽입가능
* <object width="" height="" data="파일"></object>
6. embed : 대부분의 브라우저에서 사용가능하며 , object, vedio, audio가 삽입 불가능한 HTML 파일이라면 고려해 볼 수 있다.
7. video와 audio 속성 : src는 경로, autoplay: 자동재생 단, 자동재생은 여러 브라우저가 금지하고 있기 때문에 edge를 사용하거나 자동 재생하고 싶다면, 소리 제거 속성인 muted를 사용, loop는 반복, controls는 유저가 재생할 수 있도록 만약 controls가 없다면 audio의 경우 화면에 표시되지 아니함.

### 리스트
1. 정렬되지 않은 리스트 : Ul - 리스트 아이템, li - 리스트 아이템을 감싸는 태그
2. 정렬된 리스트 : ol - 리스트 아이템, li - 리스트 아이템을 감싸는 태그, ol의 속성 type=a,A,1,i,I
3. 설명목록 태그 : dl - 설명을 이루는 한쌍을 감싸는 태그, dt- 설명대상, dd- 설명, 실무에서 잘 안쓰게되는..

### 테이블
1. table태그 - 표, tr - 행,row, td - 열, 셀, tr안에 들어감,  th - 제목 행의 셀 td 대신, 첫행 또는 첫 열에 쓴다.
2. thead, tbody, tfoot - 정보성 구분,, html4에서는 tfoot이 tbody보다 먼저
3. thead 안에 tr , td를 삽입하면 된다.
4. td의 속성 rowspan과 colspan, 행을 합친다 -> rowspan="숫자" 세로로 합쳐진다. 그 다음 td는 생략하고 작성한다.
5. caption - table태그 바로 밑에서 작성하며, 표의 제목 역할을 한다.
6. colgroup과 col - caption 바로 밑에 작성되어 colgroup으로 묶어 준후 그 안에 col태그를 사용하면 style을 이용하여 스타일을 지정할 수 있다. 이때 만약 3열에서 4열이 같은 스타일을 원한다면 3열에서 span="2"의 속성을 쓰면된다


### 아이프레임
1. 현재 문서안에 다른 HTMl 페이지 삽입하여 보여줌 : 모두 불러올 수 있는건 아님.

### 양식 form 태그
1. form : 
   * 정보를 제출하기 위한 태그, input, select와 option의 드롭박스, textarea , 정보제출 button을 포함할 수 있고, action 속성 - 정보제출시 페이지 이동, Method 속성,get,post 구현
2. 설명과 입력
   * input에 설명을 하기 위해서 label 태그를 사용 - click이 되었을 때 포커스가 input박스로 향하게 함 이때 속성for는 input의 id값과 일칫시키기
   * input은 속성 값에 따라 Input 유형이 달라짐 : 매우 많음
   * select는 옵션 메뉴를 제공하는 태그, value는 폼이 제출될 때 그 값이 전송, 선택하지 않았을때 컨텐츠가 전송됨
   * textarea는 여러줄을 입력할 수 있음, cols, row를 사용하여 가능
   * 속성 : required(필수값), placeholder(부가 설명)- Input박스에 들어갈 기본 내용(단, 들어갈만한 곳에 구현)
   * 버튼의 기본 속성은 submit임. 버튼 자체로 기능을 구현하고 싶다면 input의 속성을 button으로 구현

3. 버튼
   * type"reset"은 입력한 양식이 모두 초기화, submit은 양식제출=



### DOM(Document Object Model)
* 브라우저의 렌더링 엔진은 웹 문서를 로드하여 파싱(구문 분석)을 진행
* html안에 무엇이 head안에 무엇이 body안에 무엇이 있는지 등의 파싱을 진행
* 이렇게 만들어진 것이 DOM이다.
* 이 DOM은 각 노드(태그)를 객체(변수와 메서드)로 다루어 문서를 다룬다. 그렇다면 body.div 같은 선택이 가능해진다.
* 이렇게 만들어진 DOM Tree를 JavaScript로 조작하여 HTML을 활용할 수 있게 된다.
* 이것은 원하는 요소를 동적으로 변경을 가능하게 하고(동적 웹페이지), 원하는 요소를 쉽게 찾을 수 있게 한다(웹 스크래핑).



### 주의사항
*   대소문자를 구분해주세요
*   class에 한글 지양, id값 중복 지양, 닫는 태그 쓰는 습관
*   태그 중첩 조심, a태그 안에 button태그, 태그가 닫히기 전에 새로운 태그, 역할이 동일한 태그 중첩 

### 참고 웹사이트
1. TCP Scholl
   * http://www.tcpschool.com/html-tags/intro
2. MDN
   * https://developer.mozilla.org/ko/docs/Web/HTML
3. W3School
   * https://www.w3schools.com/html/default.asp
## 기본문법
* 컨텐츠를 가지는 태그와 컨텐츠를 가지지 않는 태그로 구분
* <태그이름></태그이름> 즉, 열리는 태그, 닫히는 태그를 이용하여 사용
* <태그이름/> 단일 태그의 셀프클로징(버전에 따라 해도되고 안해도 되는 특징)
* <태그이름 속성="값">
* 주석 <!--   내용    -->
* html 속성에는 lang으로 언어 설정


## HEAD
### head 태그
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
### 레이아웃 태그
1. 컨텐츠 분할 요소(div)
2. 레이아웃태그(header,footer,main)
* header - 블로그 글 제목, 작성일 등의 주요 정보를 담는 태그
* footer - 저작권 정보, 연락처 등의 부차적인 정보
* main - 주요 컨텐츠를 담는 태그, 무조건 한번만!
3. 레이아웃태그(section,article,aside)
  * section - 컨텐츠의 구역을 나누는 태그
  * article - 블로그 포스트, 뉴스 기사와 같은 독립적인 전달을 하는 태그
 - aside - 간접적인 정보를 전달하는 태그
1. why 레이아웃태그
 - div를 통한 단순 구분이 아닌 의미있는(Semantic) 문서구조를 작성하기 위함
 - 검색순위 우선이 되게 하는 장점이 있음

### 컨텐츠
1. 제목태그(h1~h6) - 구획의 순서를 잘 지켜야한다.
2. p태그 <문단 태그> 
3. b, strong : 글씨의 두께를 조절, b는 두껍게, strong은 강조의 의미를 가짐
4. i, em : 기울기, i= 등장인물,외국어구절, em = 기울임과 내용의 강조
5. u : 밑줄, 주석을가지는 단어임을 나타낼 수 있다.
6. s, del : s는 시각적인 취소선, del은 제거된 택스트를 나타낼 수 있음ins를 옆에 두면 추가된 텍스틀를 옆에 둘 수 있음

### 링크 이동
1. a태그의 속성 href="연결될 곳", target="새창(blank_), 기존창 등등"

### 멀티미디어
1. img : 단일태그 src속성 ㅣ 이미지 경로, alt 속성 | 이미지 로딩이 문제가 있을 때 띄우는 속성
   * svg : 그래픽이자 코드(xml)로 만들어진 이미지로, 해상도의 영향을 받지 않아 확대/축소 자유롭다.
2. figure, figcaption - 태그를 사용해 컨텐츠의 설명 혹은 범례추가
3. video : 재생은 | autoplay, 문서 내에 영상을 첨부할 수 있는 태그, src= 속성 비디오를 문서내에 첨부, Poster속성(로드전 포스터)
   * 재생하고 싶다면
4. audio : 재생은 | controls, src속성을 사용하여 소리를 문서 내에 첨부할 수 있다. 

### 리스트
1. 정렬되지 않은 리스트 : Ul - 리스트 아이템, li - 리스트 아이템을 감싸는 태그
2. 정렬된 리스트 : ol - 리스트 아이템, li - 리스트 아이템을 감싸는 태그
3. 설명목록 태그 : dl - 리스트, dt- 설명대상, dd- 설명, 실무에서 잘 안쓰게되는..

### 테이블
1. table태그 - 표, tr - 행,row, td - 열, 셀, tr안에 들어감,  th - 제목 행의 셀 td 대신
2. thead, tbody, tfoot - 정보성 구분,, html4에서는 tfoot이 tbody보다 먼저

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
   * type="reset"은 입력한 양식이 모두 초기화, submit은 양식제출

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
# node intro

웹서버 빌드,게임, 네이티브앱(vscode), 나사에서도 사용

## repl

read excute print loop

파이썬처럼 뭐 치면 답을 주는 터미널형태

노드의 콘솔

`node` 명령어로 열고 `.exit` `^d`

크롬콘솔, 브라우저 필요없음. 

# running node files

`node % touch firstScript.js`

```jsx
for(let i = 0; i <10; i++){
    console.log("hello first script");
}
```

```jsx
node % node firstScript.js //노드랑 파일네임으로 실행
hello first script
hello first script
hello first script
hello first script
hello first script
hello first script
hello first script
hello first script
hello first script
hello first script
```

# process, argv

`process` 글로벌 객체 

키워드로  노드 버전, 메모리유징 확인 가능.

process.cwd(), process.version, 

process.argv 얘는 현재 노드가 실행중인 경로, 우리가 실행중인 파일 경로를 보여줌


# file system(fs)

노드 공식문서보면 http 처리 관련 다 나와있음. 내 서블릿 책처럼 자세하게 정리되어있다. 참고


synchronous version : 실행하고 끝날때까지 기다려라. 가기전에


fs.mkdir을 사용하기위해 fs가 필요함

```java
const fs = require('fs');
```

노드에게 파일시스템 사용하겠다고 알려주기

# 모듈

require 통해서 각 js 파일들을 객체로 가져올 수 있다. import 하는거임

폴더 require도 가능. 폴더 안 내용 통째로 객체로 불러오기

외부에서 사용하게 하려면 exports 해주고

라이브러리와 함께 사용하기 시작할 땐 index.js 가 중요해짐. 조각들을 합쳐주는 중심 스크립트라서.

# Npm

노드 패키지 관리자

도서관엔 아주 많은 패키지 책들이 있다. 다른사람들이 쓴 책

익스프레스, 리액트 패키지가 있다


cli에서 쉽게 설치하고 관리할 수 있음

npm 홈페이지에서 검색해서 그 이름 제대로 가져와서  cli에서 설치하면됨

local install vs global install

기본이 로컬

# package.json

의존성 관리

스프링에서는 pom.xml 이었다

직접 만들수 있다.

`npm init`

# express

프레임워크

http 리퀘는 그냥 요청 텍스트거든 이걸 자바스크립트가 알아들을 수 있게 객체로 매치해줌


요청을 듣기위해 app.listen() 메소드 사용

포트번호, 함수를 받는다

app.use( 콜백 )

요청들어오면 이게 항상 실행됨

이제 응답은 어떻게 할지 알아보자

```jsx
app.use((req, res) => {
	res.send("hello! this is response!");
})
```

요청과 응답객체 인자 이름은 아무렇게나

저 객체는 익스프레스에 의해 만들어졌고 이 콜백을 통과한다.

익스프레스 문서를 보면 요청과 응답에 따른 여러가지 메소드를 확인할 수 있다.

포스트맨

요청정보를 보여줌

# 라우팅

`app.get()`

인자는 path 경로랑 콜백을 받는다.

```jsx
app.get('/', (req, res) => {
	res.send("This is the home page!")
})

app.get('/cats', (req, res) => {
	console.log("cat request!!!");
	res.send("meow!! 😺 ");
})

app.get('/dogs', (req, res) => {
	res.send("woooof!!");
})
```

get 요청에만 매치됨

`app.get('*', ~ )` 지정된 패스로 요청하지 않으면 요기서 만든거 띄워줌

이렇게 일일이 패스 정하지않고 패턴을 만들거임

새로운 라우트를 만들자

```jsx
app.get('/r/:subreddit', (req, res) => {
	res.send("This is a subreddit")
})
```

경로 뒤에 : 이렇게 스트링 붙는건 변수다. 뭘 입력하던지 이 결과를 반환한다.

저 변수에 받아온 값으로 코드 만들고싶음

req.params 사용. 서브레딧 스트링 부분에 요청들어온 변수를 객체에 담아준다.

```jsx
app.get('/r/:subreddit', (req, res) => {
	const { subreddit } = req.params;
	res.send('<h1>Browsing the ${subreddit} subreddit</h1>')
})
```

서브레딧에 받은거 구조분해, 템플릿리터럴로 사용

```jsx
app.get('/r/:subreddit:postId', (req, res) => {
	const { subreddit, postId } = req.params;
	res.send('<h1>Viewing Post ID: ${postId} on the ${subreddit} subreddit</h1>')
})
```

글 아이디도 사용해보기

# 쿼리스트링

```jsx
app.get('/search', (req, res) => {
	const { q } = req.query;
	if (!q) {
		res.send('nothing found if nothing search')
	}
	res.send('<h1>Search results for: ${q}</h1>')
})
```

요청 객체엔 쿼리 스트링이 있다. 키 밸류 페어로 저장됨. 쿼리객체를 q 변수로 구조분해 해서 사용

# nodemon

웹브라우저 자동 새로고침

설치하고 nodemon 키워드 사용하면됨

# Templating

ejs : embeded javascript

장고 템플릿, jsp랑 비슷

html로 보여줌

```jsx
const express = require('express');
const app = express();

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('home')
})

app.listen(3000, () => {
    console.log("listening on port 3000")
})
```

ejs 패키지 설치하고 app.set() 으로 키는 뷰 엔진, 밸류는  ejs 사용

보통 폴더는 views 안에 ejs 파일 담아서 사용함

루트요청오면 views 안에 있는 home.ejs 파일 렌더링해줌

내가 지금 node 폴더에 있었거든. 근데 한단계 위로 올라가서 거기서 index.js 찾으려고하면 에러남

```jsx
const path = require('path');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'))
```

그럴땐 요거 추가

패스 정해주는 빌트인메소드

path.join은 여러패스 하나로 조인해줌.

`<%= 4 + 5 + 1 %>`

`<%= 'hello world'.toUpperCase() %>`

자바스크립트처럼 작동

요청처리 메소드에서 변수 만들어서 렌더함수로 넘겨줄수있다.

```jsx
app.get('/rand', (req, res) => {
	const num = Math.floor(Math.random() * 10) + 1;
    res.render('random', { rand: num })
})
```

렌더함수 인자에 random.ejs파일로 키밸류 객체 만들어서 넘기기

그럼 ejs 파일은 `<%= rand %>` 그대로 받아서 사용가능

{ num: num } 이라면 { num } 하나로 써도됨

### 반복문 돌려서 같은 템플릿 패턴 사용하기

```jsx
app.get('/cats', (req, res) => {
    const cats = [
        'Blue', 'Rocket', 'Monty', 'Winston'
    ]
    res.render('cats', { cats })
})
```

```jsx
<body>
    <h1>All The Cats</h1>
    <ul>
        <% for(let cat of cats) { %>
            <li><%= cat %></li>
        <% } %>
    </ul>
</body>
```

### 레딧만들어보기

```jsx
const redditData = require('./data.json');
```

```jsx
app.get('/r/:subreddit', (req, res) => {
    const { subreddit } = req.params;
    const data = redditData[subreddit];
    if (data) {
        res.render('subreddit', { ...data });
    } else{
        res.render('notfound', { subreddit })
    }
})
```

준비된 레딧데이타 제이슨파일 가져옴

요청 파라미터 구조분해 해주고, 레딧데이터에서 쿼리스트링에 해당되는 데이터 객체를 변수에 담음

해당내용이 존재하면 서브레딧.ejs에 데이터 객체 펼쳐서 넘겨주고

없으면 notfound.ejs에 쿼리스트링 넘겨준다.

(점과 대괄호는 동일하게 작동함. 객체참조할때)

```jsx
<body>
    <h1><%= name %> subreddit</h1>
    <h2><%=description%></h2>
    <p><%=subscribers %> total subscribers</p>

    <hr>
    <% for(let post of posts) { %>
        <article>
            <p><%= post.title %> - <b><%= post.author %></b></p>
            <% if(post.img){ %>
                <img src="<%=post.img%>" alt="">
            <% } %>
        </article>
    <% } %>
</body>
```

```jsx
<body>
    <h1>I'm sorry, we couldn't find the <%= subreddit %> subreddit!</h1>
</body>
```

# static assets

클라이언트에게 응답할때 html뿐만아니라 css, js도 들어가겠지

express.static() 미들웨어

app.use(express.static('public'))

얘는 모든 요청에 실행되는 메소드

스태틱 인자에 폴더이름 넣음

```jsx
app.use(express.static(path.join(__dirname, 'public')))
```

다른 경로에서 nodemon index.js 실행해도 접근가능

```jsx
<link rel="stylesheet" href="/app.css">
```

스태틱 디렉토리는 그냥 접근 가능. 

# Bootstrap + express

부트스트랩 navbar 적용

# Partials

장고에서 했던거

헤드에 들어가는 js, bs, jq 공통적으로 사용되는것들 다 하나의 템플릿으로 만들기. partial 폴더에 헤드 떼서 만들어놓고 각 뷰에서 임포트

```jsx
<%- include('partials/head') %>
```
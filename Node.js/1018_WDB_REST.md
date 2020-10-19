# REST

`npm init -y`

`npm i express`

req객체는 req.body를 갖고있음

요청 바디에있는 키밸류 정보 포함

기본값은 undefined이고 body-parsing 미들웨어 express.json(), express.urlencoded()사용가능

```jsx
app.use(express.urlencoded({ extended: true }));
```

요청바디 파싱

익스프레스에게 어떻게 파싱할지 알려줘야함

```jsx
const express = require("express");
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/tacos", (req, res) => {
  res.send("GET /tacos response");
});

app.post("/tacos", (req, res) => {
  const { meat, qty } = req.body;
  res.send(`Ok, here are your ${qty} ${meat} tacos`);
});

app.listen(3000, () => {
  console.log("on port 3000");
});
```

서블릿때 했던거랑 비슷하다고 생각하면 된다.

코드 해석해보면 일단 익스프레스 가져오고 포트 3000으로 리슨하고있음. html 폼 액션을 get, post방식에 따라서 응답처리해주고있음. 주소는 /tacos이고. 포스트방식일 경우엔 요청정보가 바디에 숨겨져서 전송된다.

요청을 하면 요청 정보가 발생된다. 포스트는 요청시 요청바디에 인풋값 파라미터를 넘긴다. 그 넘어온 파라미터는 키밸류 페어 형태다. 포스트로 보낼 경우 요청body에 숨기면서 인코딩을 해버리기 때문에 서버에서 사용 시 디코딩 처리를 해야함.

따라서 모든 요청에 따라 실행되는 app.use()로 요청바디를 파싱할 수 있는 미들웨어가 필요하다.

넘어온 쿼리스트링 읽을 수 있게 확장해서 디코딩해주고 json으로 넘어올경우에도 읽을 수있게 json 파싱해줌

요청바디 보면 application/x-www-form-urlencoded 라는 방식으로 인코딩됨. 보통 문자열 입력 방식에 사용. 데이터를 "key : value" 와 같은 형태로 만들어줌.

이 방식일 경우 extended는 false를 넣어주면 되고,다른 인코딩방식이라면 true넣어줌. 이 경우에 따로 설치 필요한게 있어서 extended한 경우이다. 기본값이 true 라서 extended 필요없는 경우엔 false 명시해주는 것

포스트맨 다시 봐야겠다

크롬 네트워크탭에서도 요청정보 볼수있어

# REST

api, route 만들때 rest를 고려해야한다

리소스 자원은 하나의 개체다. 트윗, 유저, 이미지, 텍스트메세지 등등

설계를 위한 셋업 규칙이다. 우린 이 패턴을 따를거야

깃허브의 gist rest를 살펴보자

엔드포인트는 똑같은데 요청 동사가 다 다르다

청사진 만들어보기

GET /comments - list all comments

POST /comments - Create a new comment

기본 리소스에 두가지 다른 방식 요청으로 다른 결과 보여줄거임

GET /comments/:id - Get one comment (using ID)

PATCH /comments/:id - Update one commnet

DELETE /comments/:id - Destroy one comment

### 1. Get all comments

    ```jsx
    app.set('views', path.join(__dirname, 'views'))
    app.set('view engine', 'ejs')

    const comments = [
        {
            username: 'Todd',
            comment: 'lol That is so funny'
        },
        {
            username: 'mimimi',
            comment: 'I like it'
        }
    ]

    app.get('/comments', (req, res) => {
        res.render('comments/index', { comments })
    })
    ```

    views 경로 지정 다시봐야겠음. app.set 역할, dirname, path

    코멘트 배열 만들고 렌더함수에서 구조분해로 index.ejs에 넘겨줌

    ```jsx
    <ul>
            <% for(let c of comments) { %>
                <li><%= c.comment %> <b><%= c.username %> </b> </li>
            <% } %>
        </ul>
    ```

    얘는 여기서 배열 넘겨받고 반복문으로 코멘트 객체 정보 접근해서 보여줌.

### 2. create comments

```jsx
app.get("/comments/new", (req, res) => {
  res.render("comments/new");
});

app.post("/comments", (req, res) => {
  const { username, comment } = req.body;
  comments.push({ username, comment });
  res.send("It worked!");
});
```

new.ejs는 코멘트 생성화면 띄워줄거임

GET /comments 는 모든 코멘트 띄워주는 라우트였지

**POST /comments는 포스트방식으로 넘어온거 띄워주는 create 라우트다.**

요청바디 디코딩하고 넘어온 키밸류를 코멘트 배열의 객체 구조분해 그거에 맞게 담았음

그리고 배열에 그대로 푸시.

new.ejs:

```jsx
<body>
    <h1>Make a new comment</h1>
    <form action="/comments" method="POST">
        <section>
            <label for="username">Enter username: </label>
            <input type="text" id="username" placeholder="username" name="username">
        </section>
        <br>
        <section>
            <label for="comment">Comment Text</label>
            <br>
            <textarea name="comment" id="comment" cols="30" rows="5"></textarea>
    </section>
    <button>submit</button>
    </form>
</body>
```

input에 name 있어야 넘어간다

wowoowowow

문제가있어. 새로고침하면

중복서브밋

그래서 서브밋하고 index로 올수있도록 리다이렉트 해야함

`res.redirect()`

```jsx
app.post("/comments", (req, res) => {
  const { username, comment } = req.body;
  comments.push({ username, comment });
  res.redirect("/comments");
});
```

패스만 정해주면됨

### 3. Show

특정 코멘트 디테일보여주기

항상 유니크 identifier 가 붙어있음

imdb 둘러보기

```jsx
app.get("/comments/:id", (req, res) => {
  const { id } = req.params;
  const comment = comments.find((c) => c.id === parseInt(id));
  res.render("comments/show", { comment });
});
```

배열에 id 하드코딩하고, 쿼리스트링으로 넘어온거 url에서 구조분해한? id 변수에 담고,

코멘트 배열에 id랑 넘어온 id랑 같은 코멘트 걸러서 코멘트 변수에 담고 쇼ejs에 코멘트 변수 넘겨준다

```jsx
<body>
    <h1>Comment id: <%= comment.id %> </h1>
    <h2><%= comment.comment %> - <%= comment.username %>  </h2>
    <a href="/comments">Back to Index</a>
</body>
```

얘는 그거 받아서 보여줌

이제 코멘트 하드코딩에 문제가생김

new에서 사용자가 직접 create할 때 자동으로 id 증가해줘야하잖아

npm의 uuid패키지 사용(universally unique id)

```jsx
const { v4: uuid } = require("uuid");
```

uuid 사용은 uuid()

`id: uuid()`

`comments.push({username, comment, id: uuid() })`

아이디 생김

### 4. Update

PUT, PATCH 방식

put 은 완전히 새롭게 업뎃. 새로운 버전이됨. 리플레이스

patch는 부분적으로 수정. 우린 username, id는 유지하고싶어. 그러니 패치사용

app.put

app.method

같은 경로로 들어온다해도 show 라우트가 있고 update 라우트가 있는거

```jsx
app.patch("/comments/:id", (req, res) => {
  const { id } = req.params;
  const newCommentText = req.body.comment;
  const foundComment = comments.find((c) => c.id === id);
  foundComment.comment = newCommentText;
  res.redirect("/comments");
});
```

수정요청이 들어오겠지

쿼리스트링 아이디는 id로 파싱

요청 바디에 comment 라는 name으로 들어온 밸류를 뉴코멘트에 저장하고

넘어온 아이디랑 원래 있던 아이디랑 같은지 확인해서 원래 있던 코멘트를 뉴코멘트로 할당

# express method override

위에껀 포스트맨 사용해서 대충 업뎃 테스트만 해봤고 이젠 폼에서 업뎃할 수 있도록 라우트를 만들어야됨

```jsx
app.get("/comments/:id/edit", (req, res) => {
  const { id } = req.params;
  const comment = comments.find((c) => c.id === id);
  res.render("comments/edit", { comment });
});
```

이 코멘트에 접근하기 위해 렌더로 넘겨줌

```jsx
<body>
    <h1>Edit</h1>
    <form action="/comments/<%= comment.id %>/edit">
        <textarea name="comment" id="" cols="30" rows="10">
            <%= comment.comment %>
        </textarea>
        <button>Save</button>
    </form>
</body>
```

폼 액션에서 저렇게 코딩하면 get 요청밖에 못받음, patch, put, del이 안됨

메소드 오버라이드

클라이언트가 서포트하지 않는 풋, 딜리트 메소드를 사용할 수 있게함

`npm i method-override` 인스톨 필요

여러 사용옵션이 있음

쿼리 밸류

요청 헤더에 명시

```jsx
const methodOverride = require("method-override");

app.use(methodOverride("_method"));
```

메소드 오버라이드 require하고 미들웨어로 사용. 스트링쓸 때 언더스코어형태

이 부분 다시봐야겠다

```jsx
<h1>Edit</h1>
<form method="POST" action="/comments/<%= comment.id %>?_method=PATCH">
```

약간 트릭인데 지금 메소드 보내는 방식은 포스트지만 저기 쿼리 스트링 메소드엔 패치 메소드가 되어있다.

이제 폼으로 수정한거 코멘트 리스트에 반영됨. 업데이트가 된다

### 5. DELETE

delete 메소드 동사는 폼에서 보낼 수 없음. 그래서 위에서 했던것처럼 메소드 오버라이드 하던가 자바스크립트를 사용할 수 있다,.

클릭 이벤트로 딜리트 요청을 보내는거다 액시오스나 fetch API 사용해서

```jsx
app.delete("/comments/:id", (req, res) => {
  const { id } = req.params;
  comments = comments.filter((c) => c.id !== id);
  res.redirect("/comments");
});
```

comments는 const 배열이었지. 저걸 let으로 바꿔줬음.

```jsx
<form method="POST" action="/comments/<%= comment.id %>?_method=DELETE">
  <button>Delete</button>
</form>
```

데이터 보낼 필요 없이 딜리트만 하면 되니까 폼 안에 들어갈건 따로 없다

new 랑 에딧은 폼을 렌더하기 때문에 따로 라우트가 필요없다.

우리는 patch랑 delete 요청을 브라우저에서 또는 폼에서 보낼 수 없다.

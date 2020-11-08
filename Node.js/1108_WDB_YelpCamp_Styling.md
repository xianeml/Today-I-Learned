# yelp Styling

ejs-mate 패키지 사용할거다

: Express 4.x layout, partial and block template functions for the EJS template engine.

`npm i ejs-mate`

```java
const ejsMate = require("ejs-mate");
app.engine("ejs", ejsMate);
```

views/layouts/boilerplate.ejs:

새로 만들어줌

```java
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Boilerplate!!!</title>
</head>
<body>
    <h1>BEFORE</h1>
    <%- body %>
    <h1>AFTER</h1>
</body>
</html>
```

views/campgrounds/index.js:

```java
<% layout('layouts/boilerplate') %>
<h1>All Campgrounds</h1>
```

위아래 body태그 껍대기 다 지우고 위에 레이아웃 함수 호출. 껍데기 보일러플레이트 경로지정

campgrounds 다른 뷰템플릿 파일들에도 이렇게 적용해줌

이제 보일러플레이트에 네브바 적용

# bootstrap5! boilerplate

[https://v5.getbootstrap.com/](https://v5.getbootstrap.com/)

bolierplate.ejs:

```java
<!-- CSS only -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha2/css/bootstrap.min.css" integrity="sha384-DhY6onE6f3zzKbjUPRc2hOzGAdEf4/Dz+WJwBvEYL/lkkIsI3ihufq9hk9K4lVoK" crossorigin="anonymous">`
```

```java
<%- body %>
<!-- JavaScript Bundle with Popper.js -->
<script src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha2/js/bootstrap.bundle.min.js" integrity="sha384-BOsAfwzjNJHrJ8cZidOg56tcQWfp6y72vEJ8xQ9w6Quywb24iOsW913URv1IS4GD" crossorigin="anonymous"></script>
```

```java
<main class="container">
  <%- body %>
</main>
```

[main 태그는](http://www.tcpschool.com/html-tags/main) 해당 문서의 <body> 요소의 주 콘텐츠(main content)를 정의할 때 사용합니다.

main 태그 위에 nav바 삽입

```java
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-link active" aria-current="page" href="#">Home</a>
        <a class="nav-link" href="#">Features</a>
        <a class="nav-link" href="#">Pricing</a>
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </div>
    </div>
  </div>
</nav>
```

필요한 부분 수정

```java
<nav class="navbar sticky-top navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">YelpCamp</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
              <a class="nav-link" href="/">Home</a>
              <a class="nav-link" href="/campgrounds">Campgrounds</a>
              <a class="nav-link" href="/campgrounds/new">New Campgrounds</a>
            </div>
          </div>
        </div>
      </nav>
```

```java
<main class="container mt-5">
```

메인 태그 마진탑 5로 줌.
이 네브바만 잘라내서 새로운 ejs파일로 만들어준다

views/partials/navbar.ejs

```java
<%- include('../partials/navber') %>
    <main class="container mt-5">
```

인클루드 해줌

views/partials/footer.ejs

```java
<footer class="footer bg-dark py-3">
    <div class="container">
        <span class="text-muted">&copy; YelpCamp 2020</span>
    </div>
</footer>
```

```java
<body class="d-flex flex-column vh-10">
    <%- include('../partials/navber') %>
    <main class="container mt-5">
        <%- body %>
    </main>
    <%- include('../partials/footer') %>
```

# Adding Images

[https://source.unsplash.com/](https://source.unsplash.com/)

언스플래시 소스 api

unsplash 가서 키워드 검색하고 collection 보면 이렇게 컬렉션 링크 따올수있다.

models/campground.js

```java
const CampGroundSchema = new Schema({
  title: String,
  image: String,
  price: Number,
```

모델 업데이트. 이미지 자리 넣어줌

price도 넘버로 수정

seeds/index.js:

```java
const price = Math.floor(Math.random() * 20) + 10;
```

```java
image: "https://source.unsplash.com/collection/483251",
discription:
  "  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Hic odit aspernatur, dolor quam ipsam accusamus sapiente iusto eveniet itaque laboriosam adipisci voluptatum incidunt veritatis. Laboriosam tempore labore accusamus ipsam sequi.",
price,
```

이미지 새로 추가해주고

가격은 랜덤으로 받아올거야

`node seeds/index.js` → 몽고 db 확인

`nodemon app.js`

# Styling campgrounds index

부트스트랩 카드 사용

campgrounds/index.ejs:

앞으로 ul li 태그 안쓰고 부트스트랩 카드 사용할거야

```html
<% for(let campground of campgrounds) { %>
<div class="card mb-3">
  <div class="row">
    <div class="col-md-4">
      <img class="img-fluid" src="<%= campground.image %>" />
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title"><%= campground.title %></h5>
        <p class="card-text"><%= campground.description %></p>
        <p class="card-text">
          <small class="text-muted"><%= campground.location %></small>
        </p>
        <a class="btn btn-primary" href="/campgrounds/<%= campground._id %>"
          >View <%= campground.title %></a
        >
      </div>
    </div>
  </div>
</div>
<% } %>
```

이제 상세보기 show 페이지도 카드로 수정할거야

# Styling the new form

```html
<div class="input-group mb-3">
  <span class="input-group-text" id="basic-addon1">@</span>
  <input
    type="text"
    class="form-control"
    placeholder="Username"
    aria-label="Username"
    aria-describedby="basic-addon1"
  />
</div>
```

부트스트랩 form - input groups 요거 카피,
달러로 수정하고 price로 사용

# Styling Edit form

new 에서 썼던거 재사용하고 수정

# Styling show page

부트스트랩 component - card

footer 에러 해결하기.

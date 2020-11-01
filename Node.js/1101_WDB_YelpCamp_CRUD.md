# YELP CRUD

`npm init -y`

`npm i express mongoose ejs`

### app.js

```jsx
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Hello from YelpCamp");
});

app.listen(3000, () => {
  console.log("Serving on port 3000");
});
```

세팅

```jsx
const path = require("path");

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.get("/", (req, res) => {
  res.render("home");
});
```

### views/home.ejs:

```jsx
<body>
  <h1>home</h1>
</body>
```

### models/campground.js:

```jsx
const mongoose = require("mongoose");
const Schema = mongoose.Schema;
```

몽구스 임포트 하고 저 스키마 코드 간단하게 쓰기위한 변수 할당

```jsx
const CampGroundSchema = new Schema({
  title: String,
  price: String,
  description: String,
  location: String,
});

module.exports = mongoose.model("Campground", CampGroundSchema);
```

모델 만들고 export

### app.js:

```jsx
const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/yelp-camp", {
  useNewUrlParser: true,
  useCreateIndex: true,
  useUnifiedTopology: true,
});
```

디비 연결

```jsx
const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));
db.once("open", () => {
  console.log("Database connected");
});
```

```jsx
const Campground = require("./models/campground");
```

```jsx
app.get("/makecampground", async (req, res) => {
  const camp = new Campground({
    title: "My Backyard",
    description: "cheap camping!",
  });
  await camp.save();
  res.send(camp);
});
```

모델 가져온걸로 새 인스턴스 생성하고 디비 저장해줌

# Seeding Campgrounds

데이터 초기값 파일 만들기

seeds 폴더에 cities, seedHelpers 파일 추가

### seeds/index.js:

```jsx
const mongoose = require("mongoose");
const Campground = require("../models/campground");

mongoose.connect("mongodb://localhost:27017/yelp-camp", {
  useNewUrlParser: true,
  useCreateIndex: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));
db.once("open", () => {
  console.log("Database connected");
});
```

쓰던거 가져오고 (모델 가져올때 경로 확인)

```jsx
const seedDB = async () => {
  await Campground.deleteMany({});
  const c = new Campground({ title: "purple field" });
  await c.save();
};

seedDB();
```

원래 있던 값을 지운다

초기값 인스턴스 저장

함수 실행까지 해줘야됨

```jsx
const cities = require("./cities");
```

```jsx
const seedDB = async () => {
  await Campground.deleteMany({});
  for (let i = 0; i < 50; i++) {
    const random1000 = Math.floor(Math.random() * 1000);
    const camp = new Campground({
      location: `${cities[random1000].city}, ${cities[random1000].state}`,
    });
    await camp.save();
  }
};
```

새로 세팅

### seedHelpers.js:

```jsx
module.exports.places = [
```

### index.js:

```jsx
const { places, descriptors } = require("./seedHelpers");
```

```jsx
const sample = (array) => array[Math.floor(Math.random() * array.length)];
```

```jsx
const camp = new Campground({
  location: `${cities[random1000].city}, ${cities[random1000].state}`,
  title: `${sample(descriptors)} ${sample(places)}`,
});
```

랜덤으로 데이터 가져오기

`node seeds/index.js` 다시로딩

몽고확인하고

```jsx
seedDB().then(() => {
  mongoose.connection.close();
});
```

연결 클로즈하기

`node seeds/index.js` 다시로딩하면 바로 연결 끊어짐

이거는 필요할 때만 쓰는거야

# Campground index

app.js

```jsx
app.get("/campgrounds", async (req, res) => {
  const campgrounds = await Campground.find({});
  res.render("campgrounds/index", { campgrounds });
});
```

### views/campgrounds/index.ejs:

```jsx
<h1>All Campgrounds</h1>
<ul>
  <% for(let campground of campgrounds) {%>
      <li><%= campground.title %></li>
  <% } %>
</ul>
```

# Campground show

아이디별로 디테일화면 보여줄거임

```jsx
app.get("/campgrounds/:id", async (req, res) => {
  const campground = await Campground.findById(req.params.id);
  res.render("campgrounds/show", { campground });
});
```

### views/campgrounds/index.ejs:

```jsx
<body>
    <h1>All Campgrounds</h1>
    <ul>
        <% for(let campground of campgrounds) { %>
            <li><a href="/campgrounds/<%= campground._id %>"><%= campground.title %> </a></li>
        <% } %>
    </ul>
</body>
```

### views/campgrounds/show.ejs:

```jsx
<h1><%= campground.title %></h1>
<h2><%= campground.location %></h2>
```

# Campgrounds New & Create

app.js:

```jsx
app.get("/campgrounds/new", (req, res) => {
  res.render("campgrounds/new");
});
```

이 파일에 라우팅 작성하는 순서도 중요하다. new가 id보다 위에있어야됨

new.ejs:

```jsx
<form action="/campgrounds" method="POST">
  <div>
      <label for="title">Title</label>
      <input type="text" name="campground[title]" id="title">
  </div>
  <div>
      <label for="location">Location</label>
      <input type="text" name="campground[location]" id="location">
  </div>
  <button>Add Campground</button>
</form>
```

`name="campground[title]"` 네임을 캠프그라운드로 그룹핑할거임

app.js:

```jsx
app.post("/campgrounds", async (req, res) => {
  res.send(req.body);
});
```

```jsx
app.use(express.urlencoded({ extended: true }));
```

```jsx
app.post("/campgrounds", async (req, res) => {
  const campgorund = new Campground(req.body.campground);
  await campgorund.save();
  res.redirect(`/campgrounds/${campgorund._id}`);
});
```

# Campground Edit & Update

index.js

```jsx
app.get("/campgrounds/:id/edit", async (req, res) => {
  const campground = await Campground.findById(req.params.id);
  res.render("campgrounds/edit", { campground });
});
```

edit.ejs

```jsx
**<body>
    <h1>Edit Campground</h1>
    <form action="/campgrounds" method="POST">
        <div>
            <label for="title">Title</label>
            <input type="text" name="campground[title]" id="title" value="<%= campground.title %>">
        </div>
        <div>
            <label for="location">Location</label>
            <input type="text" name="campground[location]" id="location" value="<%= campground.location %>">
        </div>
        <button>Update Campground</button>
    </form>
    <a href="/campgrounds/<%=campground._id%>">Back to Campground</a>
</body>**
```

`npm i method-override`

app.js

```jsx
const methodOverride = require("method-override");
app.use(methodOverride("_method"));
```

콜트가 했던거라고 엄청 빨리 나간다

이 메소드 오버라이드는 쿼리스트링으로 post 방식을 다른 방식으로 수정하기 위해 사용하는거같음

```jsx
app.put("/campgrounds/:id", async (req, res) => res.send("worked!"));
```

edit.ejs:

```jsx
<form action="/campgrounds/<%= campground._id %>?_method=PUT " method="POST">
```

app.js

```jsx
app.put("/campgrounds/:id", async (req, res) => {
  const { id } = req.params;
  const campground = await Campground.findByIdAndUpdate(id, {
    ...req.body.campground,
  });
  res.redirect(`/campgrounds/${campground._id}`);
});
```

# Campground Delete

app.js:

```jsx
app.delete("/campgrounds/:id", async (req, res) => {
  const { id } = req.params;
  await Campground.findByIdAndDelete(id);
  res.redirect("/campgrounds");
});
```

show.ejs:

```jsx
<p>
  <form
    action="/campgrounds/<%= campground._id %>?_method=DELETE"
    method="POST"
  >
    <button>DELETE</button>
  </form>
</p>
```

# MongooseExpress

`npm init -y`

`npm i express ejs mongoose`

`touch index.js`

`mkdir views`

### index.js:

```jsx
const express = require("express");
const app = express();
const path = require("path");

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.listen(3000, () => {
  console.log("APP IS LISTENING ON PORT 3000!");
});
```

세팅

`nodemon index.js`

```powershell
[nodemon] starting `node index.js`
APP IS LISTENING ON PORT 3000!
```

서버 연결 성공

```jsx
app.get("/dog", (req, res) => {
  res.send("WOOF!");
});
```

라우트를 하나 만들어보자.

[http://localhost:3000/dog](http://localhost:3000/dog)

```jsx
mongoose
  .connect("mongodb://localhost:27017/farmStand", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log("MONGO CONNECTION OPEN!!!");
  })
  .catch((err) => {
    console.log("OH NO MONGO CONNECTION ERROR!!!!");
    console.log(err);
  });
```

몽구스 커넥션 프로미스 처리

```powershell
[nodemon] starting `node index.js`
APP IS LISTENING ON PORT 3000!
MONGO CONNECTION OPEN!!!
```

이제 모델 만들건데 모델 폴더 따로 만들어서 그 안에 작성할거임

앞으로 모델은 많아질거거든

### models/product.js

```jsx
const mongoose = require("mongoose");

const productSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  price: {
    type: Number,
    required: true,
    min: 0,
  },
  category: {
    type: String,
    lowercase: true,
    enum: ["fruit", "vegetable", "dairy"],
  },
});
```

일단 몽구스 require로 임포트해주고 몽구스 커넥션처리는 인덱스가 할거니까 여기선 모델정의만.

일단 스키마 객체 생성해서 컬럼과 제약조건을 만든다. 여기선 키밸류 형태로 키값과 타입을 적는 형식이다.

```jsx
const Product = mongoose.model("Product", productSchema);
```

스키마를 만든 다음 몽구스에게 알려줘야한다. 모델이름 만들고 그 이름 키값으로 스키마 저장

(몽구스는 이걸로 컬렉션을 만든다) 이제 이 모델 사용해서 인스턴스 찍어낼 수 있다.

```jsx
module.exports = Product;
```

다른모듈에서 사용할 수 있도록 지금 만든 모델 export해주기

### models/product.js:

```jsx
const Product = require("./models/product");
```

임포트 받아옴

데이터 초기값을 만들고싶음

### seeds.js:

```jsx
const mongoose = require("mongoose");
const Product = require("./models/product");

mongoose
  .connect("mongodb://localhost:27017/farmStand", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log("MONGO CONNECTION OPEN!!!");
  })
  .catch((err) => {
    console.log("OH NO MONGO CONNECTION ERROR!!!!");
    console.log(err);
  });
```

얘도 모델 임포트 해주고 몽구스 연결

내가 db에서 아무 데이터나 얻고싶을 때 사용하는 파일이다

```jsx
const p = new Product({
  name: "Ruby Grapefruit",
  price: 1.99,
  category: "fruit",
});
```

받아온 프로덕트 모델로 인스턴스 찍어내기

```jsx
p.save()
  .then((p) => {
    console.log(p);
  })
  .catch((e) => {
    console.log(e);
  });
```

이제 p 인스턴스를 디비 저장. 저장과정에서 시간이 걸리니까 프로미스 처리

```powershell
> node seeds.js
MONGO CONNECTION OPEN!!!
{
  _id: 5f9e4c8b97cd3e16fb126819,
  name: 'Ruby Grapefruit',
  price: 1.99,
  category: 'fruit',
  __v: 0
}
```

몽고쉘

`show dbs`

`use farmStand`

`show collections` //products

`db.products.find()`

지금 우리가 p 객체 하나 만들고 save하고 프로미스 작업하는 식으로 인스턴스 만들어서 db에 하나씩 insert할수도 있는데 그것보단 insertMany로 한꺼번에 넣어보자

```jsx
const seedProducts = [
  {
    name: "Fairy Eggplant",
    price: 1.0,
    category: "vegetable",
  },
  {
    name: "Organic Goddess Melon",
    price: 4.99,
    category: "fruit",
  },
  {
    name: "Organic Mini Seedless Watermelon",
    price: 3.99,
    category: "fruit",
  },
  {
    name: "Organic Celery",
    price: 1.5,
    category: "vegetable",
  },
  {
    name: "Chocolate Whole Milk",
    price: 2.69,
    category: "dairy",
  },
];
```

```jsx
Product.insertMany(seedProducts)
  .then((res) => {
    console.log(res);
  })
  .catch((e) => {
    console.log(e);
  });
```

항상 먼저 `node seeds.js` 로 새로 로딩 후 몽고쉘에서 확인할 수 있다

### index.js:

```jsx
app.get("/products", async (req, res) => {
  const products = await Product.find({});
  console.log(products);
  res.send("ALL PRODUCTS WILL BE HERE!");
});
```

라우트 바꿔주고, 모델.find()안에 빈 객체 넣으면 다 가져옴.

시간이 걸리니까 프로미스 처리. then 처리할수도 있고 async 키워드 사용할 수도있고

다시 서버 실행 `nodemon index.js`

[http://localhost:3000/products](http://localhost:3000/products)

서버 실행 후 터미널 콘솔에 모델 객체가 다 출력된다.

### views/products/index.ejs

```jsx
<body>
  <h1>hey</h1>
</body>
```

html로 보여줄 새 파일 만들어줌

### index.js

```jsx
app.get("/products", async (req, res) => {
  const products = await Product.find({});
  console.log(products);
  res.render("products/index");
});
```

이제 이 라우트 응답을 렌더로 indes.ejs 경로 지정해줌

```jsx
res.render("products/index", { products });
```

이제 어웨이트 걸어둔 모든 모델 찾아온 변수를 두번째 인자로 넣어줌

### views/products/index.ejs

```jsx
<h1>hey</h1>
    <ul>
        <% for(let product of products) { %>
            <li><%= product.name %> </li>
        <% } %>
    </ul>
```

그럼 얘는 아무 임포트 필요없이 그냥 태그로 받아와서 그 데이터 쓸 수 있음

![./1101_WDB_mongoose_express/MongooseExpress%2094c7b7ccb169417bb6e8b12b9279db13/Untitled.png](./1101_WDB_mongoose_express/MongooseExpress%2094c7b7ccb169417bb6e8b12b9279db13/Untitled.png)
굳

# Product Details

### index.js:

```jsx
app.get("/products/:id", async (req, res) => {
  const { id } = req.params;
  const product = await Product.findById(id);
  console.log(product);
  res.send("details page!");
});
```

id로 디테일 볼 수 있는 라우트 만들기

:id 요 아이디는 쿼리스트링으로 넘어온 아이디 변수에 담고

Product 모델에서 해당 id를 찾는걸 기다린다. 찾으면 콘솔출력하고 화면에 저 문구 출력보냄

대충 아무아이디 카피해서 확인해보면

[http://localhost:3000/products/5f9e4f25be53f91732a0e4e5](http://localhost:3000/products/5f9e4f25be53f91732a0e4e5) **문구 출력 볼 수 있다**

콘솔에도 찍히고

```jsx
res.render("products/show", { product });
```

얘도 이제 특정 경로로 렌더링 해줄거임. 모델에서 찾아온 데이터 같이 보내기

### views/products/show.ejs

```jsx
<body>
    <h1><%= product.name %> </h1>
    <ul>
        <li>Price: $<%= product.price %> </li>
        <li>Category: <%= product.category %> </li>
    </ul>
</body>
```

이제 index.ejs 리스트에 링크걸어줄거임. 일로 올 수 있게

### views/products/index.ejs

```jsx
<ul>
  <% for(let product of products) { %>
      <li><a href="/products/<%= product._id %>"><%= product.name %></a></li>
  <% } %>
</ul>
```

![./1101_WDB_mongoose_express/MongooseExpress%2094c7b7ccb169417bb6e8b12b9279db13/Untitled%201.png](./1101_WDB_mongoose_express/MongooseExpress%2094c7b7ccb169417bb6e8b12b9279db13/Untitled%201.png)

### views/products/show.ejs

```jsx
<a href="/products">All Products</a>
```

돌아가기 버튼도 구현

![./1101_WDB_mongoose_express/MongooseExpress%2094c7b7ccb169417bb6e8b12b9279db13/Untitled%202.png](./1101_WDB_mongoose_express/MongooseExpress%2094c7b7ccb169417bb6e8b12b9279db13/Untitled%202.png)

# Creating Products

### views/products/index.ejs

```jsx
app.get("/products/new", (req, res) => {
  res.render("products/new");
});
```

얘는 어싱크 할거없음

### views/products/new.ejs

```jsx
<body>
    <h1>Add A Product</h1>
    <form action="/products" method="POST">
        <label for="name">Product Name</label>
        <input type="text" name="name" id="name" placeholder="product name">
        <label for="price">Price</label>
        <input type="number" name="price" id="price" placeholder="product price">
        <label for="category">Select Category</label>
        <select name="category" id="category">
            <option value="fruit">fruit</option>
            <option value="vegetable">vegetable</option>
            <option value="dairy">dairy</option>
        </select>
        <button>Submit</button>
    </form>
</body>
```

폼 만들기. 전송은 프로덕트 메인으로가고

각 인풋과 라벨 달아주고 데이터 파싱위한 name 속성과 라벨과 맞추기 위한 id 속성 들어가고

서브밋버튼까지

이제 서브밋 라우트 만들겨

### views/products/index.ejs

```jsx
app.post("/products", (req, res) => {
  console.log(req.body);
  res.send("making your product!");
});
```

똑같은 /product 라우트지만 얘는 post 요청을 처리한다

```jsx
app.use(express.urlencoded({ extended: true }));
```

일단 넘어온걸 알아들을 수 있게 미들웨어로 파싱해야함

브라우저에서 큐컴버 만들어서 전송해보면 메세지도 뜨고 콘솔에도 출력되는거 확인

이제 진짜 인스턴스로 찍어내서 디비 저장해야지

```jsx
app.post("/products", async (req, res) => {
  const newProduct = new Product(req.body);
  await newProduct.save();
  console.log(newProduct);
  res.send("making your product!");
});
```

요청바디에 있는 내용(넘어온 내용) 그대로 인스턴스 생성해주고 새 변수에 담아서 그거 디비에 save

저장하는 시간 기다리기.

새로고침하면 폼 재전송 되지 않게 응답 리다이렉트 해줄거다

```jsx
res.redirect(`/products/${newProduct._id}`);
```

# Updating Products

### index.js

```jsx
app.get("/products/:id/edit", async (req, res) => {
  const { id } = req.params;
  const product = await Product.findById(id);
  res.render("products/edit", { product });
});
```

edit라우트. 모델에서 아이디로 찾아온 데이터를 edit.ejs로 보냄

이 라우트로 요청이 오면 찾은 데이터를 화면에 보여줄 수 있게 데이터 넘기는 작업만 함

### views/products/edit.ejs

```jsx
<h1>Edit Product</h1>
<form action="/products/<%=product._id%>" method="POST">
    <label for="name">Product Name</label>
    <input type="text" name="name" id="name" placeholder="product name" value="<%= product.name %>">
    <label for="price">Price</label>
    <input type="number" name="price" id="price" placeholder="product price" value="<%= product.price %>">
    <label for="category">Select Category</label>
    <select name="category" id="category" >
        <option value="fruit">fruit</option>
        <option value="vegetable">vegetable</option>
        <option value="dairy">dairy</option>
    </select>
    <button>Submit</button>
</form>
<a href="./products/<%= product._id%>">Cancel</a>
```

폼전송은 디테일 라우트로 간다. new랑 거의 같음

이미 작성된 폼을 다시 불러오는 거라 밸류에 데이터 그대로 할당해주면된다.

### index.js

```jsx
app.put("/products/:id", async (req, res) => {
  console.log(req.body);
  res.send("Put!!!");
});
```

업뎃은 put 요청 사용한다그랬지

문제는 실제로 put 요청을 만들 수 없음

저 폼 메소드는 POST 계속 사용할거고 npm 패키지 method-override가 필요하다

`npm i method-override`

```jsx
const methodOverride = require("method-override");
app.use(methodOverride("_method"));
```

설치하고 임포트

```jsx
<form action="/products/<%=product._id%>?_method=PUT" method="POST">
```

쿼리 스트링으로 PUT 요청으로 바꿔주기

```jsx
app.put("/products/:id", async (req, res) => {
  const { id } = req.params;
  const product = await Product.findByIdAndUpdate(id, req.body, {
    runValidators: true,
    new: true,
  });
  res.redirect(`/products/${product._id}`);
});
```

모델에서 아이디로 찾아서 그걸 업뎃해주는 메소드 사용.

업뎃하고 응답 리다이렉트는 상세보기 페이지로

### show.ejs

```jsx
<a href="/products/<%=product._id %>/edit">Edit Products</a>
```

eidt으로 갈수 있게 링크 추가

edit에서 셀렉트 밸류도 가져온 데이터 할당해주려면

```html
<select name="category" id="category" >
  <option value="fruit" <%= product.category === 'fruit' ? 'selected': '' %>>fruit</option>
  <option value="vegetable" <%= product.category === 'vegetable' ? 'selected': '' %>>vegetable</option>
  <option value="dairy" <%= product.category === 'dairy' ? 'selected': '' %>>dairy</option>
</select>
```

이렇게 쓰면 되는데 상당히 못생겼다

카테고리가 더 많아진다면? 옵션 태그에 반복문을 사용하는게 낫다

### index.js

```jsx
const categories = ["fruit", "vegetable", "dairy"];
```

카테고리 변수 만들어주고 이거 사용하는 애들한테 전달

```jsx
**app.get("/products/new", (req, res) => {
  res.render("products/new", { categories });
});**
```

### views/products/new.ejs:

```jsx
<select name="category" id="category">
  <% for(let category of categories) {  %>
      <option value="<%=category%>"><%= category%></option>
  <% } %>
</select>
```

이제 카테고리 새로 추가해도 동적으로 받아옴

### index.js

```jsx
app.get("/products/:id/edit", async (req, res) => {
  const { id } = req.params;
  const product = await Product.findById(id);
  res.render("products/edit", { product, categories });
});
```

### views/products/edit.ejs:

```jsx
<select name="category" id="category" >
  <% for(let category of categories) {  %>
      <option value="<%=category%>" <%=product.category === category ? 'selected' : '' %>><%= category%></option>
  <% } %>
</select>
```

못생긴건 똑같은데 그래도 동적으로 받아올 수 있음

# Deleting Products

### show.ejs:

```jsx
<form action="/products/<%=product._id %>?_method=DELETE" method="POST">
  <button>Delete</button>
</form>
```

삭제 버튼을 이렇게 폼으로 쿼리스트링 delete 방식으로 보내는구나

### index.js

```jsx
app.delete("/products/:id", async (req, res) => {
  const { id } = req.params;
  const deleteProduct = await Product.findByIdAndDelete(id);
  res.redirect("/products");
});
```

쉬운 삭제

# Filtering By Categories

카테고리별로 보여주고싶은듯. 태그

### show.ejs

```jsx
<li>Category:
	<a href="/products?category=<%= product.category %>">
		<%= product.category %>
	</a>
</li>
```

### index.js

```jsx
app.get("/products", async (req, res) => {
  const { category } = req.query;
  if (category) {
    const products = await Product.find({ category });
    res.render("products/index", { products, category });
  } else {
    const products = await Product.find({});
    res.render("products/index", { products, category: "All" });
  }
});
```

### index.ejs:

```jsx
<% if(category !== 'All') { %>
  <a href="/products">All Product</a>
<% } %>
```

다시 전체보기 갈 수 있게 링크 추가

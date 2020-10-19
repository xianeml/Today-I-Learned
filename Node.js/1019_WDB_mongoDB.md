# nosql

테이블을 서로 참조하면서 접근할 수 있다.

document oriented database

이건 xml, json 이런 파일에 데이터를 저장하는 것

우리는 테이블을 나눌 필요없고

쉽게 필드를 추가할 수 있음

# Mongo

js 베이스라면 익스프레스와 같이 사용하기 좋다.

install

[Install MongoDB Community Edition on macOS - MongoDB Manual](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/#install-mongodb-community-edition)

# mongo shell

`mongo` 라고 입력하면 이거 사용가능. 노드 레플같음

`db` 사용하는 디비 보여주는 명령어. 디폴트 디비는 test임

`show dbs` 디비들 보여줌

`use animalShelter` 이 디비 사용할거다

show dbs 해보면 이게 안보임. 아직 데이터 안넣어서그렇다

# BSON

몽고는 제이슨 형태 사용

json 파일만으로 데이터 관리하기엔 한계가 있다.

bson binary json 제이슨 컴팩트 버전

제이슨이랑 완전 같은건 아니다, 포함할 수 있는 데이터 타입도 다름

server docs 문서보면 볼게많다. crud operations 섹션 보기

# 1. insert

데이터 컬렉션을 만들거임

`show collections` 해보면 아직 암것도없음

```jsx
> db.dogs.insertOne({name:"Charlie", age: 3, breed: "corgi", catFriendly: true})

{
	"acknowledged" : true,
	"insertedId" : ObjectId("5f8bf1a89c1f861150b13cb1")
}
>
```

dogs 라는 컬렉션에 데이터를 추가했습니다

```jsx
> db.dogs.find()
{ "_id" : ObjectId("5f8bf1a89c1f861150b13cb1"), "name" : "Charlie", "age" : 3, "breed" : "corgi", "catFriendly" : true }
```

아이디 자동 생성. 모든 엘레먼트에 유니크하게생김

insertOne 이 아니라 many, multi도 할 수 있다

```jsx
> db.dogs.insert([{name: "Wyatt", breed: "Golden", age: 14, catFriendly: false},{name: "Tonya", breed: "Chihuahua", age: 17, catFriendly: true}])
BulkWriteResult({
	"writeErrors" : [ ],
	"writeConcernErrors" : [ ],
	"nInserted" : 2,
	"nUpserted" : 0,
	"nMatched" : 0,
	"nModified" : 0,
	"nRemoved" : 0,
	"upserted" : [ ]
})
> db.dogs.find()
{ "_id" : ObjectId("5f8bf1a89c1f861150b13cb1"), "name" : "Charlie", "age" : 3, "breed" : "corgi", "catFriendly" : true }
{ "_id" : ObjectId("5f8bf29a9c1f861150b13cb2"), "name" : "Wyatt", "breed" : "Golden", "age" : 14, "catFriendly" : false }
{ "_id" : ObjectId("5f8bf29a9c1f861150b13cb3"), "name" : "Tonya", "breed" : "Chihuahua", "age" : 17, "catFriendly" : true }
>
```

그냥 insert로 여러개 객체 넣을 수 있다. 객체 여러개넣을땐 배열로 넣는 거 알쥐?

저렇게 입력하면 잘 넣어졌다고 컴펌해주는 답을 보여준다. 도그 디비 확인해보면 잘들어간거 확인가능.

```jsx
> db.cats.insert({name:"Blue", age: 6, dogFriendly: false, breed: "Scottish fold"})
WriteResult({ "nInserted" : 1 })
> db.cats.find()
{ "_id" : ObjectId("5f8bf3339c1f861150b13cb4"), "name" : "Blue", "age" : 6, "dogFriendly" : false, "breed" : "Scottish fold" }
```

고양이도 넣기

# 2. finding with mongo

원하는 데이터를 디비에서 가져오기 위해 쿼리를 사용해야함

`db.collection.find()`

인자로 키밸류 객체 하나 넘겨주고 그거 해당하는 데이터 찾을 수 있음,

# 3. Updating

updateOne 은 항상 첫번째꺼만 매칭해줌

```jsx
> db.dogs.updateOne({name: 'Charlie'}, {age: 4})
uncaught exception: Error: the update operation document must contain atomic operators :
DBCollection.prototype.updateOne@src/mongo/shell/crud_api.js:565:19
@(shell):1:1
```

바꿀 대상을 첫번째 자리에 넣고, 두번째 인자 자리의 객체로 업데이트해줄거임

errrorrr

update 할 땐 \$set 이라는 연산자가 앞에 필요함

{ \$set: { <field1>: <value1>, ...} }

```jsx
> db.dogs.updateOne({name: 'Charlie'}, {$set: {age: 4}})
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }

> db.dogs.find()
{ "_id" : ObjectId("5f8bf1a89c1f861150b13cb1"), "name" : "Charlie", "age" : 4, "breed" : "corgi", "catFriendly" : true }
```

```jsx
> db.dogs.updateOne({name: 'Charlie'}, {$set: {age: 5, breed: 'Lab'}})
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }

> db.dogs.find()
{ "_id" : ObjectId("5f8bf1a89c1f861150b13cb1"), "name" : "Charlie", "age" : 5, "breed" : "Lab", "catFriendly" : true }
```

없던 내용도 새로 추가 가능

```jsx
> db.dogs.updateMany({catFriendly: true}, {$set: {isAvailable: false}})
{ "acknowledged" : true, "matchedCount" : 2, "modifiedCount" : 2 }
```

여러개 업뎃

`$currentDate` 이 연산자도 있는데 이건 문서 날짜 현재날짜로 업뎃해줌

```jsx
> db.cats.updateOne({age: 6}, {$set: {age: 7}, $currentDate: {lastChanged: true}})
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }

> db.cats.findOne()
{
	"_id" : ObjectId("5f8bf3339c1f861150b13cb4"),
	"name" : "Blue",
	"age" : 7,
	"dogFriendly" : false,
	"breed" : "Scottish fold",
	"lastChanged" : ISODate("2020-10-18T08:59:40.594Z")
}
```

조그만거 수정이 아니라 완전 바꿔버리고 싶으면 replaceOne 을 사용한다.

# 4. Deleting

```jsx
> db.cats.deleteOne({name: 'Blue'})
{ "acknowledged" : true, "deletedCount" : 1 }
```

```jsx
> db.dogs.deleteMany({isAvailable: false})
{ "acknowledged" : true, "deletedCount" : 2 }

> db.dogs.find()
{ "_id" : ObjectId("5f8bf29a9c1f861150b13cb2"), "name" : "Wyatt", "breed" : "Golden", "age" : 14, "catFriendly" : false }
>
```

```jsx
> db.dogs.deleteMany({})
{ "acknowledged" : true, "deletedCount" : 1 }
```

인자에 아무것도 안써주면 전체지우기

추가 오퍼레이터 → 다음에 다시

docs - server- reference - operations - query and projection operators

비교, 논리, 지오그래피관련, 배열관련,

```jsx
> db.dogs.find({age: {$gte: 10}})
```

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# Mongoose

몽고db랑 서버를 연결하기 위한 node.js드라이버들이 많이 있음 npm으로 설치 가능

몽구스는 odm : object document mapper

몽고랑 노드를 연결함

스키마 정의, 쿼리

몽구스는 데이터나 문서를 자바스크립트 객체로 매핑할거다

sql은 orm이다. object relational mappper

몽구스는 오라클이랑 자바 연결하는 마이바티스같은 역할

mongodb 도 보통 우리가 JDBC 코딩할때처럼, 네이티브로 프로그래밍을 할 수 있지만,

우리가 JDBC로 코딩하지 않고, ibatis, mybatis, jpa시리즈들을 사용하듯이,

몽구스를 사용하는 것 같다.

```jsx
const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/movieApp", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
```

연결하는 uri 정보 보면 로컬 몽고db 찾고, 어떤 데이터베이스 사용하고있는지 적는다.

# mogoose model

자바스크립트 클래스. 몽고db 컬렉션으로 보여줌

내가 movie 모델을 만들면 그 모델에 접근할 수 있게 몽구스 메소드 사용할 수 있음

스키마

몽고에서 서로 다른 컬렉션 key를 서로다른 자바스크립트 타입으로 매핑함

```jsx
const movieSchema = new mongoose.Schema({
  title: String,
  year: Number,
  score: Number,
  rating: String,
});
```

자바처럼 타입 정의해줌

스키마 만들고 몽구스에게 알려줘야함

```jsx
const Movie = mongoose.model("Movie", movieSchema);
```

모델이름 중요. 첫글자 대문자 `Movie`

몽구스는 이걸로 컬렉션을 만든다. pluralize(복수형)으로 만들고 소문자로 `movies`

Movie 라는 모델클래스를 만들었다

```jsx
const amadeus = new Movie({
  title: "Amadeus",
  year: 1986,
  score: 9.2,
  rating: "R",
});
```

새로운 인스턴스 생성

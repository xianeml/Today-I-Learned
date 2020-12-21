### Vue-CLI 3 설치

`npm install -g @vue/cli` / `yarn global add @vue/cli`

`vue --version`

### 환경설정

`vue create 프로젝트명`

default / yarn

`cd my-app`

`yarn serve`

### 스니펫 익스텐션 설치 : Vetur

## 컴포넌트 구성

App.vue:

- template: html 구현부분. div#app 안에 코드 작성
- script: 코드 구현. 앵귤러 component class 코드 구현과 비슷
- style: css 설정. 뷰 파일안에 한꺼번에작성

```jsx
<template>
  <div id="helllo">
      <h1>{{msg}}</h1>
  </div>
</template>

<script>
export default {
    name:"hello",
    props:{
        msg:String
    }
}
</script>
```

```jsx
<template>
  <div id="app">
    <HelloWorld msg="Mihyun"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>
```

### 실습1: bookList

BookList.vue:

```jsx
<template>
    <div class="app">
        <h1>도서목록</h1>
        <ul>
            <li>
                <img src="../assets/image/a.jpg" width="100" height="100">
                위험한 식탁
            </li>
            <li>
                <img src="../assets/image/b.jpg" width="100" height="100">
                공부의 비결
            </li>
            <li>
                <img src="../assets/image/c.jpg" width="100" height="100">
                오메트라
            </li>
            <li>
                <img src="../assets/image/d.jpg" width="100" height="100">
                행복한 여행
            </li>
            <li>
                <img src="../assets/image/e.jpg" width="100" height="100">
                해커스 토익
            </li>
            <li>
                <img src="../assets/image/f.jpg" width="100" height="100">
                도로 안내서
            </li>
        </ul>
    </div>
</template>
<script>
export default {
    name:'bookList',
}
</script>
```

전체내용 작성

```jsx
<template>
  <div>
    <BookList />
  </div>
</template>

<script>
import BookList from './components/BookList.vue';

export default {
  name: 'App',
  components: {
    BookList
  }
}
</script>
```

import 후 컴포넌트 사용

## props 속성

부모에서 자식으로 데이터 전송

### 1. array of Strings

- 자식에서 props 속성으로 데이터 처리(문자의 배열)

```jsx
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld username="홍길동" age="20" my-address="서울"/>
  </div>
</template>
```

`my-address`같은 케밥표기법으로 넘기면 받는쪽은 `myAddress`같은 카멜표기법으로 받아야함

```jsx
<template>
  <div class="hello">
    <h1>{{username}}, {{age}}, {{myAddress}}</h1>
  </div>
</template>

<script>
export default {
  name:"helloWorld",
  props:["username", "age", "myAddress"]
}
</script>
```

부모에서 지정한 여러 속성들을 스트링타입 배열로 한꺼번에 받아서 사용할 수 있다.

### 2. props 타입 지정

문자열 말고 **숫자, 배열,불린,객체등은 반드시 v-bind 문자열 사용해야 한다**.

```html
<template>
  <div id="app">
    <HelloWorld username="홍길동" v-bind:age="20" my-address="서울" isMarried
    v-bind:isMarried2="false" v-bind:phones="[100,200,300]"
    v-bind:author="{name:"Veronica", company:"Veridian Dynamics"}" />
  </div>
</template>
```

```tsx
<template>
  <div class="hello">
    <h1>{{ username }}, <br>
      {{age+100}}, <br>
      {{myAddress}}<br>
      {{isMarried}}<br>
      {{!isMarried2}}<br>
      {{phones}}<br>
      {{author.name}}
      </h1>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:{
      username:String,
      age:Number,
      myAddress:String, //카멜표기법
      isMarried:Boolean,
      isMarried2:Boolean, //주의
      phones:Array,//배열
      author:Object //주의
  }
}
</script>
```

자식은 프랍스 타입 지정해서 받음

### 1-3 type_default

```jsx
<template>
  <div class="app">
    <h1>{{username}}, {{age}}, {{myAddress}}</h1>
  </div>
</template>

<script>
export default {
  name:"HelloWorld",
  props:{
    username:String,
    age:{
      type:Number,
      default:100
    },
    myAddress:{
      type:String,
      default:"제주"
    }
  }
}
```

디폴트값을 지정해서 받을 수 있다.

## data 속성

- 컴포넌트내의 **로컬 상태 정보**를 저장하기 위하여 data 옵션 사용 가능.
- 주의할 점은 반드시 **함수 형태**로 작성해야 된다.

```jsx
<template>
  <div id="app">
    data x:{{x}}, data y:{{y}}<br>
    <HelloWorld username="홍길동" v-bind:age="20" my-address="서울"/>
  </div>
</template>

<script>
import func from '../vue-temp/vue-editor-bridge'
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
  },
data: function(){
  return {x:"홍길동", y:"40",}
}
}
</script>
```

여기서 data가 바뀌면 뷰는 리렌더링된다.

### data 및 props

```jsx
export class Person {
  username;
  age;
  constructor(u, a) {
    this.username = u;
    this.age = a;
  }
  getUsername() {
    return this.username;
  }
  getAge() {
    return this.age;
  }
}
```

```jsx
<template>
  <div id="app">
    data x :{{x}}, data y: {{y}}<br>
    data z: {{z}}<br>
    data k: {{k.aa}}, {{k.bb}}<br>
    data p: {{p.username}}, {{p.age}}<br>
    <HelloWorld username="홍길동" v-bind:age="20" my-address="서울" />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import {Person} from './components/Person';

export default {
  name:"App",
  components:{
    HelloWorld,
  },
  data: function(){
    return {
      x:"홍길동",
      y:'40',
      z:[10,20,30],
      k:{aa:'hong', bb:30},
      p:new Person("aaa", 20) //Person.js import
    };
  }
}
</script>
```

### props data 전송

```jsx
<template>
  <div id="app">
    <HelloWorld v-bind:username="x" :age="y" v-bind:arr="z" />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';

export default {
  name:"App",
  components:{
    HelloWorld,
  },
  data:function(){
    return {
      x:'홍길동',
      y:40,
      z:[10,20,30],
    };
  }
}
</script>
```

props 속성값으로 data값을 지정할 수 있다.

### 동적으로 v-bind:[속성명] 지정 가능

```jsx
<template>
  <div id="app">
    <HelloWorld v-bind:[attributeName]="x"  v-bind:age=y   :arr="z"/>
    <!-- <HelloWorld v-bind:username="x"  v-bind:age=y   :arr="z"/> 과 동일-->
  </div>
</template>

<script>
import  HelloWorld from './components/HelloWorld.vue';

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data:function () {
    return {
      x:'홍길동',   //자식에게 전달
      y:40,
      z:[100,200,300],
      attributeName:'username'  //속성명으로 사용 추가
    }
  }//end data
}
</script>
```

### 6-실습2-img_bind

```jsx
<template>
  <div class="app">
    <BookList :bookList="list" />
  </div>
</template>

<script>
import BookList from './components/BookList.vue';
export default {
  name:'App',
  components:{
    BookList,
  },
  data:function() {
    return{
      list:[  {id:'p01', name:'위험한 식탁', price:2000, date:'20170401', img:'a'},
          {id:'p02',name:'공부의 비결',price:3000,date:'20170402',img:'b'},
          {id:'p03',name:'오메르타',   price:2500,date:'20170401',img:'c'},
        {id:'p04',name:'행복한 여행',price:4000,date:'20170401',img:'d'},
        {id:'p05',name:'해커스 토익',price:2000,date:'20170401',img:'e'},
        {id:'p06',name:'도로 안내서',price:2000,date:'20170401',img:'f'},
        ]
    }
  }
}
</script>
```

```html
<template>
  <div class="app">
    <h1>도서 목록 {{bookList.length}}권</h1>
    <ul>
      <li v-for="book in bookList" v-bind:key="book.name">
        <!--v-bind:key="유일값" -->
        <img v-bind:src="require(`@/assets/image/${book.img}.jpg`)" />
        {{book.name}}
      </li>
    </ul>
    <!-- <img src='../assets/image/a.jpg'> -->
  </div>
</template>

<script>
  export default {
    name: 'BookList',
    props: {
      bookList: Array, //주의
    },
  };
</script>
```

첵 배열 받고

반복문 사용할땐 `v-for` 디렉티브 사용. 반드시 key값이 있어야한다.

이미지 src는 단순 스트링 값이 아닌 경로를 불러올 수 있게 v-bind 해야한다.

require로 경로 불러오고 템플릿리터럴 사용해서 작성. @이거는 경로 축약형

## methods 속성

- Vue 인스턴스에서 사용할 메서드를 등록하는 방법( Vue인스턴스,디렉티브,{{}} 에서 호출 가능 )
- 캐싱 없이 메서드 매번 호출

```jsx
<template>
  <div class="hello">
    <h1>{{msg}}</h1>
    <h2>{{username}}, {{age}}</h2>
    함수호출정보: {{sayEcho()}}<br>
    함수호출정보: {{test()}}<br>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  data: () => ({username: '홍길동', age:20}),
  methods:{
    sayEcho:function(){return this.username + "\t" + this.age;},
    test:function(){return this.username + "\t" + this.age}
  }
}
</script>
```

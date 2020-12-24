## Axios 엑시오스

AngularDeptWeb 스프링 프로젝트 import

myapp> `npm install --save axios`

프로젝트 프로퍼티 수정

DeptController:

`@CrossOrigin`

크로스 도메인 요청에 대한 응답 허용. 서버와 다른 곳에서 요청이 왔을 때 응답허용하게끔

`@ResponseBody` : 비동기 요청 응답

```jsx
//목록보기
	@RequestMapping(value="/",
			method=RequestMethod.GET)
	@CrossOrigin	// 크로스 도메인 요청에 대한 응답 허용
	public  @ResponseBody List<Dept> list() {
		System.out.println("list>>>>>>>>>>>>>>> 호출됨  get방식 ");
		return  service.list();
	}
```

이렇게 응답할 경우 제이슨 형태로 내보내짐

프로젝트 서버 확인

src_15_axios_dept_list - 복사본

helloworld.vue:

```jsx
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  props: {},
  data: function() {
    return { list: [] };  // 전체 사원목록 저장
  },
  beforeMount() {
    this.x();
  },
```

일단 제이쿼리 스크립트 추가

사원전체목록 저장해줄 리스트를 데이터로 만들고

마운트되기 전에 x 자동호출

```jsx
methods: {
    x: function() {
      var xxx = this.list;
      ////npm install axios --save
      //스프링에서 서버 가동후 브라우저에서 서버 주소 복/붙
      //yarn serve시 node-module없다는 에러 발생시
      //npm install --save core-js 실행
      axios
        .get("http://localhost:8095/app/") // get방식 요청
        .then((res) => {
          console.log(res);
          res.data.map(function(ele, idx) {
            xxx.push(ele);
          });
        })
        .catch((error) => console.log(error));
    },
  },
};
```

서버에 접속해서 데이터 받아오기

.then은 제이쿼리로 따지면 success인 경우에 해당.

응답정보 콘솔에 찍어보고 넘어온 데이터를 꺼내와서 하나하나 맵으로 반복돌려줌. 하나하나 배열에 저장

이제 리스트엔 데이터가 다 저장됨

```jsx
<tbody>
  <tr v-for="(dept, idx) in list" :key="idx">
    <td>{{ dept.deptno }}</td>
    <td>{{ dept.dname }}</td>
    <td>{{ dept.loc }}</td>
  </tr>
</tbody>
```

src_15_axios_dept_list2_add

add 뷰에서 데이터 추가하면 서버에보내서 저장

데이터를 list뷰에 보내서 데이터가 등록되고 얘를 화면에 뿌려주게됨

```jsx
<h2>부서등록 및 수정</h2>
    <form v-on:submit.prevent="x">
      부서번호:<input type="text" name="deptno" v-model="dept.deptno" />
      부서명:<input type="text" name="dname" v-model="dept.dname" />
      부서위치:<input type="text" name="loc" v-model="dept.loc" />
      <button>저장</button>
    </form>
```

서버에서 받을 수 있게 네임값 지정

저장을 누르면 x함수 호출 → data에 저장됨

```jsx
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
import axios from "axios";
import eventBus from "./EventBus";
export default {
  name: "DeptAdd",
  data: function() {
    return {
      dept: { // textbox 기입한 데이터 저장
        deptno: "",
        dname: "",
        loc: "",
      },
    };
  },
```

이벤트버스.vue:

```jsx
<script>
  import Vue from "vue"; var eventBus = new Vue(); export default eventBus;
</script>
```

```jsx
methods: {
    x: function(e) {
      var url = "http://localhost:8095/app/add";
      console.log("==========================", this.dept);
      axios
        .post(url, { // post 방식으로 url 요청, data전송
          deptno: this.dept.deptno,
          dname: this.dept.dname,
          loc: this.dept.loc,
        })
        .then((res) => {
          eventBus.$emit("xyz", this.dept); //insert 성공후 이벤트 버스에 저장
        })
        .catch();
    },
  },
```

저 키값으로 위에있는 데이터를 전송한다.

success된 경우에 이벤트버스에 에밋하면서 xyz라는 이벤트명으로 방금전 db에 넣었던 3가지 값을 이벤트 버스에 태워준다.

스프링 DeptController:

```jsx
//저장하기
	@RequestMapping(value="/add",
			method=RequestMethod.POST)
	@CrossOrigin
	public @ResponseBody void add(@RequestBody Dept xxx) {
		System.out.println("add>>>>>>>>>>>>>>>POST");
		 service.insert(xxx);
	}
	@RequestMapping(value="/add",
			method=RequestMethod.GET)
	@CrossOrigin
	public @ResponseBody void add2(Dept xxx) {
		System.out.println("add>>>>>>>>>>>>>>>GET");
		 service.insert(xxx);
	}
```

서버쪽에서는 전송된걸 Dept 모델클래스 만들어서 그 타입으로 받음

DeptList.vue:

이벤트버스에 태운걸 꺼내와서 추가해주면된다

```jsx
import axios from "axios";
import eventBus from "./EventBus.vue";
export default {
  name: "DeptList",
  props: {},
  data: function() {
    return { list: [] };
  },
  beforeMount() {
    this.x();
  },
  //emit처리  ////////////////////////
  created() {
    eventBus.$on("xyz", this.y); // 처리함수 등록
  },
```

이벤트 받아서 y함수에서 이걸 처리하겠다

이 y함수는 넘어온 dept 데이터 받아서 리스트에 추가해주면된다

```jsx
methods: {
    x: function() {
      var xxx = this.list;
      //스프링에서 서버 가동후 브라우저에서 서버 주소 복/붙
      //yarn serve시 node-module없다는 에러 발생시
      //npm install --save core-js 실행
      axios
        .get("http://localhost:8095/app/")
        .then((res) => {
          console.log(res);
          res.data.map(function(ele, idx) {
            xxx.push(ele);
          });
        })
        .catch((error) => console.log(error));
    }, //end x
    y: function(dept) {  // 넘어온 데이터 받기
      console.log("dept>>", dept);
      this.list.push(dept);
    }, //end y
  },
```

y함수는 넘어온 데이터 한번 찍어보고 list에 push 하면서 dept를 넘겨줌

이제 위에서

```jsx
<tbody>
  <tr v-for="(dept, idx) in list" :key="idx">
    <td>{{ dept.deptno }}</td>
    <td>{{ dept.dname }}</td>
    <td>{{ dept.loc }}</td>
  </tr>
</tbody>
```

for문 돌아가며 다시한번 뿌려줌

```jsx
### Cause: java.sql.SQLDataException: ORA-01438: value larger than specified precision allowed for this column
```

부서번호에 자릿수제한있음

### 부서삭제

부서번호로 db삭제하고 이벤트버스에 태워서 리스트로 보내줌. 리스트는 버스에서 부서번호 뽑아서 리스트에서 해당하는 정보 삭제

src_15_axios_dept_list2_add2_delete

```jsx
methods: {
    x: function(e) {
      var url = "http://localhost:8095/app/del?deptno=" + this.deptno;
      axios
        .delete(url) // delete방식 method 호출
        .then((res) => {
          eventBus.$emit("xyz2", this.deptno); //xyz2로 전달
        })
        .catch(function() {
          console.log("에러 발생");
        });
    }, //end x
  }, //end methods
};
```

url에 deptno도 파라미터로 넘겨줌

부서번호를 이벤트버스에 저장. 이제 얘를 리스트가 받아서 리스트에서 삭제하면된다

```jsx
//삭제하기
	@RequestMapping(value="/del",
			method=RequestMethod.DELETE)
	@CrossOrigin
	public @ResponseBody void del(int deptno) {
		service.delete(deptno);
	}
	@RequestMapping(value="/del2/{deptno}",
			method=RequestMethod.DELETE)
	@CrossOrigin
	public @ResponseBody void del2(@PathVariable int deptno) {
		System.out.println("@PathVariable>> del");
		service.delete(deptno);
	}
```

deptList.vue:

```jsx
y: function(dept) {
  //데이터를 list에 추가
  console.log("dept>>", dept);
  this.list.push(dept);
}, //end y
y2: function(deptno) {
  //삭제시
  var xxx = this.list;
  this.list.map(function(ele, idx) {
    if (ele.deptno == deptno) {
      xxx.splice(idx, 1);
    }
  });
}, //end y2
```

deptno에 해당하는 애 하나를 삭제함

삭제된 내용이 위 템플릿에서 다시 출력됨

## Router

`npm install vue-router`

app.vue:

```jsx
<template>
  <div id="app">
    <router-link to="/">Home</router-link><br>
    <router-link to="/login">login</router-link><br>
    <router-view></router-view>
    <!-- 라우팅 된 컴포넌트가 보여질 부분 -->
  </div>
</template>
```

src/router.js:

```jsx
import Vue from 'vue';
import VueRouter from 'vue-router';

import Bar from './components/Bar.vue';
import Foo from './components/Foo.vue';
import NotFound from './components/NotFound.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: Bar, name: 'Bar' },
  { path: '/login', component: Foo, name: 'Foo' },
  { path: '*', component: NotFound, name: 'NotFound' },
];

const router = new VueRouter({ routes });
export default router;
```

링크에 해당하는 컴포넌트 등록

라우터를 밖에서 사용할 수 있게 export

```jsx
import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

new Vue({
  router, // 라우터 등록
  render: (h) => h(App),
}).$mount('#app');
```

이제 main.js에 최종등록

앵귤러의 m module이라고 생각

### 라우터 props 전달

```jsx
<template>
  <div id="app">
    <router-link to="/">Home</router-link><br>
    <router-link to="/login/홍길동">login-foo</router-link><br>
    <router-link to="/my/1234">login-foo</router-link><br>
    <router-link to="/knu">knu</router-link><br>
    <router-view></router-view>
    <!-- 라우팅 된 컴포넌트가 보여질 부분 -->
  </div>
</template>
```

router.js

```jsx
import Vue from 'vue';
import VueRouter from 'vue-router';

import Bar from './components/Bar.vue';
import Foo from './components/Foo.vue';
import NotFound from './components/NotFound.vue';
import Knu from './components/Knu.vue';
import Baz from './components/Baz.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: Bar, name: 'Bar' },
  { path: '/login/:id', component: Foo, name: 'Foo', props: true }, //속성이름사용
  { path: '/my/:pw', component: Baz, name: 'Baz', props: true }, //속성이름 사용
  { path: '/knu', component: Knu, name: 'Knu', props: { username: '강감찬' } },
  { path: '*', component: NotFound, name: 'NotFound' },
];

const router = new VueRouter({ routes });
export default router;
```

Foo.vue:

```jsx
<template>
  <div class="hello">
    <h1>Foo</h1>
    $route.params.id: {{$route.params.id}}<br>
    id: {{id}}<br>
  </div>
</template>

<script>
export default {
 name: 'Foo',
 props: {
   id:String,
 }
}
</script>
```

Baz.vue:

```jsx
<template>
  <div>
      <h1>Bar</h1>
      {{pw}}
  </div>
</template>

<script>
export default {
    name:'Bar',
    props: {
        pw:String
    }
}
</script>
```

Knu.vue:

```jsx
<template>
    <div class="hello">
        <h1>Knu</h1>
        {{username}}
    </div>
</template>

<script>
export default {
    name: 'Foo',
    props:{
        username:String,
    }
}
</script>
```

main.js:

```jsx
import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

new Vue({
  router, // 라우터 등록
  render: (h) => h(App),
}).$mount('#app');
```

### 16 router3 - query 전송

app.vue:

```jsx
<template>
  <div id="app">
    <router-link to="/">Home</router-link><br>
      <router-link to="/login">login</router-link><br>
    <router-link :to="{ path: '/my', query: { foo:'baz'} }">/my?foo=baz</router-link><br>
    <router-view></router-view>
  </div>
</template>
```

router.js:

```jsx
import Vue from 'vue';
import VueRouter from 'vue-router';

import Bar from './components/Bar.vue';
import Foo from './components/Foo.vue';
import NotFound from './components/NotFound.vue';
import Baz from './components/Baz.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: Bar, name: 'Bar' },
  { path: '/login', component: Foo, name: 'Foo' },
  { path: '/my', component: Baz, name: 'Baz' },
  { path: '*', component: NotFound, name: 'NotFound' },
];

const router = new VueRouter({ routes });
export default router;
```

baz.vue:

```jsx
<template>
  <div>
      <h1>Baz</h1>
      {{$route.query.foo}}
  </div>
</template>

<script>
export default {
    name:'Baz',
}
</script>
```

### router4 - named route

app.vue:

```jsx
<template>
  <div id="app">
    <router-link :to="{name:'Bar'}">Bar</router-link><br>
    <router-link :to="{name:'Foo'}">Foo</router-link><br>
    <router-link :to="{name:'Baz', params: {id: 'kkkk'}}">Baz</router-link><br>
    <router-view></router-view>
  </div>
</template>
```

router.js:

```jsx
const routes = [
  { path: '/', component: Bar, name: 'Bar' },
  { path: '/login', component: Foo, name: 'Foo' },
  { path: '/my/:id', component: Baz, name: 'Baz', props: true }, //속성상
  { path: '*', component: NotFound, name: 'NotFound' },
];
```

Baz.vue:

```jsx
<template>
  <div>
      <h1>Baz</h1>
      {{$route.params.id}}<br>
      {{id}}
  </div>
</template>

<script>
export default {
    name:'Baz',
    props: {
        id:String,
    }
}
</script>
```

### router5 - children

app.vue: 위에썼던거 그대로

FooChild1.vue:

```jsx
<template>
  <div class='hello'>
    <h1>FooChild1</h1>
  </div>
</template>
```

FooChild2.vue:

```jsx
<template>
  <div>
      <h1>Foochild2</h1>
  </div>
</template>

<script>
export default {
    name: 'FooChild2'
}
</script>
```

Foo.vue:

```jsx
<template>
  <div class="hello">
    <h1>Foo</h1>
    <router-link to="/fooChild1">foo Child1</router-link><br>
    <router-link to="/fooChild2">foo Child2</router-link><br>
		<router-view></router-view>
  </div>
</template>

<script>
export default {
 name: 'Foo',
}
</script>
```

router.js:

```jsx
import Vue from 'vue';
import VueRouter from 'vue-router';

import Bar from './components/Bar.vue';
import Foo from './components/Foo.vue';
import NotFound from './components/NotFound.vue';
import FooChild1 from './components/FooChild1.vue';
import FooChild2 from './components/FooChild2.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: Bar, name: 'Bar' },
  {
    path: '/foo',
    component: Foo,
    name: 'Foo',
    children: [
      { path: '/fooChild1', component: FooChild1 },
      { path: '/fooChild2', component: FooChild2 },
    ],
  },
  { path: '*', component: NotFound, name: 'NotFound' },
];

const router = new VueRouter({ routes });
export default router;
```

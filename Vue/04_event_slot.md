## v-on

`v-on:이벤트명=“메서드()”`

`@이벤트명=“메서드명”`

```jsx
<template>
  <div>
    <h1>click</h1>
    <button v-on:click="handleEvent">v-on:click</button>
    <button @click="handleEvent">@click:handleEvent</button>
    <button v-on:click="handleEvent2" data-my='100'
      data-my2='{"a":200, "b":300}'>ok3</button>
    <button @click="xxx('홍길동')">@click="xxx('홍길동')"</button>
    <button v-on:click="xxx2('홍길동', $event)">click="xxx2('홍길동', $event)"</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:{
    msg:String,
  },
  data: () => ({num:0}),
  // 이벤트 처리 메소드 등록
  methods:{
    xxx: e => console.log("xxx====",e),
    xxx2: (data, event) => console.log("xxx2====", data, event),
    handleEvent: e => console.log("handleEvent", e),
    handleEven2: e => {
      console.log("handleEvent2", e.target.dataset.my); // 사용자 정의 데이터
      let x = JSON.parse(e.target.dataset.my2); // 문자열을 json객체로 변화
      // x={a:200, b:300}
      console.log(x.a, "\t", x.b);
    }
  }
}
</script>
```

💡 dataset에 관한 정보

[https://developer.mozilla.org/ko/docs/Learn/HTML/Howto/데이터*속성*사용하기](https://developer.mozilla.org/ko/docs/Learn/HTML/Howto/%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%86%8D%EC%84%B1_%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)

```jsx
어느 엘리멘트에나 data-로 시작하는 속성은 무엇이든 사용할 수 있습니다.
화면에 안 보이게 글이나 추가 정보를 엘리멘트에 담아 놓을 수 있어요.

dataset 객체를 통해 data 속성을 가져오기 위해서는 속성 이름의 data- 뒷 부분을 사용합니다.
(대시들은 camelCase로 변환되는 것에 주의하세요.)

보여야 하고 접근 가능해야하는 내용은 데이터 속성에 저장하지 마세요.
접근 보조 기술이 접근할 수 없기 때문입니다. 또한 검색 크롤러가 데이터 속성의 값을 찾지 못할 것입니다.

또한, JS 데이터 저장소에 저장하는 것과 비교해서 데이터 속성 읽기의 성능은 저조합니다.
```

### JSON.parse()란?

parse 메소드는 string 객체를 json 객체로 변환시켜줍니다.

### JSON.stringify란?

stringify 메소드는 json 객체를 String 객체로 변환시켜 줍니다.

### 12-event01-click-bind

```jsx
<template>
<div>
  <h1>click</h1>
  <!-- <button @click='handleEvent'>Ok-bind</button> -->
  <button @[aaa]="handleEvent">@[aaa]</button><br>
  <!-- <button @mouseover="handleEvent">@mouseover</button> -->
  <button v-on:[bbb]="handleEvent">@mouseover</button><br><!--bbb=mouseover-->
  <button @[ccc]="handleEvent">@mouseleave</button><br>
  <button v-on:[aaa]="handleEvent2" data-my="홍길동" data-my2='{"name":"홍길동","age":"20"}'>click</button>
  </div>
</template>
<script>
export default {
  name:'HelloWorld',
  props:{
    msg:String,
  },
  data:function(){
    return{
      aaa:'click',   //data속성을 이벤트이름으로 사용함
      bbb:'mouseover',
      ccc:'mouseleave'
    }
  },
  methods:{
    handleEvent:function(e){
      console.log("handleEvent==========",e);
    },
    handleEvent2:function(e){
      console.log(e, e.target.dataset.my);//사용자 정의 데이터 파싱
      var x= JSON.parse(e.target.dataset.my2); //
      console.log(x.name+'\t'+ x.age);
    }
  }

}
</script>
```

동적 바인딩으로 이벤트명을 [aaa] 데이터에서 받아옴.

### 실습7

```jsx
<template>
  <div class="hello">
    <h1>이벤트실습</h1>
    값1: <input type="text" v-model="num1"><br>
    값2: <input type="text" v-model="num2"><br>
    <button @click="sum">+계산하기</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {},
  data: () => ({num1:'', num2:'', total:''}),
  methods: {
    sum:function() {
      this.total = parseInt(this.num1) + parseInt(this.num2);
    }
  }
};
</script>
```

### 12-event-click2-exam8

```jsx
<script>
export default {
  name: 'HelloWorld',
  props: {},
  data: () => ({num1:'', num2:'', total:''}),
  methods: {
    sum:function(e) {
      let action = e.target.innerText;
      console.log("연산=======", action);
      if(action=="+"){
        this.total = parseInt(this.num1)+parseInt(this.num2);
      }else if(action=="-"){
        this.total = parseInt(this.num1)-parseInt(this.num2);
      }else if(action=="*"){
        this.total = parseInt(this.num1)/parseInt(this.num2);
      }else if(action=="/"){
        this.total = parseInt(this.num1)-parseInt(this.num2);
      }else{
        console.log("입력 데이터 오류");
      }
    }
  }
};
</script>
```

### 실습9

```jsx
<template>
  <div class="hello">
    <h1>이벤트실습</h1>
    가격: <input type="text" v-model="price"><br>
    갯수:
    <select @change="sum" v-model="quantity">
      <option value="">10</option>
      <option value="">20</option>
      <option value="">30</option>
    </select><br>
    <span>{{total}}</span>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {},
  data: () => ({price:'', quantity:'', total:''}),
  methods: {
    sum:function() {
      this.total = parseInt(this.price) * parseInt(this.quantity);
    }
  }
};
</script>
```

### 실습10

```jsx
<template>
  <div class="hello">
    <h1>교재정보</h1>
    <div v-for="(book, idx) in bookList" :key="idx">
      <input type="checkbox" :value="book.name" v-model="books">
      {{book.name}}
      <span>가격: {{book.price}}</span>
      <button v-on:click="del" data-idx="idx">삭제</button>
    </div>
    <hr>
    <button v-on:click="Alldel">전체삭제</button>
    <hr>
    {{books}}
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {},
  data: () => ({
    bookList:[
        {name:'자바의 정석', price:2000},
        {name:'jsp 정석', price:3000},
        {name:'Spring의 정석', price:4000},
        {name:'jQuery의 정석', price:1000},
        {name:'Angular의 정석', price:5000},
      ],
     books:[]
     }),
  methods: {
    del:function(e) {
      var delIdx = e.target.dataset.idx;
      console.log("delIdx =======", delIdx);
      this.bookList.splice(delIdx,1);
    },
    Alldel:function(){
      var xx = this.bookList;
      console.log(xx); // 전체 책
      console.log(this.books); // 선택된 책
      this.books.map((ele, idx) => { // books에서 책 한권 ele: 책목록
        xx.map((e, i) => {  // bookList 한권 책정보 {name...pricce}, i:idx
          if(ele==e.name){  // book의 책제목과 bookList(xx) 책제목이 동일하면
            console.log(i, idx);
            xx.splice(i,1); // i 사용주의 bookList(xx)에서 삭제
          }
        })
      })
    }
  }
};
</script>
```

`splice()` 메서드는 배열의 기존 요소를 삭제 또는 교체하거나 새 요소를 추가하여 배열의 내용을 변경합니다.

삭제버튼은 반복문 안에서 자기한테도 인덱스가 할당되어있다. 그래서 자기 인덱스로 배열에서 그대로 삭제해줌

선택삭제버튼은 선택한 책이름이 books 배열데이터에 들어가면 그것들을 반복문하고 그안에서 북리스트도 반복문 돌려서 배열 책 이름이랑 북리스트 이름이랑 일치하는 경우 리스트에서 삭제해줌.

## 이벤트 수식어

- .once 수식어는 한 번만 이벤트가 발생.
- .prevent 수식어는 preventDefault() 효과
- .stop 수식어는 stopPropagation() 효과
- .enter 수식어는 키보드 enter 친 효과
- .delete 수식어는 키보드 delete 친 효과
- .space 수식어는 키보드 space bar 친 효과
- .ctrl .up .down .alt 등

```jsx
v-on:click.once="x"
v-on:keyup.enter="xyz"
```

## emit

- 자식에서 부모로 데이터 전송은 이벤트 이용.
- 자식에서는 이벤트를 발신(emit) 하고 부모에서는 v-on 이용하여 이벤트를 수신한다.
- `this.$emit(“xyz”)`-> `v-on:xzy=“receive”`
- `this.$emit(“xyz2”,100,200)`=> `v-on:xyz2`

```jsx
<template>
  <div id="app">
    <HelloWorld
      v-on:xyz="y"
      v-on:xyz2="y2"
    /><!--이벤트로 받아서 처리할 함수지정-->
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";

export default {
  name: "App",
  components: {
    HelloWorld,
  },
  methods: {
    y: function() {
      console.log("부모의 y호출================");
    },
    y2: function(v, v2) {
      //자식에서 넘어오는 데이터를 매개변수로 받기
      console.log("부모의 y2호출==========", v, "\t", v2);
    },
  },
};
</script>
```

```jsx
<template>
  <div>
    <h1>자식에서 부모로이벤트 발생</h1>
    <button v-on:click="x">부모에게 요청</button>
    <button v-on:click="x2">부모에게 요청</button>
  </div>
</template>
<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  methods: {
    x: function() {
      console.log("자식 x의 this====", this);
      this.$emit("xyz"); //자식에서 부모로 전달될 이벤트 명칭(이벤트명)
    },
    x2: function() {
      console.log("자식 x2의 this====", this);
      this.$emit("xyz2", 100, "홍길동"); //자식에서 부모로 전달될 이벤트 명칭 xyz2 데이터두개 넘김
    },
  },
};
</script>
```

자식에서 부모이벤트핸들러로 데이터를 넘길수있다.

### 실습11

```jsx
<template>
  <div id="app">
    <h1>도서목록{{ list.length }}권</h1>
    선택된 도서목록<input type="text" v-bind:value="bookName" />
    <BookList v-bind:bookList="list" v-on:xyz="y" />
  </div>
</template>

<script>
import BookList from "./components/BookList.vue";

export default {
  name: "App",
  components: {
    BookList,
  },
  data: function() {
    return {
      list: [
        {
          id: "p01",
          name: "위험한 식탁",
          price: 2000,
          date: "20170401",
          img: "a",
        },
        {
          id: "p02",
          name: "공부의 비결",
          price: 3000,
          date: "20170402",
          img: "b",
        },
        {
          id: "p03",
          name: "오메르타",
          price: 2500,
          date: "20170401",
          img: "c",
        },
      ],
      bookName: "",//선택된 책의 제목 저장
    };
  },
  methods: {
    y: function(xxx) {
      this.bookName = xxx;//매개변수로 넘어온 책이름 저장
    },
  },
};
</script>
```

bookList 컴포넌트는 자식에서 템플릿에 만들어진 내용을 그대로 화면에 꽂아주게된다. 이벤트는 자식에서 받아온다.

```jsx
<template>
  <div>
    <ul>
      <li v-for="(book, idx) in bookList" v-bind:key="idx">
        <a v-on:click="x">
          <!---->
          <img
            v-bind:src="require(`../assets/image/${book.img}.jpg`)"
            width="100"
            heigth="100"
            v-bind:data-xxx="book.name"
          />
          {{ book.name }}
        </a>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  name: "BookList",
  props: {
    bookList: Array, //수정
  },
  methods: {
    x: function(e) {
      console.log(e.target.dataset.xxx);
      this.$emit("xyz", e.target.dataset.xxx); //책이름 전달
    },
  },
};
</script>
<style scoped></style>
```

자식에선 a태그 클릭시 x 이벤트핸들러가 호출되면 이미지에 있던 메타데이터 책이름이 에밋으로 xyz에 저장되어 부모로 전송된다. 부모는 xyz를 사용하는 이벤트 핸들러에서 책이름 변수를 이 책이름으로 지정해준다. 따라서 선택된 도서목록 Input에 클릭된 책이름이 출력된다.

## 이벤트 버스

- 부모/자식 관계가 아닌 형제 관계인 컴포넌트간의 데이터 전달 방법.
- 던지는 애 `$emit` 받는애 `&on`

```jsx
이벤트버스는 컴포넌트가 많지 않아 규모가 작은 중소 프로젝트에 사용해야 합니다.
컴포넌트가 많아지고 복잡해 지면 누가 누구에게 통신을 하고 있는지 헷갈리기 떄문에 디버깅이 너무 힘들어 지게 됩니다.
그래서 대규모 Vue 프로젝트인 경우는 Vuex라이브러리를 사용하여 통신을 하게 됩니다.

쉽게 말해 이벤트버스는 비어있는 Vue 인스턴스 객체라고 보시면 됩니다.

출처: https://uxgjs.tistory.com/133 [UX 공작소]
```

EventBus.vue:

```jsx
<script>
  //script태그만 필요 import Vue from "vue"; var eventBus = new Vue();
  //이벤트버스생성 export default eventBus;
</script>
```

```jsx
<template>
  <div class="hello">
    <h1>이벤트버스 실습</h1>
    <button v-on:click="x">HelloWorld2로 전달(이벤트로 전달)</button>
  </div>
</template>

<script>
import eventBus from "./EventBus.vue"; //import
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  methods: {
    x: function() {
      console.log("x()==============");
      eventBus.$emit("xyz"); //이벤트버스 전달이벤트 명 xyz
    },
  },
};
</script>
```

```jsx
<template>
  <div>
    HelloWorld2
    <input type="text" v-bind:value="receive" />
  </div>
</template>
<script>
import eventBus from "./EventBus";
export default {
  name: "HelloWorld2",
  data: function() {
    return {
      receive: "호출전",
    };
  },
  //eventBus.$on을 이용하여 처리할 이벤트 함수 등록
  created() {
    console.log("create호출");
    eventBus.$on("xyz", this.handleEvent); //이벤트함수 등록
  },
  methods: {
    handleEvent: function() {
      console.log("handleEvent호출됨========");
      this.receive = "호출 완료=======";
    },
  },
};
</script>
```

버튼클릭 상호작용은 헬로1에서 일어나고 그 이벤트에 대한 핸들링은 헬로2의 메소드가 담당하고 이벤트 처리 결과로 인풋에 있는 메세지가 바뀐다.

### src13 이벤트버스2 - 파라미터

```jsx
<script>
  //script태그만 필요 import Vue from "vue"; var eventBus = new Vue();
  //이벤트버스생성 export default eventBus;
</script>
```

```jsx
<template>
  <div class="hello">
    <h1>이벤트버스 실습</h1>
    <button v-on:click="x">HelloWorld2로 전달(이벤트로 전달)</button>
  </div>
</template>

<script>
import eventBus from "./EventBus.vue"; //import
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  methods: {
    x: function() {
      console.log("x()==============");
      eventBus.$emit("xyz", 100, "홍길동"); //이벤트버스 전달이벤트 명 xyz
    },
  },
};
</script>
```

```jsx
<template>
  <div>
    HelloWorld2
    <input type="text" v-bind:value="receive" />
  </div>
</template>
<script>
import eventBus from "./EventBus";
export default {
  name: "HelloWorld2",
  data: function() {
    return {
      receive: "호출전",
    };
  },
  //eventBus.$on을 이용하여 처리할 이벤트 함수 등록
  created() {
    console.log("create호출");
    eventBus.$on("xyz", this.handleEvent); //이벤트함수 등록
  },
  methods: {
    handleEvent: function(x, y) {//넘어오는 데이터를 매개변수로 받기
      console.log("handleEvent호출됨========");
      this.receive = "수신 완료=======" + x + ":" + y;
    },
  },
};
</script>
```

이번엔 헬로1이 파라미터를 보내서 헬로2가 받아서 출력해주고있음

### src-13_eventBus3_exam12

![%E1%84%87%E1%85%B2%20%E1%84%8B%E1%85%B5%E1%84%87%E1%85%A6%E1%86%AB%E1%84%90%E1%85%B3,%20%E1%84%8B%E1%85%B5%E1%84%87%E1%85%A6%E1%86%AB%E1%84%90%E1%85%B3%E1%84%87%E1%85%A5%E1%84%89%E1%85%B3,%20%E1%84%89%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%86%BA%206f6e25fc8f2143cca1d2a7577f70a4c8/Untitled.png](%E1%84%87%E1%85%B2%20%E1%84%8B%E1%85%B5%E1%84%87%E1%85%A6%E1%86%AB%E1%84%90%E1%85%B3,%20%E1%84%8B%E1%85%B5%E1%84%87%E1%85%A6%E1%86%AB%E1%84%90%E1%85%B3%E1%84%87%E1%85%A5%E1%84%89%E1%85%B3,%20%E1%84%89%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%86%BA%206f6e25fc8f2143cca1d2a7577f70a4c8/Untitled.png)

eventBus.vue:

```jsx
import Vue from 'vue';
var eventBus = new Vue();
export default eventBus;
```

Input.vue:

```jsx
<template>
  <div>
      <input type="text" v-on:keyup.enter="add" v-model="mesg">
  </div>
</template>

<script>
import eventBus from './EventBus';
export default {
    name: "HelloWorld",
    props: {
        mesg: String,
    },
    data: () => ({mesg:"",}), // 이름 저장 변수, 버스로 전달
    methods: {
        add: function() {
            eventBus.$emit("xyz", this.mesg); //이벤트버스 전달이벤트명
            this.mesg = ""; // 초기화
        }
    }
}
</script>
```

인풋에 뭘 치면 바로 mesg가 업뎃되고 엔터 땅 치면 add 함수 작동. 이벤트버스에 xyz라는 이름으로 mesg 값을 전달하고 다시 빈칸으로 초기화한다.

List.vue:

```jsx
<template>
  <div>
      <ul v-for="(a,idx) in todoList" :key="idx">
          <li>{{a}} <button v-on:click="del(idx)">삭제</button></li>
      </ul>
  </div>
</template>

<script>
import eventBus from './EventBus';
export default {
    name: "HelloWorld2",
    data: () => ({todoList: []}),
    // eventBus.$on을 이용하여 처리할 이벤트 함수 등록
    created() {
        console.log("create호출");
        eventBus.$on("xyz", this.add); //이벤트함수등록
    },
    methods: {
        add: function(m) {
            this.todoList.push(m);
        },
        del: function(idx) {
            this.todoList.splice(idx, 1);
        }
    }
}
</script>
```

생성되자마자 xyz 받아와서 add함수 실행. 투두 배열에 바로 받아온 메세지 푸시. 그거 반복문 돌려서 화면 출력. 삭제버튼 클릭하면 인덱스로 자기꺼 배열에서 삭제.

# Slot

- 부모에서 자식으로 전달할 데이터가 문자열 정보인 경우에는 props 속성 이용.
- 부모에서 자식으로 전달할 데이터가 HTML 태그인 경우에는 <slot> 태그 이용.

app.vue:

```jsx
<template>
  <div id="app">
    <HelloWorld mesg="안녕하세요">
      <!-- 슬롯영역 -->
      <div>아름다운 밤입니다.</div>
      <!-- 슬롯영역 -->
    </HelloWorld>
  </div>
</template>
```

HelloWorld.vue:

```jsx
<template>
  <div class='hello'>
    <h1>{{ mesg }}</h1>
    <slot></slot>
  </div>
</template>
```

### slot name

- named slot 을 사용하면 컴포넌트에 여러 개의 slot 적용이 가능

```jsx
<HelloWorld mesg="안녕하세요">
      <!-- 슬롯영역 -->
      <div slot="a">아름다운 밤입니다.</div>
      <div slot="b">아름다운 밤입니다.</div>
      <!-- 슬롯영역 -->
    </HelloWorld>
```

```jsx
<div class='hello'>
  <h1>{{ mesg }}</h1>
  <slot name='a'></slot>
  <slot name='b'></slot>
</div>
```

### src_14_slot2_SpeechBox

```jsx
<template>
  <div id="app">
    <HelloWorld
      mesg="안녕하세요"
      class="sanders"
      :headerText="A.header"
      :footerText="A.footer" />
    <!-- slot 영역 -->
    <div>
      <p>{{A.message}}</p>
    </div>
    <!-- slot 영역 -->
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data: function() {
    return {
      A: {
        header: "오바마",
        message: "저의 동료...",
        footer: "2017/01/01",
      },
      B: {
        header: "샌더슨",
        message: "감사합니다",
        footer: "2016/07/25",
      },
    };
  },
}
</script>

<style>
.sanders {
  background-color: antiquewhite;
}
.sanders-content {
  font-family: 굴림;
  text-decoration: underline;
}
</style>
```

```jsx
<template>
  <div class="hello">
    <div class="header">{{headerText}}</div>
    <div class="content">
      <slot></slot>
    </div>
    <div class="footer">{{footerText}}</div>
  </div>

</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    headerText: String,
    footerText: String,
  }
}
</script>
```

### src_14-slot3_speechBox_named

```jsx
<template>
  <div id="app">
    <HelloWorld class="sanders">
      <div slot="headerText">{{A.header}}</div>
      <div slot="speechBox">
        <p>{{A.message}}</p>
      </div>
      <div slot="footerText">{{A.header}}</div>
    </HelloWorld>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data: function() {
    return {
      A: {
        header: "오바마",
        message: "저의 동료...",
        footer: "2017/01/01",
      },
      B: {
        header: "샌더슨",
        message: "감사합니다",
        footer: "2016/07/25",
      },
    };
  },
}
</script>

<style>
.sanders {
  background-color: antiquewhite;
}
.sanders-content {
  font-family: 굴림;
  text-decoration: underline;
}
</style>
```

```jsx
<template>
  <div class='hello'>
    <slot name='headerText' />
    <slot name='speechBox' />
    <slot name='footerText' />
  </div>
</template>
```

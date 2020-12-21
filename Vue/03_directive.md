### 09_directive_03_v_model2_select

![img/Untitled7.png](img/Untitled7.png)

```jsx
<template>
  <div class="hello">
    <select v-model="mesg">
      <option>10</option>
            <option>20</option>
            <option>30</option>
            <option>40</option>
    </select><br>
    <input type="text" v-model="mesg"><br>
    {{mesg}}
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data:function(){
    return{
      mesg:20
    }
  }
}
</script>
```

### 09_directive3_v-model3_heckbox

![img/Untitled8.png](img/Untitled8.png)

```jsx
<template>
  <div>
    <div>좋아하는 과일을 선택하세요</div>
    <input type="checkbox" v-model="fruit" value="사과">사과<br>
    <input type="checkbox" v-model="fruit" value="배">배<br>
    <input type="checkbox" v-model="fruit" value="바나나">바나나<br>
    <input type="checkbox" v-model="fruit" value="수박">수박<br>
    선택한 과일은 :<br>
    {{fruit}}
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:{
    mesg:String,
  },
  data: () => ({fruit:[]})
}
</script>
```

## v-show, v-if

- v-if는 조건에 일치하지 않으면 렌더링 안됨. 조건에 따라 컴포넌트가 실제로 제거되고 생성된다.
- v-show는 랜더링은 되지만 화면에 안보임. css 의 display 속성만 변경

### v-show

![img/Untitled9.png](img/Untitled9.png)

```jsx
<template>
  <div>
    <div>
      <!-- v-show는 앵귤러의 ngIf와 비슷함. display:none 속성으로 작동 -->
      <p v-show=true>true</p>
      <p v-show="true">true</p>
      <p v-show="flag">"flag"</p>
      <p v-show="! false">"! false"</p>
      <p v-show="false">"false"</p>
      <p v-show=false>false</p>
      <p v-show="! true">"! true"</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:{
    mesg:String,
  },
  data: () => ({flag:true})
}
</script>
```

### v-if

![img/Untitled10.png](img/Untitled10.png)

```jsx
<template>
  <div>
    <div>
      <!-- v-if는 조건에 일치하지 않으면 렌더링 안됨
           v-show는 렌더링은 되지만 화면에 안보임 -->
      <p v-if="amount==1">v-if hello1</p>
      <p v-show="amount==1">v-show hello2</p>
      <p v-if="amount!=1">v-if hello3</p>
      <p v-show="amount!=1">v-show hello4</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:{
    mesg:String,
  },
  data: () => ({amount:1})
}
</script>
```

### 9-4_3

![img/Untitled11.png](img/Untitled11.png)

```jsx
<template>
  <div>
    <p v-if="3>1">Hello1</p>
    <p v-show="num>=num2">Hello2</p>
    <p v-if="num<num2">Hello3</p>
    <p v-show="num>num2 && 3==3">Hello4</p>
    <p v-show="num<num2 || 3==3">Hello5</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:{
    mesg:String,
  },
  data: () => ({num:1, num2:5})
}
</script>
```

### 9-5 실습4

![img/Untitled5.png](img/Untitled5.png)

```jsx
<template>
  <div>
    <h1>{{msg}}</h1>
    값입력: <input type="text" v-model="amount">
    <span v-if="amount < 100">100보다 큰 값만 입력가능</span>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:{
    msg:String,
  },
  data: () => ({amount:100})
}
</script>
```

### 9-5 실습5

![img/Untitled6.png](img/Untitled6.png)

```jsx
<template>
  <div>
    이름<input type="text" v-model="username"><br>
    <span v-if="username.length<2">이름은 2글자 이상이어야 합니다.</span><br>
    나이<input type="text" v-model="age"><br>
    <span v-if="age<10||age>120">나이는 10세 이상 120세 이하여야 합니다.</span><br>
    이름길이는: {{username.length}} / 나이: {{age}}
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:{
    msg:String,
  },
  data: () => ({username:'홍길동', age:10})
}
</script>
```

9-6 v-else-if

![img/Untitled12.png](img/Untitled12.png)

```jsx
<template>
  <div>
    <!-- v-if, v-else-if, v-else의 사용 -->
    점수: <input type="text" v-model.number="grade">
    <p v-if="grade>90">A학점</p>
    <p v-else-if="grade>80">B학점</p>
    <p v-else-if="grade>70">C학점</p>
    <p v-else>F학점</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:{
    msg:String,
  },
  data: () => ({grade:50})
}
</script>
```

## 9-7 v-for array

`v-for=“항목 in 배열|객체”`

![img/Untitled2.png](img/Untitled2.png)

```jsx
<template>
  <div>
    <!-- v-for 객체의 사용 -->
    <h1>index없이 사용</h1>
    <ul>
      <li v-for="(value, key) in person" :key="key">
        {{key}}:{{value}}
      </li>
    </ul>
    <h1>index 지정 사용</h1>
    <ul>
      <li v-for="(value, key, index) in person" :key="index">
        {{index+1}}:{{key}}:{{value}}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:{
    msg:String,
  },
  data: () => ({
    person:{
      username:'홍길동',
      age:20,
      address:'서울'
    }
  })
}
</script>
```

### 9-8_v-for_object

![img/Untitled3.png](img/Untitled3.png)

```jsx
<template>
  <div>
    <!-- v-for 객체의 사용 -->
    과일선택:
    <select v-model="result">
      <option disabled selected>과일을 선택하세요</option>
      <option v-for="(value, key, index) in fruits" :key="index"
      :value="value">{{key}}</option>
    </select><br>
    선택한 과일은: {{result}}
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props:{
    msg:String,
  },
  data: () => ({
      fruits:{
        apple:'사과',
        banana:'바나나',
        melon:'멜론'
      },
      result:''
  })
}
</script>
```

# 클래스

### static method

- static 메소드는 클래스명.메소드 형식으로 참조
- 일반 메소드는 객체생성 후 인스턴스 변수로 참조.

```java
class Employee {
	getEmployee(){
   return "hello";
 }
	static getXXX() {
   return "world";
 }
}
console.log(Employee.getXXX());  // static 메소드 참조
let emp = new Employee();
console.log(Employee.getXXX(), emp.getEmployee());
```

### generator 함수

- 객체생성후에접근가능.
- 호출했을 때 바로 실행되는게 아니라 제너레이터 객체를 받아와서 .next()를 사용해서 함수를 실행한다. 일드를 만나면 멈추고

```java
class Employee {
   *info(){
     yield "hello";
   }
}
let emp = new Employee();
let gen = emp.info()
console.log(gen.next());
```

```java
class Employee {
        constructor(name, sal)
        {
          this.name=name;
          this.salary=sal;
        }
        setName(name){
          this.name=name;
        }
        getName(sal){
          this.salary=sal;
        }
        getName(){
          return this.name;
        }
        getSalary(){
          return this.salary;
        }
        getEmployee(){
          return this.name+"\t"+this.salary;
        }
      }

      //Manager는 Employee를 상속, 생성자를 통해 depart, name, salary 초기화
      // getEmployee() 오버라이딩 depart, name, salary 정보 리턴
      class Manager extends Employee{
        constructor(depart, name, sal)
        {
          super(name,sal);
          this.depart=depart;
        }
        setDepart(depart){
          this.depart=depart;
        }
        getDepart(){
          return this.depart;
        }
        getEmployee(){
          return this.name+"\t"+this.salary+"\t"+this.depart;
        }
      }
      let man = new Manager("홍길동", 3000, "개발");
      console.log(man.getEmployee());
```

금요일에 만들었던 코드 참고해서 상속 클래스 다시 만들어보기

```java
class Manager extends Employee{
        static getInfo(){
          console.log(this);
          return "홍길동";
        }
        constructor(depart, name, sal)
        {
          super(name,sal); // 필수
          console.log("==========");
          console.log(this); //생성된 인스턴스
          this.depart=depart;
        }
        setDepart(depart){
          this.depart=depart;
        }
        getDepart(){
          return this.depart;
        }
        getEmployee(){
          return this.name+"\t"+this.salary+"\t"+this.depart;
        }
      }
      console.log(Manager.getInfo());
      let man = new Manager("홍길동", 3000, "개발");
      console.log(man.getEmployee());
```

static 함수 사용

# Map객체

- 기존 객체와의 차이점은 맵 객체는 순서보장
- key 데이터로 모든 값(기본형,참조형) 사용 가능.
- 키값 중복되면 덮어쓰기

```java
//1.객체생성
var map = new Map();
//2.정보보기
console.log(map);
//3.데이터 저장.set()
map.set("one", 100);
map.set(1, 200);
map.set(false, 300);

//4.데이터출력 .get()
console.log(map.get("one"));
console.log(map.get(1));
console.log(map.get(false));

//4.데이터출력 .entries()
var data = map.entries();
console.log(data.next());
console.log(data.next());
console.log(data.next());

//5.has 메소드
console.log(map.has("two"));//키값의 존재여부 검사
```

entries() 메서드: [key,value]형식으로반환하는iterator객체반환.

next() 메서드로 entry를 가져 온다.

```java
//5.데이터출력 .keys() 키를 반환하는 {value:키값, done: 불린값}
var data = map.keys();
console.log(data.next());
console.log(data.next());
console.log(data.next());

//6.데이터출력 .values() 메소드: 추가한 순서로 value를 가져옴
console.log("=======");
var data = map.values();
console.log(data.next().value);
console.log(data.next());
console.log(data.next());
```

keys(): 키값만 꺼내온다. iterator 객체 반환

next() 메서드로 {value: 키값, done: 불린값}를 가져 온다.

### forEach() 메서드

`map.forEach(function(value,key,map){ });`

```java
var map = new Map();
map.set("one", 100);
map.set(1, 200);
map.set(false, 200);
map.forEach(function(v,k,m){
  console.log(v,k,m);
})
```

### delete(key) 메서드

```java
var map = new Map();
map.set("one", 100);
map.set(1, 200);
map.set(false, 200);
var result = map.delete("one"); //true
console.log(result);
console.log(map.delete("two")); //false

//map.clear() 모든 entry 삭제
map.clear();
console.log(map);
```

key 값이 일치하는 entry 삭제.

삭제하면 true 리턴하고 못하면 false 리턴

# Set 객체

```java
// set: 순서 있음, 중복 불가, 내부적으로 배열로 관리
var s = new Set();
s.add("one");
s.add("one");
s.add(100);
s.add(false);
console.log(s.size); //3
console.log(s);

var data = s.values();
console.log(data.next().value);
console.log(data.next().value);
console.log(data.next().value);
```

# Promise 객체

`new Promise(function (resolve, reject) { ... } );`

내부적으로 비동기처리해줌. 이에 맞춰서 처리 코드 작성

- 성공 → resolve() 호출 -> then 메소드의 첫번째 함수 수행
- 실패 → reject() 호출 -> then 메소드의 두번째 함수 수행
- 코드가 끝까지 수행하고 나서 resolve, reject가 호출된다. 비동기적으로 수행됨

```java
//Promise 객체: 특정 작업을 비동기처리 해주는 객체
// 코드가 끝까지 수행 후 resolve() : then의 첫번째 함수 수행
// 코드가 끝까지 수행 후 reject() : then의 두번째 함수 수행
function xxx() {
    return new Promise((resolve, rejection) => {
        console.log("1");
        resolve(); // 1, 2, end, success 비동기처리
        console.log("2"); //1,2,end,fail 비동기처리
    })
};
xxx().then(() => {
    console.log("success");
}, () => {
    console.log("fail");
});
console.log("end"); //end까지 수행 후 then의 함수 선별적 호출
```

### Promise 상태 2가지

- 비동기로 처리가 되기 때문에 특정 상태를 저장해야 된다.
- [[PromiseStatus]] 속성에 저장됨.
- Pending 상태(대기상태)
- resolve 상태 또는 reject 상태 ( settled 상태 )

### 파라미터사용

- resolve(값) 또는 resovle(값) 사용 가능. 단 하나의 파라미터 값만 사용 가능
- 따라서 여러 개의 값을 전달하기 위해서는 배열 이용.
- [[PromiseValue]]에 저장됨

```java
function xxx(param){
    return new Promise((resolve, reject) => {
        console.log("1");
        if(param == "ok"){
            resolve();
        }else{
            reject();
        }
        console.log("2");
    })
}
var result = xxx("ok");
console.log(result);  // //1,2, Promise, end , success 또는 fail 선택
result.then(() => {
    console.log("success");
}, () => {
    console.log("fail");
})
console.log("end");
```

```tsx
function xxx(param) {
  return new Promise((resolve, reject) => {
    console.log('1');
    if (param == 'ok') {
      resolve([100, 200]);
    } else {
      reject({ key: '홍길동', key2: 20 });
    }
    console.log('2');
  });
}
//var result= xxx("ok2");
var result = xxx('ok');
console.log(result);
result.then(
  (x) => {
    console.log('success' + x[0] + '\t' + x[1]);
  },
  (x) => {
    console.log('fail' + x.key + '\t' + x.key2);
  }
);
console.log(result);
console.log('end');
```

### then()메서드의체인

```java
function xxx(param){
  return new Promise((resolve, reject) => {
      console.log("1");
      resolve();
      console.log("2");
  })
}
xxx().then(() => {
  console.log("success1");
  return "홍길동";
}).then((p => {
  console.log("success2" + p);
  return "안녕하세요" + p;
}).then((p => {
  console.log("success3" + p);
})
console.log("end");
```

### catch를이용한reject()처리

then() 메서드의 두 번째 함수에서 처리했던 실패 코드를 catch() 에서 사용.

```tsx
//catch를 이용한 reject처리
function xxx() {
  return new Promise(function (resolve, reject) {
    console.log('1');
    reject();
    console.log('2');
  });
}
xxx()
  .then(function () {
    console.log('success');
  })
  .catch(function () {
    console.log('fail');
  });
console.log('end');
```

# Module

import 사용해서 가져오고 export로 외부에서 사용가능하도록 내보내기 가능.

```tsx
// b.js
//export는 import {aaa} from...
export function bbb() {
  console.log('bbb 호출');
} //end function
export class Employee {
  constructor(name, sal) {
    this.name = name;
    this.sal = sal;
  }
  setName(name) {
    this.name = name;
  }
  getName() {
    return this.name;
  }
  setSalary(sal) {
    this.sal = sal;
  }
  getSalary() {
    return this.sal;
  }
  getEmployee() {
    return this.name + '\t' + this.sal;
  }
} //end Employee
```

```tsx
// c.js
//export default는 import 이름변경 from ....
export default function ccc() {
  console.log('ccc호출');
}
```

```tsx
// a.js

import { Employee, bbb } from './b.js';
/* import {default as xxx} from './c.js'; //이름변경
 import defaultExport  from './c.js';*/
import ccc from './c.js';

ccc(); // ccc호출
var e = new Employee('홍길동', 200);
console.log(e.getEmployee()); // 홍길동	200
bbb(); // bbb 호출
// xxx();
// defaultExport();
```

```java
<script type="module" src="a.js"></script>
```

html에서 js파일 임포트할 땐 스크립트 태그에 type은 module로 지정

import from에서 그냥 b를 적으면 node modules에서 찾게됨

./b 하면 지금 폴더에서 찾아줌

from 'react'같은 경우 노드모듈스에서 찾는거

여러개 함수 있고 `export default 함수1;` 하면 함수1만 import해서 이름바꿔서 사용가능

`export {함수1, 함수2, 함수3};` 할 경우 `import {함수3} from ~` 이렇게 뽑아서 사용가능

합쳐서 `import 함수1 {함수2, 함수3} from ~` 할 수 있다

export default할 필요없지만 이거는 파일에서 중요한부분이 뭔지 알려줄수있다

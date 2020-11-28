# strict 모드 (엄격 모드)란?

일반적인 javascript는 var 키워드를 안써도 실행이 된다.

```java
<script>
	mesg = "hello";
	console.log(mesg);
</script>
```

엄격모드는 var를 꼭 써라 하고 제약조건을 주는거다.

```java
<script>
        "use strict"
        var mesg = "hello";
        console.log(mesg);
    </script>
```

# var 변수

일반적으로 javascript는 블록 스코프가 아닌 함수 스코프(function scope)를 따른다.

```java
//"use strict"
console.log(n);  // undifined
var n = 100;
var n = 200; // 같은 스코프에서 재선언 가능. 덮어쓴다.
console.log(n);  // 200
if(true){
    var m = 30;
}
console.log(m); // 30
```

변수 선언부만 호이스팅되기 때문에 n이 정의되지 않아도 에러안뜨고 undefined 출력해줌

if 블럭 밖에서도 변수 m을 출력할 수 있다.

[[javascript] 호이스팅 (hoisting) 이란?](https://ojava.tistory.com/144)

# let 변수

- let 키워드를 사용하면 함수 스코프가 아닌 블록 스코프를 따른다.따라서 블록밖에 동일한 이름의 변수가 있어도 scope가 다르기 때문에 변수에 각각 값을 설정할 수 있다.
- let은 호이스팅 불가능

```java
// console.log(n);  // Cannot access 'n' before initialization
let n = 100;
console.log(n);
if(true){
    let m = 30; // if 블록스코프에서만 사용가능
}
// console.log(m); // m is not defined
```

호이스팅 안되고 블록스코프 안에서만 사용할 수 있어요

```jsx
let n = 100;
n = 200;
console.log(n); // 200
if (true) {
  let m = 30;
}
let m = 50;
console.log(m); // 50
```

값 재할당 가능

```jsx
var mesg = 'bb'; //전역객체에 추가
console.log(this.mesg, window.mesg); // bb bb

let mesg2 = 'aa'; //let 변수는 전역객체에 추가되지않음. this로 접근불가
console.log(this.mesg2, window.mesg2); // undefined undefiend

if (true) {
  console.log(mesg2); // aa
  console.log(this.mesg2); // undefined
}
```

- var 변수는 전역 객체(window)에 추가된다.
- let 변수는 전역 객체(window)에 추가되지 않는다.

```jsx
for (let i = 0; i < 10; i++) {
  console.log(i);
  let mesg = 'hello';
}
```

# const 변수

- 상수 작성시 사용.
- 선언만 할 수 없고 선언과 동시에 초기화를 해줘야한다. 초기화후엔 값을 변경할 수 없다.

```jsx
const n = 100;
// const n;
// n=100;
console.log(n);
```

```jsx
const mesg = 'hello';
try {
  mesg = 'world';
} catch (e) {
  console.log('상수값 변경 불가');
}
```

# 함수 function

```jsx
// 함수 선언식

aaa(); // undefined undefined
function aaa(n, n2) {
  console.log(n, n2);
}
aaa(10); // 10 undefined
aaa(1, 2, 3, 4); // 1 2
```

자릿수 덜 채울 경우 undefined, 넘칠경우 인자 받는곳만 출력하고 나머지는 안받음.

```jsx
function aaa(n=100, n2=200){
```

파라미터에 기본값 지정가능

## rest 파라미터

- 자바의 가변인자와 동일한 기능. ...(spread)연산자 사용
- 내부적으로 배열(Array)로 처리한다. 따라서 Array객체에서 제공하는 메서드를 사용할 수 있다.

```jsx
var bb = [1, 2, 3, [10, 9, 8]];
var aa = [1, 2, 3, ...[10, 9, 8]];
console.log(aa);
for (let i = 0; i < aa.length; i++) {
  console.log(aa[i]);
}
```

bb는 배열방 크기가 4임. aa는 인덱스 3번 배열을 펼쳐서 원래 배열에 합쳐준다. 그래서 배열방 크기는 6이다.

```jsx
function aaa(...n) {
  console.log('aaa()==== ', n);
}
aaa(1);
aaa(10, 20, 30);
aaa(1, 2, 3, 4, 5);
```

인자에서 받은걸 배열로 묶어주는 역할을 한다.

```jsx
function bbb(x, ...n) {
  console.log(x, n);
}
bbb(1);
bbb(10, 20, 30);
bbb(1, 2, 3, 4, 5);
```

이렇게 파라미터를 받게되면 앞에 하나빼고 나머지 인자들은 배열로 받게된다.

```jsx
function ccc(x, y, ...n) {
  console.log(x, y, n);
}
ccc(1);
ccc(10, 20, 30);
ccc(1, 2, 3, 4, 5);
```

```jsx
function aaa(...n) {
  for (let i in n) {
    console.log(n[i]);
  }
}
aaa(1);
aaa(10, 20, 30);
aaa(1, 2, 3, 4, 5);
```

```tsx
var obj1 = { foo: 'bar', x: 42 };
var obj2 = { name: 'baz', y: 13 };
var clonedObj = { ...obj1 };
var mergedObj = { ...obj1, ...obj2 };
console.log(clonedObj);
console.log(mergedObj);
```

```jsx
// 응용1 - 배열복사
var x = [1, 2, 3];
var x2 = [...x];
console.log(x, x2);
```

```jsx
// 응용2 - 배열연결
var k = [1, 2, 3];
var k2 = [4, 5, 6];
var k3 = [...k, ...k2];
console.log(k3);
```

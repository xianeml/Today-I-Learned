# 람다함수( arrow 함수 )

```tsx
//주의
let a = () => {};
console.log(a()); //undefined {} 실행블럭으로 인식
a = () => ({ key: '홍길동' }); //({})사용 json객체로 인식시킴
console.log(a()); //object출력
```

```tsx
// this
this.n = 20;
var a = {
  n: 10,
  b: function () {
    console.log(this.n);
  },
};
a.b();

var a2 = {
  n: 10,
  b: () => {
    console.log(this.n);
  },
};
a2.b();
```

화살표함수는 this를 바인딩하지 않는다. 따라서 객체의 메소드를 만들 땐 사용하지 않도록.

# generator 함수

`function* 함수명(){}`

- generator 함수를 호출하면 generator 객체를 생성하여 반환한다.
- 일반적으로 함수를 호출하면 {코드블록}이 실행되지만, generator 함수는 {}을 실행하지 않고 generator 객체를 생성하여 반환한다.
- generator 함수내의 코드를 실행하기 위하여 generator 객체의 next() 메서드를 호출해야 된다.

```java
// generator 함수
    function* aaa(){
        console.log('1');
        yield console.log('2');
        console.log('3');
    }
    var g = aaa();
    console.log(g)
    g.next();
```

- yield 단위로 나누어 실행 가능. 일드 여러개면 일드수만큼 next() 호출해줘야 제너레이터 전체실행됨

next()사용하다가 중간에 return() 메소드 사용하면 함수의 이터레이터를 종료할 수 있다.

데이터를 한번에 하나씩 접근 가능!

```java
function* a(k,k2){
        console.log("1");
        yield k+k2;
        yield '홍길동';
        console.log("end");
    }
    var x = a(10,20);
    console.log(x.next());
    console.log(x.next());
```

- yield 키워드 다음에 설정한 표현식을 next() 메서드를 호출할 때 리턴 가능.
- 리턴 형태는 { value:값 , done:불린값 }yield가 수행되었으면 false 값 반환, 수행되지 않으면 true 값 반환됨.

next() 호출하면 두개의 키가 있는 객체를 리턴하는데 일드로 선택한 항목이 value고 done은 남은항목이 없다는걸 알려준다. 그럼 마지막 반환에서 true가 된다.

```java
function* a(k,k2){
    console.log("1");
    yield k+k2;
//    yield '홍길동';
    console.log("end");
}
var x = a(10,20);
console.log(x.next());
console.log(x.next());
```

저렇게 일드가 없는데 넥스트 하나 더 쓰면 일드 수행 안된거라 던 트루 뜨고 end도 실행됨

```java
function* a(){
        var bbb = yield 'A';
        var aaa = yield 'B';
        console.log(aaa, bbb);
    }
    var x = a();
    console.log(x.next());
    console.log(x.next(2000));
    console.log(x.next(3000));
```

1. x.next() 호출하면 yield ‘A’가 수행되어 { value='A' done:false} 반환된다.

2. x.next(2000) 호출하면 2000을 이전 라인의 var bbb 변수에 설정하고 yield ‘B’가 수행되어 { value='B' done:false}를 반환한다.

3. x.next(3000) 호출되면 3000을 이전 라인의 var aaa 변수에 설정하고 consol에 aaa와 bbb 값을 출력한다. yield 가 더 이상 없기 때문에 {value: undefined, done: true} 반환 되어 출력된다.

# 디스트럭처링

배열이나 객체의 데이터 해체해서 다른 변수로 추출. 분할할당

### 배열 디스트럭처링

```java
var m = [10,20];
var [x,y] = [10,20];
console.log(x, y);  //10, 20
```

양쪽 모두 배열형식으로 지정해야 된다. 인덱스를 기준으로 값을 할당한다.

```java
var [k, k2, k3=100] = [10,20];
console.log(k, k2, k3);
```

값 지정 안해주면 남는공간은 undefiend가 되는데 기본값을 지정할 수 있다.

```java
var k, k2, k3;
[k, k2, k3] = [9,8,7];
console.log(k, k2, k3); //9,8,7
```

```java
var m = [10, 9, [100, 200]];
var a, a2, a3, a4;
[a, a2, [a3, a4]] = [10, 9, [100, 200]];
console.log(a, a2, a3, a4);
```

```java
var x = 10;
var x2 = 20;
[x, x2] = [x2, x];
console.log(x, x2); // 20, 10
```

```java
// spread ...n
var [a,b, ...c] = [9,8,7,6,5,4];
console.log(a,b,c);
```

```java
// 변수생략
var [,,n] = [9,8,7];
console.log(n); //7
```

```java
// 함수의 파라미터 구조분해

function aaa(n) {
	var [k, k2] = n;
	console.log(k+k2);
}
aaa([10, 20]);  //30
```

```java
var sum = ([k, k2]) =>  k+k2;
console.log(sum([10,20])); //30
```

### 객체 디스트럭처링

```java
// 디스트럭처링 json객체 사용
var {aaa,b} = {a:100, b:200};
console.log(aaa,b); //undefined 200
```

키값이 일치해야한다. Key값을 기준으로 값을 할당

```java
var a,b //변수 미리 선언
({a,b} = {a:100, b:200});
console.log(a,b);
```

미리선언된 변수 사용시 () 사용

괄호 안쓰면 에러

```java
var {a, c=1000} = {a:100, b:200};
console.log(a,c); // 100 1000
```

기본값이 더 쎄다

```java
//변수명 바꾸기
var {a:aaa, b:bbb} = {a:100, b:200};
console.log(aaa,bbb); //100 200
```

```java
// 중첩
var x = {k:100, k2: 200, ppp: {k3:300}};
var {k, k2, ppp:{k3}}=x;
console.log(k, k2,k3);  //100 200 300
console.log(x.ppp); //300
```

```java
// 함수 파라미터 //json객체의 전달
function xxx({a,b,c=100}) {
	console.log(a+b, c);
}
xxx({a:100, b:200}) //300 100
```

# json object

```java
//json객체
var k = "name";
var n = {"name":"홍길동", "age":20};
console.log(n.name, n["name"], n[k]); //연관배열 중요
```

```java
//1. 키값을 변수로 지정하여 사용하기
        var x = "username";
        var x2 = "userage";
        var obj = {x:"이순신", x2:20};
        console.log(obj);
        var obj2 = {[x]:"이순신", [x2]:20}; //변수로 키값지정
        console.log(obj2);
```

```java
var obj = {sport1: "축구", sport2: "야구", sport3: "농구"};
console.log(obj);
var s = "sport";
var obj2 = {[s+'1']: "축구", [s+"2"]: "야구", [s+"3"]:"농구"};
console.log(obj2);
```

### 메서드 선언 방식 변경 1

메서드명:function(){} 형식에서 :function이 제거됨.

```java
var person ={
  name: "홍길동",
  age: 20,
  getName: function(){ //함수이름: function(){}
      return this.name;
  },
  setName: function(n){
      this.name = n;
  },
  getAge: function() {
      return this.age;
  },
  setAge: function(a) {
      this.age=a;
  }
}
console.log(person.name, person.age);
person.setName("이순신");
person.setAge(44);
console.log(person.name, person.age);
console.log(person.getName(), person.getAge());
```

```java
var person = {
        name: "홍길동",
        age: 20,
	      getName(){ return this.name},
        setName(n){this.name = n},
        getAge(){return this.age},
        setAge(a) {this.age=a}
      };
console.log(person.getName(), person.getAge());
```

### 메서드 선언 방식 변경 2

```tsx
var person = {
  name: '홍길동',
  age: 20,
  get getName() {
    return this.name;
  }, //get주의
  set setName(n) {
    this.name = n;
  }, //set 주의
  get getAge() {
    return this.age;
  },
  set setAge(n) {
    this.age = n;
  },
};
console.log(person.getName, person.getAge);
```

- ES6에서는 get 과 set 키워드를 사용하여 메서드 사용시 가독성 향상 가능.
- 사용방법은 . (dot)로 접근하고 일반적인 메서드 호출과 다르게 ( ) 사용안함

```java
// 일반적인 함수 형태
function a(x,y){
    return x+y;
}
var result = a(10,20);
console.log(result);

// 람다함수와 디스트럭처링 적용
var result2 = ([x,y]) => x+y; //매개변수와 리턴값이 있는 람다함수
var result3 = (x,y) => x+y; //매개변수와 리턴값있음, 매개변수 여러개 괄호사용
console.log(result2([10, 20]));
console.log(result3(10, 20));
```

배열이나 문자열같은 경우 for~of 반복문사용가능

```java
// for~of
        let a = [10,20,30];
        for(let x of a){
            console.log(x);
        }
        let b = "hello";
        for(let x of b){
            console.log(x);
        }
```

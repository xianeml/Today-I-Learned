# 6) Number / String 객체 추가 메서드

---

## Number.isNaN()

값이 NaN(Not a Number) 숫자가 아닌지에 대해 판별.

기존부터 존재한 전역 isNaN() 함수의 더 엄격한 버전입니다.

> Type (number)이 Number가 아니면 false 반환합니다. number가 NaN 경우는 true 돌려줍니다. 그렇지 않은 경우는 false 리턴합니다.

```jsx
// The one and only
Number.isNaN(NaN); // true

// Numbers
Number.isNaN(1); // false
Number.isNaN(-2e-4); // false
Number.isNaN(Infinity); // false

// Values not of type number
Number.isNaN(true); // false
Number.isNaN(false); // false
Number.isNaN(null); // false
Number.isNaN(''); // false
Number.isNaN(' '); // false
Number.isNaN('45.3'); // false
Number.isNaN('1.2e3'); // false
Number.isNaN('Infinity'); // false
Number.isNaN(new Date()); // false
Number.isNaN('10$'); // false
Number.isNaN('hello'); // false
Number.isNaN(undefined); // false
Number.isNaN(); // false
Number.isNaN(function () {}); // false
Number.isNaN({}); // false
Number.isNaN([]); // false
Number.isNaN([1]); // false
Number.isNaN([1, 2]); // false
Number.isNaN([true]); // false
```

## Number.isInteger()

- 값이 정수인지 판별. 타입까지 판별. 1.0은 정수이고 1.02는 소수.
- 정수이면 true 리턴하고 아니면 false 리턴.

```tsx
//Number.isInteger 메서드 ==>정수인지 boolean 반환, 타입체크
console.log('1:', Number.isInteger(0));
console.log('2:', Number.isInteger(1.0));
console.log('3:', Number.isInteger(1.02));
console.log('4:', Number.isInteger('100'));
console.log('5:', Number.isInteger(NaN));
console.log('6:', Number.isInteger(true));

//"100"->100
console.log(parseInt('100') + 200);
console.log(Number.parseInt('100') + 200); //권장
console.log(Number);
```

## Includes(), startsWith(), endsWith()메서드

포함하냐?

대상 문자열에 지정된 문자열 존재 여부 판별

첫번째 인자에는 찾을 문자열 지정, 두번째 인자에는 시작 인덱스값(옵션)

```java
var mesg = "123hello홍길동987";
       //startWith() ===> 어떤 문자열로 시작 여부 반환
       console.log("1: ", mesg.includes("123"));
       console.log(mesg.endsWith("987"));
```

endsWith()메서드

- 대상 문자열이 지정된 문자열로 끝나는지 여부 판별, 두 번째 인자는 길이.

```tsx
let mesg = '123가나다';
console.log('1:' + mesg.endsWith('가나다'));
console.log('2:' + mesg.endsWith('가나'));
console.log('1:' + mesg.endsWith('가나', 5)); //5 글자만 사용
```

# repeat()

문자열 반복

```java
var mesg = "hello";
        console.log("1: ", mesg.repeat());  // 아무것도 안뜸
        console.log("2: ", mesg.repeat(1));  // 한번 출력
        console.log("3: ", mesg.repeat(2));  //두개 연달아 출력
        console.log("4: ", mesg.repeat(3));  //세개 연달아출력
```

# 템플릿리터럴

```java
let mesg = `hello`;
console.log(mesg);
let mesg2 = `hello world`;
console.log(mesg2);

let a2=10;
let b2=20;
console.log(`합계: ${a2+b2}`);
```

```jsx
// 배열, 문자열값, 표현식, ..문자열값
const aaa = (txt, exp) => console.log(txt, txt[0], exp, txt[1]);

// 함수호출. 매개변수로 txt전달.
aaa`hello`;
```

전달안된 두번째 인자. undifined출력

```jsx
// 문자열과 표현식을 분리하여 파라미터로 전달
const aaa1 = (txt, exp) => console.log(txt, txt[0], exp, txt[1]);

let mesg = '홍길동';
aaa2`world ${mesg}`;
```

월드는 txt에, 달러는 exp에 들어가서 출력된다.

```jsx
aaa`happy ${mesg} !!!`;
```

```jsx
const aaa4 = (txt, exp, exp2) => console.log(txt, txt[0], exp, txt[1], exp2);
aaa4 `안녕하세요 ${mesg} !!! 건강하세요 ${mesg}`;

>>(3) ["안녕하세요 ", " !!! 건강하세요 ", "", raw: Array(3)]0: "안녕하세요 "1: " !!! 건강하세요 "2: ""length: 3raw: (3) ["안녕하세요 ", " !!! 건강하세요 ", ""]__proto__: Array(0) "안녕하세요 " "홍길동" " !!! 건강하세요 " "홍길동"
```

# 배열메소드

### Array-like 객체

{key:value} 형태의 객체 특징 + 배열의 특징

`et arrLike = { 0:값, 1:값,.... , length:개수 };`

```jsx
//{key:value} 객체 특징 -> array-like 객체
let x = { 0: '홍길동', 1: '이순신', length: 3 };
console.log(x, Array.isArray(x));
console.log(x[0], x[1], x[2], x.length);
```

### Array.from() 메서드

새로운 Array객체를 생성.

`Array.from( 값, [function, 객체] );`

- 값: array-like 객체 또는 iterable 객체
- function: 배열 요소마다 호출되는 함수사용 새로운 값 생성
- 객체: function에서 this 키워드 사용시 참조하는 인스턴스.

```jsx
// 1. 첫번째 인자는 array-like 객체 또는 iterable 객체 지정
let arr = Array.from('hello');
console.log(arr, arr[0]);
```

```jsx
// 2. 두번째 인자는 배열생성하면서 수행되는 함수 지정
let arr2 = Array.from('world', (v) => console.log('>>', v));
```

```jsx
// 3. 세번째 인자는 함수내에서 this 사용시 참조할 객체 지정
let arr3 = Array.from(
  'happy',
  (v) => {
    console.log('**', v);
    return v + this.mesg; // 뒤에 나올 객체의 mesg를 참조하겠다
  },
  { mesg: '값' }
);
console.log(arr3);
console.log(Array.isArray(arr3)); //true
```

```tsx
//4. array-like 객체 지정
let arr4 = Array.from({ 0: 100, 1: 200, length: 2 });
console.log(arr4, arr4[0], arr4[1], arr4.length, Array.isArray(arr4));
```

```jsx
var arr = Array.from('hello');
console.log(arr);
var arr = Array.from('hello', (v, idx) => {
  console.log('>>>>>>', v, idx);
  return v + '!!!';
});
console.log(arr);
```

```jsx
var obj = { aaa: 100 };
//from에서 3번째 인자로 지정된 객체를 참조함. this 사용시
var arr = Array.from(
  'hello',
  function (v, idx) {
    console.log('>>>', v, idx, this.aaa); //3번째인자, obj.aaa값참조
    return v + '!!!';
  },
  obj
);
console.log(arr);
```

### **Array.of() 메서드**

우선 Array 객체가 생성되고, 이어서 파라미터에 설정값들을 생성한 배열에 추가한다.

```jsx
//Array.of 메소드 ===> 배열을 새성
var arr = Array.of(10, 20, 30);
//배열생성
console.log(arr[0]); // 10
var arr = Array.of('홍길동', '이순신');
console.log(arr, arr[1]);
```

### copyWithin() 메서드

Index 범위의 값을 복사하여 같은 배열의 지정한 위치에 설정.

`arr.copyWithin( a, [b, c] );`

a: 복사된 값을 설정 idx, b: 복사하기 위한 시작 idx, c: 복사하기 위한 끝 idx(c-1)

```tsx
//1.
var arr = [1, 2, 3, 4, 5];
let copyArr = arr.copyWithin(0);
console.log(copyArr); //1,2,3,4,5
```

```tsx
//2.
var arr = [1, 2, 3, 4, 5];
let copyArr1 = arr.copyWithin(0, 3);
console.log(copyArr1); //4,5,3,4,5
```

```tsx
//3.
var arr = [1, 2, 3, 4, 5];
let copyArr2 = arr.copyWithin(2);
console.log(copyArr2); //1,2,1,2,3
```

```tsx
//4.
var arr = [1, 2, 3, 4, 5];
let copyArr4 = arr.copyWithin(1, 0, 3);
console.log(copyArr4); //1,1,2,3,5
```

### **fill() 메서드**

Index 범위의 값을 지정한 값으로 변경한다

`arr.fill( a, [b, c] );`

a: 채울값, b:시작 idx, c:끝 idx(c-1까지)

결국 b에서 부터 c-1까지 a 값으로 설정한다.

```jsx
var arr = [1, 2, 3, 4, 5];
let copyArr = arr.fill(9);
console.log(copyArr); // [9, 9, 9, 9, 9]
```

```jsx
var arr2 = [1, 2, 3, 4, 5];
let copyArr2 = arr2.fill(9, 3);
console.log(copyArr2); // [1, 2, 3, 9, 9]
```

```jsx
var arr3 = [1, 2, 3, 4, 5];
let copyarr3 = arr3.fill(9, 2, 4);
console.log(copyarr3); // [1, 2, 9, 9, 5]
```

### entries() 메서드

배열을 {key:value} 형태로 반환.

key는 배열 index값이고 value는 배열요소 값. for~of 반복문 사용하여 iterator로 처리 가능.

```tsx
//배열의 util 클래스
var arr = ['홍길동', '이순신', '유관순'];
var x = arr.entries();
console.log(x);
for (var [key, v] of x) {
  console.log(key, v); //idx, data
}

//keys(): 배열에서 키값만 리턴
var x2 = arr.keys();
console.log(x2);
for (var key of x2) {
  console.log(key);
}
```

### find()

`arr.find(function [,obj]);`

function: 배열 요소가 반복 될 때마다 호출된다. true 리턴시 find() 종료하고 처리중인 배열 요소를 반환한다.

function(ele,idx,all){} 처럼 3가지 파라미터 변수 설정 가능하다.

- ele: 처리중인배열요소
- idx: 처리중인배열index
- all: 전체배열obj : function에서 this로 접근할 객체 지정.

```jsx
var arr = [10, 20, 30, 40, 50];
let xxx = arr.find((ele, idx, all) => {
  console.log(ele, idx, all);
  return ele == 30;
});
console.log(xxx);
```

# 클래스

- 멤버변수를 따로 적을 필요없다.
- 생성자는 클래스 하나당 하나만
- new로 객체생성 후 사용

```jsx
//1.클래스 선언식
class Person {
  setName(name) {
    this.name = name;
  }
  getName() {
    return this.name;
  }
  setAge(age) {
    this.age = age;
  }
  getAge() {
    return this.age;
  }
}
```

```jsx
//2. 사용하려면 객체생성
va p1 = new Person(); // 기본생성자 호출
p1.setName("홍길동");
p1.setAge(20);
console.log(p1.getName());
console.log(p1.getAge());
```

자바랑 다른점은 멤버변수가 따로 필요없다는것.

`p1.name="이순신";` 했을때 이름이 바뀐다.

es6버전

```jsx
//1.클래스 선언식
class Person {
  set setName(name) {
    this.name = name;
  }
  get getName() {
    return this.name;
  }
  set setAge(age) {
    this.age = age;
  }
  get getAge() {
    return this.age;
  }
}

//2. 사용하려면 객체생성
var p1 = new Person();
p1.setName = '홍길동';
p1.setAge = 20;
console.log(p1.getName);
console.log(p1.getAge);
```

get set 키워드 붙여주고 사용할 땐 함수호출이 . 으로 참조

## 생성자

- 클래스 인스턴스를 생성하고 생성한 인스턴스를 초기화 역할.
- 생성자는 하나만 지정 가능
- 명시적으로 지정하지 않으면 프로토타입 생성자 호출됨. 얘를 디폴트 생성자라 한다

```jsx
class Person {
  // 생성자 => 반드시 하나, 이름은 반드시 constructor
  constructor(
    name,
    age //생성자
  ) {
    console.log('constructor======');
    this.name = name;
    this.age = age;
  }
  set setName(name) {
    this.name = name;
  }
  set setAge(age) {
    this.age = age;
  }
  get getName() {
    return this.name;
  }
  get getAge() {
    return this.age;
  }
}

//2. 사용하려면 객체생성
var p1 = new Person('홍길동', 44);
console.log(p1.getName);
console.log(p1.getAge);

var p2 = new Person();
console.log(p2.getName);
```

```jsx
var p2 = new Person(); //객체생성가능. 자바는 컴파일부터 잡아주는데 얘는 undefined까지 띄워줌.
console.log(p2.getName);
```

```tsx
constructor(name, age);
{
  console.log('constructor========');
  this.name = name;
  this.age = age;
  return { name: 'aaa', age: 100 }; //리턴값 반환
  // return 100;//객체 데이터 반환
}
```

생성자에서 객체를 리턴하면 리턴값대로 객체생성이된다. 객체형식 아니라면 리턴값 무시

## new.target속성과 new.target.name속성

```jsx
class Person {
  //new.target 속성, new.target.name속성
  //new.target은 constructor를 참조함
  //new.target.name은 클래스의 이름
  constructor(name, age) {
    console.log(new.target);
    console.log('=============');
    console.log(new.target.name);
  }
  setName(name) {
    this.name = name;
  }
  getName() {
    return this.name;
  }
  setAge(age) {
    this.age = age;
  }
  getAge() {
    return this.age;
  }
}

// 객체 생성
var p1 = new Person('홍길동', 20);
```

- 객체 생성후에 사용 가능. ( 생성하지 않으면 undefined )
- 생성자에서 사용시 new.target 속성은 constructor를 참조한다.

# 상속

자바처럼 extends 키워드로 상속 표현

부모클래스 멤버를 자식클래스 상속받아서 사용

1. 부모 클래스에만 constructor를 작성하면, 자식 클래스의 ‘default 생성자’가 호출되고 부모 클래스의 constructor가 호출된다

2. 자식과 부모 클래스 양쪽 constructor를 작성하면 자식 constructor가 호출되지 반드시 부모 constructor를 명시적으로 호출해야 된다.

3. 자식 클래스와 부모클래스 양쪽 생성자를 작성하지 않아도 인스턴스 생성됨

```jsx
class Employee {
  // 부모클래스
  setName(name) {
    this.name = name;
  }
  setSalary(salary) {
    this.salary = salary;
  }
  getName() {
    return this.name;
  }
  getSalary() {
    return this.salary;
  }
}
```

```jsx
class Manager extends Employee {
  setDepart(depart) {
    this.depart = depart;
  }
  getDepart() {
    return this.depart;
  }
}
```

```jsx
var man = new Manager(); //자식 생성
man.setName('홍길동'); //부모
man.setSalary(1000); //부모
man.setDepart('인사'); //자식
```

```jsx
console.log(man.getName());
console.log(man.getSalary());
console.log(man.getDepart());
```

2. 자식과 부모 모두 생성자를 작성하면 자식에도 반드시 부모 생성자를 명시적으로 호출해야된다.

```tsx
class Employee {
  //생성자 작성, name, salary
  constructor(
    name,
    sal //생성자
  ) {
    console.log('부모생성자 =================');
    this.name = name;
    this.salary = sal;
  }
  setName(name) {
    this.name = name;
  }
  setSalary(sal) {
    this.salary = sal;
  }
  getName() {
    return this.name;
  }
  getSalary() {
    return this.salary;
  }
} //end Employee

class Manager extends Employee {
  //생성자 작성 , name, salary, depart
  constructor(name, sal, depart) {
    super(name, sal); //부모 생성자 명시적 호출 필수(생성자의 첫줄에 기입)
    console.log('자식 생성자===============');
    this.depart = depart;
  }
  setDepart(depart) {
    this.depart = depart;
  }
  getDepart() {
    return this.depart;
  }
} //end Mananger
var man = new Manager('홍길동', 1000, '인사'); //부모, 부모 ,자식
console.log(man.getName());
console.log(man.getSalary());
console.log(man.getDepart());
```

### 메소드 오버라이딩

```tsx
class Employee {
  //name, salary, getEmployee()
  constructor(name, sal) {
    this.name = name;
    this.salary = sal;
  }
  setName(name) {
    this.name = name;
  }
  setSalary(sal) {
    this.salary = sal;
  }
  getName() {
    return this.name;
  }
  getSalary() {
    return this.salary;
  }
  getEmployee() {
    //추가
    return this.name + '\t' + this.salary;
  }
} //end Employee

class Manager extends Employee {
  constructor(name, sal, depart) {
    super(name, sal); //부모 생성자 호출 필수
    this.depart = depart;
  }
  setDepart(depart) {
    this.depart = depart;
  }
  getDepart() {
    return this.depart;
  }
  //오버라이딩
  getEmployee() {
    return super.getEmployee() + '\t' + this.depart;
  }
} //end Mananger
var man = new Manager('홍길동', 1000, '인사');
console.log(man.getEmployee()); //오버라이딩 메소드 호출
```

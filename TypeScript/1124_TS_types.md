### 설치:

`npm install -g typescript`

# 타입스크립트의 특징

- 컴파일동작: javascript 언어는 인터프리터 언어이다. 따라서 코드가 유효한지 알기 위해서는 실행을 해야 알 수 있다. → 버그 찾기까지 시간 소요. 반면에 타입스크립트는 컴파일러에 의해서 미리 오류검사 가능. 컴파일시점에 구문오류 발견하면 컴파일 오류 발생시킴.
- 객체지향 프로그래밍 지원 : 클래스, 인터페이스, 상속등
- 강력한 정적타입 지정

### test.ts:

```java
var mes:string="hello";
console.log(mes);
```

이 변수는 문자열만 담을 수 있다고 타입 지정

### 컴파일:

`tsc test`

tsc ( typescript compiler) 키워드 뒤에 파일명 작성.

.ts까지 안써줘도 됨. 이 명령어 실행하면 test.js 파일이 만들어진다.

### 실행:

`node test`

# 변수선언 방식

`let 식별자:타입 = value;`

`let 식별자:타입;` → 초기값 undefined

`let 식별자 = value;` -> 타입은 저장되는 값에 따라 결정됨 ``

`let 식별자;` → 변수타입 any, 값 undefined

```jsx
let mesg: string = '홍길동';
let mesg2: number = 10;
let mesg3: boolean = true;
let mesg4: null = null;
let mesg5: undefined = undefined;
let mesg6 = function (): void {};

console.log(mesg, mesg2, mesg3, mesg4, mesg5, mesg6);

var b: number = 10;
var b: number = 20;
console.log(b);
```

```jsx
let fullName: string = `Bob Bobbington`;
let sentence: string = `hello, my name is ${fullName}`;

console.log(sentence);
```

# 타입스크립트의 타입

### any 타입:

- 모든 type의 super type으로서 동적 type을 나타낸다.
- 변수에 대한 type 검사 생략하는 것과 같다.

```tsx
**var a:any=null;
a=100;
console.log(a.toFixed(2)); // 100.00
a="홍길동";
console.log(a.trim(), a.length);**
```

toFixed(): 지정된 소수점 자릿수까지 보여줌.

### Built-in 타입:

number, string, Boolean, void, null, undefined

### User-defined 타입:

사용자 정의 형식: 열거형, 클래스, 인터페이스, 배열, 튜플

```jsx
//main2_array
//배열

//1.데이터 형식 []
let ex: number[] = [1, 2, 3];
console.log(ex.length);
console.log(ex);

//2.Array<데이터> 형식
let ex2: Array<number> = [1, 2, 3];
console.log(ex2.length);
console.log(ex2);
```

```jsx
//main3
//튜플 ==> 배열의 특정위치에 고정된 타입만 저장가능

//Declare a tuple type
let x: [string, number];

x = ['홍길동', 20];
// x=[20, "홍길동"];

console.log(x[0], x[1]);
// console.log(x[0], x[1], x[2]);
```

배열 방 타입을 따로따로 지정가능

```jsx
// 열거형

enum Color {Red, Green, Blue};
let c: Color=Color.Red;

console.log(Color.Red);  //0

// 초기값 설정
enum Color2 {Red=1, Green, Blue}; //1,2,3
let c2:Color2 = Color2.Green;
console.log(c2); //2

// 명시적 값설정
enum Color3 {Red=1, Green=3, Blue=4};
let c3:Color3=Color3.Green;
console.log(c3); //3
```

초기화 되지 않은 열거형의 첫번째 값은 '0'으로 시작한다.

값을 지정해 주면, 다음부터는 자동증가

# Type Assertion

- Type Assertion은 변수의 타입을 다른 타입으로 변경하는 것을 의미한다. (형변환)
- 현재타입 → any → 목적타입 순으로 기본설정
- '타입 캐스팅'은 런타임에 타입이 변경됨을 의미하지만, Type Assertion은 컴파일 시점에 변경됨.

```tsx
//any 타입은 바로 <타입> 사용가능
let someValue: any = 'this is a string';
let strLength: number = (<string>someValue).length;
console.log(strLength);

//as 형식이 주로 사용됨
let strLength2: number = (someValue as string).length;
console.log(strLength2);
```

```tsx
// 현재타입 --> any --> 목적타입
var str = '1';
var str4: string = (str as any) as string;
console.log(str4);

// 현재타입 --> any --> 목적타입
var str2: number = <number>(<any>str);
var str3: string = <string>(<any>str2);
console.log(str, str2, str3);
```

### 모듈 연습:

```tsx
export class Person {
  constructor(public name: string, public age: number, public address: string) {
    console.log('생성자 호출');
  }
  getName() {
    return this.name;
  }
  getAge() {
    return this.age;
  }
  getAddress() {
    return this.address;
  }
}
```

```tsx
import { Person } from './person';

var p = {
  name: '홍길동',
  age: 20,
  address: '서울',
};

console.log(p);
var p2 = p as Person;
console.log(p2);
var p3: Person = new Person('홍길동', 20, '서울');
console.log(p3.getName() + '\t' + p3.getAge());
```

```tsx
// 출력결과
{ name: '홍길동', age: 20, address: '서울' }
{ name: '홍길동', age: 20, address: '서울' }
생성자 호출
홍길동  20
```

```tsx
/*
type assertion
TypeScript 사용시 원하는 방식으로 유형이 유추되고 분석된 뷰를 재정의 할 수 있음
컴파일러에게 사용자가 타입을 정해주고, 컴파일러에게 추측해서는 안된다고 알려주는 것
*/

interface User {
  bar: number;
  baz: string;
}
var u: User = {} as User;
// {} 타입을 User 타입으로 변경, 컴파일러에게 타입을 알려주는 방법이다
u.bar = 100;
u.baz = '홍길동';
console.log(u);
```

객체 기본값으로 텅텅빈거를 초기화했고 User 인터페이스 객체의 타입만 받는다.

u 객체의 bar 변수에는 넘버 할당, baz에는 문자 할당

```tsx
//출력결과
{ bar: 100, baz: '홍길동' }
```

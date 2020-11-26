# 배열 ( array )

- type을 지정하기 때문에 같은 데이터만 저장이 가능하다. (타입지정 안하면 any) 만약 다른 데이터를 저장하기 위해서는 튜플(tuple)을 사용한다.
- typescript에서의배열은다음과같이선언과초기화작업필요.

```tsx
// 1. 배열 선언
var nums: number[];

// 2. 배열 초기화
nums = [10, 9, 8, 7];

// 3. 출력
console.log(nums[0], nums[1]);

for (var x in nums) {
  console.log('in ' + nums[x]);
}
for (var x2 of nums) {
  console.log('of: ' + x2);
}
```

- 튜플: 배열과는 다르게 서로 다른 데이터형을 저장하는 용도.

# union

- Union은 하나 또는 두가지 타입을 결합하는 기능으로서 여러 타입 중 하나일 수 있는 값을 표현하는 강력한 방법.
- 두 개 이상의 데이터 타입이 파이프 기호(|)를 사용하여 조합되어 union형식을 나타낸다.

```tsx
// 1. 변수
var mesg0: string | number;
mesg0 = 100;
console.log(mesg0); //100

mesg0 = '홍길동';
console.log(mesg0); // 홍길동

// 2. 함수 파라미터
function xxx0(n: number | string) {
  console.log(n);
}
xxx0('홍길동'); // 홍길동
xxx0(100); // 100
```

```tsx
// 3. 배열 파라미터
function xxx2(n: number[] | string[]) {
  console.log(n);
}
xxx2([1, 2, 3]);
xxx2(['홍길동', '이순신']);

var mesg00: string | number | string[];
mesg00 = 100;
mesg00 = '홍길동';
mesg00 = ['a', 'b', 'c'];
console.log(mesg00); // [ 'a', 'b', 'c' ]
```

```tsx
// ? 사용 가능
function kk(n?: number | string) {
  console.log(n);
}
kk();
kk(100);
kk('aa');
```

```tsx
function aaa(n: any): string | number {
  return n;
}

var _x: string | number = aaa('홍길동');
var _x2: string | number = aaa(2000);
console.log(_x, _x2);
```

함수 호출 결과를 유니언타입 변수에 담았다

# interface

- interface는 typescript의 entity(객체)가 반드시 준수해야 되는 구문을 정의. ( ? 사용하면 옵션 설정 가능 )
- interface내에는 멤버(속성, 메서드) 선언만 가능.실제 멤버를 정의할 때는 파생 클래스를 이용한다.( 파생 클래스에서 멤버 추가 불가. Interface에서 선언된 멤버만 사용 가능 )

```tsx
/*
interface가 필요한 이유
1. size 속성이 필요하지만 문제없이 실행된다.
*/
function xyz(p: { label: string }) {
  console.log(p.label);
}
var m0 = { size: 10, label: '홍' };
xyz(m0);
```

라벨만 받고있는 파라미터에 두 키를 가진 객체를 넣으면 사이즈가 안맞음

근데도 실행됨

```tsx
// 2. interface로 구현
interface ppp {
  size: number;
  label: string;
}

function xyz2(p: ppp) {
  console.log(p.size, '\t', p.label);
}
var m1 = { size: 10, label: '홍' };
xyz2(m1);
var m2 = { label: '홍' };
// xyz2(m2); // 에러발생
```

함수 xyz2의 매개변수를 ppp인터페이스 타입으로 받는다.

함수호출할때 파라미터로 넘어온 객체 형태가 인터페이스랑 맞아야 실행됨

```tsx
interface IPerson {
  firstName: string;
  lastName: string;
  sayHi: () => string;
}
var customer: IPerson = {
  firstName: 'Tom',
  lastName: 'Hanks',
  sayHi: (): string => 'Hi there',
};

console.log('Customer Object');
console.log(customer.firstName);
console.log(customer.lastName);
console.log(customer.sayHi);
```

사람 인터페이스를 만들었어. 걔는 갖춰야할 형식을 객체로 갖고있어.

고객이라는 객체는 사람인터페이스 타입 형식을 갖춰서 만들어진다.

참조할땐 만들어진 고객에서 객체키값으로 참조.

```tsx
var employee: IPerson = {
  firstName: 'Jim',
  lastName: 'Blakes',
  sayHi: (): string => 'hello',
};
console.log('Employee Object');
console.log(employee.firstName);
console.log(employee.lastName);
console.log(employee.sayHi());

var xxx1 = {
  aaa: () => 'aa',
  bbb: () => 'bb',
  ccc: () => 'cc',
  ddd: (n) => n,
};
console.log(xxx1.aaa());
console.log(xxx1.bbb());
console.log(xxx1.ccc());
console.log(xxx1.ddd(1111));
```

```tsx
// interface에 Union 사용
interface IPerson {
  firstName: string;
  lastName: string;
  mesg: string | number | string[];
  sayHi: () => string;
}

var kkk: IPerson = {
  firstName: '20',
  lastName: 'Hanks',
  sayHi: (): string => 'hi there',
  mesg: '안녕하세요',
};

console.log(kkk.mesg);

var kkk2: IPerson = {
  firstName: '20',
  lastName: 'hanks',
  sayHi: (): string => 'hi there',
  mesg: 200,
};
console.log(kkk2.mesg);

var kkk3: IPerson = {
  firstName: '20',
  lastName: 'hanks',
  sayHi: (): string => 'hi there',
  mesg: ['hi', 'how', 'are', 'you'],
};
console.log(kkk3.mesg);
```

```tsx
// interface에 Union 사용
interface IPerson {
  firstName: string;
  lastName: string;
  mesg2: string | number | string[] | ((x) => string);
  sayHi: () => string;
}

var yyy4: IPerson = {
  firstName: '20',
  lastName: 'hanks',
  sayHi: (): string => 'hi there',
  mesg2: (x) => '안녕하세요' + x,
};
var fn: any = yyy4.mesg2;
console.log(fn('홍길동'));
```

### 배열

```tsx
interface namelist {
  [index: number]: string;
}
var list: namelist = ['aa', 'bb', 'cc'];
list[3] = 'ddd';
console.log(list); // [ 'aa', 'bb', 'cc', 'ddd' ]

interface namelist2 {
  [index: number]: number;
}
var list2: namelist2 = [1, 2, 3];
list2[3] = 100;
console.log(list2); // [ 1, 2, 3, 100 ]

interface age {
  [index: string]: number;
}
var agelist: age = {};
agelist['one'] = 100;
agelist['two'] = 200;
agelist['three'] = 300;
console.log(agelist); // { one: 100, two: 200, three: 300 }
```

배열의 인덱스 타입, 밸류의 타입을 지정가능

배열이 사용하는 키의 종류와 그 배열에 들어있는 항목의 타입을 모두 지정할수있다

키의 타입을 설정하기 위해서는 [index:타입] 형식을 이용한다.

### readonly

- 인터페이스에 선언된 변수값은 초기화 이후에 변경 불가

```tsx
interface Point {
  readonly x: number;
  readonly y: number;
}

let p1: Point = {
  x: 10,
  y: 20,
};
console.log(p1.x, p1.y);
```

### 인터페이스 상속

```tsx
interface Person {
  age: number;
}
interface Musician extends Person {
  instrument: string; //age:number 포함
}

var drummer: Musician = {
  age: 20,
  instrument: '드럼',
};
console.log('나이', drummer.age);
console.log('악기', drummer.instrument);
```

인터페이스 간 상속

```tsx
// type assertion
var drummer2 = <Musician>{};
drummer2.age = 20;
drummer2.instrument = 'Drums';
console.log('나이', drummer2.age);
console.log('악기', drummer2.instrument);

// type of assertion (as 사용)
var drummer3 = {} as Musician;
drummer3.age = 20;
drummer3.instrument = '기타';
console.log('나이', drummer3.age);
console.log('악기', drummer3.instrument);
```

Musician 인터페이스 타입의 객체를 받는 변수 만들고 빈값 초기화.

객체 접근해서 값 세팅

```tsx
interface IParent1 {
  v1: number;
}
interface IParent2 {
  v2: number;
}
interface Child extends IParent1, IParent2 {}

var Iobj: Child = { v1: 100, v2: 200 };
console.log(Iobj.v1, '\t', Iobj.v2);
```

여러개의 인터페이스를 다중상속 가능.

# 클래스

```tsx
class Greeter {
  greeting: string;
  constructor(mesg: string) {
    this.greeting = mesg;
  }
  greet(): string {
    return 'hello, ' + this.greeting;
  }
}

let greeter = new Greeter('world'); // 객체생성
console.log(greeter.greet()); // hello, world
greeter.greeting = 'aa'; // 문자 세팅
console.log(greeter.greet()); // hello, aa
```

이 클래스는 생성자에 greeting 문자를 받는다. 객체생성할 때 문자를 보내야한다.

필드의 greet 함수는 받아온 greeting 문자를 리턴한다.

### constructor와 상속

1. 자식 클래스와 부모 클래스 양쪽 constructor를 작성하지 않아도 인스턴스 생성( default constructor 사용 )

2. 부모 클래스에만 constructor를 작성하면, 자식 클래스의 ‘default 생성자’가 호출되고 부모 클래스의  constructor가 호출된다.

3. 자식 클래스에만 constructor를 작성하면 자식 클래스의 constructor가 호출되고 반드시 부모 constructor를 명시적으로 호출해야 된다

4. 자식과 부모 클래스 양쪽 constructor를 작성하면 자식 constructor가 호출되지만 반드시 부모 constructor를 명시적으로 호출해야 된다.

```tsx
class Shape {
  area: number;
  constructor(a: number) {
    this.area = a;
  }
}
class Circle extends Shape {
  constructor(num: number) {
    super(num); // area값 그대로 받아옴
  }
  disp(): void {
    console.log('area of the circle' + this.area);
  }
}
var obj = new Circle(223);
obj.disp();
```

```tsx
class Employee {
  name: string;
  salary: number;
  constructor(name: string, salary: number) {
    this.name = name;
    this.salary = salary;
  }
  getEmployee(): string {
    return this.name + '\t' + this.salary;
  }
}

class Manager extends Employee {
  depart: string;
  constructor(name, salary, depart) {
    super(name, salary);
    this.depart = depart;
  }
  getEmployee(): string {
    return this.name + '\t' + this.salary + '\t' + this.depart;
  }
}

let man = new Manager('홍길동', 4000, '개발');
console.log(man.getEmployee());
```

```tsx
class StaticMem {
  static num: number;
  static disp(): void {
    console.log(StaticMem.num);
  }
}
StaticMem.num = 12;
StaticMem.disp();
```

```tsx
class Encapsulate {
  str: string = 'hello';
  private str2: string = 'world'; //접근제한자
}

var obj0 = new Encapsulate();
console.log(obj0.str);
// console.log(obj0.str2); // 접근불가

// 상속
class A {
  public a: number = 10;
  private b: number = 20;
  protected c: number = 30;
}

class B extends A {
  info() {
    console.log(this.a);
    // console.log(this.b); // 접근불가
    console.log(this.c);
  }
}
var aa = new B();
aa.info();
```

private은 객체참조변수.변수명 으로 접근이 안된다.

그래서 클래스에 get set 메소드 만들어놓고 꺼내서 사용했다. 이게 은닉화다.

```tsx
class BBB {
  str: number;
  info(x: number) {
    console.log(x);
  }
  constructor(public x2: number) {
    console.log(x2);
    this.str = x2;
  }
}
var xx2 = new BBB(100);
console.log(xx2.x2);
console.log(xx2.str);
```

```tsx
class ZZZ {
  constructor(public x0: number, public x1: string) {
    console.log(x0 + '\t' + x1);
  }
}
var x99 = new ZZZ(100, '홍');
console.log(x99.x0 + '\t' + x99.x1);
```

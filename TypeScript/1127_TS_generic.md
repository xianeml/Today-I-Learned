### Class 와 interface

```tsx
interface ILoan {
  interest: number;
}
class AgriLoan implements ILoan {
  interest: number;
  rebate: number;
  constructor(interest: number, rebate: number) {
    this.interest = interest;
    this.rebate = rebate;
  }
}

var obj = new AgriLoan(10, 1);
console.log('Interest is : ' + obj.interest + ', Rebate is: ' + obj.rebate);
console.log(typeof obj, obj instanceof AgriLoan);

// 다형성 가능
var obj2: ILoan = new AgriLoan(100, 2); // 다형성 생성
console.log(typeof obj2, obj2 instanceof AgriLoan);
```

```tsx
Interest is : 10, Rebate is: 1
object true
object true
```

### 추상클래스

```tsx
abstract class Animal {
  abstract makeSound(): void;
  move(): void {
    console.log('Animal move');
  }
}

class Cat extends Animal {
  makeSound(): void {
    console.log('makeSound');
  }
}
var c = new Cat();
c.makeSound(); // makeSound
c.move(); // Animal move
```

추상클래스에 있는 move()도 참조할 수 있다.

# typescript의 object

```tsx
var person = {
  firstName: 'Tom',
  lastName: 'Hanks',
  sayEcho: function () {
    console.log('sayEcho()');
  },
  phones: ['010', '02'],
};
console.log(person.firstName);
console.log(person.lastName);
person.sayEcho();
console.log(person.phones[0], person.phones[1]);
```

### Type Template

일반적인 자바스크립트의 객체와 다르게 typescript에서는 객체에 속성 및 메서드를 나중에 추가하기 위해서는 type template 방식으로 처리해야 된다.

```tsx
var person = {
  firstName: 'Tom',
  lastName: 'Hanks',
  // type template
  sayEcho: function () {},
  email: '',
};

// 멤버 추가
person.sayEcho = function (): string {
  console.log('SayEcho');
  return 'Test';
};
person.email = 'aa@daum.net';

console.log(person.firstName, person.sayEcho(), person.email);
```

템플릿만 적어두고 구현은 밖에서 가능

### 객체파라미터1

함수의 파라미터로 객체 표현식을 사용할 수 있다.

```tsx
var student = {
  username: '홍길동',
  age: 20,
};
function info2(str: { username: string; age: number }) {
  console.log(str.username + '\t' + str.age);
}

function info(str) {
  console.log(str.username + '\t' + str.age);
}
info(student);
info2(student);
```

### 객체파라미터2

함수의 파라미터로 익명 객체( anonymous object)을 사용할 수 있다

```tsx
function info4(str: { readonly username: string; age?: number }) {
  console.log(str.username + '\t' + str.age);
}
info4({ username: '홍길동', age: 20 });
info4({ username: '홍길동' }); // 홍길동  undefined
```

# Duck typing

두 객체가 같은 형태의 속성을 공유하면 두 객체는 같은 타입으로 간주한다.

객체의 실제 타입이 아닌 객체의 특정 속성의 존재 여부를 확인하여 적합성을 검사한다.

```tsx
class Sparrow {
  sound = '참새 짹짹';
}
class Parrot {
  sound = '앵무새 안녕~';
}
class Duck {
  sound = '오리 꽥꽥~';
  swim() {
    alert('오리가 헤엄치다!!');
  }
}
var parrot: Parrot = new Sparrow();
var sparrow: Sparrow = new Parrot();
var parrotTwo: Parrot = new Duck();

console.log(parrot.sound); // sparrow가 실행
console.log(sparrow.sound); // parrot 실행
console.log(parrotTwo.sound); // duck 실행

var xxx = parrotTwo as Duck; // 형변환
xxx.swim();
```

swim() 찍어보려면 Duck으로 형변환해야한다.

```tsx
// 인터페이스 선언
interface Point {
  x: number;
  y: number;
}

// 인터페이스 사용 1: 객체사용
var p: Point = {
  x: 10,
  y: 20,
};
console.log(p.x + '\t' + p.y);
```

```tsx
// 인터페이스 사용 2: 클래스 사용
class X implements Point {
  x: number;
  y: number;
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
}
var k = new X(10, 20);
console.log(k.x + '\t' + k.y);
```

```tsx
// duck typing 적용 예
function kkk(k: Point, k2: Point) {
  console.log(k.x + '\t' + k.y);
  console.log(k2.x + '\t' + k2.y);
}
kkk({ x: 1, y: 2 }, { x: 3, y: 4 });
kkk({ x: 5, y: 6 }, { x: 7, y: 8 });
// 같은 속성을 가지므로 Point로 인식함
```

k:Point와 {x:1,y:2}는 같은 속성 형태를 가지기 때문에 duck typing 가능

# Generic

```tsx
class Box {
  obj: any;
  setValue(obj: any) {
    this.obj = obj;
  }
  getValue() {
    return this.obj;
  }
}

var a: Box = new Box();
a.setValue('홍길동');
var str: string = a.getValue() as string;
console.log(str);

var b: Box = new Box();
b.setValue(new Date());
var str2: Date = b.getValue() as Date;
console.log(str2);
```

```tsx
class Box2<T> {
  obj: T; // generic 타입 지정
  setValue(obj: T) {
    // 파라미터 타입지정
    this.obj = obj;
  }
  getValue(): T {
    // 리턴타입 지정
    return this.obj;
  }
}

var x: Box2<string> = new Box2<string>();
x.setValue('홍길동');
var xx: string = x.getValue();
console.log(xx);

var y: Box2<Date> = new Box2<Date>();
y.setValue(new Date());
var yy: Date = y.getValue();
console.log(yy);
```

any타입과 제너릭으로 아무타입 받기

```tsx
interface Product {
  mesg: (x: any) => any;
}

class Car implements Product {
  mesg(x: any) {
    return x;
  }
}

var c1 = new Car();
var m = c1.mesg('홍길동');
console.log(m);

var c2 = new Car();
var m2 = c2.mesg(new Date());
console.log(m2);
```

```tsx
interface Product2<T> {
  mesg: (x: T) => T;
}

class Car2<T> implements Product2<T> {
  mesg(x: T) {
    return x;
  }
}

var cc: Car2<string> = new Car2<string>();
var mm = cc.mesg('이순신');
console.log(mm);

var dd: Car2<Date> = new Car2<Date>();
var mmm = dd.mesg(new Date());
console.log(mmm);
```

이것도 any 인터페이스 구현

```tsx
// 1. 함수의 제네릭
function six<T>(n: T): T {
  return n;
}

var aa = six<number>(100);
var bb = six<string>('aaa');
var ccc = six<boolean>(true);
console.log(aa + '\t' + bb + '\t' + ccc);
```

<파라미터타입>(파라미터타입) : 리턴타입

```tsx
// 2. 배열의 제네릭 사용
function one<T>(n: T[]): number {
  return n.length;
}
console.log(
  one<number>([1, 2])
);
console.log(
  one<string>(['aa', 'bb'])
);
console.log(
  one<boolean>([true, false])
);

function two<T>(n: T[]): string {
  return n.length + '';
}
console.log(
  two<number>([1, 2])
);
console.log(
  two<string>(['aa', 'bb'])
);
console.log(
  two<boolean>([true, false])
);
```

```tsx
class Box4<T> {
  obj;
  setValue(obj: T): void {
    this.obj = obj;
  }
  getValue(): T {
    return this.obj;
  }
}
function aaa<T>(p: T) {
  console.log((<Box4<string>>(<any>p)).getValue());
}
var ppp: Box4<string> = new Box4<string>();
ppp.setValue('홍길동');
var ppp2: Box4<number> = new Box4<number>();
ppp2.setValue(10);

aaa(ppp);
aaa(ppp2);
```

# namespace

관련 코드를 논리적으로 그룹화하는 방법

패키지 개념이랑 비슷하다

```tsx
// 1. namespace없이
class MyDate {
  day: number;
}

var d: MyDate = new MyDate();
d.day = 20;
```

```tsx
namespace MyNameSpace {
  export interface IPerson {
    username: string;
    age: number;
  }
}

var kk: MyNameSpace.IPerson = {
  username: '홍길동',
  age: 10,
};
console.log(kk.username, kk.age);
```

namespace 외부에서 접근해야 되는 경우에는 export 키워드 사용.

외부에서 `네임스페이스이름.클래스이름` 으로 참조한다.

```tsx
namespace MyNameSpace2 {
  export interface IPerson {
    email: string;
    phone: number;
  }
}

var kk2: MyNameSpace2.IPerson = {
  email: 'aaa@daum.net',
  phone: 12345,
};
console.log(kk2.email, kk2.phone);
```

```tsx
namespace MyNameSpace {
  export interface IPerson {
    username: string;
    age: number;
  }
  export class Math {
    eng: number;
    kor: number;
    constructor(eng: number, kor: number) {
      this.eng = eng;
      this.kor = kor;
    }
    getInfo() {
      return this.eng + '\t' + this.kor;
    }
  }
  export var user = {
    name: '이순신',
    age: 33,
  };
}
```

```tsx
var kk: MyNameSpace.IPerson = {
  username: '홍길동',
  age: 10,
};
console.log(kk.username + '\t' + kk.age);
var m0 = new MyNameSpace.Math(100, 200);
console.log(m0.eng + '\t' + m0.kor);
console.log(MyNameSpace.user.name + '\t' + MyNameSpace.user.age);
```

이 네임스페이스 패키지에 인터페이스도 담을 수 있고 클래스도 담을 수 있다.

외부 ts파일에 있는 네임스페이스 참조하려면

<reference path="sample.ts" /> 태그 사용

컴파일할땐 `tsc —out app.js` 이런식으로 —out 붙여서 명령 작성

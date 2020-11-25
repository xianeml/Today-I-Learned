# 변수 scope

**전역 범위( global scope ):**

프로그래밍 구조 외부에서 변수 선언됨. 이 변수는 코드내의 어느 위치에서나 접근 가능.

**클래스 범위( class scope ):**

클래스 안의 메서드 밖에서 선언된 변수. 필드(field)라고 부른다.

이 변수는 클래스를 객체 생성후에 사용 가능.

필드(field)는 정적(static) 으로 지정할 수 있다.(클래스명.정적변수 형태로 접근)

**로컬 범위( local scope ):**

메서드안에서 선언된 변수. 선언된 블록내에서만 접근 가능.

```tsx
var global_num = 10; // 전역변수

class Numbers {
  num_val = 20; // 필드변수
  static s_val = 30; //static 변수

  xxx(): void {
    var local_num = 40; // 로컬변수
    console.log(global_num, Numbers.s_val); //전역, static 변수
  }
}

console.log(global_num); //10
console.log(Numbers.s_val); //30

var n = new Numbers();
var result = n.num_val; // 객체 생성 후 필드변수 접근가능
console.log(result); // 20
n.xxx(); // 10 30
```

# 연산자

```tsx
// 산술연산자
var num1: number = 10;
var num2: number = 3;
var res: number = 0;

res = num1 + num2;
console.log('+ : ', res);
res = num1 - num2;
console.log('- : ', res);
res = num1 * num2;
console.log('* : ', res);
res = num1 / num2;
console.log('/ : ', res, res.toFixed(2));
res = num1 % num2;
console.log('% : ', res); //1
```

```tsx
// 증감연산자
var n1: number = 10;
var n2: number = 3;

n1++; //n1 사용후 +1 증가
console.log('++ : ', n1); //11
n2--; //n2 사용후 -1
console.log('-- : ', n2); //2

var n3: number = 10;
var n4 = ++n3; //+1 증가 후 n3 사용
console.log('전치 ' + n3, n4);
var n5 = n3++;
console.log('후치 ' + n3, n5);
```

```tsx
// 비교연산자
var n1: number = 10;
var n2: number = 3;

console.log('n1==n2', n1 == n2); //f
console.log('n1!=n2', n1 != n2); //t
console.log('n1>n2', n1 > n2); //t
console.log('n1>=n2', n1 >= n2); // t
console.log('n1<n2', n1 < n2); // f
console.log('n1<=n2', n1 <= n2); //f
```

```tsx
// 논리연산자
var n1: number = 10;
var n2: number = 3;

console.log(n1 > n2 && 3 > 4); //false
console.log(n1 > n2 || 3 > 4); //true
console.log(n1 > n2, !(n1 > n2)); //true false
```

```tsx
// 대입연산자
var n1: number = 10;
var n2: number = 3;

n2 += n1;
console.log(n1, n2);
n2 -= n1;
console.log(n1, n2); // 10 -7
n2 *= n1;
console.log(n1, n2);
n2 /= n1;
console.log(n1, n2); // 10 0.3
n2 %= n1;
console.log(n1, n2); // 10 3
```

한줄씩 주석처리해서 결과확인

```tsx
// 삼항연산자
var n1: number = 10;
var n2: number = 3;

var n3: number = n1 > n2 ? 100 : 200;
console.log(n3); //100
```

```tsx
// typeof 사용
var n1: number = 10;
var test: string = 'abc';

console.log(typeof n1); //number
console.log(typeof test); //string
```

# if 조건문

```tsx
// 1. 단일 if 문
var n1: number = 5;
if (n1 > 0) {
  console.log('n is positive');
}

// 2. if~else 문
var n2: number = 12;
if (n2 % 2 == 0) {
  console.log('even');
} else {
  console.log('odd');
}
```

```tsx
// 3. 다중 if 문
var n3: number = 2;
if (n3 > 0) {
  console.log(n3 + ' is positive');
} else if (n3 < 0) {
  console.log(n3 + ' is negative');
} else {
  console.log(n3 + ' is 둘다아님');
}
```

```tsx
// 4. switch 문
var grade: string = 'A';
switch (grade) {
  case 'A': {
    console.log('굿');
    break;
  }
  case 'B': {
    console.log('bbb');
    break;
  }
  case 'C': {
    console.log('ccc');
    break;
  }
  case 'D': {
    console.log('poor');
    break;
  }
  default: {
    console.log('Invalid choice');
    break;
  }
}
```

# for 반복문

```tsx
// 1. for문
var num: number = 5;
var i: number;
var factorial = 1;

for (let i = num; i >= 1; i--) {
  factorial *= i;
}

console.log(factorial); // 120

// 2. while문
var num: number = 5;
var factorial: number = 1;
while (num >= 1) {
  factorial = factorial * num;
  num--;
}
console.log(factorial); // 120
```

```tsx
// 3. do~while문
var num: number = 10;
do {
  console.log(num);
  num--;
} while (num >= 0);
```

num이 0일 때까지 감소하며 출력

```tsx
// 4. for ~ in
var x: any = [1, 2, 3];
for (var x2 in x) {
  console.log(x2, x[x2]);
}

var xx: any = 'abc';
for (var x2 in xx) {
  console.log('>>', xx[x2]);
}
var xxx: any = { k1: 100, k2: 200, k3: 300 };
for (var x2 in xxx) {
  console.log('>>', x2, xxx[x2]);
}
```

배열에서 for~in 사용시 x2 변수가 인덱스에 해당한다. 객체에서는 키값에 해당.

```tsx
// 5. for ~ of
// 반복할 수 있는 대상은 반드시 iterable 객체만 가능하고 실제값 반환
var y: any = 'abc';
for (var y2 of y) {
  console.log(y2);
}

var yy: any = ['a2', 'b2', 'c2'];
for (var y2 of yy) {
  console.log(y2);
}

// {key:value} 형식에서는 for~of 안됨
var yyy: any = { k: 100, k2: 200, k3: 300 };
for (var y3 of yyy) {
  console.log(y3); // 출력안됨
}
```

객체는 iterable 객체가 아니기 때문에 for~of 사용 불가.

# function

```tsx
function greet(): string {
  //return type 명시
  return 'HEllo';
}

function caller() {
  var msg = greet();
  console.log(msg);
}
caller();
```

### Parameterized 함수

인자리스트가 일치해야 한다

a. Callby value

이 메소드는 인수의 실제 값을 함수의 형식 매개 변수로 복사한다.이 경우 함수 내의 매개 변수에 대한 변경 사항은 인수에 영향을 미치지 않음.

b. Call by pointer, reference

이 메소드는 인수의 주소를 형식 매개 변수에 복사한다.함수 내에서 주소는 호출에 사용 된 실제 인수에 액세스하는 데 사용된다. 즉, 매개 변수 변경 사항은 인수에 영향을 미친다.

```tsx
// 1. 기본 call by value
function test_param(n1: number, s1: string) {
  n1 = 200;
  console.log(n1); // 200
  console.log(s1); //string
}
var num = 100;
test_param(num, 'string');
console.log(num); // 100
```

```tsx
// 2. call by pointer
class Person {
  username: string;
  constructor(n) {
    this.username = n;
  }
  setUsername(n) {
    this.username = n;
  }
  getUsername() {
    return this.username;
  }
}

var p = new Person('홍길동');
function test_param2(pp: Person) {
  pp.setUsername('이순신');
}
test_param2(p);
console.log(p.getUsername()); // 이순신
```

```tsx
// 3. call by pointer 배열 예제
var str: string[] = ['홍길동', '이순신', '유관순'];
function changeName(s: string[]) {
  s[0] = '강감찬';
}
console.log('변경전', str);
changeName(str);
console.log('변경후', str);

/*
변경전 [ '홍길동', '이순신', '유관순' ]
변경후 [ '강감찬', '이순신', '유관순' ]
```

### Optional Parameters ( 선택적 매개변수)

이름에 물음표(?)를 추가하여 매개 변수를 선택적으로 표시 가능

선택적 매개 변수는 함수의 마지막 인수로 설정 해야 함.

값을 전달하지 않으면 undefined로 설정됨

```tsx
function test_param(n1: number, s1: string, s2?: string) {
  console.log(n1);
  console.log(s1);
  console.log(s2);
}

test_param(123, 'string');
test_param(123, 'string', 'hello');
```

```tsx
function test_param2(x, y, ...n: string[]) {
  console.log(x, y, n);
}
test_param2(1, 2, 'aaa', 'bbb', 'ccc');
test_param2('a', 'b', 'aaa', 'bbb', 'ccc');

/*
1 2 [ 'aaa', 'bbb', 'ccc' ]
a b [ 'aaa', 'bbb', 'ccc' ]
```

### default Parameters ( 기본 매개변수 )

```tsx
function calculate_discount(price: number, rate: number = 0.5) {
  var discount = price * rate;
  console.log('discount Amount ' + discount);
}
calculate_discount(1000); // 500
calculate_discount(1000, 0.3); // 300
```

### 람다함수

```tsx
// 1. 함수 표현식 이용
var a = function () {
  console.log('a');
};
a();

// 람다 표현식
var a2 = () => console.log('a2');
a2();
```

```tsx
// 1. 함수 표현식 이용
var a = function (x: number) {
  console.log('a' + x);
};
a(10);

// 람다 표현식
var a2 = (x: number) => console.log('a2' + x);
a2(10);

// 파라미터가 1개면 ()생략 가능
var a3 = x: number => console.log('a3', x);
a3(10);
```

### 오버로딩

인자 리스트가 다르고 함수명이 동일한 것을 ‘오버로딩 함수‘ 라고 부른다.

```tsx
// 1. 함수선언
function disp(n: number): void;
function disp(n: number, s: string): void;
function disp(n: number, s: string, n2: number): void;

// 2. 함수 정의
function disp(n: number, s?: string, n2?: number): void {
  console.log(n, s, n2);
}

// 3. 함수 호출
disp(100);
disp(100, 'aa');
disp(100, 'hello', 200);
```

```tsx
// 갯수가 같지만 타입이 다른 경우
// 1. 선언
function xxx(n: number): void;
function xxx(n: string): void;
// 2. 정의
function xxx(n: any): void {
  console.log(n);
}
xxx(10);
xxx('20');
```

```tsx
// 1. 함수선언
function disp(n: number): void;
function disp(s: string): void;
function disp(n: number, s: string): void;
function disp(s: string, n: number): void;

// 2. 함수 정의
function disp(n: any, s?: any): void {
  console.log(n, s);
}

// 3. 함수 호출
disp(100); // 100 undefined
disp('홍길동'); // 홍길동 undefined
disp(100, '200'); // 100 200
disp('aa', 200); // aa 200
```

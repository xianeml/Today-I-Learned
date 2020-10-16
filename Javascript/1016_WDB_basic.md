# js basic

wdb 새로 업뎃된거 복습

# Numbers

only one type

제곱은 2\*\*4 = 16 이렇게 표현

NaN : not a number

# Strings

strings are indexed

indices = index의 복수형

# Template Literals

자바스크립트 표현식 사용해서 문자열 연결

백틱이랑 \${} 두개를 사용. 저 중괄호 안엔 변수사용이나 자바스크립트 코드 줌.

문자열과 변수 연결할 때 유용

```jsx
function greet(name){
	return 'Hi, ${name.toUpperCase()}!`;
}

greet('Leo');
```

url 입력할 때 이거 사용하면 유용

저렇게 간단한 변환이 아니라 대규모 변환이 필요하면 외부에서 처리하고 결괏값 변수 저장해서 템플릿 코드에서 사용

# Math.pow(2,3);

제곱해줌 2\*\*3

# array

push - add to end 끝

pop - remove from end 끝

shift = remove from start 첫

unshift - add to start 첫

const로 만든 배열을 수정하는건 가능한데 배열 자체를 통째로 다른 배열로 만드는건 안됨

# for ... of

파이썬 for ~in 이랑 똑같음

for~in은 객체에서 사용

# lexical scope

'어휘상의' - 그 변수가 소스코드 내 어디에서 선언되었는지 고려한다는 것을 의미

중첩함수에서 이너는 외부 변수 접근 가능, 외부는 이너변수 접근 불가. 당연하게도 이너변수는 이너에서 사용되고 사라지니까.

# higher order functions

일급함수 :다른 함수의 인자로 사용가능, 함수 리턴가능

```jsx
function callTwice(func) {
  func();
  func();
} //함수 받아서 실행해주는 함수

function rollDie() {
  const roll = Math.floor(Math.random() * 6) + 1;
  console.log(roll);
}

callTwice(rollDie); //함수 보내주기
```

--

### 일급

: 값으로 다룰수있다

- 변수에 담을 수 있다
- 함수나 메소드의 인자로 넘길 수 있다
- 함수나 메소드에서 리턴할 수 있다

자바스크립트에서 모든 값은 일급이다

모든 객체는 일급객체이며 함수도 객체이자 일급객체

일급함수

- 아무때나(런타임에서도) 선언가능
- 익명선언가능
- 익명선언한것도 함수나 메소드 인자로 넘길 수 있다👇

```jsx
function callAndAdd(a, b) {
  return a() + b();
}

callAndAdd(
  function () {
    return 10;
  },
  function () {
    return 5;
  }
);
```

저 함수 호출할 때 익명함수 두개 선언했고 그게 바로 인자로 넘어가서 리턴값 실행. 이렇게도 되는구나

객체는 메소드를 갖고있잖아. 객체 사용하기 위한 메소드

근데 함수는 자기 자체가 기능이야

쉽게 참조하고 전달 실행 가능

--

# returning functions, Defining methods

함수를 호출하지 않았지만 리턴으로 함수를 실행함

나중에 다시듣자

# this

this 값은 함수가 호출된 맥락에 따라 달라짐.

객체 안에서 this는 지 객체를 가리킴.

window - 빌트인 객체

# Map

```jsx
const titles = movies.map(function(movie) {
	return movie.title;
});⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
```

```jsx
let cleanNames = function (arr) {
  return arr.map(function (item) {
    //리턴 중요!
    return item.trim();
  });
};
```

cleanNames() 호출해서 사용하려면 그 함수가 리턴하는 값이 있어야한다.

# arrow function

more compact: remove return keyword!

```jsx
const rollDie = () => (
	Math.floor(Math.random() * 6) + 1;
)
```

(이 한줄)을 리턴할거다

```jsx
const add = (a, b) => a + b;
```

() 이거 안쓰고 인라인 쓰기도 가능.

# setTimeout, setInterval

실행 딜레이

# every(), some()

불리언 메소드

every : 모든애가 테스트 통과하면 트루

some: 테스트 통과하는애 하나라도 있으면 트루

테스트 코드 작성

```jsx
let allEvens = (arr) => arr.every((num) => num % 2 === 0);
```

# reduce()

accumulator 누산기: 연산결과 임시저장소

다시보자.

# arrow function and 'this'

화살표함수안에 있는 키워드 this는 그 함수가 만들어진 스코프의 this 와 같다

--
화살표 함수는 일반 함수와는 달리 ‘고유한’ `this`를 가지지 않습니다. 화살표 함수에서 `this`를 참조하면, 화살표 함수가 아닌 ‘평범한’ 외부 함수에서 `this` 값을 가져옵니다.

아래 예시에서 함수 `arrow()`의 `this`는 외부 함수 `user.sayHi()`의 `this`가 됩니다.

별개의 this가 만들어지는 건 원하지 않고, 외부 컨텍스트에 있는 this를 이용하고 싶은 경우 화살표 함수가 유용합니다.

--

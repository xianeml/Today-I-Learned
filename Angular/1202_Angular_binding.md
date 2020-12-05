# 바인딩

컴포넌트는 화면 구현을 담당하는 template과 비즈니스로직을 담당하는 컴포넌트 클래스 간의 상호 작용을 위한 방법으로 바인딩(binding)을 이용한다.

## 단방향{{}}

: 인터폴레이션 단방향 호출

컴포넌트 클래스의 데이터를template의 html에게 전달할 때 사용된다. 메소드도 호출 가능함

app.component.ts:

```tsx
export class AppComponent {
  title = '단방향 {{}}, 인터폴레이션 바인딩실습';
  name = '홍길동';
  age = 20;
  address = '서울';
}
```

app.component.html:

```tsx
<h1>{{ title }}</h1>;
이름: {
  {
    name;
  }
}
<br />;
나이: {
  {
    name;
  }
}
<br />;
주소: {
  {
    name;
  }
}
<br />;
```

src_4-2_binding_user

```tsx
export class AppComponent {
  title = '바인딩 실습';
  user = {
    name: '홍길동',
    age: 20,
    address: '서울',
  };
}
```

속성에 객체 사용

```tsx
<h1>{{ title }}</h1>;
{
  {
    user.name;
  }
}
{
  {
    user.age;
  }
}
{
  {
    user.address;
  }
}
```

객체접근

### 타입스크립트 적용

4-3_person

app/person.ts:

```tsx
export class Person {
  constructor(
    public name: string,
    public age: number,
    public address: string
  ) {}
}
```

app.component.ts

```tsx
import { Component } from '@angular/core';
import { Person } from './person';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'my-app';
  user: Person = {
    name: '홍길동',
    age: 20,
    address: '서울',
  };
}
```

import 후 Person타입으로 user 객체 작성

4-4 book

```tsx
<h1>books</h1>
<app-book></app-book>
```

```tsx
@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css'],
})
export class BookComponent {
  //implements OnInit 삭제 또는 //ngOnInit():void 구현
  titleName = '도서목록';
  books = [
    {
      id: 'p01',
      name: '위험한 식탁',
      price: 2000,
      date: '20190401',
      img: 'a.jpg',
    },
    {
      id: 'p01',
      name: '위험한 식탁',
      price: 2000,
      date: '20190401',
      img: 'a.jpg',
    },
    {
      id: 'p02',
      name: '공부의 비결',
      price: 3000,
      date: '20190401',
      img: 'b.jpg',
    },
    {
      id: 'p03',
      name: '오메르타 ',
      price: 2500,
      date: '20190401',
      img: 'c.jpg',
    },
    {
      id: 'p04',
      name: '행복한 여행',
      price: 4000,
      date: '20190401',
      img: 'd.jpg',
    },
    {
      id: 'p05',
      name: '해커스 토익',
      price: 2000,
      date: '20190401',
      img: 'e.jpg',
    },
  ];

  getTitleName() {
    return this.titleName;
  }
}
```

```tsx
<h1>{{ getTitleName() }} {{ books.length }}권</h1>
<ul>
  <li *ngFor="let book of books">
    <!-- directive -->
    <img src="assets/image/{{ book.img }}" width="100" height="100" />
    {{ book.name }}
  </li>
</ul>
```

### 인터페이스 만들기

`ng g interface book/book`

book 폴더 경로 밑에 book 인터페이스 만들어주는 명령어

book.ts:

```tsx
export interface Book {
  id: string;
  name: string;
  price: number;
  data: string;
  img: string;
}
```

book.component.ts:

```tsx
import { Book } from './book';
```

임포트부터

```tsx
export class BookComponent {
  //implements OnInit 삭제 또는 //ngOnInit():void 구현
  titleName = '도서목록';
  books: Book[] = [
```

어제했던거에서 타입을 Book 인터페이스 형태로 바꿔줌

app.module.ts:

```tsx
@NgModule({
  declarations: [
    AppComponent,
    BookComponent
  ],
```

book.component.html:

```tsx
<h1>{{ getTitleName() }} {{ books.length }}권</h1>
<ul>
  <li *ngFor="let book of books">
    <!-- directive -->
    <img src="assets/image/{{ book.img }}" width="100" height="100" />
    {{ book.name }}
  </li>
</ul>
```

### [속성] 바인딩

`[속성명] = "변수명"`

태그 안에 속성에 [] 묶어주면 속성값으로 이걸 쓰게됨. 속성값은 클래스에 있는 변수 이름이다.

컴포넌트 클래스의 데이터를template인 HTML태그의 특정 **속성값으로 전달**할 때 사용된다.

app.component.ts:

```tsx
export class AppComponent {
  title = '속성 바인딩 실습';
  imgName = 'assets/image/a.jpg';
  imgWidth = 200;
  imgHeight = 200;
}
```

이 변수명을 html에서 속성값으로 사용하면 바인딩이 된다.

app.component.html

```html
<h1>{{title}}</h1>
다음 이미지의 파일명과 width/height 값을 속성 바인딩으로 설정한다.<br />
<img [src]="imgName" [width]="imgWidth" [height]="imgHeight" />
```

## class 바인딩

`[class.CSS클래스명]=boolean값`

CSS 스타일을 적용할지 여부를 결정할 수 있다. true인 경우에 CSS 스타일이 적용된다.

app.component.css

```css
ul {
  list-style: none;
}
.font-red {
  color: red;
}
.font-blue {
  color: blue;
}
```

```tsx
<h1>{{ title }}</h1>
<ul>
  <li>css적용됨</li>
</ul>
<p [class.font-red]="true">홍길동</p>
<p [class.font-blue]="true">이순신</p>
<p [class.font-red]="result">유관순</p>
```

클래스명과 불리언값 지정

result 속성값은 컴포 클래스에서 받아옴

false 설정하면 적용안됨

```tsx
export class AppComponent {
  title = 'my-app';
  result = true;
}
```

## 이벤트 바인딩

`(이벤트명)="callback()"`

이벤트 명을 괄호로 묶고 뒤엔 콜백함수 호출

컴포넌트 클래스의 메서드가 콜백으로 호출된다.

```tsx
export class AppComponent {
  title = '이벤트 바인딩 실습';
  handleEvent(): void {
    console.log('handleEvent');
  }
  handleEvent2(name: string): void {
    console.log('handleEvent2===', name);
  }
}
```

```html
<h1>{{ title }}</h1>
<button (click)="handleEvent()">이벤트처리</button>
<button (click)="handleEvent2('홍길동')">이벤트처리2</button>
```

```tsx
export class AppComponent {
  title = '이벤트 바인딩 실습';
  handleEvent(event): void {
    console.log('handleEvent====', event);
  }
  handleEvent2(event, name: string): void {
    console.log('handleEvent2====', event, '\t', name);
  }
}
```

```html
<h1>{{title}}</h1>
<button (click)="handleEvent($event)">이벤트처리</button>
<button (click)="handleEvent2($event, '홍홍')">이벤트처리</button>
```

이벤트 객체 전달은 $event 사용

### 이벤트-체크박스, select

input

```html
<h1>{{ title }}</h1>
<h1>input 실습</h1>
<input #phone placeholder="phone number" />
<!--id지정 -->
<button (click)="callPhone(phone.value)">Call</button>
```

```tsx
export class AppComponent {
  title = 'template reference variable #var 실습';
  flag = false;
  callPhone(phone: number): void {
    console.log(phone);
  }
}
```

플래그는 체크박스 쓸 때 사용

```tsx
<h2>select 실습</h2>
<select #fruit (change)="change(fruit.value)">
  <option>바나나</option>
  <option>사과</option>
  <option>옥수수</option>
  <option>고구마</option>
</select>
```

```tsx
change(v:string) {
  console.log(v);
}
```

checkbox

```tsx
flag = false; // 전체선택 checkbox 상태값 설정
check(m: boolean) {
  console.log(m);
  this.flag = m;
}
```

```html
<h2>checkbox 실습</h2>
전체: <input type="checkbox" #xxx (click)="check(xxx.checked)" /><br />
야구: <input type="checkbox" value="야구" [checked]="flag" /><br />
축구: <input type="checkbox" value="축구" [checked]="flag" /><br />
농구: <input type="checkbox" value="농구" [checked]="flag" /><br />
```

체크 되었냐 여부 속성은 컴포넌트 클래스의 flag 변수값을 받아온다. 모두 일단 false 되어있음,

이제 전체선택을 클릭하면 check함수 호출. ture 전송. 체크함수는 트루 받아서 플래그값도 트루로 변경해줌.

그럼 플래그를 사용하던 애들도 전부 true가 되기때문에 전체선택이 작동하게됨.

## 양방향 바인딩

`[(ngModel)]=“변수명”;`

template과 컴포넌트 클래스간에 양방향(two-way) 바인딩 처리 가능. template은사용자입력을처리할수 있는위젯을사용한다.

app.module.ts:

앱컴포넌트가 사용하는 모듈들이 등록되어있음

```tsx
import { FormsModule } from '@angular/forms'; //양방향 바인딩을 위한 import
```

```tsx
@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    FormsModule // 사용
  ],
```

```jsx
export class AppComponent {
  title = '양방향 바인딩 실습';
}
```

```tsx
<h1>{{ title }}</h1>
<!-- app.module.ts에 FormsModule 필요 -->
입력: <input type="text" [(ngModel)]="title" />
```

인풋에 입력한 값을 컴포넌트 클래스의 title 속성에 바로 바인딩해주고있음.

실습예제1

```tsx
<h1>{{title}}</h1>
<button (click)="handleEvent($event)">Angular</button>
<button (click)="handleEvent($event)">jQuery</button>
<button (click)="handleEvent($event)">Angular</button>
선택한 버튼 라벨값: {{label}}
```

```tsx
export class AppComponent {
  title = '이벤트 바인딩 실습예제1';
  label = '';
  handleEvent(event: any) {
    this.label = event.target.innerText;
  }
}
```

event.target.innerText 사용해서 라벨값 넘겨주기.

라벨속성을 사용해 화면에 단방향 바인딩

실습예제2

```tsx
.input {
  background-color: yellow;
}
```

```tsx
<h1>{{title}}</h1>
아이디:
<input type="text" (focus)="handleEvent(true)" (blur)="handleEvent(false)"
[class.input]="flag">
```

blur이벤트는 focus를 잃었을 때 발생함.

```tsx
export class AppComponent {
  title = '이벤트 바인딩 실습2, class 바인딩';
  flag = false;
  handleEvent(m: boolean) {
    this.flag = this.flag;
  }
}
```

실습예제3

```html
<h1>{{ title }}</h1>
아이디:
<input type="text" (keyup)="handleEvent($event)" /><br />
입력데이터: {{ label }}<br />
입력데이터 길이: {{ len }}
```

```tsx
export class AppComponent {
  title = '이벤트 바인딩 실습예제3';
  label = '';
  len = '';
  handleEvent(event: any) {
    this.label = event.target.value;
    this.len = event.target.value.length;
  }
}
```

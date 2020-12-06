### 실습문제4 bookSearch

검색어 입력시 일치하는 목록 반환

```jsx
<h1>{{ title }}{{title.length}}권</h1>
검색: <input type="text" #xyz (keyup)="searchName(xyz.value, $event)">
<h2>클릭한 도서목록</h2>
<ul>
  <li *ngFor="let book of booksResult">
    <!-- directive -->
    <img src="assets/image/{{ book.img }}" width="100" height="100" />
    {{ book.name }}
  </li>
</ul>
```

```jsx
export class BookComponent {
  title = '도서목록';
  booksResult = []; // 검색된 배열을 담을 배열
  constructor() {
    for (var book of this.books) {
      this.booksResult.push(book); // 배열에 저장
    }
  }
  books: Book[] = [
    //interface의 배열 타입선언
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
      date: '20170402',
      img: 'b.jpg',
    },
    {
      id: 'p03',
      name: '오메르타',
      price: 2500,
      date: '20170401',
      img: 'c.jpg',
    },
    {
      id: 'p04',
      name: '행복한 여행',
      price: 4000,
      date: '20170401',
      img: 'd.jpg',
    },
    {
      id: 'p05',
      name: '해커스 토익',
      price: 2000,
      date: '20170401',
      img: 'e.jpg',
    },
    {
      id: 'p06',
      name: '도로 안내서',
      price: 2000,
      date: '20170401',
      img: 'f.jpg',
    },
  ];
  getTitleName() {
    return this.title;
  }

  searchName(keyword, event) {
    // 검색어 입력시
    //var searchName = event.target.value;
    var searchName = keyword;
    this.booksResult = []; // 초기화 후 검색결과 저장
    if (searchName == '') {
      for (var book of this.books) {
        this.booksResult.push(book);
      }
    } else {
      for (var book of this.books) {
        console.log('실행된 검색어 ', searchName);
        if (book.name.indexOf(searchName) != -1) {
          // 검색어가 있다면 // 검색어가없을때 -1이나온다. 포함된게없단뜻
          this.booksResult.push(book);
        }
      }
    }
    console.log(this.booksResult);
  }
}
```

### 실습문제5

app.module.ts

```tsx
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, FormsModule],
```

formsmodule 추가

```html
<h2>{{ title }}</h2>
<br />
<select [(ngModel)]="fruit">
  <option>바나나</option>
  <option>딸기</option>
  <option>사과</option></select
><br />
선택한 과일: {{ fruit }}
```

이 셀렉트 밸류값으로 바로 fruit 바인딩

```tsx
export class AppComponent {
  title = '좋아하는 과일을 선택하세요';
  fruit = '딸기';
}
```

component.ts랑 소통하는게 아니라 html에서 요소와 직접 소통.

# ppt5강 - Component 분리

중첩컴포넌트 사용해 레이아웃 작성시 부모와 자식간 데이터 전송 복잡해짐

부모 컴포넌트------→ 자식 컴포넌트로 데이터 전송:  
`@Input() +속성`

자식 컴포넌트------→ 부모 컴포넌트로 데이터 전송: 
`@Output() + 이벤트(EventEmitter)`

### @Input() + 속성1

```html
<h1>부모컴포넌트</h1>
<h3>다음은 자식 컴포넌트 입니다.</h3>
<app-child username="홍길동" userage="20"></app-child>
```

부모컴포에서 자식 선택자 적어주면서 전달할 데이터를 속성과 값으로 적어준다.

```tsx
export class ChildComponent implements OnInit {
  title = '부모 컴포넌트에서 데이터 전달';
  @Input() username: string;
  @Input() userage: number;

  constructor() {}

  ngOnInit(): void {}
}
```

자식은 그 데이터를 받기위해 @Input() 사용해서 속성이름 그대로 써줘서 받으면 된다.

```tsx
error TS2564: Property 'username' has no initializer and is not definitely assigned in the constructor.
```

username! 을 해보자. —> 느낌표 붙여서 해결!

userage 에러 —> age를 string 타입으로 받아야 해결된다.

### @Input() + 속성2 // [전달할 속성명]=“클래스변수명"

```tsx
export class AppComponent {
  title = 'my-app';
  app_username = '홍길동';
  app_userage = 20;
}
```

```html
<h1>부모컴포넌트</h1>
<h3>다음은 자식 컴포넌트입니다.</h3>
<app-child [username]="app_username" [userage]="app_userage"></app-child>
<!-- app_userage, app_username 클래스 속성을 속성과 속성값으로 child에게 전달함-->
```

```tsx
export class ChildComponent implements OnInit {
  title = '부모 컴포넌트에서 데이터 전달';
  @Input() username!: string;
  @Input() userage!: number;

  constructor() {}
  ngOnInit(): void {}
}
```

```tsx
<p>child works!</p>;
이름: {
  {
    username;
  }
}
<br />;
나이: {
  {
    userage;
  }
}
```

### 3 @Input 속성바인딩

```tsx
export class AppComponent {
  title = 'my-app';
  app_friends = ['홍길동', '이순신', '유관순'];
}
```

```tsx
<h1>부모 컴포넌트</h1>
<h3>다음은 자식 컴포넌트입니다.</h3>
<app-child [friends]="app_friends"></app-child>
<!-- app_userage, app_username 클래스 속성을 속성과 속성값으로 child에게 전달-->
```

```tsx
export class ChildComponent implements OnInit {
  @Input() friends!: string[];
  constructor() {}
  ngOnInit(): void {}
}
```

```tsx
<div *ngFor="let friend of friends">
    {{friend}}
</div>
```

### 4 @Output+이벤트

자식 컴포넌트에서 부모 컴포넌트로 데이터를 전달할 때 사용하는 방법

자식은 사용자 정의 이벤트와 @Output을 사용하여 부모에게 데이터를 전달하고 부모는 template의 속성에 지정된 이벤트를 사용하여 데이터를 이용할 수 있다.

```tsx
<p>child works!</p>
<button (click)="send('홍길동')">부모에게 데이터 전송</button>
```

```html
<h1>부모컴포넌트</h1>
<h3>다음은 자식컴포넌트입니다.</h3>
<app-child (customEvent)="handleEvent($event)"></app-child>
<h3>자식에게서 전달받은 데이터는</h3>
{{response}}
```

```tsx
export class AppComponent {
  title = 'my-app';
  response = '';
  handleEvent(event: any) {
    this.response = event;
  }
}
```

```tsx
export class ChildComponent implements OnInit {
  //부모에게 사용자 정의 이벤트 전달할 EventEmitter 객체
  @Output() customEvent = new EventEmitter();
  send(name: any) {
    this.customEvent.emit(name); // 부모에게 데이터 전달
  }

  constructor() {}

  ngOnInit(): void {}
}
```

1. 자식에서 button 클릭 ->
2. 이벤트 핸들러에 데이터 전송: `send(홍길동)` ->
3. 부모이벤트에 데이터 전달하기: `this.customEvent.emit('홍길동');` ->
4. 자식에서 발생한 이벤트 캐치해서 핸들러에 전달: `(customEvent)=handleEvent($evnet)` ->
5. 응답할 변수값을 받아온 데이터로 할당:`response = event` ->
6. 메세지 띄워주기: `{{response}}`

### 실습문제1 input_book

부모 컴포넌트인 app.component.ts 파일에서 books 데이터를 저장하고 자식 컴포넌트인 book.component.ts에 전달하여 출력한다.

```tsx
export class AppComponent {
  title = '도서목록'; //자식에게 전송
  books = [
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
      date: '20170402',
      img: 'b.jpg',
    },
    {
      id: 'p03',
      name: '오메르타',
      price: 2500,
      date: '20170401',
      img: 'c.jpg',
    },
    {
      id: 'p04',
      name: '행복한 여행',
      price: 4000,
      date: '20170401',
      img: 'd.jpg',
    },
    {
      id: 'p05',
      name: '해커스 토익',
      price: 2000,
      date: '20170401',
      img: 'e.jpg',
    },
    {
      id: 'p06',
      name: '도로 안내서',
      price: 2000,
      date: '20170401',
      img: 'f.jpg',
    },
  ];
}
```

```tsx
<app-book [bookList]="books" [title]="title"></app-book>
```

```tsx
export class BookComponent {
  @Input() bookList!: [];
  @Input() title!: string;
}
```

```html
<h1>{{ title }} {{ bookList.length }}권</h1>
<ul>
  <li *ngFor="let book of bookList">
    <img src="assets/image/{{ book.img }}" />{{ book.name }}
  </li>
</ul>
```

# 리액트 세팅, 컴포넌트, props, state

npx는 공간 사용 덜한다. 

일단 전역에 리액트 사용가능하게 `npm install -g create-react-app` 세팅

폴더 만들어서 그 폴더에서 터미널 열어서 `create-react-app`  

폴더 구조는 보여지는 html 을 담고있는 퍼블릭폴더와

컴포넌트 자료들을 갖고있는 src폴더로 나뉜다.  

  

```java
<div id="root"></div>
```

인덱스 html에서 루트 아이디 있지 

```jsx
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

그걸 index.js에서 리액트돔 렌더 함수 안에 셀렉트하고있음. 사용자정의태그 app이 보일거야. 컴포넌트 실제 구현은 임포트 통해서 앱 파일 불러옴. index.js, app.js 는 같은 src폴더 안에 있다.  

컴포넌트 클래스는 대문자로 시작. 컴포넌트 상속받고

안에 렌더 함수 있어야한다. 자바스크립트 함수는 function 키워드 쓰잖아 근데 최신js는 클래스 안에 함수에 펑션키워드 생략함. 리턴할 태그를 넣어주면 된다.

컴포넌트 안에는 하나의 최상위 태그가 있어야됨. div나 header나 

```jsx
class Subject extends Component {
  render(){
    return (
      <header>
        <h1>WEB</h1>
        world wide web!
      </header>
    );
  }
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <Subject />
      </div>
    );
  }
}
```

위에서 만든 컴포넌트를 앱 컴포넌트 안에 app div 안에 사용자정의 태그로 클래스 이름 써주면 화면에 딱 나타난다.

# props

이제 내 맘대로 태그 만들었는데 그 태그 사용하면서 속성을 맘대로 바꿔주고싶음.

내가 원하는 대로 태그를 만들었잖아 이제 이 태그를 사용할 때 내가 직접 속성을 아무거나 다양하게 주고 싶어
서브젝트 컴포넌트로 가서 타이틀을 웹으로 바꿔 주고 싶은 거지 그럼 타이틀 쓰고 있는 H 원으로 가서 거기에다가 웹으로 바꾼 내용을 이 컴포넌트가 받아 줘야 돼 그러니까 여기서 그 문법을 사용하려면 일단은 자바스크립트 문법을 사용해야되고 HTML 태그안에서 자바스크립트가 들어갈려면 { 작성하고 그 안에 this. 안에서 프로퍼티를 선택하고 거기에서 타이틀을 골라서 중괄호 닫아 주면 이제 내가 태그에서 지정한 속성을이 원래 태그가 받을 수 있는 거야

태그는 어트리뷰트(속성)을 갖는다. 같은 태그라는 공통점, 속성이라는 차이점을 줄 수있다.

```jsx
<Subject title="WEB" sub="world wide web!" />
```

이걸 이렇게 속성을 주고싶어. 지금 이렇게 속성을 준 것 자체도 내가 사용자정의 속성을 준거야 이런 속성이 이름은 원래 없지

```jsx
<header>
  <h1>{this.props.title}</h1>
  {this.props.sub}
</header>
```

html태그 안에 자바스크립트 사용하려면 {}중괄호 사용해야된다

내부적으로 훨씬 효과적으로 바뀜. 리팩토링됨.

```jsx
<Subject title="react" sub="for ui" />
```

위에서 서브젝트 컴포넌트 클래스 하나 만들어놨지.

그걸 이제 앱 컴포넌트에서 사용자정의 태그로 마구 찍어낼수 있어. 이 태그 안에서 다른 속성을 부여할 수도 있고. 서브젝트 컴포는 사용자정의태그가 무슨 속성을 지알아서 만들던 그냥 this.props.속성이름 으로 받아오기만 하면 된다. 틀만 주면 됨.

# 컴포넌트 분리

src안에 components 폴더에 각각 만들어줌.

한거번에 한 파일에 만들어둔  컴포넌트를 하나의 컴포넌트 파일들로 일 일이 분리를 시켜줄거야

분리 시켜주려고 컴포넌트 하나를 새 파일에 옮겨 왔어 근데 아직 실행이 안 돼 이 컴포넌트를 로딩 해 줄 수 있는 기능을 가져와야 돼

```jsx
import React, { Component } from 'react';
```

```jsx
export default TOC;
```

임포트와 익스포트하면 외부에서 사용 가능

이제 이 컴포넌트를 외부에서 사용할 수 있어 앱 컴포넌트에 가서 위에 임 포트로 T O C를 불러와서  from 뒤에 T O C 의 주소를 적어 주면 돼

# state

props가 사용자가 제품 조작하는 인터페이스 역할. 컴포넌트 사용에 필요

만드는 사람은 내부적인 매커니즘 구현, 스테이트. 컴포넌트 프랍스 값에 따라 내부 구현에 필요한것

컴포넌트 요리조리 바꾸고싶을때 프롭스 사용. 사용자는 컴포넌트 내부에 사용되는 것들(스테이트)을 알필요없다. 얘네 둘은 철저히 분리되어있어야한다.

props값이 **하드코딩** 되어 있다?

```jsx
하드 코딩 : 소스 코드 안에 데이터를 직접 작성.
값이 계속 바뀌면 일일이 수정하기 힘들어.
```

constructor 함수는 렌더함수보다 먼저실행됨. 가장먼저 초기화시켜줄 애들은 이 안에 작성한다. 

```jsx
this.state = {}
```

이걸로 스테이트를 초기화함

이렇게 하면은 데이터를 그대로 하드 코딩해서 드러낼 필요 없이 변수에 담는 것처럼 활용 할 수 있어

```jsx
this.state = {
      subject:{title:"WEB", sub:"world wide web!"}
    }
```

일단 서브젝트라는 프로퍼티를 만들어서 스테이트화 할거임. 

```jsx
<Subject 
        title={this.state.subject.title} 
        sub={this.state.subject.sub} />
```

짠

index.js에는 

```jsx
ReactDOM.render(
    <App />,
  document.getElementById('root')
);
```

앱이 어떻게 생겼는지 뭘 갖고있는지 알수없다. 철저히 내부정보를 은닉하는거

좋은 사용성 만드는 핵심이다. 전선이 빠져나온 핸드폰을 누가 좋아하겠나

내부적으로 사용하는건 스테이트를 사용한다.

 

이렇게 상위 컴포넌트인 App의 스테이트를 하위 컴포넌트 subject에 전달하고 싶을 땐 상위컴포넌트의 스테이트를 `{this.state.subject.title}` 하위 컴포넌트 프랍스(속성)값으로 전달하는게 가능해진다.

toc 스테이트 만들어서 전달

```jsx
contents:[
        {id:1, title:'html', desc:'html is for info~'},
        {id:2, title:'CSS', desc:'CSS is for info~'},
        {id:3, title:'JS', desc:'JS is for info~'},
        
      ]
```

컨텐츠라는 프로퍼티 추가. 데이터가 여러개면 대괄호로 배열을 만들어서 그 안에 각각 객체 써서 사용,

```jsx
<TOC data={this.state.contents}/>
```

```jsx
class TOC extends Component {
    render() {

      var lists = [];
      var data = this.props.data;
      var i = 0;
      while(i < data.length){
      lists.push(<li key={data[i].id}><a href={"/content/"+data[i].id}>{data[i].title}</a></li>)
        i = i + 1;
      }
```

여러게 요소를 자동으로 생성 하는 경우에는 키 프로퍼티를 부여해주라는 에러가 떠. 그래서 식별자로 li태그 안에 리스트 키 아이디값을 줬다.

근데 contens 프로퍼티도 아니고 /content/는 어디서 나온거지?

```jsx
return (
        <nav>
          <ul>
            {lists}
          </ul>
        </nav>
      )
```

배열 갖다놓기


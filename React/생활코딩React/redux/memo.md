# 리덕스

하나의 상태를 갖는다. 상태는 그냥 객체다.

하나의 객체 안에 앱에서 필요한 모든 데이터를 넣는다.

여러곳에 흩어져있는것보다 훨씬 데이터관리가 쉬워진다.

이 상태는 중요하기때문에 외부로부터 철저히 차단.

디스패쳐, 리듀서라는 함수만 접근권한을 갖는다. 내가 직접 스테이트 값을 바꾸지 못해.

데이터를 가져올때도 getState를 통해서만 가져올수있어

스테이트가 바뀌든 말든 그 스테이트 사용하는 애들은 자기일만 하면 된다.

데이터를 바꿀때 원본을 건들이지않음. 원본 복제해서 바꿈. 각각의 상태변화가 서로에게 영향을 주지 않는다

그리고 이전의 상태까지도 꼼꼼하게 레코딩한다

## 전체적인 흐름 파악하는게 중요

store에 모든 정보가 저장된다.

이 안에는 state에 실제 정보가 저장된다. 직접 접근 불가능

스테이트에 접근하기 위해서 거쳐야할 과정이있다.

스토어를 데이터를 가진 은행이라고 보면 데이터 얻기위해 은행앞에서 많은 은행원과 처리과정을 거쳐야하는것.

store를 만들면서 reducer도 만들어야한다.

```jsx
var store = Redux.createStore(reducer);
```

리덕스 만들기

렌더는 스토어 밖에 있다. 리덕스랑 상관없이 내가 짜는 코드

UI만들어주는 역할

렌더는 언제나 스테이트 값 참조해서 html ui를 만든다.

스테이트 바뀔때마다 render 호출하면 알아서 ui 갱신해주면 좋겠지

그 때 사용하는게 subscribe

값이 변경되었을 때 구동할 함수를 등록해주는 역할

스토어에 렌더함수를 구독해놓으면 스테이트 바뀔때마다 렌더 호출하면서 ui 갱신 가능

# action과 reducer

onsubmit 이벤트 발생하면 스토어에 디스패치로 객체를 하나 보내는데

type이 create 이다. 이건 액션을 의미함

이 객체가 액션이고 얘를 디스패치에게 전달한다.

디스패치는 리듀서를 호출해서 스테이트 값 바꾸고 subscribe 통해서 렌더함수 호출함

dispatch가 reducer호출할 때 두 개의 값을 전달함

1. 현재값
2. 액션데이터

이렇게 코드 가공해서 리턴을 해주는데 리턴하는 객체는 스테이트의 새로운 값이 된다.

리듀서는 스테이트 가공자다.

이제 렌더가 다시 호출되어야돼. 바뀌었으니까

디스패치가 구독자 다 호출함. 렌더도 호출되면서 렌더 역할 실행

겟스테이트 하고 가져와서 화면에 갱신.

이제 새로운 스테이트에 맞게 ui가 바뀐다!

이게 리덕스가 동작하는 흐름이다

# 리덕스를 쓰면 좋은 이유

부품은 독립성이 있어야한다. 어디에 갖다놔도 작동해야됨

리덕스 상태관리 툴은 액션이 발생할때마다 다 기록함. 영상으로 재생도됨

현재 상태를 제이슨으로 다운받아서 임포트하면 복원가능

중앙집중적 상태관리, 상태기록 등 놀라운 기능이 많다

# without-redux 파일에 redux 적용

redux cdn 적용 가능하다.

```jsx
function reducer(state, action) {
  if (state === undefined) {
    return { color: "yellow" };
  }
}

var store = Redux.createStore(reducer);
```

리듀서 만들고 초기값 만들기

```jsx
var state = store.getState();
<div style="background-color:${state.color}">
```

스테이트 가져와서 컬러 받아주기

```jsx
<input type="button" value="fire" onclick="
	store.dispatch({type:'CHANGE_COLOR', color:'red'});
">
```

dispatch로 객체를 하나 넘겨주는데 타입이 반드시 있어야한다.

스테이트를 바꿀 때 얘가 리듀서에게 요 액션넘긴다

리듀서는 이전스테이트와 새 액션을 받아서 새로운 스테이트를 리턴한다

```jsx
Object.assign({}, { feeling: "😆" }, { city: "seoul" });
```

객체 복제해서 복사본 변경하기

첫번째 인자엔 빈 객체, 그 객체를 복사해서 새로운 객체를 추가하게 된다.

```jsx
function reducer(state, action) {
  if (state === undefined) {
    return { color: "yellow" };
  }
  var newState;
  if (action.type === "CHANGE_COLOR") {
    newState = Object.assign({}, state, { color: action.color });
  }
  return newState;
}
```

이제 자동 렌더링하도록 subscribe 만들기

```jsx
store.subscribe(red);
```

# Redux DevTools

[깃헙 저장소](https://github.com/zalmoxisus/redux-devtools-extension) 들어가서 크롬 확장앱 추가

```jsx
var store = Redux.createStore(
  reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);
```

스토어 만들 때 인자에 코드 추가

깃 버전관리같음

# 정적웹페이지 부품화

태그 전부다 함수형 컴포로 만들어서 화면에 그려주고 있음

```jsx
<div id="subject"></div>
```

```jsx
function subject() {
  document.querySelector("#subject").innerHTML = `
      <header>
      <h1>WEB</h1>
      Hello, WEB!
      </header>
      `;
}

subject();
```

리덕스 스토어 만들기:

```jsx
function reducer(state, action) {
  if (state === undefined) {
    return {
      contents: [
        { id: 1, title: "HTML", desc: "HTML is .." },
        { id: 2, title: "CSS", desc: "CSS is .." },
      ],
    };
  }
}
var store = Redux.createStore(reducer);
```

```jsx
function TOC() {
  var state = store.getState();
  var i = 0;
  var liTags = "";
  while (i < state.contents.length) {
    liTags =
      liTags +
      `
        <li>
            <a href="${state.contents[i].id}">
							${state.contents[i].title}</a>
        </li>`;
    i++;
  }
  document.querySelector("#toc").innerHTML = `
    <nav>
      <ol>${liTags}</ol>
    </nav>
    `;
}
```

```jsx
liTags +
  `
	<li>
	    <a onclick="
	        event.preventDefault();
	        var action = {type:'SELECT', id:${state.contents[i].title}}
	        store.dispatch(action);
	    " href="${state.contents[i].id}">
	    ${state.contents[i].title}</a>
	</li>`;
```

```jsx
function reducer(state, action) {
  if (state === undefined) {
    return {
      selected_id: null,
      contents: [
        { id: 1, title: "HTML", desc: "HTML is .." },
        { id: 2, title: "CSS", desc: "CSS is .." },
      ],
    };
  }
  var newState;
  if (action.type === "SELECT") {
    newState = Object.assign({}, state, { selected_id: action.id });
  }
  return newState;
}
```

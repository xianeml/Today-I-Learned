# Map()

```jsx
import React from "react";
import "./App.css";

const list = [
  {
    title: "React",
    url: "https://reactjs.org/",
    author: "Jordan Walke",
    num_comments: 3,
    points: 4,
    objectID: 0,
  },
  {
    title: "Redux",
    url: "https://redux.js.org/",
    author: "Dan Abramov, Andrew Clark",
    num_comments: 2,
    points: 5,
    objectID: 1,
  },
];

function App() {
  return (
    <div>
      <h1>My Hacker Stories</h1>
      <label htmlFor="search">Search: </label>
      <input id="search" type="text" />
      <hr />
      {list.map((item) => (
        <div key={item.objectID}>
          <span>
            <a href={item.url}>{item.title}</a>
          </span>
          <span>{item.author}</span>
          <span>{item.num_comments}</span>
          <span>{item.points}</span>
        </div>
      ))}
    </div>
  );
}

export default App;
```

# 컴포넌트 분리

```jsx
import React from "react";
import "./App.css";

const list = [
  {
    title: "React",
    url: "https://reactjs.org/",
    author: "Jordan Walke",
    num_comments: 3,
    points: 4,
    objectID: 0,
  },
  {
    title: "Redux",
    url: "https://redux.js.org/",
    author: "Dan Abramov, Andrew Clark",
    num_comments: 2,
    points: 5,
    objectID: 1,
  },
];

const App = () => (
  <div>
    <h1>My Hacker Stories</h1>
    <label htmlFor="search">Search: </label>
    <input id="search" type="text" />
    <hr />
    <List />
  </div>
);

const List = () =>
  list.map((item) => (
    <div key={item.objectID}>
      <span>
        <a href={item.url}>{item.title}</a>
      </span>
      <span>{item.author}</span>
      <span>{item.num_comments}</span>
      <span>{item.points}</span>
    </div>
  ));

export default App;
```

# 리액트 상태

useState()훅 : 리액트의 경우, 리액트 useState 훅은 배열을 반환하는 함수입니다

![%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20ecf92354ef774c72a7e3fbfebb96a657/Untitled%201.png](%E1%84%80%E1%85%B5%E1%84%8E%E1%85%A9%20ecf92354ef774c72a7e3fbfebb96a657/Untitled%201.png)

```jsx
const [searchTerm, setSearchTerm] = React.useState("");

const handleChange = (event) => {
  setSearchTerm(event.target.value);
};
```

```jsx
<input id="search" type="text" onChange={handleChange} />

      <p>
        Searching for <strong>{searchTerm}</strong>
      </p>
```

# search 컴포넌트 분리

기능분리. 앱의 자식 컴포 상태임. 이 상태를 앱으로도 올려서 공유하고싶음.

콜백핸들러 사용.

```jsx
const handleSearch = (event) => {
    console.log(event.target.value);
  };

  return (
    <div>
      <h1>My Hacker Stories</h1>

      <Search onSearch={handleSearch} />
```

앱에서 서치로 함수(콜백 핸들러) 전달

이벤트핸들러인데 여기서 사용안하고 자식에서 콜백 호출하면 그때 여기서 작동됨

```jsx
const Search = (props) => {
  const [searchTerm, setSearchTerm] = React.useState("");

  const handleChange = (event) => {
    setSearchTerm(event.target.value);

    props.onSearch(event);
  };
```

서치가 프랍스로 그 핸들러 함수 호출해서 사용

컴포넌트 계층구조를 통해 소통하기.

# 상태끌어올리기

항상 연관된 모든 컴포넌트가 상태를 관리하는 컴포넌트 (상태에서 직접 정보를 사용)이거나 그 아래에서 props를 통해서 가져온 정보를 사용하는 컴포넌트일 때만 상태를 관리하세요. 아래의 컴포넌트가 상태를 업데이트해야 하면 콜백 핸들러를 내려보내세요. (Search 컴포넌트의 예를 확인하세요) 컴포넌트가 상태를 이용해야 한다면 (예. 보여주기), props로 내려보내세요.

# props 핸들링 심화

```jsx
const Search = props => {
	const { search, onSearch } = props;

	return (
```

props 객체 구조분해. props.~ 로 접근할 필요없어짐. 근데 함수 시그니처에서 구조분해해보자

```jsx
const Search = ({ search, onSearch }) => (
```

위 내용이 더 간단해짐. props 객체 자체를 사용하지 않아. 컨테이너일 뿐이야. 구조분해해서 필요한 정보만 가져온다.

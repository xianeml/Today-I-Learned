# 리액트 사이드 이펙트

로컬저장소 사용하기(브라우저 API 사용해서 리액트 범위 밖과 상호작용),

컴포에서 데이터 가져오기, 직접 DOM 조작하기 등

```jsx
const [searchTerm, setSearchTerm] = React.useState(
  localStorage.getItem("search") || "React"
);
```

set은 아래에서 해준다. 이건 로컬스토리지에 뭐가 저장되어 있으면 겟 해서 상태 초기화해주는 부분이야.

> The `getItem()` method of the Storage interface, when passed a key name, will return that key's value, or null if the key does not exist, in the given Storage object.

로컬저장소에 검색어를 저장하고 저장된 값이 있으면 스테이트 초기화, 없으면 초기상태를 '리액트'로

검색어 상태가 업뎃될때마다 useEffect 훅을 사용해서 사이드 이펙트를 유발하도록 한다. 입력필드 사용 후 새로고침하면 브라우저는 가장 최근 검색어를 기억해야한다.

```jsx
React.useEffect(() => {
  localStorage.setItem("search", searchTerm);
}, [searchTerm]);
```

브라우저의 로컬스토리지에 식별자를 동반한 현재 스테이트를 저장한다.

이 함수가 effect

effect 훅이 이 함수 내부에 있기 때문에 스테이트 접근도 바로 가능함.

마운트(Mount)는 DOM 객체가 생성되고 브라우저에 나타나는 것을 의미합니다.

두번째 인자에 있는 변수의 종속성 배열이라는 게 구조분해된 state를 가리키는 것 같다. 이 스테이트가 변하면 이펙트 함수가 실행되고, 마운트부터 시작해서 스테이트 변할때마다 이펙트 실행.

---

[Using the Effect Hook - React](https://ko.reactjs.org/docs/hooks-effect.html)

useEffect가 하는 일은 무엇일까요? useEffect Hook을 이용하여 우리는 리액트에게 컴포넌트가 렌더링 이후에 어떤 일을 수행해야하는 지를 말합니다. 리액트는 우리가 넘긴 함수를 기억했다가(이 함수를 ‘effect’라고 부릅니다) DOM 업데이트를 수행한 이후에 불러낼 것입니다. 위의 경우에는 effect를 통해 문서 타이틀을 지정하지만, 이 외에도 데이터를 가져오거나 다른 명령형(imperative) API를 불러내는 일도 할 수 있습니다.

마운팅과 업데이트라는 방식으로 생각하는 대신 **effect를 렌더링 이후에 발생하는 것**으로 생각하는 것이 더 쉬울 것입니다. 리액트는 effect가 수행되는 시점에 이미 DOM이 업데이트되었음을 보장합니다.

---

useEffect는 컴포넌트의 생명주기 메서드를 구현하기 위해 사용됨

# 리액트 커스텀 훅

위에서 만든 훅으로 useSemiPersistentState라는 이름의 새로운 커스텀 훅을 만들기. 상태를 관리하면서 로컬 스토리지와 동기화된다.

```jsx
const useSemiPersistenceState = (key, initialState) => {
```

```jsx
const [searchTerm, setSearchTerm] = useSemiPersistenceState("search", "React");
```

원래 key를 search라고 해놨는데 저 커스텀훅을 재사용하기 위해 적절한 이름으로 바꿔놓고 실제로 훅 사용할 때 디테일한 값을 넣어주는 걸로 변경한거다.

# 리액트 컴포넌트 재사용

Search 컴포넌트가 실질적으로 “검색” 기능이 없기 때문에, search 도메인 속성들을 다른 애플리케이션에서도 재사용이 가능

```jsx
<InputWithLabel
  id="search"
  label="Search"
  value={searchTerm}
  onInputChange={handleSearch}
/>
```

```jsx
const InputWithLabel = ({ id, label, value, type = "text", onInputChange }) => (
  <>
    <label htmlFor="{id}">{label} </label>&nbsp;
    <input id={id} type={type} value={value} onChange={onInputChange} />
  </>
);
```

# 리액트 컴포넌트 구성

children prop 사용

```jsx
<InputWithLabel
  id="search"
  label="Search"
  value={searchTerm}
  onInputChange={handleSearch}
>
  <strong>Search:</strong>
</InputWithLabel>
```

```jsx
const InputWithLabel = ({
  id,
  value,
  type = "text",
  onInputChange,
  children,
}) => (
  <>
    <label htmlFor="{id}">{children} </label>&nbsp;
```

# 명령형 리액트

useRef 다시보기

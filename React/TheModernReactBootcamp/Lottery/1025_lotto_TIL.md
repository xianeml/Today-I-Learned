**Minimize your State**

you want to try to put as little data in state as possible.

State Should Live On the Parent

downward data flow

# Lottery

![StatePattern,%20Lottery%204361cca07d4040aaa5fe95ece0fcbdd7/Untitled.png](StatePattern,%20Lottery%204361cca07d4040aaa5fe95ece0fcbdd7/Untitled.png)

### Lottery.js:

```jsx
Array.from({ length: numBalls });
```

`Array.from()` 메서드는 유사 배열 객체(array-like object)나반복 가능한 객체(iterable object)를 얕게 복사해새로운Array 객체를 만듭니다.

[Array.from을 통한 배열의 초기화](https://velog.io/@teihong93/Array.from%EC%9D%84-%ED%86%B5%ED%95%9C-%EB%B0%B0%EC%97%B4%EC%9D%98-%EC%B4%88%EA%B8%B0%ED%99%94)

```jsx
const [nums, setNums] = useState(Array.from({ length: numBalls }));
```

스테이트 초기값으로 맥스볼 크기만큼의 빈 배열을 만들어줌.

```jsx
return (
    <section className="Lottery">
      <h1>{title}</h1>
      <div>
        {nums.map((n) => (
          <Ball num={n} />
        ))}
      </div>
      <button onClick={generate}>Generate</button>
    </section>
  );
};
```

타이틀 밑에는 볼 컴포가 있다.

### Ball.js:

```jsx
const Ball = ({ num }) => {
  return <div className="Ball">{num}</div>;
};
```

볼은 num 속성 받아와서 div 안에 장착함. num값이 뭐였을지 보자

### Lottery.js:

```jsx
{
  nums.map((n) => <Ball num={n} />);
}
```

num값은 nums 배열에 있던 아이템 하나하나(n)였다. 이걸 볼 컴포 디브에 장착하면 아이템 하나하나 만큼 div 박스가 생성됨

```jsx
<button onClick={generate}>Generate</button>
```

버튼을 클릭하면 제너레이트를 실행한다.

```jsx
const generate = () => {
  setNums(nums.map((n) => Math.floor(Math.random() * maxNum) + 1));
};
```

얘는 nums 배열을 업데이트한다. 넘스 배열 아이템들 하나하나에 랜덤넘버를 부여해준다.

내가 알아보기 쉽게 코드를 더 정리해보고 다이스에서 했던 쉐이킹 애니까지 적용하면 좋을 것 같다.

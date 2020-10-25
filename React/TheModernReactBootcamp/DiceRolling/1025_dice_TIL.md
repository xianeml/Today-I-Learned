# dice rolling

date: Oct 25, 2020

![dice%20rolling%20efe31430c7544766ac4dbd9bfb967cf6/roll_dice.gif](dice%20rolling%20efe31430c7544766ac4dbd9bfb967cf6/roll_dice.gif)

버튼을 클릭하면 주사위 한 쌍을 흔들어서 랜덤한 결과를 보여준다.

## 컴포넌트

- **_RollDice_** - a parent component (rendered by App) that renders the dice and a button to roll.
- **_Die_** - an individual die that takes props and displays the correct face of the die based on props.

# App.js

```java
function App() {
  return (
    <div className="App">
      <RollDice />
    </div>
  );
}
```

롤다이스만 리턴

# Die.js

```jsx
const Die = ({ face, rolling }) => {
  return <i className={`Die fas fa-dice-${face} ${rolling && "shaking"}`}></i>;
};
```

주사위 이미지는 폰트어썸 태그 활용

부모 RollDice 컴포넌트에서 face, rolling 속성을 받아온다.

face는 지금 주사위가 어떤 면을 보여주고 있는지를 나타내며, 폰트어썸 클래스 이름을 props 값으로 동적으로 바꿔주고 있다.

rolling은 버튼을 눌러서 주사위가 돌아가고 있는지를 확인하는 속성으로, 돌아가고 있으면 "shanking"이라는 클래스네임을 붙인다.

\*\*

`&&` 는 첫번째 falsy를 찾는다.

- 각 피연산자는 불린형으로 변환됩니다. 변환 후 값이 `false`이면 평가를 멈추고 해당 피연산자의 **변환 전** 원래 값을 반환합니다.
- 피연산자 모두가 평가되는 경우(모든 피연산자가 `true`로 평가되는 경우)엔 마지막 피연산자가 반환됩니다.

# RollDice.js

```java
return (
    <div className="RollDice">
      <div className="RollDice-container">
        <Die face={die.die1} rolling={die.rolling} />
        <Die face={die.die2} rolling={die.rolling} />
      </div>
      <button onClick={roll} disabled={die.rolling}>
        {die.rolling ? "Rolling..." : "Roll Dice!"}
      </button>
    </div>
  );
```

주사위 두개랑 버튼을 보여준다.

어떤 면을 보여줄지는 랜덤으로 가져올거고 롤링상태도 동적으로 받아올거다.

버튼은 roll 이벤트 핸들러를 작동시키고, 롤링중일 땐 클릭을 막아놓는다.

롤링중이라면 버튼 텍스트도 바뀐다.

```jsx
const sides = ["one", "two", "three", "four", "five", "six"];
```

Die 컴포에게 face 속성으로 넘겨줄 배열이다. 주사위의 6면이 담겨있다.

```jsx
const [die, setDie] = useState({ die1: "one", die2: "one", rolling: false });
```

주사위의 상태를 스테이트로 관리한다. 주사위 상태의 초기값으로 객체에 3가지 정보를 담았다. 1번주사위 숫자, 2번주사위 숫자, 현재돌아가는 중인가를 나타낸다.

```jsx
const roll = () => {
  //pick 2 new rolls
  const newDie1 = sides[Math.floor(Math.random() * sides.length)];
  const newDie2 = sides[Math.floor(Math.random() * sides.length)];
  //set state with new rolls
  setDie({
    die1: newDie1,
    die2: newDie2,
    rolling: true,
  });

  //wait one second, then set rolling to false
  setTimeout(() => {
    setDie({ die1: newDie1, die2: newDie2, rolling: false });
  }, 1000);
};
```

버튼을 클릭하면 실행하는 함수다.

주사위에 들어갈 숫자를 sides 배열에서 랜덤으로 뽑아오고, setDie를 통해 상태를 업데이트 한다. 버튼이 클릭되었으니 롤링속성도 트루로 바뀐다.

그리고 롤링은 1초만 돌아갔다가 다시 제자리로 돌아와야하기 때문에 setTimeout()함수를 사용해 롤링상태를 기존 false로 바꿔준다.

# Die.css

```jsx
.shaking {
  animation-name: wobble;
  animation-duration: 1s;
}

@keyframes wobble {
  from {
    transform: translate3d(0, 0, 0);
  }

  15% {
    transform: translate3d(-25%, 0, 0) rotate3d(0, 0, 1, -5deg);
  }

  30% {
    transform: translate3d(20%, 0, 0) rotate3d(0, 0, 1, 3deg);
  }

  45% {
    transform: translate3d(-15%, 0, 0) rotate3d(0, 0, 1, -3deg);
  }

  60% {
    transform: translate3d(10%, 0, 0) rotate3d(0, 0, 1, 2deg);
  }

  75% {
    transform: translate3d(-5%, 0, 0) rotate3d(0, 0, 1, -1deg);
  }

  to {
    transform: translate3d(0, 0, 0);
  }
}
```

주사위에 키프레임 애니메이션이 적용되었다. 주사위가 롤링 상태라면 쉐이킹이 1초간 적용된다.

# RollDice.css

- `flex-flow` CSS 속성은 `flex-direction`, `flex-wrap` 속성의 단축 속성입니다
- `min-height: 100vh;` : vh 단위를 처음봤다. `vertical height` 라고 뷰포트 값의 100분의 1단위라고 한다.

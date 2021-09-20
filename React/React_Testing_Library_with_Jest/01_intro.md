# 01 intro

date: 2021년 9월 20일

# 리액트 테스팅 라이브러리

- 사용자가 실제 사용하는것처럼 소프트웨어를 테스트한다.
  - 내부 코드 구현을 테스트하는게 아님
- 테스트 아이디가 아니라 접근성 마커로 돔 요소를 찾는다?
- 테스트를 위해 가상 돔을 제공한다.
- 브라우저 없이 테스팅할 수 있어

# Jest

- 테스트 러너 실행해서 성공 실패 정의함

# react test

- npx cra 하고 npm test 실행.

### 테스팅 라이브러리 문법 살펴보자

```jsx
import { render, screen } from '@testing-library/react'
import App from './App'

test('renders learn react link', () => {
  render(<App />)
  const linkElement = screen.getByText(/learn react/i)
  expect(linkElement).toBeInTheDocument()
})
```

- render : 파라미터로 받은 jsx를 위한 가상 돔을 만든다.
- screen: 스크린 객체의 getByText 함수로 돔에서 요소를 찾는다. 파라미터는 정규식. //안에 스트링 담겨있고 i는 case insensitive라고 대소문자 상관없이 받겠다는뜻. 걍 스트링으로 써도됨 ''
- expect: assertion이라고함. 테스트가 성공 또는 실패 결과 나오도록 트리거해줌.

# Assertions

표명, 확실한지 확인

```jsx
expect(linkElement).toBeInTheDocument()
```

- expect : jest 전역. 어설션 스타트
- 파라미터: 테스트 주제
- matcher: 테스트 타입, comes from 제스트 돔
- 매쳐 인자: refines matcher

```jsx
expect(element.textContent).toBe('hello')
expect(elementsArray).toHaveLength(7)
```

### jest-dom

- cra에서 기본적으로 같이 딸려옴
- src/setupTests.js가 각 테스트 전에 jest-dom 임포트해줌. 매쳐 사용가능하도록
- dom 기반 매쳐
  - toBeVisable() 돔에서 얘가 보이냐, toBeChecked() 체크박스 체크드되었냐 등

# Jest Watch Mode

- 마지막 커밋에서 변화를 감지함
- 이 파일과 관련된 테스트만 실행함
- 변경 없으면 실행안함
- run all tests

# 제스트가 어떻게 동작해

- test라는 전역 함수가 파라미터 두개를 받음
  1. 테스트의 문자열 설명
  2. 테스트 함수
- 함수를 실행하다가 에러가 던져지면 테스트는 실패
  - assertions은 expectation이 실패하면 에러 던짐
- 에러없으면 테스트 성공
  - 테스트 비어있어도 성공

# TDD

test driven development

- 코드 작성 전 테스트 작성부터
  - 그런 다음 테스트 통과하기 위한 코드를 작성한다
- 빨강 초록 테스팅
  - 코드 작성 전엔 테스트 실패 상태
  - 코드 작성 후에는 성공 상태

### 왜 TDD?

- 코드 작성 후에 보면 이게 잡일로 느껴지지 않을겨
- 효율적. 변경 후 또 다시 알아서 테스트 실행해볼 수 있어. 바뀔때마다 일일이 테스트할 필요가 없다.

# types of tests

- 유닛 테스트: 고립된 코드 단위 하나를 테스트
- 통합 테스트: 여러 코드 단위가 함께 작동되는걸 테스트
- 기능 테스트: 소프트웨어의 각 기능을 테스트
- End-to-end Tests: 실제 브라우저와 서버를 사용. (싸이프레스, 셀레니움)

# 기능 테스트

- 유닛테스트
  - 최대한 고립되어야해. 의존성도 목업으로 사용. 내부를 테스트함.
  - 고립되어 있으면 테스트 실패 원인을 정확히 볼 수 있음.
  - 근데 사용자가 소프트웨어랑 어떻게 상호작용하는지 테스트하는 것과는 거리가 멀다
- 기능테스트
  - 모든 관련 단위 포함. 행동을 테스트
  - 유저-소프트웨어 상호작용 테스트와 가까움.
  - 실패테스트 디버깅 하기 좀 더 어려움

# TDD vs BDD

- 테스팅 라이브러리가 구현보다 행동 테스트한다며 BDD로 부르면 되는거 아니여?
  - BDD 의미 : 다양한 역할 간 콜라보 포함됨. (개발자, QA, 협력사)
  - 서로다른 그룹이 상호작용하는 과정을 정의함
  - 우리는 개발만 집중하면 되니까 TDD!

# 접근성과 요소 찾기

- 테스팅 라이브러리는 접근성 신경써서 finding 하라고 추천함
- 공식문서에 쿼리 우선순위가 적혀있음
- cra 예제에는 a태그 매쳐를 getByText 사용했지만 사실 a태그는 링크 클릭으로 사용자와 상호작용하는거니까 getByRole 매쳐가 더 적절함.
- role_definitions 참고

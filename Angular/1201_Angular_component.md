# Angular

- TypeScript 기반
- 가장 복잡하고 큰 러닝커브(내부 동작 매커니즘 포함)
- 구글 지원
- 커뮤니티 및 잘 정리된 문서 지원
- 가장 빠르게 릴리즈된 프레임워크(2010년
- 이전 버전의 AngularJS 보다 랜더링 성능이 향상
- 홈페이지: angular.io

```tsx
npm install -g typescript
npm install -g @angular/cli
```

```tsx
ng new my-app
cd my-app
ng serve --open
```

src폴더만 건들일거고 이거만 백업해두면 된다.

src/app/app.component.html:

서버 실행 후 로켓 띄워줬던 화면

src/app/app.module.ts:

사용하는데 필요한 모듈 불러오기

### Angular 구성요소

링크: https://angular.io/guide/architecture

- component: @Component 장식자 + component 클래스
- template: 화면구성 역할을 담당하고 html로 작성. HTML를 통해서 Angular에게 component를 rendering 하는 방법을 알려준다.
- directive: template의 html태그내의 속성 핸들링. directive가 제시하는 지침에 따라서 template의 DOM이 동적으로 변경된다.
- service: 컴포넌트가 공통적으로 사용되는 비즈니스 로직 처리 담당. 일반적으로 @Injectable 사용하여 서비스 클래스를 생성한다 (http service, logging service, data service,특정 계산 서비스등)
- module: 각 구성요소 관리 ( Component, Service, Directive 등 )
- DI도 사용. 주로 service 주입

### app 폴더 구조

app.component.html 이 화면에 보여지는 영역

css, ts가 여기 속함

app.module.ts는 app컴포에서 사용할 수 있는 api를 모듈형태로 모아두고 있음

ts 열어서 컴포넌트 selector 보면 선택자 이름을 알 수 있다

index.html:
`<app-root></app-root>`

여기서 앱 컴포를 불러와줌

app.component.ts:

```tsx
@Component({
  selector: 'app-root', //선택자
  //백틱사용, template로 변경, styles로 변경
  template: `
    <table>
      <tr>
        <td><h1>홍길동</h1></td>
        <td><h2>안녕</h2></td>
      </tr>
    </table>
  `,
  styles: [
    `
      h1 {
        color: red;
      }
    `,
    `
      h2 {
        background: yellow;
      }
    `,
  ],
})
```

- @Component: 컴포넌트와 관련된 설정 정보를 지정하는 영역
- selector 속성 : Component의 인스턴스를 생성하고 삽입하도록 지시하는 CSS 선택자.
- templateUrl, template 속성: HTML 템플릿 파일의 상대 경로 또는 HTML 코드
- templateUrl을 template로 변경해서 `` 백틱 사용해 코드작성 가능
- styleUrls, styles 속성: CSS 스타일시트 파일의 상대 경로 또는 CSS 코드 - styleUrls-> styles로 변경해서 백틱사용 코드작성 가능.

### Angular의 Component 중심의개발

`ng g component my`

app컴포넌트 밑에 자식 컴포넌트 my가 생성됨

중첩된 레이아웃으로 화면을 구현 - 계층구조로 관리됨

```tsx
<h1>자식컴포넌트 포함</h1>
다음과 같이 자식 컴포넌트 selector를 지정하면
자동으로 자식컴포넌트 template이 삽입된다.<br>
<app-my></app-my>
```

my 자식컴포가 app컴포html에 <app-my>라는 선택자로 포함되고있고

app컴포는 index.html에 <app-root>라는 선택자로 포함되고있다

Chid실습

`ng g component child`

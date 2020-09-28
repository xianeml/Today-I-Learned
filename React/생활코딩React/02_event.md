# 이벤트

```jsx
<h1><a href="/" onClick={function(){
            
          }}>{this.state.subject.title}</a></h1>
```

이게 완전한 html이 아니라서 리액트문법을 따라야됨. 온클릭은 반드시 중간에 대문자로 이어줘야 하고 속성값은 {} 중괄호로 집어넣는다.

익명함수는 이벤트 핸들러. 첫 파라미터로 이벤트 객체를 받기로 약속되어있음. 

먼저 이벤트 없이 화면 모드 바꿔주는 연습해본다.

웰컴모드와 읽기모드 두가지가 있다.

리액트에서는 컴포넌트랑 프로퍼티 값이 바뀌면 렌더 함수가 다시 호출 돼. 컴포넌트가 가진 렌더가 다 실행되면서 화면이 다시 그려져

앱 안에 스테이트 프로퍼티랑 렌더함수 새로 추가.

```jsx
this.state = {
      mode:'welcome',
      subject:{title:"WEB", sub:"world wide web!"},
      welcome:{title:"welcome", desc:"hello react"},
      contents:[
              {id:1, title:'html', desc:'html is for info~'},
              {id:2, title:'CSS', desc:'CSS is for info~'},
              {id:3, title:'JS', desc:'JS is for info~'},  
            ]
    }
```

```jsx
render(){
    var _title, _desc =null;

      if(this.state.mode ==='welcome'){
        _title = this.state.welcome.title;
        _desc = this.state.welcome.desc;

      }else if(this.state.mode === 'read'){
        _title = this.state.contents[0].title;
        _desc = this.state.contents[0].desc;
      }
```

모드는 스테이트에서 바꿔줄 수 있고 웰컴모드면 웰컴 프로퍼티를,

리드모드라면 그냥 컨텐츠 프로퍼티 데이터를 보여준다.

언더바 변수가 뭔지 알아봐야겠음. >> 지역변수로 사용하겠다고 표시하는 것.

모드 스테이트에 따라서 컨텐트 컴포넌트의 프로퍼티 값이 달라짐.

```jsx
<Content title={_title} desc={_desc} />
```

html모양 태그 안에서 자바스크립트로 만들어진 변수를 사용하기 위해 {} 중괄호로 감싸준것.

## 이벤트에서 state 변경하기

```jsx
return (
      <div className="App">
        {/* <Subject></Subject> */}
        <header>
          <h1><a href="/" onClick={function(e){
            console.log(e);
            e.preventDefault();
            //this.state.mode='welcome';
            this.setState({
              mode: 'welcome'
            });
          }.bind(this)}>{this.state.subject.title}</a></h1>
          {this.state.subject.sub}
      </header>
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc} />
      </div>
  );
```

a태그 안에 속성으로 이벤트 속성 이름에서 온 클릭을 대문자로 써 줘야 돼 

이벤트 막을 땐 이벤트 객체의 preventDefault함수를 사용하면 이벤트를 막을 수 있어

지금 리드모드 상태에서 이 a태그를 클릭하면 welcome 모드로 바꿔주려고 해.

그럼 스테이트 프로퍼티 값을 바로 바꿔주면 될까?

```jsx
this.state.mode='welcome';
```

얘는 두가지 문제가 있다.

이벤트 핸들러 안에서 작성된 this는 컴포넌트 자기 자신(스테이트를 가진 App)을 가리키지 않고 아무것도 세팅이 안 되어있어

그래서 이 this.state를 사용하려면 함수가 끝나는 바깥쪽에 바로 .바인드(this) 붙이고 함수 안에서 this.setState 하고 그 안에 또 파라미터로 객체 타입으로 모드는 웰컴이다 이렇게  설정을 해 주면 이제 웰컴모드로 바뀌어.

### 함수.bind(this)

**바인드는 this가 컴포넌트 자신을 가리키도록 합쳐준다. 함수안에 this가 아무값도 못가지니까 강제로 밖에서 주입해주는거야.**

렌더함수 안에서 this는 렌더함수를 갖고있는 자기자신 컴포넌트를 가리킨다

### this.setState()

생성자 함수 안에 있는 스테이트 값은 직접 바꿔줄수있거든, 근데 이미 컴포넌트 생성 끝나고 동적으로 스테이트 값 바꿀땐 this.setState에 변경하고 싶은 값을 객체형태로 준다.

# 컴포넌트 이벤트 만들기

```jsx
<Subject
          title={this.state.subject.title}
          sub={this.state.subject.sub}
          onChangePage={function(){
            this.setState({mode:'welcome'});
          }.bind(this)}
        >
```

```jsx
class Subject extends Component {
  render() {
    return (
      <header>
          <h1><a href="/" onClick={function(e){
            e.preventDefault();
            this.props.onChangePage();
          }.bind(this)}>{this.props.title}</a></h1>
          {this.props.sub}
      </header>
    );
  }
}
```

```jsx
        <TOC onChangePage={function(){
          this.setState({
            mode:'read',
            selected_content_id:0
          })
        }.bind(this)} 
					data={this.state.contents}></TOC>
```

```jsx
render(){
    var _title, _desc =null;
      if(this.state.mode ==='welcome'){
        _title = this.state.welcome.title;
        _desc = this.state.welcome.desc;
      }else if(this.state.mode === 'read'){
        var i = 0;
        while(i < this.state.contents.length){
          var data = this.state.contents[i];
          i = i+1;
          if(data.id === this.state.selected_content_id){
            _title = data.title;
            _desc = data.desc;
            break;
          }
        }
```

클릭한 컨텐트가가 본문에 나오도록.

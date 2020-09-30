# CRUD

toc랑content 컴포넌트 사이에 컨트롤 컴포넌트를 만들어 준다

얘네들은 ul,li 태그로 이루어져 있고 각각 a태그를 달고 있는데  
링크는  Create 업데이트 delete로 이루어져 있고 이걸 그대로 컨트롤 컴포넌트로 가져 가

그리고 app.js의 컨트롤 컴포넌트는 프로퍼티로 사용자 정의 속성으로 온 체인지 모드라는 이벤트 속성을 만들고  
 이벤트에 핸들러를 그 안에 써줄거야

링크 하나 하나 클릭했을 때 저 온 체인지 모드 받을거야

```jsx
class Control extends Component {
  render() {
    return (
      <ul>
          <li><a href="/create" onClick={function(e){
            e.preventDefault();
            this.props.onChangeMode('create');
          }.bind(this)}>create</a></li>
          <li><a href="/update" onClick={function(e){
            e.preventDefault();
            this.props.onChangeMode('update');
          }.bind(this)}>update</a></li>
          <li><input onClick={function(e){
            e.preventDefault();
            this.props.onChangeMode('delete');
          }.bind(this)} type="button" value="delete"></input></li>
        </ul>
    );
  }
}
```

하위컴포 컨트롤이 부모컴포 앱에 이벤트 줄때 프랍스 쓰잖아

부모 컴포속성에 있는 이벤트속성 값을 여기서 적어서 보내줌.

언더바 변수는 헷갈리지 않게 표시하거나 지역변수로 사용한다는걸 알려줄때 쓴다

```jsx
<Control onChangeMode={function(_mode){
          this.setState({
            mode:_mode
          })
        }.bind(this)}></Control>
```

자식컴포에서 받은 모드로 속성값을 setState 해서 바꿔줌.

이제 얘네 누르면 모드가 바껴

# 19.3.create 구현

이제 cud 버튼 각각 클릭하면 작동할 새로운 write모드를 만들거다

각 기능들을 구현할 create update delete 컴포넌트를 따로 만들어준다

## create mode

c클릭하면 readcontent를 폼으로 바꿔서 직접 데이터 입력할 수 있게 만들거야

readcontent 자리를 `{_article}` 로 만든다.

렌더에 reate모드 추가

```jsx
else if(this.state.mode === 'create'){
  _article = <CreateContent title={_title} desc={_desc}></CreateContent>
}
```

createContent 컴포에서 타이틀, 내용 가져올거다.

## form 구현

createContent:

```jsx
<form action="/create_process" method="post"
  onSubmit={function(e){
    e.preventDefualt();
    alert('submit!!');
  }.bind(this)}> 
  <p><input type="text" name="title" placeholder="title"></input></p>
	<textarea name="desc" placeholder="description"></textarea>
	<p>
	  <input type="submit"></input>
	</p>
</form>
```

submit하고 페이지 넘어가지 않게 이벤트 발생후 막아둠.

```jsx
<form action="/create_process" method="post"
	onSubmit={function(e){
  e.preventDefualt();
  this.props.onSubmit(
    e.target.title.value,
    e.target.desc.value
	);
```

폼에 입력된 title과 desc 값을 얻어보자

이벤트 객체의 타겟(폼) 속성값을 onSubmit  핸들러 인자로 전달

```jsx
else if(this.state.mode === 'create'){
  _article = <CreateContent onSubmit={function(_title, _desc){
    console.log(_tile, _desc);
  }.bind(this)}></CreateContent>
```

얘는 전달된거 받아와서 콘솔에 한번 찍어줌

## 폼에서 받은 데이터로 컨텐츠를 바꾸기

```jsx
class App extends Component {
  constructor(props){
    super(props);
    this.max_content_id=3;
    this.state = {
      mode:'create',
      selected_content_id:2,
      subject:{title:"WEB", sub:"world wide web!"},
      welcome:{title:"welcome", desc:"hello react"},
      contents:[
              {id:1, title:'html', desc:'html is for info~'},
              {id:2, title:'CSS', desc:'CSS is for info~'},
              {id:3, title:'JS', desc:'JS is for info~'},  
            ]
    }
  }
```

스테이트에 있는 contents 배열 끝에 폼에서 받은 내용을 새로 추가해줄거야.

기존에 있던 아이디를 읽어서 그것보다 하나 더큰 아이디로 추가해줄것.

`this.max_content_id=3;` 데이터 추가할때 아이디 정보 알기위한 변수라 스테이트로 안해도됨. 불필요한 렌더링 발생가능

```jsx
else if(this.state.mode === 'create'){
	_article = <CreateContent onSubmit={function(_title, _desc){
	  this.max_content_id = this.max_content_id +1;
	  var _contents = this.state.contents.concat(
	    {id:this.max_content_id, title:_title, desc:_desc}
	  )
	  this.setState({
	    contents:_contents
	  });
	  console.log(_title, _desc);
}.bind(this)}></CreateContent>
```

배열에 내용 추가할 때 push는 원본을 바꾸고

concat은 원본에 추가해서 새로운 배열을 리턴한다. 내가만든 원본 배열은 그대로 있음

성능생각해서 concat 사용해라

아티클 변수는 기본적으로 웰컴모드 타이틀, 내용 보여줬다

create 모드 되면 폼에서 받은 내용으로 콘캣해서 새 배열 만들고, 스테이트의 콘텐츠 배열 새로 세팅. 이 모든걸 아티클 변수에 담아서 아티클 내용을 폼에서 받은 데이터로 보여준다.

## shouldComponentUpdate()

부모 컴포 스테이트가 바뀌면 자식컴포의 모든 렌더함수가 반응해서 렌더링된다.

근데 쓸데없이 렌더링되는 것도 문제다.

shouldComponentUpdate() 함수를 사용하면 컴포넌트 렌더링할지말지 결정할 수 있다.

리턴을 false로 하면 그 컴포넌트의 렌더함수 작동을 막는다.

파라미터 2개를 받는데 (프랍스 바뀐 값, 현재 스테이트값)을 받는다

toc 컴포의 스테이트가 바뀌면 렌더가 호출, 아니면 렌더 막자.

```jsx
class TOC extends Component {
  shouldComponentUpdate(newProps, newState){
    console.log('===>TOC render shouldComponentUpdate'
    ,newProps.data
    ,this.props.data
    );
    if(this.props.data === newProps.data){
      return false;
    }
    return true;
  }
```

배열에 push 쓰고 싶을 땐 `Array.from()` 사용해서 콘캣처럼 쓸 수 있다. 배열 복제해줌.

객체 복사는 `Object.assign()` 사용.

immutable.js 라이브러리를 사용하면 원본 불변으로 객체, 배열을 바꿔준다.

모든 코드가 일관되게 원본불변으로 사용할 수 있음.

# 20 업데이트 구현


create랑 내용이 비슷하다. 기존의 read 모드 컨텐츠 가져와서 폼 구성해서 내용 수정해주는 역할이니까


createcontent복사해서 update컴포 생성

렌더함수 리팩토링

모드 바꿔주는 코드 전부 getContent() 함수 안에 넣고 리턴은 `_article`,  
  {_article}로 본문 나태내던 곳을 `{this.getContent()}` 로 바꿔줌. 

contents 띄워주던 부분을 업데이트 역할로 준다

getReadContent() 함수로 리팩토링:

```jsx
getReadContent(){
    var i = 0;  //반복문 시작
        while(i < this.state.contents.length){
          var data = this.state.contents[i];  //현재 컨텐츠 번호
          if(data.id === this.state.selected_content_id){  
            return data;
            break;
          }
          i = i + 1;
        }
  }
```

```jsx
}else if(this.state.mode === 'read'){
       var _content = this.getReadContent();
        _article = <ReadContent title={_content.title} desc={_content.desc}></ReadContent>
```

```jsx
}else if(this.state.mode === 'update'){
        _content = this.getReadContent();
        _article = <UpdateContent data={_content} onSubmit={function(_title, _desc){
```

update form:

props 데이터는 리드온리라 업데이트할 수 없음

스테이트화 시켜줘야한다.

```jsx
constructor(props){
    super(props);
    this.state={
      title:this.props.data.title
    }
  }
```

```jsx
<input 
  type="text"
  name="title" 
  placeholder="title"
  value={this.state.title}
  onChange={function(e){
    this.setState({title:e.target.value});
  }.bind(this)}
></input>
```

한글자씩 바뀌는걸 바로 스테이트에 렌더링해줌. 타이틀 인풋에 글자 입력할때마다 스테이트 바뀜. desc도 스테이트에 만든다

```jsx
this.state={
      title:this.props.data.title,
      desc:this.props.data.desc
    }
```

```jsx
<textarea 
	onChange={function(e){
	this.setState({desc:e.target.value});
	}.bind(this)}
	name="desc" 
	placeholder="description" 
	value={this.state.desc}
></textarea>
```

리팩토링:

```jsx
inputFormHandler(e){
      this.setState({[e.target.name]:e.target.value});
    }
```

중복되는건 함수로 빼준다. 

새로운 대괄호 문법사용 → 이벤트가 발생되는 타겟을 알아서 찾음

```jsx
this.inputFormHandler = this.inputFormHandler.bind(this);
```

생성자에 bind도 빼준다

```jsx
onChange={this.inputFormHandler}
```

속성엔 요것만 쓰면 된다

id인풋 추가:

```jsx
<input type="hidden" name="id" value={this.state.id}></input>
```

```jsx
this.state={
      id:this.props.data.id,
```

업데이트 렉

# 21. delete 구현

```jsx
<Control onChangeMode={function(_mode){
  if(_mode === 'delete'){
    if(window.confirm('delete?')){
      var _contents = Array.from(this.state.contents);
      var i = 0;
      while(i<_contents.length){
        if(_contents[i].id === this.state.selected_content_id){
          _contents.splice(i,1);
          break;
        }
        i=i+1;
      }
      this.setState({
        mode:'welcome',
        contents:_contents
      })
    }
  }else{
    this.setState({
      mode:_mode
    });
  }
}.bind(this)}></Control>
```

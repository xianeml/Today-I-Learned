
MVC 패턴이 장고에선 MTV로 구성됨. 뷰가 템플릿, 컨트롤러 역할을 뷰가 함. 

서블릿 생각해보면 서블릿 역할이 장고에선 뷰, jsp역할을 장고에선 템플릿이 한다.

# 1. 회원관리 페이지 설정

urls.py에 장고 auth 패키지 뷰 가져와서 로그인, 로그아웃, 비번변경, 비번변경 완료, 사용자등록, id중복확인, 회원가입결과 총 7개의 뷰에 대한 url 패턴을 지정한다.

# 2. 회원가입 뷰

views.py:

```jsx
def user_register_page(request):
    return render(request, 'user_register.html')
```

회원정보등록 페이지 요청이 오면 user_register.html 해당 페이지를 보여준다. 뷰가 이런 로직 담당.

user_register.html

```jsx
{% extends "base.html" %}

{% block title %}
회원가입 
{% endblock  %}

{% block script %}
{% load static %}<script src = "{% static 'boardapp/assets/js/user.js %}"></script>
{% endblock  %}

{% block content %}

{% endblock %}
```

회원가입 폼이 들어갈 템플릿 화면을 만든다. 베이스 탬플릿 사용해서 기본 틀 만들고 회원가입에 필요한 폼 내용들을 넣으면 된다.

### 아이디 중복확인:

```jsx
<input type="button" value="중복확인" onClick="idCheck()" />
<span id="idcheck-result"></span>
```

```jsx
function idCheck() {
	if (!$('#username').val())
	{
		alert("ID를 입력해 주시기 바랍니다.");
		return;
	}

	$.ajax({
		type: "POST",
		url: "/boardapp/user_register_idcheck/",
		data: {
			'username': $('#username').val(),
			'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
		},
		success: function(response) {
			$('#idcheck-result').html(response);
		},
	});	
}
```

중복되는지 아이디 인풋값 넘겨주고 처리결과를 span에 써준다. 아이디 넘길때 위조방지처리까지. 애이잭스 요청받은거 응답해주는 뷰도 만들자

view.py:

```jsx
from boardapp.models import *
from django.http import HttpResponse

def user_register_idcheck(request):
	if request.method == "POST":
		username = request.POST['username']
	else:
		username = ''

	idObject = User.objects.filter(username__exact=username)
	idCount = idObject.count()

	if idCount > 0:
		msg = "<font color='red'>이미 존재하는 ID입니다.</font><input type='hidden' name='IDCheckResult' id='IDCheckResult' value=0 />"
	else:
		msg = "<font color='blue'>사용할 수 있는 ID입니다.</font><input type='hidden' name='IDCheckResult' id='IDCheckResult' value=1 />"

	return HttpResponse(msg)
```

포스트방식으로 넘어온 아이디 있으면 파싱. 

유저 모델에 넘어온 아이디로 검색되는게 있으면 변수에 저장

저장된 게 1개 이상이면 중복메세지 리턴하고 아니면 사용가능 메세지 리턴.

### 이메일 셀렉트 이벤트:

```jsx
<input type="text" id="email_id" value="" size="8" />
@ <input type="text" id="email_domain" value="" size="8" />
<select id="email_selection" onChange="changeEmailDomain()">
	<option value="" selected="selected">--선택하세요--</option>
	<option value="naver.com">naver.com</option>
	<option value="hanmail.net">hanmail.net</option>
	<option value="gmail.com">gmail.com</option>
	<option value="me.com">me.com</option>
</select>
```

```jsx
function changeEmailDomain() {
	$('#email_domain').val($('#email_selection').val());	
}
```

온체인지 이벤트 발생하면 도메인 밸류를 셀렉트한 밸류로 입력해준다.

### 회원가입 취소버튼:

```jsx
<input type="button" value="취소" onClick="cancelUserRegister()"/>
```

```jsx
function cancelUserRegister() {
	var result = confirm("회원가입을 취소하시겠습니까?");	

	if (result)
	{
		$(location).attr('href', '/boardapp/login');
	}
}
```

취소 물어보고 결과 있으면 로그인 페이지로 돌아간다

### 회원가입 버튼:

```jsx
<input type="button" value="회원가입" onClick="userRegister()"/>
```

```jsx
function userRegister() {
	if (!$('#username').val())
	{
		alert("아이디를 입력해 주시기 바랍니다.");
		return;
	}
	if (!$('#IDCheckResult').val()) {
		alert("ID 중복체크를 먼저 진행해 주시기 바랍니다.");
		return;
	}
	if (!$('#password').val()) {
		alert("비밀번호를 입력해 주시기 바랍니다.");
		return;
	}
	if($('#password').val().length < 8) {
		alert('비밀번호는 최소 8자 이상이여야 합니다.');
		alert($('#password').val().length );
		return;
	}
	if ($('#password').val() != $('#password_check').val()) {
		alert("비밀번호가 일치하지 않습니다.");
		return;
	}
	if (!$('#last_name').val())
	{
		alert("이름을 입력해 주시기 바랍니다.");
		return;
	}
	if (!$('#phone1').val() || !$('#phone2').val() || !$('#phone3').val())
	{
		alert("전화번호를 올바르게 입력해 주시기 바랍니다.");
		return;
	}
	if (!$('#email_id').val() || !$('#email_domain').val())
	{
		alert("E-mail 주소를 올바르게 입력해 주시기 바랍니다.");
		return;
	}
	if (!$('#birth_year').val() || !$('#birth_month').val() || !$('#birth_day').val())
	{
		alert("생년월일을 올바르게 입력해 주시기 바랍니다.");
		return;
	}

	$('#phone').val($('#phone1').val() + "-" + $('#phone2').val() + "-" + $('#phone3').val());
	$('#email').val($('#email_id').val() + "@" + $('#email_domain').val());

	$('#register_form').submit();
}
```

폼 빈칸방지와 입력 조건들은 다 요 함수에서 설정함. #phone, #email은 인풋 떨어져있는거 한꺼번에 내용붙여서 전달하려고 히든으로 만들어놨다

### 회원가입결과처리:

```jsx
def user_register_result(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		last_name = request.POST['last_name']
		phone = request.POST['phone']
		email = request.POST['email']
		birth_year = int(request.POST['birth_year'])
		birth_month = int(request.POST['birth_month'])
		birth_day = int(request.POST['birth_day'])

	try:
		if username and User.objects.filter(username__exact=username).count() == 0:
			date_of_birth = datetime(birth_year, birth_month, birth_day)

			user = User.objects.create_user(
				username, password, last_name, email, phone, date_of_birth
			)

			redirection_page = '/boardapp/user_register_completed/'
		else:
			redirection_page = '/boardapp/error/'
	except:
		redirection_page = '/boardapp/error/'

	return redirect(redirection_page)
```

들어온 데이터 검사해서 변수에 담고 아이디 중복 없으면 모델객체 생성해서 정보 저장한다. 그러고 페이지는 가입완료 페이지로 이동. 데이터 중복 있거나 예외 생기면 에러페이지로.

가입완료 페이지는 메세지 간단하게 보여주고 로그인과 메인으로 갈수있는 버튼 만들기. 뷰도 등록해줌

# 3. 로그인/로그아웃 뷰

장고패키지 로그인뷰 사용.

```jsx
LOGIN_REDIRECT_URL = '/boardapp/'
LOGOUT_REDIRECT_URL = '/boardapp/'
```

로그인, 로그아웃 성공시 이동할 경로 지정

id, 비번 입력하고 로그인 클릭하면 login함수 실행해서 폼 유효성 검사. 엔터만 눌러도 서브밋 되게 js 작성해줌

# 4. 회원정보조회/비번 변경

장고의 passwordChangeview를 사용한다. 

비밀번호 변경시 유효성검사 스크립트 추가

변경 완료 후 passwordchangedoneview를 사용

각각 템플릿만 만들어줌

화면 테스트해보니 css가 이상했는데 div logo 하나 빼먹어서 그랬다

아직 다른 변수 지정 안해서 a태그 링크는 다 지워놨다.
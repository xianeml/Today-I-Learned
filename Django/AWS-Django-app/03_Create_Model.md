# ch16 세팅시작

## 1.aws - cli 설치부터 시작~

`brew install awscli`

`aws configure`

## 2.vscode-ftp 연결 성공

나는 이거 하면 우분투에 있는 장고 앱을 여기서 할 수 있는줄 알았음. 연결되서 기분은 좋은데 이 방법이 아니었다.  
gui사용해서 장고 코딩하려면 우분투 가상환경 머신 써서 해야하는듯

## 2-1. 파일 전송을 위한 연결

저번에 터미널환경에서 SSH로 ec2 서버연결했지

파일전송은 FTP 사용하지만 ec2 인스턴스 연결은 SCP(Secure Copy Protocol) 사용함.

맥 scp는 ssh와 동일한 프로토콜 사용함.따라서 scp문법으로 터미널에서 파일공유가능

나는 맥이라서 푸티 이런거 필요없음. ssh연결 쓰면 되니까

이걸로 ec3 인스턴스의 사용자 루트 디렉토리로 파일 업로드함. 파일 업로드, 다운 가능.

이걸 터미널에서 하지않고 ide 통해서 디렉토리 쉽게 하려고 ftp 연결한거다.

### test.txt파일 ec2서버 사용자 루트 디렉토리로 보내기:

```jsx
% chmod 400 [/키페어경로]
% scp -i [/키페어경로] [/Desktop/test.txt]
ubuntu@ec2-3-35-139-124.ap-northeast-2.compute.amazonaws.com:~
test.txt
```

scp연결하려면 ssh처럼 파일권한설정 400변경부터.

### 서버에 있는 test.txt 내 컴 현재경로에 다운받기:

```jsx
% scp -i [키페어경로] ubuntu@ec2-3-35-139-124.ap-northeast-2.compute.amazonaws.com:~/test.txt test2.txt
test.txt                                           100%    4     0.3KB/s   00:00
% ls
Applications	Document	Library		Pictures	learn
Desktop		Documents	Movies		Public		test2.txt
```

vscode ftp remote 다시 시작했더니 새로 다운로딩 되면서 home폴더에 test.txt 생김!

ve 폴더 보니까 파이썬, 장고 잘 설치되어있음

지금 pwd 경로는 홈의 우분투인데 vscode에서 프로젝트폴더가 안보임

### VNC 원격pc 접속 필요 없음

내가 직접 리눅스 서버 갖고있는거 아니고 가상서버 임대해서 쓰는거니까 화면 테스트하려고 데스크탑 환경 구축하고 원격접속하는 거 비효율적.

그리고 무료티어가 고성능 서버도 아니라 속도저하,안정성 떨어짐. 추천은 하지 않지만 테스트가 필요할 수 있어서 책에 소개해놓은것.

터미널에서 우분투 runserver 안됨. 로컬에서 작업 다 하고 파일 보내야함. 로컬에서 만들기로 결정

## 3.RDS 다시 만들기

지난번에 비밀번호 자동생성으로 체크하고 넘겼는데 직접 지정해줘야 db연결할때 편하다.

보안그룹 새로 생성해서 디비 생성 후 한글설정 맞춰줌. 퍼블릭 액세스 예

## 4.MySQL 워크벤치 연결 성공

엔드포인트랑 포트만 필요하고 비번 따로 안쳤는데 연결됐다.

mysql 디비 생성

```jsx
create database awsdjangodb;
use awsdjangodb;
```

## 5.가상환경에 장고세팅

```jsx
ubuntu@ip-172-~$ python3 --version

sudo apt install python3-pip

pip3 install --user virtualenv

cat .profile

ubuntu@ip-172-~$ source ~/.profile

ubuntu@ip-172-~$ virtualenv --version
virtualenv 20.0.31 from /home/ubuntu/.local/lib/python3.6/site-packages/virtualenv/__init__.py

virtualenv ve

source ve/bin/activate

python3 -m pip install --upgrade pip

pip install django~=2.1

pip freeze

django-admin startproject awsdjangoproj

cd awsdjangoproj

python manage.py startapp boardapp
```

## 6.터미널에서 나노에디터로 settings.py 수정하다가 migrate, runserver 안되길래 cli 포기하고 로컬에서 장고프로젝트 시작 >> 근데 문제는 db 이름이었음

```jsx
'boardapp.apps.BoardappConfig',

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':	'awsdjangodb',
	},
    }
}

**LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'**
```

mysql에서 만든 db 네임이랑 똑같이 써야됨.

세팅파일 수정 후 뜨는 migrate 오류는 mysqlclient설치로 해결:

```jsx
(ve) awsdjangoproj % pip install mysqlclient
(ve) awsdjangoproj % python manage.py migrate
```

## 7.db연결 잘 해결되어서 테이블 만들기 시작.

mysql

```jsx
alter table `awsdjangodb` . `auth_user`
ADD COLUMN `phone` VARCHAR(45) NOT NULL after `date_joined`,
ADD COLUMN `date_of_birth` DATETIME NOT NULL after `phone`,
change COLUMN `date_joined` `date_joined` datetime NOT NULL after `email`,
change COLUMN `first_name` `first_name` VARCHAR(30) NOT NULL after `is_active`,
change COLUMN `is_staff` `is_staff` tinyint(1) NULL,
change COLUMN `is_active` `is_active`  tinyint(1) NULL;
```

```jsx
create table `board_categories` (
`id` int(10) NOT NULL auto_increment,
`category_type` varchar(45) not null default 'Nomal',
`category_code` varchar(100) not null,
`category_name` varchar(100) not null,
`category_desc` varchar(200) not null,
`list_count` int(10) default '20',
`authority` int(1) default '0',
`creation_date` datetime default current_timestamp,
`last_update_date` datetime default null,
primary key(`id`)
) ENGINE = InnoDB default charset=utf8
```

```jsx
CREATE TABLE `boards` (
`id` int(10) NOT NULL auto_increment,
`category_id` int(10) not null,
 `user_id` int(10)  not null,
`title` varchar(300) not null,
`content` text not null,
`register_date` datetime default current_timestamp,
`last_update_date` datetime default null,
`view_count` int(10) default '0',
`image` varchar(255) default null,
primary key(`id`),
key `board_category_fix_idx` (`category_id`),
key `board_user_fk_idx` (`user_id`),
constraint `board_category_fk` foreign key (`category_id`) references `board_categories` (`id`) on delete no action on update no action,
constraint `board_user_fk` foreign key (`user_id`) references `auth_user` (`id`) on delete no action on update no action
) ENGINE = InnoDB default charset=utf8
```

```jsx
CREATE TABLE `board_replies` (
`id` int(10) NOT NULL auto_increment,
`article_id` int(10) not null,
 `user_id` int(10)  not null,
`lever` tinyint(1) default '1',
`content` text not null,
`reference_reply_id` int(10) default '0',
`register_date` datetime default current_timestamp,
`last_update_date` datetime default null,
primary key(`id`),
key `user_reply_fix_idx` (`user_id`),
key `article_reply_fk_idx` (`article_id`),
constraint `article_reply_fk` foreign key (`article_id`) references `boards` (`id`) on delete no action on update no action,
constraint `user_reply_fk` foreign key (`user_id`) references `auth_user` (`id`) on delete no action on update no action
) ENGINE = InnoDB default charset=utf8
```

```jsx
CREATE TABLE `board_likes` (
`id` int(10) NOT NULL auto_increment,
`article_id` int(10) not null,
 `user_id` int(11)  not null,
`register_date` datetime default current_timestamp,
primary key(`id`),
key `like_article_fix_idx` (`article_id`),
key `like_user_fk_idx` (`user_id`),
constraint `like_article_fk` foreign key (`article_id`) references `boards` (`id`) on delete no action on update no action,
constraint `like_user_fk` foreign key (`user_id`) references `auth_user` (`id`) on delete no action on update no action
) ENGINE = InnoDB default charset=utf8
```

`“create is not valid input at this position ”`

이 에러는 위에 쿼리문 안지우고 연속으로 이어써서 그럼.

## 8.장고에서 models.py 모델 생성

- 코드 다시보기

## 9.url 설정

## 10.기본 레이아웃 설정

내가 바꿀거다. jsp를 보고나니까 템플릿코드에 좀더 익숙해졌다. 템플릿코드 자동완성 익스텐션 찾아보기

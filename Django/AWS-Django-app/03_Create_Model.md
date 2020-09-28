# ch16 세팅시작

## 1.aws - cli 설치부터 시작~

`brew install awscli`

`aws configure` 

## 2.vscode-ftp 연결 성공

나는 이거 하면 우분투에 있는 장고 앱을 여기서 할 수 있는줄 알았음. 연결되서 기분은 좋은데 이 방법이 아니었다.  
gui사용해서 장고 코딩하려면 우분투 가상환경 머신 써서 해야하는듯

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
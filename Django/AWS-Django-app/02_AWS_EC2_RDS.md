# AWS
AWS는 아마존의 클라우드 컴퓨팅 사업이다. 아마존이 대량의 웹서버를 미리 준비해서 기업이나 개인에게 사용량과 기한에 따라서 비용을 받고 제공하는 형태다. 서버를 하루 종일 시간 투자하며 직접 관리 하지 않아도 되고, 필요한 만큼만 서비스를 사용하고 비용을 지불하면 되기 때문에 비용과 유지보수 면에서 장점이 크다.

# EC2
Elastic Compute Cloud는 개발자에게 가상화된 서버를 하나의 인스턴스 형태로 제공한다. 다양한 운영체제를 선택할 수 있다.

### ec2 인스턴스 생성
1. 아마존 웹서비스에서 계정 만들고 리전은 서울
2. ec2 인스턴스 생성(1년무료 프리 티어)
3. 운영체제는 우분투
3. 인스턴스 생성시 세부 정보는 딱히 건드릴 게 없다.
4. 키페어 잘 보관

### 터미널 환경에서 서버 연결
1. 인스턴스의 public DNS(IPv4) 확인
2. 보안그룹 인바운드 포트 확인
3. SSH 연결. 
`ssh -i /[키페어 경로] [ubuntu]@[서버주소]`

(이제 개발도구 사용 원격연결 봐야함. vscode ftp-simple 사용하자)  
(aws-cli 설치하기)


# RDS
AWS에서 관계형 데이터베이스를 설정할 수 있다. MySQL, Oracle ...  

### DB 인스턴스 생성
1. MySQL선택
2. PVC 보안그룹 새로 생성
3. 나머지 세부정보는 안건드림

### 파라미터 그룹 설정을 안했구나

### MySQL 연결
MySQL 새로 설치하고 연결하려는 과정에서 삽질이 이어졌다.  
1. brew로 mysql 설치하고 홈페이지에서 workbench 다운  
2. 서버시작 `mysql.server start`  
3. 워크벤치 새 커넥션 -> db인스턴스 주소(RDS 엔드포인트 참고), 포트, 계정(rds db계정), 비번 입력  
4. 난 계속 커넥션 연결에 실패했다.  
5. db 인스턴스 수정 -> 퍼블릭 액세스 가능성 yes  (**보안취약**)   
**연결실패 메세지** : Your connection attempt failed for user ' ' to the MySQL server at database~  


## 선택지
1. IDE연결, RDS 다시, mysql workbench 서버등록 다시
3. 로컬에서 앱 만들고 배포할때만 사용

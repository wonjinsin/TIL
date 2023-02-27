### Real MYSQL 8.0 1권
- 2장. 설치와 설정
	- 서버 업그레이드
		1. MYSQL 서버의 데이터 파일을 그대로 두고 업그레이드하는 방법
			- 인플레이스 업그레이드 라고함
			- 업그레이드시 한번에 한단계씩만 가능해서, 버전이 많이 다르면 여러번 해줘야 함
		2. mysqldump 도구등을 이용해서 덤프후 이동
			- 논리적 업그레이드 라고함
	- 서버 설정
		- 글로벌 변수와 세션변수
			- 글로벌 변수는 MYSQL 서버 인스턴스에서 전체적으로 영향을 미치는 시스템 변수
			- 세션 변수는 개별 커넥션마다 다른 변수 (autocommit을 1로 하면 내가 접속한 커넥션의 세션에서만 on이 됨, 다른거 말고)
		- 정적변수와 동적 변수
			- 동적변수는 서버가 기동중인 상태애서 변경 가능
			- MYSQL 8.0부터는 SET PERSIST를 이용하면 현재 기동중인 MYSQL 뿐만아니라, 껐다 켰을때도 영구적으로 설정파일에도 기록됨
			```
			SET GLOBAL max_connection=5000; // Global 변수 수정
			SET PERSIST max_connection=5000; // Global 변수 수정과 mysqld-auto.cnf에도 기록됨
			SET PERSIST_ONLY max_connection=5000; // mysqld-auto.cnf에만 기록됨 
			```
	
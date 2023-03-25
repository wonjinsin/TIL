## binlog
- 각 쿼리들이 기록되는 로그
- readonly는 master의 binlog를 읽고, 동기화함

### mysql의 binlog확인
```
SHOW BINARY LOGS;
```

### mysql의 binlog retention 확인
- binlog retention hours 만큼 binlog 기록함
```
call mysql.rds_show_configuration;
```

### mysql binlog local에 저장
```
mysqlbinlog --read-from-remote-server --host=db-test.c7a9eoq5qsx7.ap-northeast-2.rds.amazonaws.com --port=3306 --user root --password --raw --result-file=/tmp/ mysql-bin-changelog.000005
```

### 저장된 binlog sql파일로 복원
```
mysqlbinlog mysql-bin-changelog.000005 > binlog5.sql
```

### 특정 데이터베이스의 지정된 날짜 동안의 bin로그 텍스트로 변환
mysqlbinlog --database=DB이름 --start-date="시작날짜" --stop-date="종료날짜" "mysql bin로그 경로" > binlog.sql
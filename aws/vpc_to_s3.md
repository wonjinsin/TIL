## 개요

private(rds 접속용), public subnet(외부 api 접속용)에 연결돼있는 lambda에서 s3에서 getObject를 할때 timeout이 나는 문제가 발생
이게 lambda가 private이나 public 둘중 하나에서 뜨기 때문에 만약에 private에서 뜨면은 외부랑 접속이 안됨

## 수정

vpc endpoint를 s3를 연결해서 만들고, private subnet에 설정을 해줌

참고: https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html#types-of-vpc-endpoints-for-s3

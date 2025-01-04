### private ec2에 연결하는 방법

1. private subnet에 natgateway(외부 nat) 연결(public), nat gateway자체는 public subnet을 바라보고, private subnet이 nat gateway를 route table에서 바라 봐야함

2. ec2는 iam(ssm, AmazonSSMManagedInstanceCore을 가지고 있어야함)

3. security group, all tcp가 해당 VPC의 CIDR INBOUND를 허락하게끔

4. ec2는 해당 private subnet에 생성, iam은 위에서 생성한 iam

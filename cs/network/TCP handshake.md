# TCP handshake

## TCP 3way handshake란?
> TCP 3way Handshake는 TCP/IP프로토콜을 이용해서 통신을 하는 응용프로그램이 데이터를 전송하기 전에 
먼저 정확한 전송을 보장하기 위해 상대방 컴퓨터와 사전에 세션을 수립하는 과정을 의미한다.<br>
즉, 서로 연결이 잘되있는지 확인하는 과정

### SYN, SYN/ACK, ACK
- SYN
  - 클라이언트가 서버에게 접속을 요청하는 SYN flag 패킷 보냄
  - 클라이언트는 SYN/ACK를 기다리는 SYN_SENT 상태가 됨
  - 서버는 Listen 상태여야로 포트 서비스가 열려 있어야함(서버가 다음 상태를 하기 위해선)

- SYN/ACK
  - 서버가 SYN을 받고, 클라이언트에게 요청을 수락한다는 ACK와 SYN flag(클라이언트에게 포트를 열어달라는)가 설정된 패킷을 발송
  - 서버의 상태는 SYN_RECEIVE가 되고, 발송 후 클라이언트의 응답을 기다림

- ACK
  - 클라이언트는 서버에게 서버로부터 응답을 받았다는 ACK flag를 보내주고, 그 이후에는 데이터를 전송하면 된다

## TCP 4way handshake란?
> TCP 3way가 세션을 생성시키기 위에 작동한다면, TCP 4way는 세션을 종료 시키는데 사용 됨

### FIN, ACK, FIN, ACK
- FIN
  - 클라이언트가 서버에게 연결게 종료 하겠다는 FIN flag 전송

- ACK
  - 서버는 클라이언트에게 온 요청을 받았다는 ACK flag를 클라이언트에게 보낸다
  - 데이터를 보내는 동안 TIME_OUT 상태가 됨

- FIN
  - TIME_OUT 상태의 서버는 데이터를 모두 보내고, 연결이 종료되었다고 클라이언트에게 FIN flag을 보냄

- ACK
  - 클라이언트는 서버에게 FIN flag를 받았다는 ACK flag를 보냄
  - 클라이언트는 아직 서버에게 못받은 데이터가 있을 경우를 대비해 잉여 패킷을 기다리는 과정을 가짐


참고: <br>
https://mindnet.tistory.com/entry/네트워크-쉽게-이해하기-22편-TCP-3-WayHandshake-4-WayHandshake
https://asfirstalways.tistory.com/356
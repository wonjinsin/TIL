bytes(10)    # 0이 10개 들어있는 바이트 객체 생성, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
bytes([10, 20, 30, 40, 50])    # 리스트로 바이트 객체 생성, b'\n\x14\x1e(2'
bytes(b'hello')    # 바이트 객체로 바이트 객체 생성, b'hello

'hello'.encode()     # str을 bytes로 변환, b'hello'
b'hello'.decode()    # bytes를 str로 변환 'hello'

x = '안녕'.encode('euc-kr')  # x.decode('euc-kr'), '안녕'
y = '안녕'.encode('utf-8')  # y.decode('utf-8'), '안녕'

bytes('안녕', encoding='euc-kr')  # b'\xbe\xc8\xb3\xe7'
bytearray('안녕', encoding='cp949')  # bytearray(b'\xbe\xc8\xb3\xe7')

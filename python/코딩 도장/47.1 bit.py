bin(13)    # 10진수 13을 2진수로 변환
'0b1101'  # 0b는 2진수라는 의미, 0o는 8진수, 0x는 16진수
0b1101     # 2진수 1101을 10진수로 변환, 이건 즉시 변환
13


bin(0b1101 & 0b1001)    # 비트 AND '0b1001'
13 & 9                  # 비트 AND 9
bin(0b1101 | 0b1001)    # 비트 OR '0b1101'
13 | 9                  # 비트 OR 13
bin(0b1101 ^ 0b1001)    # 비트 XOR '0b100'
13 ^ 9                  # 비트 XOR 4
bin(~0b1101)            # 비트 NOT '-0b1110'
~13                     # 비트 NOT -14

0b0011 << 2    # 비트를 왼쪽으로 2번 이동 12
bin(12)  # '0b1100'
0b1100 >> 2    # 비트를 오른쪽으로 2번 이동 3
bin(3)  # '0b11'

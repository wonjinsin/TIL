'I am %s.' % 'james'
'I am %d years old.' % 20
'%f' % 2.3  # 2.300000
'%.2f' % 2.3  # 2.30
'%.3f' % 2.3  # 2.300
'%10s' % 'python'  # '    python'
'%-10s' % 'python'  # 'python    '
'Today is %d %s.' % (3, 'April')

# format method
'Hello, {0}'.format('world!')  # '{인덱스}'.format(값)
'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
'{0} {0} {1} {1}'.format('Python', 'Script')  # 'Python Python Script Script'
'Hello, {} {} {}'.format('Python', 'Script', 3.6)  # 'Hello, Python Script 3.6'
'Hello, {language} {version}'.format(
    language='Python', version=3.6)  # 'Hello, Python 3.6'

# 문자열 포매팅에 변수를 그대로 사용하기
w = "world"
f'Hello {w}'

# format 메서드로 문자열 정렬하기
# 왼쪽 정렬 '{인덱스:<길이}'.format(값)
'{0:<10}'.format('python')  # 'python    '
# 오른쪽 정렬 '{인덱스:>길이}'.format(값)
'{0:>10}'.format('python')  # '    python'
'{:>10}'.format('python')  # '    python', 인덱스 사용안하면 생략가능

# 숫자 개수 맞추기
'%03d' % 1  # '001'
'{0:03d}'.format(35)  # '035'
'{0:0<10}'.format(15)    # 길이 10, 왼쪽으로 정렬하고 남는 공간은 0으로 채움

s = 'Hello, world!'
s = s.replace('world', 'Python')

# 문자열 'apple'에서 a를 1, e를 2, i를 3, o를 4, u를 5로 바꿉니다.
table = str.maketrans('aeiou', '12345')
'apple'.translate(table)  # '1ppl2'

# apple-pear-grape-pineapple-orange
'-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])

'python'.upper()  # PYTHON

'PYTHON'.lower()  # python

'   Python   '.lstrip()  # 'Python   '
'   Python   '.rstrip()
'   Python   '.strip()

', python.'.lstrip(',.')  # ' python.'
', python.'.rstrip(',.')  # ' python.'
', python.'.strip(',.')  # ' python.'

# 'python'의 길이를 10으로 만든 뒤 왼쪽으로 정렬하고 남는 공간을 공백 4칸으로 채웁니다.
'python'.ljust(10)  # 'python    '
'python'.rjust(10)  # '    python'

# 가운데 정렬
'python'.center(10)  # '  python  '
'python'.center(11)  # '   python  ', 왼쪽에 공백 3칸

# method chaning
'python'.rjust(10).upper()  # '    PYTHON'

'35'.zfill(4)        # 문자 앞에 0을 채움, '0035'

'apple pineapple'.find('pl')  # 2, 인덱스 찾기
'apple pineapple'.find('xy')  # -1
'apple pineapple'.rfind('pl')  # 12
'apple pineapple'.index('pl')  # 이것도 인덱스 찾지만 없으면 에러
'apple pineapple'.rindex('pl')  # 12
'apple pineapple'.count('pl')  # 2

# re.match('패턴', '문자열')

import re
re.match('Hello', 'Hello, world!')
# 문자열이 있으므로 정규표현식 매치 객체가 반환됨, <_sre.SRE_Match object; span=(0, 5), match='Hello'>
re.match('Python', 'Hello, world!')     # 문자열이 없으므로 아무것도 반환되지 않음

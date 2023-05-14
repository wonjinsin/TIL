from fractions import Fraction
from decimal import Decimal
import sys
import math
0.1 + 0.2  # 0.30000000000000004
"""
1부터 10까지 정수는 10개지만 실수는 무한히 많습니다.
컴퓨터에서는 숫자를 비트로 표현하는데 실수는 유한개의 비트로 정확하게 표현할 수가 없습니다.
따라서 실수는 유한개의 비트를 사용하여 근삿값으로 표현합니다. 즉, 0.30000000000000004는 0.3을 표현한 근삿값입니다.
"""

0.1 + 0.2 == 0.3  # False

# 비교법 1
x = 0.1 + 0.2
math.fabs(x - 0.3) <= sys.float_info.epsilon

# 비교법 2
math.isclose(0.1 + 0.2, 0.3)  # True

Decimal('0.1') + Decimal('0.2')  # Decimal('0.3')

# 10을 3으로 나누면 순환소수 3.33333...이지만 분수 3분의 10으로 표현 Fraction(10, 3)
Fraction('10/3')

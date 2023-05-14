"""
폴더(디렉터리) 안에 __init__.py 파일이 있으면 해당 폴더는 패키지로 인식됩니다. 
그리고 기본적으로 __init__.py 파일의 내용은 비워 둘 수 있습니다(파이썬 3.3 이상부터는 __init__.py 파일이 없어도 패키지로 인식됩니다. 
하지만 하위 버전에도 호환되도록 __init__.py 파일을 작성하는 것을 권장합니다).
"""

# 현재 패키지의 operation, geometry 모듈을 가져옴
"""
from . import operation    # 현재 패키지에서 operation 모듈을 가져옴
from . import geometry     # 현재 패키지에서 geometry 모듈을 가져옴
"""
"""
import calcpkg    # calcpkg 패키지만 가져옴, 위에처럼 선언하면 다른데서 이렇게 쓸수있음 
 
print(calcpkg.operation.add(10, 20))    # operation 모듈의 add 함수 사용
print(calcpkg.operation.mul(10, 20))    # operation 모듈의 mul 함수 사용
 
print(calcpkg.geometry.triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(calcpkg.geometry.rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용
"""

# 현재 패키지의 operation, geometry 모듈에서 각 함수를 가져옴
"""
from .geometry import triangle_area, rectangle_area
from .operation import add, mul
or
from .operation import *    # 현재 패키지의 operation 모듈에서 모든 변수, 함수, 클래스를 가져옴
from .geometry import *     # 현재 패키지의 geometry 모듈에서 모든 변수, 함수, 클래스를 가져옴
"""
"""
사용하는 쪽
from calcpkg import *    # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴, 다른데서 아래처럼 사용가능
 
print(add(10, 20))    # operation 모듈의 add 함수 사용
print(mul(10, 20))    # operation 모듈의 mul 함수 사용
 
print(triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용
"""

__all__ = ['add', 'triangle_area']    # calcpkg 패키지에서 add, triangle_area 함수만 공개

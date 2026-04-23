'''
import = 다른 파일에서 기능 가져오기
마치 레고블록처럼 내가 다 만들 필요 없이 누군가 만들어둔 블록을 가져다 사용하는 것

import 기능
기능.특정기능사용()

from 기능 import 특정기능3번, 특정기능4번

특정기능3번()
특정기능4번()

굳이 기능. 붙이지 않고 import 뒤에서 사용하겠다 표기한 기능명칭을 직접적으로 작성할 수 있다.

import math
from math import sqrt

둘다 math 라는 곳에서 기능을 가져오는 건데 문제가 되지 않나요?! ==> 문제 안된다.

sqrt 는 math.을 앞에 붙이지 않고 작성할 것이다.
sqrt 이외 나머지 기능들은 math. 에서 가져온 기능이다 라고 앞에 붙여서 사용할 뿐
'''

import math # math 안에 들어있는 기능 모~두 가져오기
print(math.pi)
print(math.floor(3.7)) # 파이썬 자체에서 제공하지 않아 math 부서에서 만들어서 제공 내림
print(math.ceil(3.7))  # 파이썬 자체에서 제공하지 않아 math 부서에서 만들어서 제공 오름
print(round(3.7)) # 반올림 파이썬 자체에서 제공하는 기능이므로 math에서 만들지 않았다.

from math import sqrt  # math 안에서 sqrt 라는 기능만 가져와서 사용하겠다.
print(sqrt(16))  # 대놓고 math 에서 sqrt 만 가져와서 사용한다 했기 때문에 math. 을 생략



"""
모듈 = 도구 하나
라이브러리 = 도구 모음함
프레임워크 = 공장 시스템





"""
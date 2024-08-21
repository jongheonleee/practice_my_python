# 복잡한 형태
from functools import reduce
from operator import mul

def fact(n) :
  return reduce(lambda a, b : a*b, range(1, n+1))

# 개선된 버전
def fact2(n) :
  return reduce(mul, range(1, n+1))

# methodcaller 사용
from operator import methodcaller

s = 'The Time has come'
upcase = methodcaller('upper')
res = upcase(s)
print(res)
hiphenate = methodcaller('replace', ' ', '-')
res = hiphenate(s)
print(res)

# partial()로 인수 고정 활용해보기,
# 첫 번째는 콜러블, 그 뒤로는 바인딩할 위치 인수와 키워드 인수가 원하는 만큼나옴
from functools import partial

triple = partial(mul, 3)
res = triple(7)
print(res)

import unicodedata, functools

nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print(s1 + ", " + s2)
print(s1 == s2)
print(nfc(s1) == nfc(s2))
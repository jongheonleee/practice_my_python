# collections.dict
# - OrderDict : 순서 보장
# - ChainMap : 계층형 맵, 탐색 범위 : 로컬 - 글로벌 - 빌트인
# - Counter : 모든 키에 대해 카운팅 매핑
# - UserDict : 상속 용도, 상속해서 사용자가 정의
import collections


list = [('a', 1), ('b', 2), ('d', 3), ('c', 4)]
target = 'abcdefacvdaaa'

ordered = collections.OrderedDict(list)
print(ordered)
for k, v in ordered.items() :
  print(k + ' : ' + str(v))

chained = collections.ChainMap(list)
print(chained)
print(chained.items())

counter = collections.Counter(target)
print(counter)
print(counter.most_common())


class StrKeyDict(collections.UserDict) : # MutableMapping 상속하므로 가변 객체임

  def __missing__(self, key):
    if isinstance(key, str) :
      raise KeyError(key)

    return self[str(key)]

  # Mapping.get() 을 상속받아서 사용함. 굳이 get() 구현할 필요 없음

  def __contains__(self, key):
    return str(key) in self.data

  def __setitem__(self, key, value):
    self.data[str(key)] = value

d = StrKeyDict(list)
print(d)
d[12] = 30
print(d.data)
d['a'] = 30
print(d.data)
print(dir(d))

# dict에서 읽기 전용 mappingproxy 객체를 생성하는 MappingProxyType이 있음
from types import MappingProxyType

d = {1 : 'A'}
d_proxy = MappingProxyType(d)
d_proxy

print(d_proxy[1])

d_proxy[1] = '3333'

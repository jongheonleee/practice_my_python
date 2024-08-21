s = {1, 2, 1, 1, 3}
print(s)

# 집합 요소는 해시할 수 있어야함, 기본적으로 중복 항목을 제거함
l = [1, 2, 3, 4, 4, 5, 6, 7, 7]
not_duplicated_list = list(set(l))
print(not_duplicated_list)

# 집합 사용할 때 {} 사용하는게 성능이 좋음
from dis import dis

print(dis('{1}'))
print(dis('set([1])'))

# 불변 집합은 frozenset() 임
fs = frozenset(range(10))
print(fs)
print(dir(s))
print(dir(fs)) # add, clear, update 메서드가 없음

# 지능형 집합
from unicodedata import name

s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(s)


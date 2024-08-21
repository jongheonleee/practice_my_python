class StrKeyDict0(dict) :

  def __missing__(self, key) :
    if isinstance(key, str) : # 타입 확인
      raise KeyError(key)
    return self[str(key)] # iv 값 반환

  def get(self, key, default=None):
    try : # iv 탐색 및 반환
      return self[key] # __getitem__ 호출
      # KeyError 발생 x -> __missing__() 호출
    except KeyError : # 없으면 KeyError
      return default

  def __contains__(self, key):
    return key in self.keys() or str(key) in self.keys() # in 연산으로 순차적으로 탐색

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d['4'])
# print(d[1])


print(d.get('2'))
print(d.get('4'))
print(d.get('1', 'N/A'))

print(dir(d))
print(d.items())
print(2 in d)
print(1 in d)

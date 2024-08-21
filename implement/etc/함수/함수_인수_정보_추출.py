import inspect

from clip import clip

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

# 좀 더 명확하게 나타내기
from inspect import signature

sig = signature(clip)
print(sig)
print(str(sig))

for name, param in sig.parameters.items() :
  print(param.kind, ':', name, '=', param.default)



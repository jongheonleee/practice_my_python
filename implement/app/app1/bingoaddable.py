import itertools
from tombola import Tombola
from bingo import BingoCage

class AddableBingoCage(BingoCage) :
  def __add__(self, other):
    if isinstance(other, Tombola) :
      return AddableBingoCage(self.inspect() + other.inspect())

    else : # __radd__ 호출하는 것 보다 TypeError 발생시키는 것이 좋음
      return NotImplemented

  def __iadd__(self, other):
    if isinstance(other, Tombola) :
      other_iterable = other.inspect()

    else :
      try :
        other_iterable = iter(other)

      except TypeError :
        self_cls = type(self).__name__
        msg = 'right operand in += must be {!r} or an iterable'
        raise TypeError(msg.format(self_cls))

    self.load(other_iterable)
    return self

# 간단한 사용
vowels = 'AEIOU'
globe = AddableBingoCage(vowels)
print(globe.inspect())
print(globe.pick() in vowels)
print(len(globe.inspect()))
globe2 = AddableBingoCage('XYZ')
globe3 = globe + globe2
print(len(globe3.inspect()))
void = globe + [10, 20]

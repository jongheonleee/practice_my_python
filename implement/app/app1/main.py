from tombola import Tombola
from tombolist import TomboList

print(issubclass(TomboList, Tombola))

t = TomboList(range(100))
print(isinstance(t, Tombola))

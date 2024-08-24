import itertools


gen = itertools.takewhile(lambda n : n < 3, itertools.count(1, .5))
list(gen)

def aritprog_gen(begin, step, end=None) :
  first = type(begin + step)(begin)
  ap_gen = itertools.count(first, step)

  if end is not None :
    ap_gen = itertools.takewhile(lambda n : n < end, ap_gen)

  return ap_gen
from functools import wraps

def coroutine(func) :
  """데커레이터 : func를 기동해서 첫 번째 yield까지 진행함"""
  @wraps(func)
  def primer(*args, **kwargs) :
    gen = func(*args, **kwargs)
    next(gen)
    return gen
  return primer()
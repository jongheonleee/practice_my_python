def averager() :
  """이동 평균 코루틴 코드"""
  total = 0.0
  count = 0
  average = None

  while True :
    term = yield average
    total += term
    count += 1
    average = total/count

coro_avg = averager()
print(next(coro_avg)) # 코루틴 가동 시킴
print(coro_avg.send(10))
print(coro_avg.send(20))
print(coro_avg.send(30))
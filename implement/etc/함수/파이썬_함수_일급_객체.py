# 일급객체?
# 1. 런타임에 생성할 수 있어야함
# 2. 변수나 구조체에 할당 할 수 있음
# 3. 함수의 인수로 전달할 수 있음
# 4. 함수의 반환값으로 사용할 수 있음

def fact(n) :
  """return n!!"""
  return 1 if n < 2 else n * fact(n-1)

print(fact(15))
print(fact.__doc__)
print(type(fact))
print(dir(fact))


# 함수를 객체로서 사용해보기, 일급 객체 특징 이해하기
f = fact
print(f)
print(f(5))
print(map(f, range(15)))
print(list(map(f, range(15))))

# 고위함수? 함수를 인수로 받음, 함수를 반환함
sample = ['aaaaaa', 'kkk', 'eee', 'b', 'c', 'd']
sorted_sample = sorted(sample, key=len)
print(sorted_sample)

def reverse(word) :
  return word[::-1]

res = reverse('test!')
print(res)
sorted_sample = sorted(sample, key=reverse)
print(sorted_sample)

list = [fact(n) for n in range(10) if n % 2 == 0]
print(list)
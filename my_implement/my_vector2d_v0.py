import math
from array import array

"""
내가 배운 것 
- 1. typecode의 의미 : array, struct에서 데이터(iv)를 어떤 타입으로 저장할지 명시함 
- 2. tuple() 활용 : tuple(self) -> self의 iv로 구성된 튜플 생성. 이를 __eq__, __str__에서 활용함 
"""


class MyVector2d :

  # typecode가 'd'인 경우, 이는 더블형 부동소수점 수(64비트 부동소수점 수)를 의미
  # 이는 array 모듈과 struct 모듈 등에서 데이터의 정확한 형식을 지정하는 데 사용함
  typecode = 'd'

  def __init__(self, x, y):
    """객체의 iv를 초기화함"""
    # iv 초기화
    self.x = float(x)
    self.y = float(y)

  def __iter__(self):
    """객체를 시퀀스처럼 사용할 수 있게함. 즉, 일일이 값 꺼내는 지능형 제너레이터 만듦"""
    # iv를 일일이 반환하는 제너레이터를 반환함
    return (i for i in (self.x, self.y))

  # 개선 -> tuple(self) == tuple(other)
    # tuple(self)를 하면 self에 있는 모든 iv를 __iter__ 호출해서 튜플에 담음
    # 새로운 tuple을 반환함
    # 즉, 튜플로서 iv의 모든 요소를 비교함
  def __eq__(self, other):
    """객체의 동등성을 비교하기 위함"""
    # 같은 타입인지 확인, 아니면 TypeError
    if not isinstance(other, MyVector2d) : # 왠만하면 if isinstance()없는 코드를 작성해야함
      raise TypeError

    # __iter__를 호출해서 모든 iv의 값이 일치하는지 확인
    return all(a == b for a, b in zip(self, other))

  def __repr__(self):
    """객체를 문자열로 표현(repr)"""
    # 반환 형식 템플릿 설정
    template = '{}({!r}, {!r})'

    # 클래스 이름 조회
    cls_name = type(self).__name__

    # iv 조회해서 해당 템플릿에 넣어서 반환
    return template.format(cls_name, *self)

  # 개선 -> str(tuple(self))
    # tuple(self)를 통해서 self의 모든 iv를 담은 튜플을 만듦
    # 이를 str()으로 호출해서 문자열로 반환
  def __str__(self):
    """객체를 문자열로 표현(str)"""
    # 반환 형식 템플릿 설정
    template = '({!r}, {!r})'

    # iv 조회해서 해당 템플릿에 넣어서 반환
    return template.format(*self)

  def __bytes__(self):
    """
    __bytes__ 메서드는 객체를 바이트로 표현하기 위해 typecode와 데이터를 바이트로 변환하고 이를 결합한 결과를 반환
    """""
    # ord()는 단일 문자인 self.typecode를 아스키코드 값으로 나타냄
    # 이를 bytes()를 호출해서 바이트코드로 다시 표현함
    # 또한, 모든 iv를 self.typecode 타입의 배열로 표현하고 이를 bytes()를 호출해서 바이트 시퀀스 만듦
    return bytes(ord(self.typecode)) + bytes(array(self.typecode, self))


  def __abs__(self):
    """(0, 0)과 (x, y) 사이의 거리를 반환"""
    return math.hypot(self.x, self.y)

  def __bool__(self):
    """해당 객체가 Truchy, Falchy인지 반환"""
    return bool(abs(self))

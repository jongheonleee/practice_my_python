# 🛠️ 파이썬 OOP 연습 

### 📋 구현 대상 
> ### 1. vector2d_v0 
> - [테스트 코드](learning/test_vector2d_v0.py)
> - [구현 코드](my_implement/my_vector2d_v0.py)

<br>


### 📌 학습 과정 소개
> 1. 학습 테스트 코드를 작성해서 구현해야할 객체를 분석합니다.
> 2. 학습 테스트 코드를 기반으로 객체를 구현합니다(일종의 TDD 적용)
> 3. 기존의 학습 테스트 코드를 TDD로서 활용합니다. 즉, 분석한 객체 부분을 구현할 객체로 대체합니다.

<br>

### 🧑🏻‍🏫 학습 과정 구체적으로 소개 

- 구현할 객체(플루언트 파이썬 책에 나온 객체)

```python
from array import array
import math


class Vector2d:
  typecode = 'd'

  def __init__(self, x, y):
    self.x = float(x)
    self.y = float(y)

  def __iter__(self):
    return (i for i in (self.x, self.y))

  def __repr__(self):
    class_name = type(self).__name__
    return '{}({!r}, {!r})'.format(class_name, *self)

  def __str__(self):
    return str(tuple(self))

  def __bytes__(self):
    return (bytes([ord(self.typecode)]) +
            bytes(array(self.typecode, self)))

  def __eq__(self, other):
    return tuple(self) == tuple(other)

  def __abs__(self):
    """math.hypot(x, y) 함수는 두 점 (0, 0)과 (x, y) 사이의 유클리드 거리를 계산"""
    return math.hypot(self.x, self.y)

  def __bool__(self):
    return bool(abs(self))

```

- 학습 테스트
  - unittest 라이브러리 활용
  - 학습 목록 작성. 일종의 기능 분석 
  - 그에 맞는 테스트 코드 작성
  
```python
from unittest import TestCase
from implement.pythonic_object.vector2d_v0 import Vector2d # 분석 대상이 되는 클래스
from my_implement.my_vector2d_v0 import MyVector2d # 추후에 구현할 클래스 

# Vector 학습 및 검증 테스트 코드
class TestVector2d_v0(TestCase):
  # 테스트 대상 기능 목록 및 테스트 범위 작성
  # 1. 생성자 호출 : __init__()
  ### - 매개변수 두개로 이루어진 튜플 전달할 경우 성공적으로 인스턴스를 생성함
  ### - 숫자가 아닌 매개변수 두개로 이루어진 튜플을 전달할 경우 인스턴스 생성을 하지 못함 -> TypeError
  ### - 매개변수가 두개가 아닌 경우, 1개나 3개 ...
  #### - 2개 보다 적을 경우 실패 -> TypeError
  #### - 2개 보다 많은 경우 성공

  ### > 이 이후에 테스트 전제 조건 : 인스턴스를 성공적으로 생성했다

  # 2. 반복처리 기능 : __iter__()
  ### - iv를 1, 2를 가지고 있음, 1, 2를 반복해서 출력하는 제너레이터를 생성함.
  ### - iv를 1.0, 2.0를 가지고 있음, 1.0, 2.0를 반복해서 출력하는 제너레이터를 생성함
  ### - iv를 10.0, 25.0를 가지고 있음, 10.0, 25.0를 반복해서 출력하는 제너레이터를 생성함

  # 3. 객체 문자열 표현(개발자) : __repr__()
  ### > 출력 형식 예시 : Vector2d(1.0, 2.0)
  ### - iv를 1, 2를 가지고 있음 -> Vector2d(1.0, 2.0)
  ### - iv를 1.0, 2.0을 가지고 있음 -> Vector2d(1.0, 2.0)
  ### - iv를 10.0, 25.0을 가지고 있음 -> Vector2d(10.0, 25.0)

  # 4. 객체 문자열 표현(개발자) : __str__()
  ### > 출력 형식 예시 : (1.0, 2.0)
  ### - iv를 1, 2를 가지고 있음 -> (1.0, 2.0)
  ### - iv를 1.0, 2.0을 가지고 있음 -> (1.0, 2.0)
  ### - iv를 10.0, 25.0을 가지고 있음 -> (10.0, 25.0)

  # 5. 객체를 바이트 시퀀스로 표현 : __bytes__()
  ### > 출력 형식 예시 : b'd\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@'
  ### - iv를 1, 2를 가지고 있음 -> b'd\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@'
  ### - iv를 1.0, 2.0을 가지고 있음 -> b'd\x00\x00\x00\x00\x00\x00$@\x00\x00\x00\x00\x00\x00(@'
  ### - iv를 10.0, 25.0을 가지고 있음 -> b'd\x00\x00\x00\x00\x00\x00\xe0?333333\x0b@'

  # 6. 객체 동등성 비교 : __eq__()
  ### - iv를 1, 2를 가지고 있는 벡터 2개 -> True
  ### - iv를 1.0, 2.0을 가지있는 벡터와 iv 1, 2를 가지고 있는 벡터 -> True
  ### - iv를 1.0, 2.0을 가지있는 벡터와 iv 10.0, 25.0를 가지고 있는 벡터 -> False

  # 7. 객체의 크기를 표현 : __abs__()
  ### > math.hypot(x, y) 함수는 두 점 (0, 0)과 (x, y) 사이의 유클리드 거리를 계산해서 반환
  ### - iv를 1, 2를 가지고 있음 -> 2.23606797749979
  ### - iv를 1.0, 2.0을 가지고 있음 -> 2.23606797749979
  ### - iv 10.0, 25.0를 가지고 있음 -> 26.925824035672523

  # 8. 객체가 Truchy, Falchy인지 표현 : __bool__()
  ### > 객체의 크기가 0이면 False, 그게 아니면 True
  ### - iv가 0, 0를 가지고 있음 -> False
  ### - iv가 1.0, 2.0을 가지고 있음 -> True
  ### - iv가 10.0, 25.0을 가지고 있음 -> True


  # 1. 생성자 호출 테스트 로직
  def run_success_create_test_with_params(self, func, param, expected):
    actual = func(*param)
    self.assertEquals(actual, expected)
    print(actual.__bytes__())

    for a, b in zip(actual, expected) :
      self.assertEquals(a, b)

  def run_fail_create_test_with_params(self, func, param, expected):
    with self.assertRaises(expected) as context :
      func(param)

  # 1. 생성자 호출 테스트
  def test_create(self):
    # 성공 테스트 더미
    success_dummy = [
      # 매개변수가 2개이며 타입이 숫자형인 경우
      (Vector2d, (1, 2), Vector2d(1, 2)),
      (Vector2d, (10.0, 12.0), Vector2d(10.0, 12.0)),
      (Vector2d, (0.5, 3.4), Vector2d(0.5, 3.4))
    ]


    # 실패 테스트 더미
    fail_dummy = [
      ### 매개변수 타입 충족 x
      (Vector2d, (None, None), TypeError),
      (Vector2d, 'abcd', TypeError),
      (Vector2d, ('!@#$', '!@#'), TypeError),
      (Vector2d, ('a', 'b'), TypeError),

      ### 매개변수 개수 충족 x
      (Vector2d, (), TypeError),
      (Vector2d, (10.0), TypeError),

      # 매개변수가 2개보다 많지만, 타입이 숫자형인 경우
      (Vector2d, (1, 2, 3, 4), TypeError),
      (Vector2d, (10.0, 12.0, 23, 24), TypeError),
      (Vector2d, (0.5, 3.4, 0.1), TypeError)
    ]


    # 성공 테스트 실행
    for func, param, expected in success_dummy :
      with self.subTest(func = func, param = param, expected = expected) :
        self.run_success_create_test_with_params(func, param, expected)

    # 실패 테스트 실행
    for func, param, expected in fail_dummy :
      with self.subTest(func = func, param = param, expected = expected) :
        self.run_fail_create_test_with_params(func, param, expected)

  # 2. 반복 처리 호출 테스트 로직
  def run_success_iterator_test_with_params(self, func, param, expected):
    # 벡터 생성
    actual = func(*param)
    self.assertIsInstance(actual, Vector2d)

    # 제너레이터 조회
    actual_iterator = actual.__iter__()

    # 내용 비교
    for a, b in zip(expected, actual_iterator) :
      self.assertEquals(a, b)

  # 2. 반복 처리 테스트
  def test_iterator(self):
    # 성공 테스트 더미
    success_dummy = [
      (Vector2d, (1, 2), (i for i in (1, 2))),
      (Vector2d, (1.0, 2.0), (i for i in (1.0, 2.0))),
      (Vector2d, (10.0, 25.0), (i for i in (10.0, 25.0)))
    ]

    # 성공 테스트 실행
    for func, param, expected in success_dummy :
      with self.subTest(func = func, param = param, expected = expected) :
        self.run_success_iterator_test_with_params(func, param, expected)

  # 3. 객체 문자열로 표현(repr) 테스트 로직
  def run_success_repr_test_with_params(self, func, param, expected):
    # 객체 생성
    actual = func(*param)
    # __repr__호출 및 반환
    actual_str = actual.__repr__()
    # 결과 비교
    self.assertEquals(actual_str, expected)

  # 3. 객체 문자열로 표현(repr) 테스트
  def test_repr(self):
    # 성공 테스트 더미
    success_dummy = [
      (Vector2d, (1, 2), 'Vector2d(1.0, 2.0)'),
      (Vector2d, (10.0, 12.0), 'Vector2d(10.0, 12.0)'),
      (Vector2d, (0.5, 3.4), 'Vector2d(0.5, 3.4)')
    ]

    # 성공 테스트 실행
    for func, param, expected in success_dummy :
      with self.subTest(func = func, param = param, expected = expected) :
        self.run_success_repr_test_with_params(func, param, expected)

  # 4. 객체 문자열로 표현(str) 테스트 로직
  def run_success_str_test_with_params(self, func, param, expected):
    # 객체 생성
    actual = func(*param)
    # __str__ 호출 및 반환값 저장
    actual_str = actual.__str__()
    # 내용 비교
    self.assertEquals(actual_str, expected)

  # 4. 객체 문자열로 표현(str) 테스트
  def test_str(self):
    # 성공 데이터 더미
    success_dummy = [
      (Vector2d, (1, 2), '(1.0, 2.0)'),
      (Vector2d, (10.0, 12.0), '(10.0, 12.0)'),
      (Vector2d, (0.5, 3.4), '(0.5, 3.4)')
    ]

    # 성공 테스트 실행
    for func, param, expected in success_dummy :
      with self.subTest(func = func, param = param, expected = expected) :
        self.run_success_str_test_with_params(func, param, expected)

  # 5. 객체 바이트 시퀀스로 표현 테스트 로직
  def run_success_bytes_test_with_params(self, func, param, expected):
    # 객체 생성
    actual = func(*param)

    # __bytes__ 호출 및 결과 저장
    actual_bytes = actual.__bytes__()

    # 출력(추후에 내용 비교로 바꾸기)
    print(actual_bytes)
    # self.assertEquals(actual_bytes, expected)

  # 5. 객체 바이트 시퀀스로 표현 테스트
  def test_bytes(self):
    # 성공 테스트 더미
    success_dummy = [
      (Vector2d, (1, 2), "b'd\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@'"),
      (Vector2d, (10.0, 12.0), "b'd\x00\x00\x00\x00\x00\x00$@\x00\x00\x00\x00\x00\x00(@'"),
      (Vector2d, (0.5, 3.4), "b'd\x00\x00\x00\x00\x00\x00\xe0?333333\x0b@'")
    ]

    # 성공 테스트 실행
    for func, param, expected in success_dummy :
      with self.subTest(func = func, param = param, expected = expected) :
        self.run_success_bytes_test_with_params(func, param, expected)

  # 6. 객체 동등성 비교(eq) 테스트 로직
  def run_eq_test_with_param(self, func, param1, param2, expected):
    # 두 객체를 생성함
    v1 = func(*param1)
    v2 = func(*param2)

    # 두 객체를 비교함
    actual = v1 == v2

    # 비교결과와 예측 결과 비교
    self.assertEquals(actual, expected)

  # 6. 객체 동등성 비교(eq) 테스트
  def test_eq(self):
    # 더미 데이터
    dummy = [
      (Vector2d, (1, 2), (1, 2), True),
      (Vector2d, (1, 2), (1.0, 2.0), True),
      (Vector2d, (1.0, 2.0), (10.0, 25.0), False)
    ]

    # 테스트 실행
    for func, param1, param2, expected in dummy :
      with self.subTest(func = func, param1 = param1, param2 = param2, expected = expected) :
        self.run_eq_test_with_param(func, param1, param2, expected)

  # 7.객체의 크기(abs)를 표현 테스트 로직
  def run_abs_test_with_param(self, func, param, expected):
    # 객체 생성
    actual = func(*param)

    # abs로 객체 호출, 크기(거리) 반환
    actual_abs = abs(actual)

    # 값 비교
    self.assertEquals(actual_abs, expected)

  # 7.객체의 크기(abs)를 표현 테스트
  def test_abs(self):
    # 더미 데이터
    dummy = [
      (Vector2d, (1, 2), 2.23606797749979),
      (Vector2d, (1.0, 2.0), 2.23606797749979),
      (Vector2d, (10.0, 25.0), 26.925824035672523)
    ]

    # 테스트 실행
    for func, param, expected in dummy :
      with self.subTest(func = func, param = param, expected = expected) :
        self.run_abs_test_with_param(func, param, expected)

  # 8. 객체가 Truchy, Falchy인지 표현 테스트 로직
  def run_bool_test_with_param(self, func, param, expected):
    # 객체 생성
    actual = func(*param)

    # 해당 객체에 bool() 호출
    actual_bool = bool(actual)

    # 결과값 비교
    self.assertEquals(actual_bool, expected)

  # 8. 객체가 Truchy, Falchy인지 표현 테스트
  def test_bool(self):
    # 더미 데이터
    dummy = [
      (Vector2d, (0, 0), False),
      (Vector2d, (1.0, 2.0), True),
      (Vector2d, (10.0, 25.0), True)
    ]

    # 테스트 실행
    for func, param, expected in dummy :
      with self.subTest(func = func, param = param, expected = expected) :
        self.run_bool_test_with_param(func, param, expected)

```

- TDD 적용 하면서 점진적으로 구현
- 밑에 예시는 vector2d_v0을 스스로 구현해봄
  - (1) 위 과정에서 코드의 의도를 명확하게 파악함
  - (2) 파이썬 코드 작성에 익숙해짐
  
```python
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
    """
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

```
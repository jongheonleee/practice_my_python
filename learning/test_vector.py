from unittest import TestCase
from implement.pythonic_object.vector import Vector


# Vector 학습 및 검증 테스트 코드
class TestVector(TestCase):

  # 테스트 대상 기능 목록 및 테스트 범위 작성
  ### 1. 생성자 호출
  ### - 시퀀스 형을 매개변수로 전달해서 생성자 호출하는 경우 성공
  ### - 기본 생성자를 호출하는 경우 예외 발생(TypeError)
  ### - 문자열을 매개변수로 전달해서 생성자를 호출하는 경우 예외 발생
  ### - None 매개변수를 전달해서 생성자 호출하는 경우 예외 발생

  ### 2.

  def run_success_test_with_params(self, func, param, expected):
    actual = func(param)
    self.assertEquals(actual, expected)

    for a, b in zip(actual, expected) :
      self.assertEquals(a, b)

  def run_fail_test_with_params(self, func, param, expected):
    with self.assertRaises(expected) as context :
      func(param)

  # 1. 생성자 호출 테스트
  def test_create(self):
    # 성공 테스트 더미
    success_dummy = [
      (Vector, range(1), Vector(range(1))),
      (Vector, range(10), Vector(range(10))),
      (Vector, range(10), Vector(range(10)))
    ]

    # 실패 테스트 더미
    fail_dummy = [
      (Vector, None, TypeError),
      (Vector, 'abcd', TypeError),
      (Vector, '!@#$', TypeError)
    ]

    # 성공 테스트 실행
    for func, param, expected in success_dummy :
      with self.subTest(func = func, param = param, expected = expected) :
        self.run_success_test_with_params(func, param, expected)

    # 실패 테스트 실행
    for func, param, expected in fail_dummy :
      with self.subTest(func = func, param = param, expected = expected) :
        self.run_fail_test_with_params(func, param, expected)

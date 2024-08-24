import re, reprlib

RE_WORD = re.compile('\w+')

class Sentence:

  def __init__(self, text):
    self.text = text
    self.words = RE_WORD.findall(text)

  def __repr__(self):
    return 'Sentence(%s)' % reprlib.repr(self.text)


  # 반복형, __iter__를 통해 반복자를 반환하는 것
  # 제너레이터 함수 활용
  # yield 키워드를 가진 함수는 제너레이터, 제너레이터를 호출하면 제너레이터 객체 반환
  # 제너레이터 함수는 제너레이터 팩토리임
  def __iter__(self) :
    """
    해당 함수는 제너레이터 함수로서, 호출되면 반복자 인터페이스를 구현한
    제너레이터 객체를 생성함
    """
    for word in self.words :
      yield word

    return # 제너레이터 함수 안에 있는 return 문은 제너레이터 객체가 StopIterator 예외를 발생하게 만듦


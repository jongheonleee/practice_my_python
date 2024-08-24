import re, reprlib

RE_WORD = re.compile('\w+')

class Sentence :

  def __init__(self, text):
    self.text = text

  def __repr__(self):
    return 'Sentence(%s)' % reprlib.repr(self.text)

  def __iter__(self):
    # finditer()는 self.text에서 RE_WORD에 대응되는 단어들의 반복자인 MatchObject 객체를 생성함
    # re.finditer()는 re.findall()의 느긋한 버전, 리스트 대신 필요에 따라 re.MatchObject 객체를 생성하는 제너레이터 반환함 
    for match in RE_WORD.finditer(self.text) :
      # match.group() 메서드는 MatchObject 객체에서 매칭되는 텍스트를 추출함
      yield match.group()

import re, reprlib

RE_WORD = re.compile('\w+')

class Sentence:

  def __init__(self, text):
    self.text = text
    self.words = RE_WORD.findall(text)

  def __getitem__(self, index):
    return self.words[index]

  def __len__(self):
    return len(self.words)

  def __repr__(self):
    return 'Sentence(%s)' % reprlib.repr(self.text)

# 간단한 실행
s = Sentence('"The time has come!!, " the Walrus said,')
print(s)

# 내부적으로 Iterator 활용한 반복처리
for word in s :
  print(word)

# 위에 코드는 밑에와 같은 코드임
# for i in range(0, len(s)) :
#   print(s[i])

# it = iter(s) 반복자를 취득함
# while True :
#   try :
#     print(next(it)) 반복자에서 요소 추출(next)
#   except StopIteration : 요소가 없는 경우
#     del it 반복자 삭제하고 반복문 탈출
#     break

print(list(s))
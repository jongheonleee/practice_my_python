class MyVector2d :

  def __init__(self, x, y):
    """객체의 iv를 초기화함"""
    # iv 초기화
    self.x = float(x)
    self.y = float(y)

  def __iter__(self):
    """객체를 시퀀스처럼 사용할 수 있게함. 즉, 일일이 값 꺼내는 지능형 제너레이터 만듦"""
    # iv를 일일이 뽑아주는 제너레이터를 반환함
    return (i for i in (self.x, self.y))

  def __eq__(self, other):
    """객체의 동등성을 비교하기 위함"""
    # 같은 타입인지 확인, 아니면 TypeError
    if not isinstance(other, MyVector2d) :
      raise TypeError

    # __iter__를 호출해서 모든 iv의 값이 일치하는지 확인
    return all(a == b for a, b in zip(self, other))
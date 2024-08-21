import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

# ABC 가변 시퀀스 상속
class FrenchDeck2(collections.MutableSequence) :
  # cv
  ranks = [str(n) for n in range(2, 11) + list('JQKA')]
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    # iv
    self._cards = [Card(rank, suit) for suit in self.suits
                                    for rank in self.ranks]

  def __len__(self):
    return len(self._cards)

  def __getitem__(self, index):
    return self._cards[index]

  def __setitem__(self, index, value):
    self._cards[index] = value

  def __delitem__(self, index):
    del self._cards[index]

  def insert(self, index, value):
    self._cards.insert(index, value)

from string import ascii_lowercase
class bishop():
  def __init__(self, colour, position):
    self.colour = colour
    self.position = position

  def set_position(self, position):
    self.position = position

  def get_type(self):
    return "b"

  def get_position(self):
    return self.position

  def get_colour(self):
    return self.colour

  def move_logic(self, move):
    self.move_list = []
    self.alpha = ascii_lowercase.index(move[0])
    self.numeral = int(move[1])
    for x in range(-8, 9):
      self.test_alpha = self.alpha + x
      self.test_alpha2 = self.alpha - x
      try:
        self.test_alpha = ascii_lowercase[self.test_alpha]
        self.test_alpha2 = ascii_lowercase[self.test_alpha2]
      except:
        continue
      self.test_numeral = self.numeral + x
      self.test_move = self.test_alpha + str(self.test_numeral)
      self.test_move2 = self.test_alpha2 + str(self.test_numeral)
      self.move_list.append(self.test_move)
      self.move_list.append(self.test_move2)
    return self.move_list
  
  def move(self, move):
    self.moves = self.move_logic(move)
    if (move in self.moves) == True:
      self.position = move
      return True
    else:
      return False
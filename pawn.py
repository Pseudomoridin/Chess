from string import ascii_lowercase
class pawn():
  def __init__(self, colour, position):
    self.colour = colour
    self.position = position
    self.atStart = True

  def set_position(self, position):
    self.position = position

  def get_type(self):
    return "p"

  def get_position(self):
    return self.position

  def get_colour(self):
    return self.colour

  def move_logic(self, move):
    self.move_list = []
    self.alpha = self.position[0]
    self.alpha = ascii_lowercase.index(self.alpha)
    self.numeral = int(self.position[1])
    self.test_alpha = self.alpha
    if self.colour == "white":
      self.test_numeral = self.numeral + 1
      if self.atStart == True:
        self.test_numeral2 = self.numeral + 2
        self.test_move2 = ascii_lowercase[self.test_alpha] + str(self.test_numeral2)
        self.move_list.append(self.test_move2)
    elif self.colour == "black":
      self.test_numeral = self.numeral - 1
      if self.atStart == True:
        self.test_numeral2 = self.numeral - 2
        self.test_move2 = ascii_lowercase[self.test_alpha] + str(self.test_numeral2)
        self.move_list.append(self.test_move2)
    self.test_move = ascii_lowercase[self.test_alpha] + str(self.test_numeral)
    self.move_list.append(self.test_move)
    print(self.move_list)
    return self.move_list
  
  def move(self, move):
    self.moves = self.move_logic(move)
    if (move in self.moves) == True:
      self.position = move
      self.atStart = False
      return True
    else:
      return False

from string import ascii_lowercase
class queen():
  def __init__(self, colour, position):
    self.colour = colour
    self.position = position

  def set_position(self, position):
    self.position = position

  def get_type(self):
    return "Q"

  def get_position(self):
    return self.position

  def get_colour(self):
    return self.colour

  def move_logic(self, move):
    self
  
  def move(self, move):
    self.moves = self.move_logic()
    if (move in self.moves) == True:
      self.position = move
      return True
    else:
      return False

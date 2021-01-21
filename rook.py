from string import ascii_lowercase
class rook():
  def __init__(self, colour, position):
    self.colour = colour
    self.position = position

  def set_position(self, position):
    self.position = position

  def get_type(self):
    return "r"

  def get_position(self):
    return self.position
    
  def move_logic(self, x, y):
    self.change_x = abs(self.position[0] - x)
    self.change_y = abs(self.position[1] - y)
    if not(self.change_x == 0 and self.change_y == 0) and self.change_x + self.change_y > 0:
      return True
    else:
      return False
  
  def move(self, x, y):
    if self.move_logic(x, y) == True:
      self.position[0] = x
      self.position[1] = y
      return True
    else:
      return False

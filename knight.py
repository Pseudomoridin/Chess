from string import ascii_lowercase
class knight():
  def __init__(self, colour, position):
    self.colour = colour
    self.position = position
  
  def set_position(self, position):
    self.position = position

  def get_type(self):
    return "n"

  def get_position(self):
    return self.position

  def move_logic(self, x, y):
    self.change_x = abs(self.position[0] - x)
    self.change_y = abs(self.position[1] - y)
    if self.change_y > self.change_x:
      self.c = self.change_x
      self.change_x = self.change_y
      self.change_y = self.c
    if self.change_x == 2 and self.change_y == 1:
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

class king():
  def __init__(self, colour):
    self.colour = colour
    if self.colour == "white":
      self.position = [5, 0]
    elif self.colour == "black":
      self.position = [5, 8]
  
  def set_position(self, x, y):
    self.position[0] = x
    self.position[1] = y

  def get_type(self):
    return "king"

  def get_position(self):
    return self.position

  def move_logic(self, x, y):
    self.change_x = abs(self.position[0] - x)
    self.change_y = abs(self.position[1] - y)
    if (self.change_x >= 1) and (self.change_y >= 1):
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

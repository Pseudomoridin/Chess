class rook():
  def __init__(self, colour, side):
    self.colour = colour
    self.side = side
    self.position = []
    if self.side == "one":
      self.position.append(1)
    elif self.colour == "two":
      self.position.append(8)
    if self.colour == "white":
      self.position.append(1)
    elif self.colour == "black":
      self.position.append(8)

  def set_position(self, x, y):
    self.position[0] = x
    self.position[1] = y

  def get_type(self):
    return "rook"

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

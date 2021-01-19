class pawn():
  def __init__(self, x, colour):
    self.colour = colour
    self.x = x
    self.at_start = True
    self.position = [self.x]
    if self.colour == "white":
      self.position.append(2)
    elif self.colour == "black":
      self.position.append(7)

  def set_position(self, x, y):
    self.position[0] = x
    self.position[1] = y

  def get_type(self):
    return "pawn"

  def get_position(self):
    return self.position

  def move_logic(self, change):
    if self.colour == "white":
      self.change = change - self.position[1]
    elif self.colour == "black":
      self.change = self.position[1] - change
    if self.change == 2 and self.at_start == True:
      self.at_start = False
      return True
    elif self.change == 1:
      self.at_start = False
      return True

  def take_logic(self, x, y):
    if self.colour == "white":
      self.change_y = y - self.position[1]
    elif self.colour == "black":
      self.change_y = self.position[1] - y
    self.change_x = abs(self.position[0] - x)
    if self.change_y == 1 and self.change_x == 1:
      return True
  
  def move(self, x, y):
    if self.position[0] != y:
      if self.take_logic(x, y) == True:
        self.position[0] = x
        self.position[1] = y
    else:
      if self.move_logic(y) == True:
        self.position[1] = y
    if self.position[1] == 8 or self.position[1] == 1:
      return "r_up"
    else:
      return ""

from bishop import bishop
from king import king
from knight import knight
from pawn import pawn
from queen import queen
from rook import rook

class board():
  def __init__(self):
    self.chessboard = [
      [rook("white", "one"), knight("white", "one"), bishop("white", "one"), queen("white"), king("white"), bishop("white", "two"), knight("white", "two"), rook("white", "two")],
      [],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [],
      [rook("black", "one"), knight("black", "one"), bishop("black", "one"), queen("black"), king("black"), bishop("black", "two"), knight("black", "two"), rook("black", "two")],
    ]
    for x in range(8):
      self.chessboard[1].append(pawn(x, "white"))
    for x in range(8):
      self.chessboard[6].append(pawn(x, "black"))

  def return_board(self):
    print_board = []
    for x in range(8):
      print_board.append([])
      for y in range(8):
        try:
          print_board[x].append(self.chessboard[x][y].get_type())
        except:
          print_board[x].append("0")
    return print_board

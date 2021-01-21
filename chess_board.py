from bishop import bishop
from king import king
from knight import knight
from pawn import pawn
from queen import queen
from rook import rook
from string import ascii_lowercase

class board():
  def __init__(self):
    self.chessboard = {
      "a1" : rook("white", "a1"),  "a2" : pawn("white", "a2"),  "a7" : pawn("black", "a7"),  "a8" : rook("black", "a8"),
      "b1" : knight("white", "b1"),"b2" : pawn("white", "b2"),  "b7" : pawn("black", "b7"),  "b8" : knight("black", "b8"),
      "c1" : bishop("white", "c1"),"c2" : pawn("white", "c2"),  "c7" : pawn("black", "c7"),  "c8" : bishop("black", "c8"),
      "d1" : queen("white", "d1"), "d2" : pawn("white", "d2"),  "d7" : pawn("black", "d7"),  "d8" : queen("black", "d8"),
      "e1" : king("white", "e1"),  "e2" : pawn("white", "e2"),  "e7" : pawn("black", "e7"),  "e8" : king("black", "e8"),
      "f1" : bishop("white", "f1"),"f2" : pawn("white", "f2"),  "f7" : pawn("black", "f7"),  "f8" : bishop("black", "f8"),
      "g1" : knight("white", "g1"),"g2" : pawn("white", "g2"),  "g7" : pawn("black", "g7"),  "g8" : knight("black", "g8"),
      "h1" : rook("white", "h1"),  "h2" : pawn("white", "h2"),  "h7" : pawn("black", "h7"),  "h8" : rook("black", "h8"),
    }

  def get_piece(self, position):
    return self.chessboard[position]

  def return_board(self):
    print_board = []
    for x in range(8):
      print_board.append([])
      for y in range(8):
        try:
          position = ascii_lowercase[y] + str(x+1)
          print_board[x].append(self.get_piece(position).get_type())
        except:
          print_board[x].append("-")
    return print_board

  def move_piece(self, move):
    self

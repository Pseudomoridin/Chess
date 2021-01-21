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
    self.storage_board = self.chessboard

  def get_piece(self, y, x):
    return self.chessboard[x][y]

  def store_board(self):
    for x in range(len(self.chessboard)):
      for y in range(len(self.chessboard[x])):
        try:
          self.position = self.chessboard[x][y].get_position()
          self.storage_board[self.position[1]][self.position[0]] = self.chessboard[x][y]
        except:
          self.storage_board[x][y] = "-"
    self.chessboard = self.storage_board

  def return_board(self):
    print_board = []
    for x in range(8):
      print_board.append([])
      for y in range(8):
        try:
          print_board[x].append(self.chessboard[x][y].get_type())
        except:
          print_board[x].append("-")
    return print_board

  def move_piece(self, move):
    self.move = move
    self.start = self.move[:self.move.index(" to ")]
    self.end = self.move[self.move.index(" to ")+4:]
    if self.start[0] == 'a':
      self.piece = self.get_piece(0, int(self.start[1])-1)
    elif self.start[0] == 'b':
      self.piece = self.get_piece(1, int(self.start[1])-1)
    elif self.start[0] == 'c':
      self.piece = self.get_piece(2, int(self.start[1])-1)
    elif self.start[0] == 'd':
      self.piece = self.get_piece(3, int(self.start[1])-1)
    elif self.start[0] == 'e':
      self.piece = self.get_piece(4, int(self.start[1])-1)
    elif self.start[0] == 'f':
      self.piece = self.get_piece(5, int(self.start[1])-1)
    elif self.start[0] == 'g':
      self.piece = self.get_piece(6, int(self.start[1])-1)
    elif self.start[0] == 'h':
      self.piece = self.get_piece(7, int(self.start[1])-1)
    
    if self.end[0] == 'a':
      self.piece.move(0, int(self.end[1])-1)
    elif self.end[0] == 'b':
      self.piece.move(1, int(self.end[1])-1)
    elif self.end[0] == 'c':
      self.piece.move(2, int(self.end[1])-1)
    elif self.end[0] == 'd':
      self.piece.move(3, int(self.end[1])-1)
    elif self.end[0] == 'e':
      self.piece.move(4, int(self.end[1])-1)
    elif self.end[0] == 'f':
      self.piece.move(5, int(self.end[1])-1)
    elif self.end[0] == 'g':
      self.piece.move(6, int(self.end[1])-1)
    elif self.end[0] == 'h':
      self.piece.move(7, int(self.end[1])-1)

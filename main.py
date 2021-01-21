from chess_board import board

chessboard = board()
#"""
while True:
  print_board = chessboard.return_board()
  x = 1
  for row in print_board:
    print("")
    print(x, end='   ')
    x += 1
    for item in row:
      print(item, end=' ')
  print("\n\n\tA B C D E F G H")
  chessboard.move_piece(input())
  chessboard.store_board()
#"""
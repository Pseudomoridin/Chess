from chess_board import board

chessboard = board()
print_board = chessboard.return_board()
for row in print_board:
  print()
  for item in row:
    print(item, end=' ')
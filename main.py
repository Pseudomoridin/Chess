from chess_board import board
input_chess = []
chessboard = board()

"""
import tkinter as tk

def handle_click_a1(event):
  input_chess.append("a1")
def handle_click_b1(event):
  input_chess.append("b1")
def handle_click_c1(event):
  input_chess.append("c1")
def handle_click_d1(event):
  input_chess.append("d1")
def handle_click_e1(event):
  input_chess.append("e1")
def handle_click_f1(event):
  input_chess.append("f1")
def handle_click_g1(event):
  input_chess.append("g1")
def handle_click_h1(event):
  input_chess.append("h1")

def handle_click_a2(event):
  input_chess.append("a2")
def handle_click_b2(event):
  input_chess.append("b2")
def handle_click_c2(event):
  input_chess.append("c2")
def handle_click_d2(event):
  input_chess.append("d2")
def handle_click_e2(event):
  input_chess.append("e2")
def handle_click_f2(event):
  input_chess.append("f2")
def handle_click_g2(event):
  input_chess.append("g2")
def handle_click_h2(event):
  input_chess.append("h2")

def handle_click_a3(event):
  input_chess.append("a3")
def handle_click_b3(event):
  input_chess.append("b3")
def handle_click_c3(event):
  input_chess.append("c3")
def handle_click_d3(event):
  input_chess.append("d3")
def handle_click_e3(event):
  input_chess.append("e3")
def handle_click_f3(event):
  input_chess.append("f3")
def handle_click_g3(event):
  input_chess.append("g3")
def handle_click_h3(event):
  input_chess.append("h3")

def handle_click_a4(event):
  input_chess.append("a4")
def handle_click_b4(event):
  input_chess.append("b4")
def handle_click_c4(event):
  input_chess.append("c4")
def handle_click_d4(event):
  input_chess.append("d4")
def handle_click_e4(event):
  input_chess.append("e4")
def handle_click_f4(event):
  input_chess.append("f4")
def handle_click_g4(event):
  input_chess.append("g4")
def handle_click_h4(event):
  input_chess.append("h4")

def handle_click_a5(event):
  input_chess.append("a5")
def handle_click_b5(event):
  input_chess.append("b5")
def handle_click_c5(event):
  input_chess.append("c5")
def handle_click_d5(event):
  input_chess.append("d5")
def handle_click_e5(event):
  input_chess.append("e5")
def handle_click_f5(event):
  input_chess.append("f5")
def handle_click_g5(event):
  input_chess.append("g5")
def handle_click_h5(event):
  input_chess.append("h5")

def handle_click_a6(event):
  input_chess.append("a6")
def handle_click_b6(event):
  input_chess.append("b6")
def handle_click_c6(event):
  input_chess.append("c6")
def handle_click_d6(event):
  input_chess.append("d6")
def handle_click_e6(event):
  input_chess.append("e6")
def handle_click_f6(event):
  input_chess.append("f6")
def handle_click_g6(event):
  input_chess.append("g6")
def handle_click_h6(event):
  input_chess.append("h6")

def handle_click_a7(event):
  input_chess.append("a7")
def handle_click_b7(event):
  input_chess.append("b7")
def handle_click_c7(event):
  input_chess.append("c7")
def handle_click_d7(event):
  input_chess.append("d7")
def handle_click_e7(event):
  input_chess.append("e7")
def handle_click_f7(event):
  input_chess.append("f7")
def handle_click_g7(event):
  input_chess.append("g7")
def handle_click_h7(event):
  input_chess.append("h7")

def handle_click_a8(event):
  input_chess.append("a8")
def handle_click_b8(event):
  input_chess.append("b8")
def handle_click_c8(event):
  input_chess.append("c8")
def handle_click_d8(event):
  input_chess.append("d8")
def handle_click_e8(event):
  input_chess.append("e8")
def handle_click_f8(event):
  input_chess.append("f8")
def handle_click_g8(event):
  input_chess.append("g8")
def handle_click_h8(event):
  input_chess.append("h8")

def update():
  return_board = chessboard.return_board()
  x = 0
  for row in return_board:
    y = 0
    for item in row:
      buttons_list[x][y]['text'] = item[0]
      try:
        if item[1] == "white":
          buttons_list[x][y]['bg'] = "white"
          buttons_list[x][y]['fg'] = "black"
        if item[1] == "black":
          buttons_list[x][y]['bg'] = "black"
          buttons_list[x][y]['fg'] = "white"
      except:
        buttons_list[x][y]['bg'] = "white"
        buttons_list[x][y]['bg'] = "white"
      y += 1
    x +=1

def go():
  global input_chess
  if len(input_chess) == 2:
    try:
      input_fin = input_chess[0] + " to " + input_chess[1]
      chessboard.move_piece(input_fin)
    except:
      print("failure")
    input_chess = []
    update()
#  window.after(1000, go())

root = tk.Tk()
root.withdraw()
window = tk.Toplevel(root)
frame_1 = tk.Frame(master = window)
frame_2 = tk.Frame(master = window)
frame_3 = tk.Frame(master = window)
frame_4 = tk.Frame(master = window)
frame_5 = tk.Frame(master = window)
frame_6 = tk.Frame(master = window)
frame_7 = tk.Frame(master = window)
frame_8 = tk.Frame(master = window)

a1 = tk.Button(master = frame_1, height = 2, width = 3)
a1.pack(side = tk.LEFT)
a1.bind('<Button-1>', handle_click_a1)
b1 = tk.Button(master = frame_1, height = 2, width = 3)
b1.pack(side = tk.LEFT)
b1.bind('<Button-1>', handle_click_b1)
c1 = tk.Button(master = frame_1, height = 2, width = 3)
c1.pack(side = tk.LEFT)
c1.bind('<Button-1>', handle_click_c1)
d1 = tk.Button(master = frame_1, height = 2, width = 3)
d1.pack(side = tk.LEFT)
d1.bind('<Button-1>', handle_click_d1)
e1 = tk.Button(master = frame_1, height = 2, width = 3)
e1.pack(side = tk.LEFT)
e1.bind('<Button-1>', handle_click_e1)
f1 = tk.Button(master = frame_1, height = 2, width = 3)
f1.pack(side = tk.LEFT)
f1.bind('<Button-1>', handle_click_f1)
g1 = tk.Button(master = frame_1, height = 2, width = 3)
g1.pack(side = tk.LEFT)
g1.bind('<Button-1>', handle_click_g1)
h1 = tk.Button(master = frame_1, height = 2, width = 3)
h1.pack(side = tk.LEFT)
h1.bind('<Button-1>', handle_click_h1)


a2 = tk.Button(master = frame_2, height = 2, width = 3)
a2.pack(side = tk.LEFT)
a2.bind('<Button-1>', handle_click_a2)
b2 = tk.Button(master = frame_2, height = 2, width = 3)
b2.pack(side = tk.LEFT)
b2.bind('<Button-1>', handle_click_b2)
c2 = tk.Button(master = frame_2, height = 2, width = 3)
c2.pack(side = tk.LEFT)
c2.bind('<Button-1>', handle_click_c2)
d2 = tk.Button(master = frame_2, height = 2, width = 3)
d2.pack(side = tk.LEFT)
d2.bind('<Button-1>', handle_click_d2)
e2 = tk.Button(master = frame_2, height = 2, width = 3)
e2.pack(side = tk.LEFT)
e2.bind('<Button-1>', handle_click_e2)
f2 = tk.Button(master = frame_2, height = 2, width = 3)
f2.pack(side = tk.LEFT)
f2.bind('<Button-1>', handle_click_f2)
g2 = tk.Button(master = frame_2, height = 2, width = 3)
g2.pack(side = tk.LEFT)
g2.bind('<Button-1>', handle_click_g2)
h2 = tk.Button(master = frame_2, height = 2, width = 3)
h2.pack(side = tk.LEFT)
h2.bind('<Button-1>', handle_click_h2)


a3 = tk.Button(master = frame_3, height = 2, width = 3)
a3.pack(side = tk.LEFT)
a3.bind('<Button-1>', handle_click_a3)
b3 = tk.Button(master = frame_3, height = 2, width = 3)
b3.pack(side = tk.LEFT)
b3.bind('<Button-1>', handle_click_b3)
c3 = tk.Button(master = frame_3, height = 2, width = 3)
c3.pack(side = tk.LEFT)
c3.bind('<Button-1>', handle_click_c3)
d3 = tk.Button(master = frame_3, height = 2, width = 3)
d3.pack(side = tk.LEFT)
d3.bind('<Button-1>', handle_click_d3)
e3 = tk.Button(master = frame_3, height = 2, width = 3)
e3.pack(side = tk.LEFT)
e3.bind('<Button-1>', handle_click_e3)
f3 = tk.Button(master = frame_3, height = 2, width = 3)
f3.pack(side = tk.LEFT)
f3.bind('<Button-1>', handle_click_f3)
g3 = tk.Button(master = frame_3, height = 2, width = 3)
g3.pack(side = tk.LEFT)
g3.bind('<Button-1>', handle_click_g3)
h3 = tk.Button(master = frame_3, height = 2, width = 3)
h3.pack(side = tk.LEFT)
h3.bind('<Button-1>', handle_click_h3)


a4 = tk.Button(master = frame_4, height = 2, width = 3)
a4.pack(side = tk.LEFT)
a4.bind('<Button-1>', handle_click_a4)
b4 = tk.Button(master = frame_4, height = 2, width = 3)
b4.pack(side = tk.LEFT)
b4.bind('<Button-1>', handle_click_b4)
c4 = tk.Button(master = frame_4, height = 2, width = 3)
c4.pack(side = tk.LEFT)
c4.bind('<Button-1>', handle_click_c4)
d4 = tk.Button(master = frame_4, height = 2, width = 3)
d4.pack(side = tk.LEFT)
d4.bind('<Button-1>', handle_click_d4)
e4 = tk.Button(master = frame_4, height = 2, width = 3)
e4.pack(side = tk.LEFT)
e4.bind('<Button-1>', handle_click_e4)
f4 = tk.Button(master = frame_4, height = 2, width = 3)
f4.pack(side = tk.LEFT)
f4.bind('<Button-1>', handle_click_f4)
g4 = tk.Button(master = frame_4, height = 2, width = 3)
g4.pack(side = tk.LEFT)
g4.bind('<Button-1>', handle_click_g4)
h4 = tk.Button(master = frame_4, height = 2, width = 3)
h4.pack(side = tk.LEFT)
h4.bind('<Button-1>', handle_click_h4)


a5 = tk.Button(master = frame_5, height = 2, width = 3)
a5.pack(side = tk.LEFT)
a5.bind('<Button-1>', handle_click_a5)
b5 = tk.Button(master = frame_5, height = 2, width = 3)
b5.pack(side = tk.LEFT)
b5.bind('<Button-1>', handle_click_b5)
c5 = tk.Button(master = frame_5, height = 2, width = 3)
c5.pack(side = tk.LEFT)
c5.bind('<Button-1>', handle_click_c5)
d5 = tk.Button(master = frame_5, height = 2, width = 3)
d5.pack(side = tk.LEFT)
d5.bind('<Button-1>', handle_click_d5)
e5 = tk.Button(master = frame_5, height = 2, width = 3)
e5.pack(side = tk.LEFT)
e5.bind('<Button-1>', handle_click_e5)
f5 = tk.Button(master = frame_5, height = 2, width = 3)
f5.pack(side = tk.LEFT)
f5.bind('<Button-1>', handle_click_f5)
g5 = tk.Button(master = frame_5, height = 2, width = 3)
g5.pack(side = tk.LEFT)
g5.bind('<Button-1>', handle_click_g5)
h5 = tk.Button(master = frame_5, height = 2, width = 3)
h5.pack(side = tk.LEFT)
h5.bind('<Button-1>', handle_click_h5)


a6 = tk.Button(master = frame_6, height = 2, width = 3)
a6.pack(side = tk.LEFT)
a6.bind('<Button-1>', handle_click_a6)
b6 = tk.Button(master = frame_6, height = 2, width = 3)
b6.pack(side = tk.LEFT)
b6.bind('<Button-1>', handle_click_b6)
c6 = tk.Button(master = frame_6, height = 2, width = 3)
c6.pack(side = tk.LEFT)
c6.bind('<Button-1>', handle_click_c6)
d6 = tk.Button(master = frame_6, height = 2, width = 3)
d6.pack(side = tk.LEFT)
d6.bind('<Button-1>', handle_click_d6)
e6 = tk.Button(master = frame_6, height = 2, width = 3)
e6.pack(side = tk.LEFT)
e6.bind('<Button-1>', handle_click_e6)
f6 = tk.Button(master = frame_6, height = 2, width = 3)
f6.pack(side = tk.LEFT)
f6.bind('<Button-1>', handle_click_f6)
g6 = tk.Button(master = frame_6, height = 2, width = 3)
g6.pack(side = tk.LEFT)
g6.bind('<Button-1>', handle_click_g6)
h6 = tk.Button(master = frame_6, height = 2, width = 3)
h6.pack(side = tk.LEFT)
h6.bind('<Button-1>', handle_click_h6)


a7 = tk.Button(master = frame_7, height = 2, width = 3)
a7.pack(side = tk.LEFT)
a7.bind('<Button-1>', handle_click_a7)
b7 = tk.Button(master = frame_7, height = 2, width = 3)
b7.pack(side = tk.LEFT)
b7.bind('<Button-1>', handle_click_b7)
c7 = tk.Button(master = frame_7, height = 2, width = 3)
c7.pack(side = tk.LEFT)
c7.bind('<Button-1>', handle_click_c7)
d7 = tk.Button(master = frame_7, height = 2, width = 3)
d7.pack(side = tk.LEFT)
d7.bind('<Button-1>', handle_click_d7)
e7 = tk.Button(master = frame_7, height = 2, width = 3)
e7.pack(side = tk.LEFT)
e7.bind('<Button-1>', handle_click_e7)
f7 = tk.Button(master = frame_7, height = 2, width = 3)
f7.pack(side = tk.LEFT)
f7.bind('<Button-1>', handle_click_f7)
g7 = tk.Button(master = frame_7, height = 2, width = 3)
g7.pack(side = tk.LEFT)
g7.bind('<Button-1>', handle_click_g7)
h7 = tk.Button(master = frame_7, height = 2, width = 3)
h7.pack(side = tk.LEFT)
h7.bind('<Button-1>', handle_click_h7)


a8 = tk.Button(master = frame_8, height = 2, width = 3)
a8.pack(side = tk.LEFT)
a8.bind('<Button-1>', handle_click_a8)
b8 = tk.Button(master = frame_8, height = 2, width = 3)
b8.pack(side = tk.LEFT)
b8.bind('<Button-1>', handle_click_b8)
c8 = tk.Button(master = frame_8, height = 2, width = 3)
c8.pack(side = tk.LEFT)
c8.bind('<Button-1>', handle_click_c8)
d8 = tk.Button(master = frame_8, height = 2, width = 3)
d8.pack(side = tk.LEFT)
d8.bind('<Button-1>', handle_click_d8)
e8 = tk.Button(master = frame_8, height = 2, width = 3)
e8.pack(side = tk.LEFT)
e8.bind('<Button-1>', handle_click_e8)
f8 = tk.Button(master = frame_8, height = 2, width = 3)
f8.pack(side = tk.LEFT)
f8.bind('<Button-1>', handle_click_f8)
g8 = tk.Button(master = frame_8, height = 2, width = 3)
g8.pack(side = tk.LEFT)
g8.bind('<Button-1>', handle_click_g8)
h8 = tk.Button(master = frame_8, height = 2, width = 3)
h8.pack(side = tk.LEFT)
h8.bind('<Button-1>', handle_click_h8)

buttons_list = [[a1,b1,c1,d1,e1,f1,g1,h1],[a2,b2,c2,d2,e2,f2,g2,h2],[a3,b3,c3,d3,e3,f3,g3,h3],[a4,b4,c4,d4,e4,f4,g4,h4],[a5,b5,c5,d5,e5,f5,g5,h5],[a6,b6,c6,d6,e6,f6,g6,h6],[a7,b7,c7,d7,e7,f7,g7,h7],[a8,b8,c8,d8,e8,f8,g8,h8]]

frame_1.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()
frame_5.pack()
frame_6.pack()
frame_7.pack()
frame_8.pack()

update()
while True:
  window.update()
  window.after(0, go())

window.mainloop()
#"""

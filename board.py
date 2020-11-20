import random
import os
from time import sleep

def clear():
    os.system('clear')

def print_fractal(a):
  for x in a:
    l = ""
    for y in x:
      if y:
        l += "█"
      else:
        l += " "
    print(l)

class Board():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.posx = 0
    self.posy = 0
    a = []
    for _ in range(x):
      j = []
      for _ in range(y):
        j.append([])
      a.append(j)
    self.board = a

  def randomise(self):
    a = []
    for _ in range(self.y):
      j = []
      for _ in range(self.x):
        j.append(round(random.random()))
      a.append(j)
    self.board = a
  
  def display(self):
    print("-" * self.x)
    for x in self.board:
      l = ""
      for y in x:
        if y:
          l += "█"
        else:
          l += " "
      print(l)
    print("-" * self.x)

  def pendown(self):
    self.pendown = True
  
  def penup(self):
    self.pendown = False

  def move(self, direction, magnitude):
    if direction == "right":
      if self.posx + magnitude < self.x:
        for box in range(magnitude):
          self.board[self.posy][self.posx + box] = True
      self.posx += magnitude
    elif direction == "left":
      if self.posx - magnitude >= 0:
        for box in range(magnitude):
          self.board[self.posy][self.posx - box - 2] = True
      self.posx -= magnitude
    elif direction == "down":
      if self.posy + magnitude < self.y:
        for box in range(magnitude + 1):
          self.board[self.posy + box][self.posx - 1] = True 
      self.posy += magnitude
    elif direction == "up":
      if self.posy - magnitude >= 0:
        for box in range(magnitude - 1):
          self.board[self.posy - box][self.posx + 1] = True
      self.posy -= magnitude

clear()

c = Board(50, 20)
# c.randomise()
c.display()
sleep(0.5)
clear()
c.move("right", 10)
# c.posy = 3
# c.move("left", 10)
# c.posy = 6#
c.display()
c.move("down", 5)
sleep(0.2)
clear()
c.display()
c.move("left", 2)
sleep(0.2)
clear()
c.display()
c.move("down", 2)
sleep(0.2)
clear()
c.display()
c.move("right", 8)
sleep(0.2)
clear()
c.display()
# c.move("up", 2)
# c.move("up", 2)
# c.move("left", 2)

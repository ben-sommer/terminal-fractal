#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os
from time import sleep

def clear():
    os.system('clear')

class Board():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.posx = 0
    self.posy = 0
    self.direction = 0
    a = []
    for _ in range(y):
      j = []
      for _ in range(x):
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
    print("--" * self.x)
    for x in self.board:
      l = ""
      for y in x:
        if y:
          l += "██"
        else:
          l += "  "
      print(l)
    print("--" * self.x)
  
  def turn(self, direction):
    new_direction = self.direction + direction
    if new_direction >= 360:
      new_direction = new_direction - 360
    elif new_direction < 0:
      new_direction = new_direction + 360
    self.direction = new_direction
  
  def forward(self, magnitude):
    self.move(self.direction, magnitude)

  def move(self, direction, magnitude):
    if direction == 90:
      for box in range(magnitude):
        self.board[self.posy][self.posx + box] = True
      self.posx += magnitude
    elif direction == 270:
      for box in range(magnitude):
        self.board[self.posy][self.posx - box - 2] = True
      self.posx -= magnitude
    elif direction == 180:
      for box in range(magnitude + 1):
        self.board[self.posy + box][self.posx - 1] = True 
      self.posy += magnitude
    elif direction == 0:
      for box in range(magnitude + 1):
        self.board[self.posy - box][self.posx - 1] = True
      self.posy -= magnitude

clear()

c = Board(50, 50)

c.posx = 25
c.posy = 25

commands = []
limit = 8

for z in range(limit):
  newList = []
  alternate = 1
  for x in commands:
    newList.append(alternate)
    alternate = alternate * -1
    newList.append(x)
  newList.append(alternate)
  alternate = alternate * -1
  commands = newList
for x in commands:
  c.turn(x*90)
  c.forward(1)

c.display()

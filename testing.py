from math import *

def countdown(total, speed):
  clock = total
  tickspeed = speed
  while clock>0:
    print(clock)
    clock -= tickspeed

countdown(30,1)

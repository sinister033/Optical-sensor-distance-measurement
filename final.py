from os import confstr
from dictionaries import units, xyModes
import mouse
import struct
import math
import time
from random import randint


f = open( "/dev/input/mice", "rb" ); 


quadrentCodes = [8,24,56,40]
leftClickCodes = []
rightClickCodes = []
midClickCodes = []
midLeftCodes = []
midRightCodes = []

unit = list(units.keys())[0]
mode = xyModes[0]

for elem in quadrentCodes:
  leftClickCodes.append(elem+1)
  rightClickCodes.append(elem+2)
  midClickCodes.append(elem+4)
  midLeftCodes.append(elem+5)
  midRightCodes.append(elem+6)

distanceDots = 0

currentUnitIndex = 0
currentModeIndex = 0
bluetoothConnected = False
blue_com = None

unitKeys = list(units.keys())
unit = unitKeys[currentUnitIndex]
mode = xyModes[currentModeIndex]


def cycleUnits():
  global unit, currentUnitIndex
  if currentUnitIndex < len(unitKeys) - 1 :
    currentUnitIndex = currentUnitIndex + 1
    unit = unitKeys[currentUnitIndex]
  else: 
    currentUnitIndex = 0
    unit = unitKeys[currentUnitIndex]
  print(unit)

def cycleModes():
  global mode, currentModeIndex
  if currentModeIndex < len(xyModes) - 1:
    currentModeIndex = currentModeIndex + 1
    mode = xyModes[currentModeIndex]
  else:
    currentModeIndex = 0
    mode = xyModes[currentModeIndex]
  print(mode)





def incrementDots(increment): 
  global distanceDots 
  distanceDots = distanceDots + increment

def resetDots():
  global distanceDots
  distanceDots = 0

def print_output(distanceDots, divisor):
  print(distanceDots/divisor, unit)

      

def main():
  
  while 1:
    data = f.read(3)  # Reads the 3 bytes 
    
    tuple = struct.unpack('3b',data)
    
    print(tuple)
    if tuple[0] in leftClickCodes:

      if currentModeIndex == 0:
          incrementDots(math.sqrt( tuple[1]**2 + tuple[2]**2))
      elif currentModeIndex == 1:
          incrementDots( tuple[1] )
      elif currentModeIndex == 2:
          incrementDots( math.abs(tuple[1]) )
      elif currentModeIndex == 3:
          incrementDots( tuple[2] )
      elif currentModeIndex == 4:
          incrementDots( math.abs(tuple[2]) )
      else:
          incrementDots(math.sqrt( tuple[1]**2 + tuple[2]**2))

      print_output(distanceDots, units[unit])
      mouse.move("500", "500")
    
    elif tuple[0] in rightClickCodes:
      cycleUnits()
      print_output(distanceDots, units[unit])
      mouse.move("500", "500")


    elif tuple[0] in midClickCodes:
      cycleModes()
      print_output(distanceDots, units[unit])
      mouse.move("500", "500")
    
    elif tuple[0] in midLeftCodes:
      resetDots()
      print_output(distanceDots, units[unit])
      mouse.move("500", "500")


if __name__ == "__main__": main()

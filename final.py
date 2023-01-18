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
  # global distance_travelled
  print(distanceDots/divisor, unit)
  # distance_travelled = distanceDots/divisor

def get_data():
  global var
  while 1:
    data = f.read(3)  # Reads the 3 bytes 
    
    tuple = struct.unpack('3b',data)
    
    print(tuple)
    if tuple[0] in leftClickCodes:
      if currentModeIndex == 0:
          incrementDots( tuple[1] )
          break
      elif currentModeIndex == 1:
          incrementDots(abs(tuple[1]) )
      elif currentModeIndex == 2:
          incrementDots( tuple[2] )
      elif currentModeIndex == 3:
          incrementDots(abs(tuple[2]) )
      elif currentModeIndex == 4:
          incrementDots(math.sqrt( tuple[1]**2 + tuple[2]**2))
      else:
          incrementDots(math.sqrt( tuple[1]**2 + tuple[2]**2))
      # if mouse.is_pressed(button='left') == False:
      #   print_output(distanceDots, units[unit])
      var = distanceDots/units[unit]
      print(var)
      mouse.move("500", "500")
    
    elif tuple[0] in rightClickCodes:
      resetDots()
      print_output(distanceDots, units[unit])
      mouse.move("500", "500")


    elif tuple[0] in midClickCodes:
      cycleModes()
      print_output(distanceDots, units[unit])
      mouse.move("500", "500")     

def comm():
  get_data()
  return distanceDots, units[unit], unit, var



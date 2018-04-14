#section 9 of the zeal python documentation = classes
# run this file by running `python3.5 toyrobot.py`

class Robot:
  """The toy robot class"""
  compass = ['N','E','S','W']

  def __init__(self, name, table_height, table_width):
    self.name = name
    self.facing = None
    self.x = None
    self.y = None
    self.table_height = table_height
    self.table_width = table_width
  
  def place(x,y,facing):
    if x >= table_width or y >= table_height:
      print("invalid placement")
      return false
    self.x = x
    self.y = y

    if facing in compass:
      self.facing = facing
    else:
      self.facing = 'N'
      
    return true
  
  

robot = Robot('alex')
print(robot.name)
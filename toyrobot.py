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
  
  def place(self, x, y, facing):
    if x >= self.table_width or y >= self.table_height:
      print("invalid placement")
      return False
    self.x = x
    self.y = y

    if facing in self.compass:
      self.facing = facing
    else:
      self.facing = 'N'
      
    return True
  
  # shall move forward, where forward is one position in the direction
  # it's facing, and shall refuse to move if doing so would result in
  # the robot falling 'off' the table.
  def move(self):
    if self.facing == 'N' and self.y + 1 < self.table_height:
      self.y += 1
      return True
    elif self.facing == 'E' and self.x + 1 < self.table_width:
      self.x += 1
      return True
    elif self.facing == 'S' and self.y - 1 >= 0:
      self.y -= 1
      return True
    elif self.facing == 'W' and self.x - 1 >= 0:
      self.x -= 1
      return True
    
    return False
  
  def turn(self, direction):
    return False # to be implemented
    

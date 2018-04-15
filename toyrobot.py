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
    self.placed = False
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
      
    self.placed = True
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
    if direction == 'RIGHT':
      # get the index value of the self.facing value in compass
      # and increment it , and overflow it if necessary
      newIndex = ( self.compass.index(self.facing) + 1 ) % 4
      self.facing = self.compass[newIndex]
      return True
    elif direction == 'LEFT':
      # same as above except decrement and underflowing back up
      # to a value of 3 from -1 is not necessary because python
      # understands -1 to be the last element which is what we want
      newIndex = ( self.compass.index(self.facing) - 1 )
      self.facing = self.compass[newIndex]
      return True
    else:
      return False
    
  def report(self):
    return str(self.x) + ', ' + str(self.y) + ', ' + self.facing

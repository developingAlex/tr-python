#section 9 of the zeal python documentation = classes
# run this file by running `python3.5 toyrobot.py`

class Robot:
  """The toy robot class"""
  facing = 'N'

  def __init__(self, name):
    self.name = name
    self.facing = None
    self.x = None
    self.y = None

robot = Robot('alex')
print(robot.name)
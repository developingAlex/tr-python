#section 9 of the zeal python documentation = classes

class Robot:
  """The toy robot class"""
  facing = 'N'

  def __init__(self, name):
    self.name = name
    self.facing = None
    self.x = None
    self.y = None

  def place(self, )
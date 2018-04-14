#run by going `python -m unittest test_toyrobot`

import unittest

# import the toyrobot module
import toyrobot

# import the Robot class
from toyrobot import Robot


class RobotTestCase(unittest.TestCase):
  def setUp(self):
    self.robot = Robot('Testy', 5, 5)
  
  def testPlacement(self):
    self.robot.place(4,4,'S')
    self.assertEqual(self.robot.facing, 'S')
    self.assertEqual(self.robot.x, 4)
    self.assertEqual(self.robot.y, 4)
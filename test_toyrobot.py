#run by going `python -m unittest test_toyrobot`

import unittest

# import the toyrobot module
import toyrobot

# import the Robot class
from toyrobot import Robot


class RobotTestCase(unittest.TestCase):
  def setUp(self):
    self.robot = Robot('Testy', 5, 5)
  
  def testSetUp(self):
    self.assertEqual(self.robot.name, 'Testy')
    self.assertEqual(self.robot.table_height, 5)
    self.assertEqual(self.robot.table_width, 5)

  def testValidPlacement(self):
    # if the placement is allowed, place returns True
    self.assertTrue(self.robot.place(0,4,'S'))
    self.assertTrue(self.robot.place(4,4,'S'))
    # go ahead and test the properties match our parameters
    self.assertEqual(self.robot.facing, 'S')
    self.assertEqual(self.robot.x, 4)
    self.assertEqual(self.robot.y, 4)
  
  def testInvalidPlacementFacing(self):
    self.robot.place(4,4,'X') # should succeed, facing 'N' since 'X' is invalid
    self.assertEqual(self.robot.facing, 'N')

  def testInvalidPlacementCoords(self):
    # our board is 5x5 and 0-indexed
    # if the placement is refused, place returns False
    # a position of 6 is off by two.
    self.assertFalse(self.robot.place(6,6,'N'))
    # a position of 5 is off by one:
    self.assertFalse(self.robot.place(5,5,'N'))
  
  def testValidMove(self):
    self.robot.place(0,0,'N')
    # shall move forward, where forward is one position in the direction
    # it's facing, and shall refuse to move if doing so would result in
    # the robot falling 'off' the table.
    self.assertTrue(self.robot.move())
    self.assertEqual(self.robot.x, 0)
    self.assertEqual(self.robot.y, 1)
    
  def testInvalidMove(self):
    self.robot.place(0,0,'S')
    self.assertFalse(self.robot.move())
    self.assertEqual(self.robot.x, 0)
    self.assertEqual(self.robot.y, 0)

  
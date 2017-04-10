#source_user_name: overkillen
import unittest
from kol1 import Plane, Simulation
from StringIO import StringIO
class MyTest(unittest.TestCase):

	def setUp(self):
		self.simulation = Simulation()
		self.current_orientation = 1337.1
		self.plane = Plane(self.current_orientation)
	def test_Plane(self):
		self.assertEqual(self.plane.current_orientation, self.current_orientation)
	def test_tilt_correction(self):
		#self.current_orientation = abs(self.current_orientation) - abs(int(self.current_orientation))
		self.plane.tilt_correction()
		self.assertLessEqual(self.plane.current_orientation, 1)
	def test_add_error_to_orientation(self):
		angle_error = 10
		self.plane.add_error_to_orientation(angle_error)
        #self.current_orientation = self.current_orientation + angle_error
		self.assertEqual(self.plane.current_orientation, self.current_orientation + angle_error)
	def test_generate_angle_error(self):
        #TODO: statistic analyze!
		pass
	def test_print_separator(self):
		out = StringIO()
		out.stdout = out
		self.simulation.print_separator()
		output = out.getvalue().strip()
		#Not working! self.assertEqual('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++',output)

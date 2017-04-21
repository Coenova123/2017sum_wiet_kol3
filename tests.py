#source_user_name: overkillen
import unittest
import sys
from kol1 import Plane, Simulation
from StringIO import StringIO


class MyTest(unittest.TestCase):
	def setUp(self):
		self.simulation = Simulation()
		self.current_orientation = 1337.1
		self.plane = Plane(self.current_orientation)

	def test_setUp_wrong_Plane(self):
		try:
			new_plane = Plane()
		except:
			new_plane = Plane(self.current_orientation)
		self.assertEqual(new_plane.current_orientation, self.current_orientation)

	def test_setUp_simulation(self):
		self.assertNotEqual(self.simulation, None)

	def test_setUp_Plane(self):
		self.assertNotEqual(self.plane, None)

	def test_Plane(self):
		self.assertEqual(self.plane.current_orientation, self.current_orientation)

	def test_wrong_Plane(self):
		text_to_fail = "some_text_that_should_fail"
		try:
			wrong_plane = Plane(text_to_fail)
		except:
			wrong_plane = Plane(self.current_orientation)
		self.assertEqual(wrong_plane.current_orientation, self.current_orientation)

	def test_tilt_correction(self):
		#self.current_orientation = abs(self.current_orientation) - abs(int(self.current_orientation))
		self.plane.tilt_correction()
		self.assertLessEqual(self.plane.current_orientation, 1)

	def test_add_error_to_orientation(self):
		angle_error = 10
		self.plane.add_error_to_orientation(angle_error)
		#self.current_orientation = self.current_orientation + angle_error
		self.assertEqual(self.plane.current_orientation, self.current_orientation + angle_error)

	def test_wrong_add_error_to_orientation(self):
		wrong_angle_error = "wrong_error_to_fail_program"
		correct_angle_error = 10
		try:
			self.plane.add_error_to_orientation(wrong_angle_error)
		except:
			self.plane.add_error_to_orientation(correct_angle_error)
		#self.current_orientation = self.current_orientation + angle_error
		self.assertEqual(self.plane.current_orientation, self.current_orientation + angle_error)

	def test_360_add_error_to_orientation(self):
		angle_error = 360
		self.plane.add_error_to_orientation(angle_error)
		#self.current_orientation = self.current_orientation + angle_error
		# Should be equal - 360 degrees = 0 degrees
		self.assertEqual(self.plane.current_orientation, self.current_orientation)

	def test_print_separator(self):
		saved_stdout = sys.stdout
		try:
			out = StringIO()
			sys.stdout = out
			self.simulation.print_separator()
			output = out.getvalue().strip()
			self.assertEqual('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++', output)

		finally:
			sys.stdout = saved_stdout

	def test_None_generate_angle_error(self):
		self.assertNotEqual(self.simulation.generate_angle_error(), None)

	'''This is stupid :/ - but test something :)'''
	def test_generate_angle_error(self):
		gauss = []
		iterations = 1000
		MU = 0 #Hardcoded from kol1.py
		SIGMA = 10
		for i in range(iterations):
			gauss.append(self.simulation.generate_angle_error())
		mean = sum(gauss) / float(len(gauss))
		self.assertLessEqual(abs(mean - MU), 0.1*SIGMA) # difference 1%

import random

SIGMA = 10
MU = 0


class Simulation:
    def simulate(self):
        plane = Plane(self.generate_angle_error())
        while True:
            self.print_separator()
            print "Current orientation is {:06.3f}".format(plane.current_orientation)
            plane.tilt_correction()
            print "After tilt correction current orientation is {:06.3f}".format(plane.current_orientation)
            should_be_break = raw_input("Should stop? y-true \n")
            if should_be_break == 'y':
                break
            plane.add_error_to_orientation(self.generate_angle_error())

    def print_separator(self):
        print "+" * 60

    def generate_angle_error(self):
        return random.gauss(MU, SIGMA)


class Plane:
    def __init__(self, current_orientation):
        self.current_orientation = current_orientation

    def tilt_correction(self):
        self.current_orientation = abs(self.current_orientation) - abs(int(self.current_orientation))

    def add_error_to_orientation(self, angle_error):
        self.current_orientation = self.current_orientation + angle_error

if __name__ == "__main__":
   simulation = Simulation()
   simulation.simulate()



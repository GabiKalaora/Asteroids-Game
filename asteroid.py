import random
import math
from screen import Screen


START_POINT = 0
SIZE = 3
SPEED = [-4, -3, -2, -1, 1, 2, 3, 4]


class Asteroid:
    """This department is responsible for creating asteroids"""
    def __init__(self):
        self.__location_x = random.choice(
            range(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X))
        self.__speed_x = random.choice(SPEED)
        self.__location_y = random.choice(
            range(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y))
        self.__speed_y = random.choice(SPEED)
        self.__size = SIZE
        self.__degrees = START_POINT
        self.__radius = 0

    def get_location_x(self):
        """ gets asteroids location on the X axis """
        return self.__location_x

    def set_location_x(self, location_x):
        """ sets new asteroids location on the X axis """
        self.__location_x = location_x

    def get_location_y(self):
        """ gets asteroids location on the y axis """
        return self.__location_y

    def set_location_y(self, location_y):
        """ sets new asteroids location on the y axis """
        self.__location_y = location_y

    def get_speed_x(self):
        """ gets asteroids speed on the X axis """
        return self.__speed_x

    def set_speed_x(self, speed_x):
        """ sets new asteroids speed on the X axis """
        self.__speed_x = speed_x

    def get_speed_y(self):
        """ gets asteroids speed on the Y axis """
        return self.__speed_y

    def set_speed_y(self, speed_y):
        """ sets new asteroids speed on the Y axis """
        self.__speed_y = speed_y

    def get_size(self):
        """gets size of asteroid"""
        return self.__size

    def set_size(self, integer):
        """sets size of asteroid"""
        self.__size = integer

    def get_degrees(self):
        """gets the heading/degree of asteroid """
        return self.__degrees

    def set_degrees(self, degrees):
        """sets new heading/degree of asteroid """
        self.__degrees = degrees

    def get_radius(self):
        """gets radius of asteroid according to asteroid size"""
        return (self.__size * 10) - 5

    def has_intersection(self, obj):
        """checks if asteroid has intersection with other object meaning if
        object entered his area """
        distance = math.sqrt(
            math.pow((obj.get_location_x() - self.__location_x), 2) + math.pow(
                (obj.get_location_y() - self.__location_y), 2))
        if distance <= (self.get_radius() + obj.get_radius()):
            return True
        return False

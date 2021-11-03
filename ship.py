import random
from screen import Screen


START_POINT = 0
RADIUS = 1
LIFE = 3


class Ship:
    """This department is responsible for creating the ship"""
    def __init__(self):
        self.__location_x = random.choice(range(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X))
        self.__speed_x = START_POINT
        self.__location_y = random.choice(range(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y))
        self.__speed_y = START_POINT
        self.__degrees = START_POINT
        self.__radius = RADIUS
        self.__life = LIFE

    def get_location_x(self):
        """ gets ships location on the X axis """
        return self.__location_x

    def set_location_x(self, direction_x):
        """ sets new ships location on the X axis """
        self.__location_x = direction_x

    def get_location_y(self):
        """ gets ships location on the y axis """
        return self.__location_y

    def set_location_y(self, direction_y):
        """ sets new ships location on the y axis """
        self.__location_y = direction_y

    def get_speed_x(self):
        """ gets ships speed on the X axis """
        return self.__speed_x

    def set_speed_x(self, speed_x):
        """ sets new ships speed on the X axis """
        self.__speed_x = speed_x

    def get_speed_y(self):
        """ gets ships speed on the Y axis """
        return self.__speed_y

    def set_speed_y(self, speed_y):
        """ sets new ships speed on the Y axis """
        self.__speed_y = speed_y

    def get_degrees(self):
        """gets the heading/degree of ship """
        return self.__degrees

    def set_degrees(self, degrees):
        """sets new heading/degree of ships according to users choice """
        self.__degrees += degrees

    def get_radius(self):
        """gets radius of ship"""
        return self.__radius

    def get_life(self):
        """gets amount of life's users has left to play """
        return self.__life

    def set_life(self, life):
        """sets amount of life's users has left to play """
        self.__life += life

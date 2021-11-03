RADIUS = 4


class Torpedo:
    """This department is responsible for creating torpedoes"""
    def __init__(self):
        self.__location_x = 0
        self.__speed_x = 0
        self.__location_y = 0
        self.__speed_y = 0
        self.__heading_movement = 0
        self.__radius = RADIUS
        self.__torp_count = 0

    def get_location_x(self):
        """ gets torpedo location on the X axis """
        return self.__location_x

    def set_location_x(self, location_x):
        """ sets new torpedo location on the X axis """
        self.__location_x = location_x

    def get_location_y(self):
        """ gets torpedo location on the y axis """
        return self.__location_y

    def set_location_y(self, location_y):
        """ sets new torpedo location on the y axis """
        self.__location_y = location_y

    def get_speed_x(self):
        """ gets torpedo speed on the X axis """
        return self.__speed_x

    def set_speed_x(self, speed_x):
        """ sets new torpedo speed on the X axis """
        self.__speed_x = speed_x

    def get_speed_y(self):
        """ gets torpedo speed on the Y axis """
        return self.__speed_y

    def set_speed_y(self, speed_y):
        """ sets new torpedo speed on the Y axis """
        self.__speed_y = speed_y

    def get_heading_movement(self):
        """gets heading/degree of direction of torpedo"""
        return self.__heading_movement

    def set_heading_movement(self, heading_movement):
        """sets heading/degree of direction of torpedo"""
        self.__heading_movement = heading_movement

    def get_radius(self):
        """gets radius of torpedo"""
        return self.__radius

    def get_torp_count(self):
        """gets count of torpedo for torpedo life span"""
        return self.__torp_count

    def set_torp_count(self, mun):
        """updates count of torpedo for torpedo life span"""
        self.__torp_count += mun

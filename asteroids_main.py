from screen import Screen
import sys
import random
from ship import Ship
import math
from asteroid import Asteroid
from torpedo import Torpedo

BIG_ASTER = 25
MID_ASTER = 15
SMALL_ASTER = 5
DEFAULT_ASTEROIDS_NUM = 5
LIFE = 3


class GameRunner:
    """This class runs a game called Asteroids in which the spacecraft attempts
     to blast asteroids using torpedoes"""
    def __init__(self, asteroids_amount):
        self.asteroids_amount = asteroids_amount
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__random_x = random.choice(
            range(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X))
        self.__random_y = random.choice(
            range(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y))
        self.__ship = Ship()
        self.__lst_asteroid = []
        self.__lst_torpedo = []
        self.__score = 0
        self.__add_asteroid()

    def run(self):
        """this method runs through do loop and screen and runs the game"""
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        """this method runs through game loop and updates screen accordingly"""
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def ship_movement(self):
        """this method handles ship movement by considering the users choice
        to press up = speeds up ship, right = changes degrees, left =
        changes degrees """
        self.__screen.draw_ship(self.__ship.get_location_x(),
                                self.__ship.get_location_y(),
                                self.__ship.get_degrees())
        if self.__screen.is_left_pressed():
            self.__ship.set_degrees(7)
        if self.__screen.is_right_pressed():
            self.__ship.set_degrees(-7)
        if self.__screen.is_up_pressed():
            self.object_movement(self.__ship)

    def object_movement(self, object):
        """updates objects(all objects = asteroid, ship) speed by
        following formula """
        object.set_speed_x((object.get_speed_x() + math.cos(
            math.radians(object.get_degrees()))))
        object.set_speed_y((object.get_speed_y() + math.sin(
            math.radians(object.get_degrees()))))

    def object_location(self, object):
        """this method updates objects(all objects = torpedo, asteroid,
        ship) by using updated speed we got from object movement in formula """
        object.set_location_x(self.__screen_min_x + (
                object.get_location_x() + object.get_speed_x() - self.__screen_min_x)
                              % (self.__screen_max_x - self.__screen_min_x))
        object.set_location_y(self.__screen_min_y + (
                object.get_location_y() + object.get_speed_y() - self.__screen_min_y) %
                              (self.__screen_max_y - self.__screen_min_y))

    def set_asteroids_amount(self, asteroids_amount):
        """update asteroid amount"""
        self.asteroids_amount += asteroids_amount

    def torpedo_movement(self, torp):
        """this method sets torpedo speed """
        torp.set_speed_x((self.__ship.get_speed_x() + (
                2 * math.cos(math.radians(self.__ship.get_degrees())))))
        torp.set_speed_y((self.__ship.get_speed_y() + (
                2 * math.sin(math.radians(self.__ship.get_degrees())))))

    def __add_asteroid(self):
        """this method adds asteroid while the ship is not at that location """
        while self.asteroids_amount:
            asteroid = Asteroid()
            if asteroid.get_location_x() != self.__ship.get_location_x() or asteroid.get_location_y() != self.__ship.get_location_y():
                self.__screen.register_asteroid(asteroid, asteroid.get_size())
                self.object_location(asteroid)
                self.__lst_asteroid.append(asteroid)
                self.set_asteroids_amount(-1)

    def asteroid_explosion(self, asteroid, torpedo):
        """this method handels asteroid explosion by torpedo while
        consideing asteroid size """
        if asteroid.get_radius() == SMALL_ASTER:
            self.__screen.unregister_asteroid(asteroid)
            self.__lst_asteroid.remove(asteroid)
            return
        asteroid_1 = Asteroid()
        asteroid_2 = Asteroid()
        if asteroid.get_radius() == BIG_ASTER:
            asteroid_1.set_size(2)
            asteroid_2.set_size(2)
        elif asteroid.get_radius() == MID_ASTER:
            asteroid_1.set_size(1)
            asteroid_2.set_size(1)
        self.asteroid_1_from_explosion(asteroid, torpedo, asteroid_1)
        self.asteroid_2_from_explosion(asteroid, torpedo, asteroid_2)
        self.__screen.unregister_asteroid(asteroid)
        self.__lst_asteroid.remove(asteroid)

    def asteroid_1_from_explosion(self, asteroid, torpedo, asteroid_1):
        """adds and creates first asteroid from explosion according to
        exploded asteroid size """
        asteroid_1.set_location_x(asteroid.get_location_x())
        asteroid_1.set_location_y(asteroid.get_location_y())
        asteroid_1.set_speed_x(
            (torpedo.get_speed_x() + asteroid.get_speed_x()) / math.sqrt(
                math.pow(2, asteroid.get_speed_x()) + math.pow(
                    asteroid.get_speed_y(), 2)))
        asteroid_1.set_speed_y(
            (torpedo.get_speed_y() + asteroid.get_speed_y()) / math.sqrt(
                math.pow(2, asteroid.get_speed_x()) + math.pow(
                    asteroid.get_speed_y(), 2)))
        self.__screen.register_asteroid(asteroid_1, asteroid_1.get_size())
        self.__screen.draw_asteroid(asteroid_1, asteroid_1.get_location_x(),
                                    asteroid_1.get_location_y())
        self.object_location(asteroid_1)
        self.__lst_asteroid.append(asteroid_1)

    def asteroid_2_from_explosion(self, asteroid, torpedo, asteroid_2):
        """adds and creates second asteroid from explosion according to
        exploded asteroid size """
        asteroid_2.set_location_x(asteroid.get_location_x())
        asteroid_2.set_location_y(asteroid.get_location_y())
        asteroid_2.set_speed_x(-((
                                         torpedo.get_speed_x() + asteroid.get_speed_x()) / math.sqrt(
            math.pow(2, asteroid.get_speed_x()) + math.pow(
                asteroid.get_speed_y(), 2))))
        asteroid_2.set_speed_y(-((
                                         torpedo.get_speed_y() + asteroid.get_speed_y()) / math.sqrt(
            math.pow(2, asteroid.get_speed_x()) + math.pow(
                asteroid.get_speed_y(), 2))))
        self.__screen.register_asteroid(asteroid_2, asteroid_2.get_size())
        self.__screen.draw_asteroid(asteroid_2, asteroid_2.get_location_x(),
                                    asteroid_2.get_location_y())
        self.object_location(asteroid_2)
        self.__lst_asteroid.append(asteroid_2)

    def update_torpedo(self):
        """this method handles all relevant attributes in torpedo such as
        location, screen time """
        for torp in self.__lst_torpedo:
            self.object_location(torp)
            self.__screen.draw_torpedo(torp, torp.get_location_x(),
                                       torp.get_location_y(),
                                       torp.get_heading_movement())
            self.torpedo_life_span(torp)

    def torpedo_life_span(self, torpedo):
        """this method take care of life span of of torpedo before
        despairing from screen """
        torpedo.set_torp_count(1)
        if torpedo.get_torp_count() >= 200:
            self.__screen.unregister_torpedo(torpedo)
            self.__lst_torpedo.remove(torpedo)

    def update_asteroid(self):
        """this method handles all relevant attributes in asteroid such as
        asteroid location, intersection with ship or torpedo """
        for aster in self.__lst_asteroid:
            self.object_location(aster)
            self.__screen.draw_asteroid(aster, aster.get_location_x(),
                                        aster.get_location_y())
            self.asteroid_ship_intersection(aster)
            self.torpid_asteroid_interaction(aster)
        self.__screen.set_score(self.__score)

    def asteroid_ship_intersection(self, asteroid):
        """this method handles intersection of asteroid with ship such as
        remove life from ship, remove asteroid from game """
        if asteroid.has_intersection(self.__ship):
            self.__ship.set_life(-1)
            self.__screen.show_message('Injury', "Didn't you see that ?!")
            self.__screen.remove_life()
            self.__screen.unregister_asteroid(asteroid)
            self.__lst_asteroid.remove(asteroid)

    def torpid_asteroid_interaction(self, asteroid):
        """this method handles intersection between torpedo and asteroid
        such as adding score and calling all relevant functions for this
        intersection """
        for torp in self.__lst_torpedo:
            if asteroid.has_intersection(torp):
                self.asteroid_explosion(asteroid, torp)
                self.__screen.unregister_torpedo(torp)
                self.__lst_torpedo.remove(torp)
                radius = asteroid.get_radius()
                if radius == BIG_ASTER:
                    self.__score += 20
                elif radius == MID_ASTER:
                    self.__score += 50
                else:
                    self.__score += 100

    def torpedo_shooting(self):
        """this method handles list of torpedoes and location, movement of
        each torpedo from list of torpedoes """
        if len(self.__lst_torpedo) <= 10:
            torpedo = Torpedo()
            self.__lst_torpedo.append(torpedo)
            self.__screen.register_torpedo(torpedo)
            torpedo.set_location_x(self.__ship.get_location_x())
            torpedo.set_location_y(self.__ship.get_location_y())
            torpedo.set_heading_movement(self.__ship.get_degrees())
            self.__screen.draw_torpedo(torpedo, torpedo.get_location_x(),
                                       torpedo.get_location_y(),
                                       torpedo.get_heading_movement())
            self.object_location(torpedo)
            self.torpedo_movement(torpedo)

    def Exit(self):
        """this method handles exiting the game options by winning game or
        exiting by pressing q or by destroying all asteroids """
        if len(self.__lst_asteroid) == 0:
            self.__screen.show_message('you win',
                                       'you destroyed all asteroids')
            self.__screen.end_game()
            sys.exit()
        elif self.__ship.get_life() == 0:
            self.__screen.show_message('you loss',
                                       'you do not have any more life')
            self.__screen.end_game()
            sys.exit()
        elif self.__screen.should_end():
            self.__screen.show_message('your request has been accepted',
                                       "We'll see you next round")
            self.__screen.end_game()
            sys.exit()

    def _game_loop(self):
        """this is main method that runs a single movement of game while
        considering all relevant methods used for ship, asteroid, torpedo """
        self.ship_movement()
        self.object_location(self.__ship)
        self.update_asteroid()
        if self.__screen.is_space_pressed():
            self.torpedo_shooting()
        if self.__lst_torpedo:
            self.update_torpedo()
        self.Exit()


def main(amount):
    """runs GameRunner class. this func runs the game"""
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)

import operator
import utility
import json
import client_json
import json
import game
from game_object import GameObject

## @class Mappable
#  @brief The base object for all mappable things
class Mappable(GameObject):

    def __init__(self, connection, parent_game, id, x, y):
        self._connection = connection
        self._parent_game = parent_game
        self._id = id
        self._x = x
        self._y = y


    @property
    def id(self):
        return self._id
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y





class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("lives cannot be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    def _get_level(self):
        return self._level

    def _set_level_(self, level):
        if level >= 1:
            self._level = level
        else:
            print("Level cannot be 0 or less")
            self._level = 1

    level = property(_get_level, _set_level_)

    def __str__(self):
        return f"Name: {self.name}, Lives: {self._lives}, Level: {self.level}, Score: {(self.level - 1) * 1000}"

class InsufficientSweetsException(Exception):
    """Custom exception example inheriting from Exception class"""

    def __init__(self, sweets):
        self.msg = f"Not enough sweets to eat {sweets} sweets!"

    def __str__(self):
        return self.msg

class Person:
    """ Simple Person class to demo OO principles and a custom exception"""

    def __init__(self, name, gender, sweets=0):
        self._name = name
        self._gender = gender.upper()
        self._sweets = sweets

    def __str__(self):
        return f"Name: {self.get_name()} Gender: {self.get_gender()} has sweet count of: {self.get_sweets()}"

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender

    def give_sweets(self, num):
        self._sweets += num
        return

    def get_sweets(self):
        return self._sweets

    def eat_sweets(self, num):
        if num > self._sweets:
            raise InsufficientSweetsException(num)
        else:
            self._sweets -= num
            return f"{self.get_name()} now has {self.get_sweets()} sweets!"

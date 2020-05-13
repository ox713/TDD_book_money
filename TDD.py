
class Money(object):
    def __init__(self, amount):
        self._amount = amount

    def equals(self, money_obj):
        if self.__class__ == money_obj.__class__:
            return self._amount == money_obj._amount
        else:
            return None

    # fabric method
    def dollar(self):
        return Dollar(self._amount)

    def franc(self):
        return Franc(self._amount)

    def times(self, value_times):
        return Money(self._amount * value_times)


class Dollar(Money):
    # умножение
    def times(self, value_times):
        return Money(self._amount * value_times)



class Franc(Money):
    # умножение
    def times(self, value_times):
        return Money(self._amount * value_times)



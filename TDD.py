
class Money(object):
    def __init__(self, amount):
        self._amount = amount

    def equals(self, money_obj):
        return self._amount == money_obj._amount

class Dollar(Money):
    # умножение
    def times(self, value_times):
        return Dollar(self._amount * value_times)



class Franc(Money):
    # умножение
    def times(self, value_times):
        return Franc(self._amount * value_times)



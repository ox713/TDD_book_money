
class Money(object):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def equals(self, money_obj):
        if self.currency() == money_obj.currency():
            return self._amount == money_obj._amount
        else:
            return None


    def times(self, value_times):
        return Money(self._amount * value_times)

    def currency(self):
        return self._currency








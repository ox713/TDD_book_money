class Dollar(object):
    def __init__(self, amount):
        self.amount = amount

    # умножение
    def times(self, value_times):
        return Dollar(self.amount * value_times)

    def equals(self, dollar_obj):
        # здесь у автора заглушка в виде true, но он сделал отрицательный пример и пришлось писать функцию
        return self.amount == dollar_obj.amount



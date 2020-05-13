class Dollar(object):
    def __init__(self, amount):
        self.__amount = amount

    # умножение
    def times(self, value_times):
        return Dollar(self.__amount * value_times)

    def equals(self, dollar_obj):
        # здесь у автора заглушка в виде true, но он сделал отрицательный пример и пришлось писать функцию
        return self.__amount == dollar_obj.famount()

    def famount(self):
        return self.__amount



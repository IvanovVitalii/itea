# OOP


class Market:

    TOTAL_NUMS_SOLD_PRODUCT = 0

    def __init__(self, name_market, num_sold_product):
        self._name_market = name_market
        self._num_sold_product = num_sold_product
        Market.TOTAL_NUMS_SOLD_PRODUCT += num_sold_product

    def add_num_sold(self, value):
        self._num_sold_product += value
        Market.TOTAL_NUMS_SOLD_PRODUCT += value

    def total_sold(self):
        return '\n'\
               f'Продано товаров магазином {self._name_market}: {self._num_sold_product}''\n' \
               ''f'Всего продано: {Market.TOTAL_NUMS_SOLD_PRODUCT}'


ashan = Market('Ashan', 500)
ashan.add_num_sold(150)
print(ashan.total_sold())

moyo = Market('MOYO', 200)
moyo.add_num_sold(150)
print(moyo.total_sold())

novus = Market('NOVUS', 1000)
novus.add_num_sold(700)
print(novus.total_sold())
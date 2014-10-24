__author__ = 'anthonymace'

class InventoryItem:

    def __init__(self, name, price, id, quantity):
        self._name = name
        self._price = price
        self._id = id
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def id(self):
        return self._id

    @property
    def quantity(self):
        return self._quantity

    def getValue(self):
        return self._price * self._quantity

    def __str__(self):
        return self._name + ": " + self._price
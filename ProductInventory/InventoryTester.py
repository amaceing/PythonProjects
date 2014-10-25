__author__ = 'anthonymace'

from InventoryItem import InventoryItem
from InventoryManager import InventoryManager

def main():
    inventory_list = InventoryManager()
    item1 = InventoryItem("Macbook", 1555.55, 123, 2)
    print(item1)
    print(item1.get_value())

main()
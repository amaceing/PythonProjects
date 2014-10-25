__author__ = 'anthonymace'

class InventoryManager:

    def __init__(self):
        self.items_list = []

    def add_item(self, item):
        self.items_list.append(item)

    def remove_item(self, item):
        if item in self.items_list:
            self.items_list.remove(item)
        else:
            print("This item isn't in the inventory list!")

    def get_item_count(self):
        return len(self.items_list)

    def get_list_value(self):
        total_value = 0
        for item in self.items_list:
            total_value += item.get_value()

        return total_value

    def find_item(self, item):
        if item in self.items_list:
            return item

    def view_inventory(self):
        print(self.items_list)

    def __str__(self):
        for item in self.items_list:
            print(item)

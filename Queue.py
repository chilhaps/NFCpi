from Item import Item
import os

class Queue:
    def __init__(self, items_list = []):
        self.items_list = items_list

    def set_items_list(self, list):
        self.items_list = list

    def get_items_list(self):
        return self.items_list
    
    def get_item_by_index(self, int):
        return self.items_list[int]
    
    def get_length(self):
        return len(self.items_list)
    
    def populate(self, dir):
        temp_list = os.listdir(dir)
        temp_list.sort(key = str.casefold)
        items_list = []

        for i in range(len(temp_list) - 1, -1, -1):
            for j in range(i, len(temp_list) - 1):
                if ('.' in temp_list[j] and '.' not in temp_list[j + 1]):
                    temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]

        for name in temp_list:
            if name[0] == '.':
                continue
            
            items_list.append(Item(dir, name))
            os.chdir(dir)
            
        self.set_items_list(items_list)
    
    def display_contents(self):
        for i in range(len(self.items_list)):
            print('[{}]: {}'.format(i, self.items_list[i].get_name()))

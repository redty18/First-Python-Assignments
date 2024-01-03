class ListOperations:
    def __init__(self):
        self.newList = []

    def add_number(self, num):
        self.newList.append(num)
    
    def remove_number(self, num):
        if num in self.newList:
            self.newList.remove(num)
        else:
            print(num, "Not Found")
    
    def display_numbers(self):
        print(self.newList)

list1 = ListOperations()

list1.add_number(1)
list1.add_number(2)
list1.add_number(3)
list1.add_number(4)
list1.add_number(5)

list1.display_numbers()

list1.remove_number(5)

list1.display_numbers()
class setOperations:
    def __init__(self):
        self.unique_number = set()

    def add_number(self, num):
        self.unique_number.add(num)
    
    def remove_number(self, num):
        if num in self.unique_number:
            self.unique_number.remove(num)
        else:
            print(num, "Not Found")
    
    def display_numbers(self):
        print(self.unique_number)

set1 = setOperations()

set1.add_number(1)
set1.add_number(2)
set1.add_number(3)

set1.display_numbers()

set1.remove_number(3)

set1.display_numbers()
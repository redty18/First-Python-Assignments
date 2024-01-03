class studentDatabase:
    def __init__(self):
        self.newList = []

    def add_student(self, string):
        self.newList.append(string)
    
    def remove_student(self, string):
        if string in self.newList:
            self.newList.remove(string)
        else:
            print(string, "Not Found")
    
    def display_students(self):
        print(self.newList)

list1 = studentDatabase()

list1.add_student("Adit")
list1.add_student("Joe")
list1.add_student("Bob")

list1.display_students()

list1.remove_student("Joe")

list1.display_students()


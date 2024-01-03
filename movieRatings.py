class movieRatings:
    def  __init__(self):
        self.newList = []

    def add_rating(self, num):
        self.newList.append(num)

    def remove_rating(self, num):
        if num in self.newList:
            self.newList.remove(num)
        else:
            print(num, "Not Found")
    
    def calculate_average(self):
        count = 0
        for num in self.newList:
            count += num
        print(count / len(self.newList))
            

list1 = movieRatings()

list1.add_rating(50)
list1.add_rating(50)
list1.add_rating(60)
list1.add_rating(60)
list1.add_rating(70)

list1.remove_rating(60)

list1.calculate_average()


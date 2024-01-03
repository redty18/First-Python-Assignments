class wordTracker:
    def __init__(self):
        self.words = set()

    def add_word(self, word):
        self.words.add(word)
    
    def remove_word(self, word):
        if word in self.words:
            self.words.remove(word)
        else:
            print(word, "Not Found")
    
    def display_words(self):
        print(self.words)

set1 = wordTracker()

set1.add_word("Adit")
set1.add_word("Joe")
set1.add_word("Bob")

set1.display_words()

set1.remove_word("Bob")

set1.display_words()
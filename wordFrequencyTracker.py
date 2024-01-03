class wordFrequencyTracker:
    def __init__(self):
        self.word_counts = {}

    def add_sentence(self, sentence):
        list1 = sentence.split()
        for word in list1:
            self.word_counts[word] = self.word_counts.get(word, 0) + 1
    
    def remove_word(self, word):
        if word in self.word_counts:
            self.word_counts[word] -= 1
            if self.word_counts[word] == 0:
                del self.word_counts[word]
    
    def display_word_counts(self):
        print(self.word_counts)

dict1 = wordFrequencyTracker()
dict1.add_sentence("Hi Hello Hi My Name Is Adit")      

dict1.display_word_counts()

dict1.remove_word("Hi")
dict1.remove_word("Hi")

dict1.display_word_counts()

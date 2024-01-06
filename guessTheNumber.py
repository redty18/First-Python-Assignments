import tkinter as tk
import random


class GuessingGame:
    def __init__(self, tkObject):
        self.tkObject = tkObject
        self.tkObject.geometry("600x360")
        self.tkObject.title("Guess The Number Game")


        #adding Guess The Number label
        self.target = random.randint(1, 30)
        self.label = tk.Label(self.tkObject, text="Guess The Number")
        self.label.pack()


        #adding input box
        self.guess_entry = tk.Entry(self.tkObject)
        self.guess_entry.pack()


        #adding Button which will call checkGuessedNumber function after clicking it
        self.guessBtn = tk.Button(self.tkObject, text="guess", command=self.checkGuessedNumber)
        self.guessBtn.pack()


        self.resultLabel = tk.Label(self.tkObject, text="")
        self.resultLabel.pack()


       
    def checkGuessedNumber(self):
        user_guessed_number = int(self.guess_entry.get())
        result_text = ""
        if (user_guessed_number == self.target):
            result_text = "Congratulations!!!!!!!"
        elif user_guessed_number > self.target:
            result_text = "Guessed too high!!, try again"
        elif user_guessed_number < self.target:
            result_text = "Guessed too low!!, try again"
       
        self.resultLabel.config(text=result_text)


   
tkObjectForRunningApp = tk.Tk()
gameOfGuess = GuessingGame(tkObjectForRunningApp)


tkObjectForRunningApp.mainloop()

import enum
from tkinter import *
from tkinter import messagebox
import words

root = Tk()
#get word is a command that pulls a word from the words.py file using random library
word = words.get_word()
#define all the colors
GREEN = "#007d21"
YELLOW = "#e2e600"
BLACK = "#000000"
WHITE = "#FFFFFF"
#decleare the frames and other variables
root.config(bg=BLACK)

guessnum = 1

wordInput = Entry(root)
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)

#actual function and make sure the person stays under 5 guesses and uses only 5 letter words.
def getGuess():

    global word
    guess = wordInput.get()

    global guessnum
    guessnum += 1

    if guessnum <= 5:

        if len(guess) == 5:

            if word == guess: #CORRECT
                messagebox.showinfo("correct!", f"correct! the word was {word.title()}")
            else:             #INCORRECT
                for i, letter in enumerate(guess):

                    label = Label(root, text=letter.upper())
                    label.grid(row=guessnum, column=i, padx=10, pady=10)

                    if letter == word[i]: #if they get the letter right and right spot
                        label.config(bg=GREEN, fg=BLACK)

                    if letter in word and not letter == word[i]: #if the letter is in the word, but not in the right spot, then make it yellow
                        label.config(bg=YELLOW, fg=BLACK)
                    
                    if letter not in word:
                        label.config(bg=BLACK, fg=WHITE)

        else:
            messagebox.showerror("please use 5 characters", "please use 5 characters in your guess")
    
    else:
        messagebox.showerror("you lose!", f"You Lose! The word was {word}")


wordGuessButton = Button(root, text="Guess", command=getGuess)
wordGuessButton.grid(row=999, column=3, columnspan=2)


root.mainloop()
#!/usr/bin/env python3
"""
Created on Fri Mar  2 15:39:47 2018

@author: jsilvey

----------------WELCOME TO BEE BETA VERSION!----------------

---ABOUT---
Bee is a spelling quiz game with a GUI! As I have worked
with Python before, I thought it would be beneficial to work
for the Python badge by learning a completely new skill: how
to create a GUI in Python.

---DIRECTIONS---
Launch the game by pressing "New Game."
You'll see four randomly-selected words. Some of them may
be misspelled.
Click the button corresponding to a misspelled word, and
press "Enter" to submit your answer. If no words are
misspelled, simply click the "All Correct" button.
If you got all the misspelled words, you'll get 20 pts!
Press "New Game" to begin fresh.

---BETA---
For now, Bee only contains a dictionary of only seven
words--but someday, I plan to connect an external file
with a large sampling of word pairs. 

Thanks, and enjoy!
Joy

"""
import random
import tkinter as tk

# the small test dictionary of word pairs
spelling = {1:['acceptable','acceptible'], \
2:['accidentally','accidentaly'], \
3:['accommodate','accomodate'], \
4:['acquire','aquire'], \
5:['acquit','aquit'], \
6:['a lot','alot'], \
7:['amateur','amature']}

class Root(tk.Tk):
    def __init__(self, word_dict):
        super().__init__()

        self.spelling = word_dict

        self.title("Bee BETA")
        self.geometry("335x200")

        self.game_points = 0
        self.round_points = 0

        # a list of two lists--the first containing words spelled correctly,
        # the second containing words spelled incorrectly
        self.current_words = None
        self.words_this_round = None
        
        # a list of four shuffled randomly-selected words, with some possible 
        # spelling errors
        self.mapping_list = ["", "", "", ""]

        # setting the frame widgets that will hold our misspelled words and buttons
        self.word_frame = tk.Frame(self)
        self.button_frame = tk.Frame(self)
        self.word_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = "w")
        self.button_frame.grid(row = 2, column = 0, columnspan = 3, sticky = "s")

        # creating the buttons for New Game, Enter, and All Correct
        self.play_round = tk.Button(self.button_frame, text = "New Game", padx = 20, command = self.new_game).grid(row = 4, column = 0, pady = 5, padx = 5)
        self.enter = tk.Button(self.button_frame, text = "Enter", padx = 20, command = self.check_ans).grid(row = 4, column = 1, pady = 5, padx = 5)
        self.all_correct = tk.Button(self.button_frame, text = "All Correct", padx = 20, command = self.check_all_correct).grid(row = 4, column = 2, pady = 5, padx = 5)

        # the variables that hold the checkbutton states -- 0 for unchecked, 1 for checked
        self.var_1 = tk.IntVar()
        self.var_2 = tk.IntVar()
        self.var_3 = tk.IntVar()
        self.var_4 = tk.IntVar()

        self.state_variables = [self.var_1, self.var_2, self.var_3, self.var_4]

        # creating the actual checkbuttons for the misspelled words
        self.button1 = tk.Checkbutton(self.word_frame, variable = self.var_1, background = "#4DD0E1", \
        text = self.mapping_list[0], width = 20, height = 3)
        self.button2 = tk.Checkbutton(self.word_frame, variable = self.var_2, background = "#DAF7A6", \
        text = self.mapping_list[1], width = 20, height = 3)
        self.button3 = tk.Checkbutton(self.word_frame, variable = self.var_3, background = "#DAF7A6", \
        text = self.mapping_list[2], width = 20, height = 3)
        self.button4 = tk.Checkbutton(self.word_frame, variable = self.var_4, background = "#4DD0E1", \
        text = self.mapping_list[3], width = 20, height = 3)

        # arranging the buttons in the parent widget
        self.button1.grid(row = 0, column = 0, sticky = "w")
        self.button2.grid(row = 0, column = 1, sticky = "w")
        self.button3.grid(row = 1, column = 0, sticky = "w")
        self.button4.grid(row = 1, column = 1, sticky = "w")

        # creating the labels for Game Points, Round Points, and Status Message
        self.game_points_label = tk.Label(self.word_frame, text = "Game Points: " + str(self.game_points))
        self.round_points_label = tk.Label(self.word_frame, text = "Round Points: " + str(self.round_points))
        self.message = tk.Label(self.word_frame, text = "")
        self.game_points_label.grid(row = 2, column = 0, sticky = "w")
        self.round_points_label.grid(row = 3, column = 0, sticky = "w")
        self.message.grid(row = 2, column = 1, sticky = "e", padx = 10)
        
    def random_num(self, length):
        """
        Returns a random integer from range size length
        """
        a = random.uniform(1, length+1)
        return int(a)
    
    def random_sequence(self, length):
        """
        Takes an int as argument for length of a range of values. 
        Returns a tuple of four randomly assigned and unique ints 
        from the range.
        """
        a = self.random_num(length)
        b = self.random_num(length)
        while a == b:
            b = self.random_num(length)
        c = self.random_num(length)
        while a == c or b == c:
            c = self.random_num(length)
        d = self.random_num(length)
        while a == d or b == d or c == d:
            d = self.random_num(length)
        return (a, b, c, d)
        
    def random_wrong_choice(self):
        """
        Returns either a 0 or 1 randomly
        """
        a = random.uniform(0, 2)
        return int(a)
  
    def assemble_wordlist(self, is_new_game = True):
        """
        The heart of the game. Assembles the words that will be used
        in a round. All entries are randomly chosen, and then the misspelled
        or correctly-spelled versions are randomly selected. 
        """
        self.current_words = [[], []]
        words_this_round = self.random_sequence(len(self.spelling))

        for i in words_this_round:
            a = self.random_wrong_choice()
            self.current_words[a].append(self.spelling[i][a])
            
        guess_words = self.current_words[0] + self.current_words[1]
        mapping_key = self.random_sequence(4)
        
        for value in mapping_key:
            self.mapping_list[value-1] = guess_words[0]
            guess_words = guess_words[1:]

        # this updates the checkbutton widgets with the chosen words for the round
        self.button1.configure(text = self.mapping_list[0])
        self.button2.configure(text = self.mapping_list[1])
        self.button3.configure(text = self.mapping_list[2])
        self.button4.configure(text = self.mapping_list[3])

        # is_new_game resets the game points. This code is triggered by the "New Game" button.
        if is_new_game:
            self.game_points = 0
            self.round_points = 0
            self.game_points_label.configure(text = "Game Points: " + str(self.game_points), foreground = "black")
            self.round_points_label.configure(text = "Round Points: " + str(self.round_points), foreground = "black")

    def new_game(self):
        """
        Resets the checkbutton variables to 0, so any currently-checked boxes become unchecked.
        Calls assemble_wordlist to generate a new round.
        """
        for var in self.state_variables:
            var.set(0)
        self.message.configure(text = "New Game - Begin!")
        self.assemble_wordlist()

    def grade_solution(self):
        """
        Checked whether the Entered solution is a valid one.
        Updates the score labels to reflect the earned score.
        Calls assemble_wordlist(False) to generate a new round for a continuing game.
        """
        correct = True
        for idx in range(4):
            if self.state_variables[idx].get() == 1:
                if self.mapping_list[idx] not in self.current_words[1]:
                    correct = False
            else:
                if self.mapping_list[idx] not in self.current_words[0]:
                    correct = False

        if correct:
            self.message.configure(text = "Proud of you!")
            self.round_points = 20
            self.game_points += 20
            color = "#56AD08"
        else:
            self.message.configure(text = "Noooooope, no way.")
            self.round_points = 0
            color = "red"
        
        for var in self.state_variables:
            var.set(0)

        self.game_points_label.configure(text = "Game Points: " + str(self.game_points), foreground = color)
        self.round_points_label.configure(text = "Round Points: " + str(self.round_points), foreground = color)

        self.assemble_wordlist(False)
    
    def check_all_correct(self):
        """
        This fn is called when "All Correct" is pressed.
        Checks first to ensure that a game is in progress.
        Next checks to ensure that no checkbuttons are active.
        If they are, updates the Status Message to remind the user to uncheck before submitting.
        """
        if self.mapping_list[0] != "":

            something_checked = False

            for var in self.state_variables:
                if var.get() == 1:
                    something_checked = True

            if not something_checked:
                self.grade_solution()
            else: 
                self.message.configure(text = "Uncheck that, please.")

    def check_ans(self):
        """
        This fn is called when "Enter" is pressed.
        Checks first to ensure that a game is in progress.
        Next checks to ensure that at least one checkbutton is active.
        If not, updates the Status Message to remind the user to check something before submitting.
        """
        if self.mapping_list[0] != "":

            none_checked = True

            for var in self.state_variables:
                if var.get() == 1:
                    none_checked = False

            if not none_checked:
                self.grade_solution()
            else:
                self.message.configure(text = "Gotta pick SOMETHING.")

# the function that launches the GUI
if __name__ == "__main__":
    root = Root(spelling)
    root.mainloop()

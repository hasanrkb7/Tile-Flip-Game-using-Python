# importing python gui TKinter and random library
import tkinter as tk
import random

# initializing some global value for future work
pressed = -1
flipped_tiles = 16
moves = 0
high_score = 0


# function to check the score and win and printing the value
def check_win():
    #initializing global variable high_score and moves
    global high_score, moves
    # checking if flipped_tiles is 0 or not
    if flipped_tiles == 0:
        # checking the moves is passed the high score or not if move is less than high score set moves to high score
        if moves <= high_score or high_score == -1:
            high_score = moves
            # open the high score file
            f = open('high_score.txt', 'w')
            # writing the high score in the text file
            f.write(str(high_score))
            f.close()
            # printing the number of clicks and high score into gui
        win_lbl['text']='CLICKS: '+str(moves)+', BEST: '+str(high_score)

def print_moves():
    win_lbl['text'] = 'CLICKS: ' + str(moves)

# function for load the new game
def new_game():
    # initializing some variable for future work
    global pressed, flipped_tiles, buttons, colours, moves, win_lbl, high_score
    #  initially setting the values of pressed variable to -1
    pressed = -1
    # flipped_tiles to number of tiles
    flipped_tiles = 16
    moves = 0
    #initializing a list variable for buttons
    buttons = {}
    win_lbl['text'] = ''

    f = open('high_score.txt', 'r')
    high_score = int(f.readline().strip())
    f.close()
    # shuffeling all the colors using random to make the game difficult
    random.shuffle(colours)

    k=0
    # creating all 16 tiles button
    for i in range(4):
        for j in range(4):
            btn = b(k)
            buttons[k] = btn
            if k!= len(colours)-1: k+=1

    k=0
    # setting color to each tiles
    for i in range(4):
        for j in range(4):
            buttons[k].bttn.grid(row=i, column=j, sticky='nsew')
            if k!= len(colours)-1: k+=1




# class to set the rule of the games
class b:

    def __init__(self, k):
        self.index = k
        # creating a self button
        self.bttn = tk.Button(frm,
                             width=6, height=2,
                             borderwidth=6,
                             bg='white', activebackground = colours[self.index],
                             command=self.btn_press
                             )
    # function to set and store the color of the pressed button
    def btn_press(btn):
        global pressed, moves
        btn.bttn.configure(bg=colours[btn.index])
        moves += 1
        print_moves()
        if pressed == -1:
            pressed = btn.index
        else:
            btn.compare_pressed_btns()
            # function to compare the previous pressed button with the present pressed button
    def compare_pressed_btns(btn):
        global pressed
        global flipped_tiles
        # if the presents pressed button color dont match the previous pressed button color then configure the both button to white
        # and set the pressed button to -1
        if (colours[btn.index] != colours[pressed]):
            btn.bttn.configure(bg='white')
            buttons[pressed].bttn.configure(bg='white')
            pressed = -1
            # if the presents pressed button color  match the previous pressed button color then disable the both button
        elif colours[btn.index] == colours[pressed] and (btn.index != pressed):
            btn.bttn['state'] = tk.DISABLED
            buttons[pressed].bttn['state']= tk.DISABLED
            pressed = -1
            flipped_tiles -= 2
            check_win()

        elif  btn.index == pressed:
            btn.bttn.configure(bg='white')
            pressed = -1

# loading the GUI
window = tk.Tk()
# creating the title
window.title('Flip!')
# configuring the background
window.config(bg = 'black')

# configuring row and colums
window.rowconfigure([0,1],weight=1,pad=2)
window.columnconfigure(0,weight =1, pad=2)

# creating the first frame
frm = tk.Frame(window, bg='Gray')
frm.grid(row = 0, column=0, sticky='nsew')

frm.rowconfigure(list(range(4)), minsize=50, pad=2)
frm.columnconfigure(list(range(4)), minsize=50, pad=2)

buttons = {}
# list variable with all the colors
colours=['YellowGreen', 'Violet', 'Tomato', 'SlateBlue', 'DarkCyan', 'Orange','DodgerBlue', 'ForestGreen']*2
random.shuffle(colours)

# creating second frame with background khaki
frm2 = tk.Frame(window, bg='Khaki')

win_lbl = tk.Label(frm2,
                  width=19, height=1,
                 bg='PowderBlue',
                 relief=tk.GROOVE,
                 borderwidth=2)
win_lbl.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')


new_game_btn = tk.Button(text='NEW GAME',
                        master=frm2,
                       width=10, height=1, borderwidth=3,
                       bg='Plum',
                       command=new_game)
new_game_btn.grid(row=0, column=1, padx=5, pady=5, sticky = 'nsew')

frm2.grid(row=1, column=0, sticky='nsew')
# calling the function new game
new_game()
# continously making the loop to keep the screen on
window.mainloop()

from tkinter import *
import random
from hiddenLayer import *


def display_message():
    global prev
    global player
    buttons[prev[0]][prev[1]].config(text="x",bg="#F0F0F0")
    if check_winner() is False:
        player = players[1]
        label.config(text="your turn")
    elif check_winner() is True:
        label.config(text="bot win")
    elif check_winner() == "Tie":
        label.config(text="Tie!")


def bot_turn(oppo):
    global count
    global player
    global prev
    if count > 8:
        return
    val = calc(grid, count, prev, oppo)
    row = val[0]
    column = val[1]
    if buttons[row][column]['text'] == "" and check_winner() is False:
        prev = val
        window.after(2000, display_message)
        grid[prev[0]][prev[1]] = False
        player = 'o'
        count += 1


def next_turn(row, column):
    global count
    global player
    global grid
    if buttons[row][column]['text'] == "" and check_winner() is False:
        grid[row][column] = True
        buttons[row][column]['text'] = player
        if check_winner() is False:
            player = players[0]
            label.config(text="bot turn")
        elif check_winner() is True:
            label.config(text=("you win"))
        elif check_winner() == "Tie":
            label.config(text="Tie!")
        count += 1
        bot_turn([row, column])


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    else:
        return False


def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global count
    count = 0
    global player
    global prev
    global grid
    grid = [[None, None, None],
            [None, None, None],
            [None, None, None]]
    player = random.choice(players)
    label.config(text=("your" if player == "o" else "bot")+" turn")
    for row in range(3):
        label.config(text=("your" if player == "o" else "bot")+" turn")
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")
    if player == 'x':
        val = calc([], count, None, None)
        player = 'o'
        count += 1
        prev = val
        grid[prev[0]][prev[1]] = False
        window.after(2000, display_message)


prev = None
count = 0
window = Tk()
window.title("Unbreakable bot")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
grid = [[None, None, None],
        [None, None, None],
        [None, None, None]]
label = Label(text=("your" if player == "o" else "bot")+ " turn", font=('consolas',40))
label.pack(side="top")
reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")
frame = Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                  command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
if player == 'x':
    val = calc([], count, None, None)
    player = 'o'
    count += 1
    prev = val
    grid[prev[0]][prev[1]] = False
    window.after(2000, display_message)
window.mainloop()
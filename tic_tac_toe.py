#headers
from tkinter import *
import sys
root = Tk()
root.geometry("300x400")
root.title("TIC TAC TOE")
#data elements
START = True
player1_name = "O"
player2_name = "X"
#start function
def Start():
    global player1_name, player2_name, START
    turn['text'] = "{}{} Turn".format(player1_name, "'s")
    turn.place(x = 115, y = 315)
    START = True
#winCheck function        
def WinCheck():
    if b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O":
        if sys.platform == "darwin":
            b1['bg'] = "#FEFEFE"; b2['bg'] = "#FEFEFE"; b3['bg'] = "#FEFEFE"
        else:
            b1['bg'] = "#54ADFF"; b2['bg'] = "#54ADFF"; b3['bg'] = "#54ADFF"
        return "player1"
    elif b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O":
        if sys.platform == "darwin":
            b4['bg'] = "#FEFEFE"; b5['bg'] = "#FEFEFE"; b6['bg'] = "#FEFEFE"
        else:
            b4['bg'] = "#54ADFF"; b5['bg'] = "#54ADFF"; b6['bg'] = "#54ADFF"
        return "player1"
    elif b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O":
        if sys.platform == "darwin":
            b7['bg'] = "#FEFEFE"; b8['bg'] = "#FEFEFE"; b9['bg'] = "#FEFEFE"
        else:
            b7['bg'] = "#54ADFF"; b8['bg'] = "#54ADFF"; b9['bg'] = "#54ADFF"
        return "player1"
    elif b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O":
        if sys.platform == "darwin":
            b1['bg'] = "#FEFEFE"; b4['bg'] = "#FEFEFE"; b7['bg'] = "#FEFEFE"
        else:
            b1['bg'] = "#54ADFF"; b4['bg'] = "#54ADFF"; b7['bg'] = "#54ADFF"
        return "player1"
    elif b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O":
        if sys.platform == "darwin":
            b2['bg'] = "#FEFEFE"; b5['bg'] = "#FEFEFE"; b8['bg'] = "#FEFEFE"
        else:
            b2['bg'] = "#54ADFF"; b5['bg'] = "#54ADFF"; b8['bg'] = "#54ADFF"
        return "player1"
    elif b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O":
        if sys.platform == "darwin":
            b3['bg'] = "#FEFEFE"; b6['bg'] = "#FEFEFE"; b9['bg'] = "#FEFEFE"
        else:
            b3['bg'] = "#54ADFF"; b6['bg'] = "#54ADFF"; b9['bg'] = "#54ADFF"
        return "player1"
    elif b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O":
        if sys.platform == "darwin":
            b1['bg'] = "#FEFEFE"; b5['bg'] = "#FEFEFE"; b9['bg'] = "#FEFEFE"
        else:
            b1['bg'] = "#54ADFF"; b5['bg'] = "#54ADFF"; b9['bg'] = "#54ADFF"
        return "player1"
    elif b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O":
        if sys.platform == "darwin":
            b3['bg'] = "#FEFEFE"; b5['bg'] = "#FEFEFE"; b7['bg'] = "#FEFEFE"
        else:
            b3['bg'] = "#54ADFF"; b5['bg'] = "#54ADFF"; b7['bg'] = "#54ADFF"
        return "player1"
    
    if b1['text'] == "X" and b2['text'] == "X" and b3['text'] == "X":
        if sys.platform == "darwin":
            b1['bg'] = "#FEFEFE"; b2['bg'] = "#FEFEFE"; b3['bg'] = "#FEFEFE"
        else:
            b1['bg'] = "#54ADFF"; b2['bg'] = "#54ADFF"; b3['bg'] = "#54ADFF"
        return "player2"
    elif b4['text'] == "X" and b5['text'] == "X" and b6['text'] == "X":
        if sys.platform == "darwin":
            b4['bg'] = "#FEFEFE"; b5['bg'] = "#FEFEFE"; b6['bg'] = "#FEFEFE"
        else:
            b4['bg'] = "#54ADFF"; b5['bg'] = "#54ADFF"; b6['bg'] = "#54ADFF"
        return "player2"
    elif b7['text'] == "X" and b8['text'] == "X" and b9['text'] == "X":
        if sys.platform == "darwin":
            b7['bg'] = "#FEFEFE"; b8['bg'] = "#FEFEFE"; b9['bg'] = "#FEFEFE"
        else:
            b7['bg'] = "#54ADFF"; b8['bg'] = "#54ADFF"; b9['bg'] = "#54ADFF"
        return "player2"
    elif b1['text'] == "X" and b4['text'] == "X" and b7['text'] == "X":
        if sys.platform == "darwin":
            b1['bg'] = "#FEFEFE"; b4['bg'] = "#FEFEFE"; b7['bg'] = "#FEFEFE"
        else:
            b1['bg'] = "#54ADFF"; b4['bg'] = "#54ADFF"; b7['bg'] = "#54ADFF"
        return "player2"
    elif b2['text'] == "X" and b5['text'] == "X" and b8['text'] == "X":
        if sys.platform == "darwin":
            b2['bg'] = "#FEFEFE"; b5['bg'] = "#FEFEFE"; b8['bg'] = "#FEFEFE"
        else:
            b2['bg'] = "#54ADFF"; b5['bg'] = "#54ADFF"; b8['bg'] = "#54ADFF"
        return "player2"
    elif b3['text'] == "X" and b6['text'] == "X" and b9['text'] == "X":
        if sys.platform == "darwin":
            b3['bg'] = "#FEFEFE"; b6['bg'] = "#FEFEFE"; b9['bg'] = "#FEFEFE"
        else:
            b3['bg'] = "#54ADFF"; b6['bg'] = "#54ADFF"; b9['bg'] = "#54ADFF"
        return "player2"
    elif b1['text'] == "X" and b5['text'] == "X" and b9['text'] == "X":
        if sys.platform == "darwin":
            b1['bg'] = "#FEFEFE"; b5['bg'] = "#FEFEFE"; b9['bg'] = "#FEFEFE"
        else:
            b1['bg'] = "#54ADFF"; b5['bg'] = "#54ADFF"; b9['bg'] = "#54ADFF"
        return "player2"
    elif b3['text'] == "X" and b5['text'] == "X" and b7['text'] == "X":
        if sys.platform == "darwin":
            b3['bg'] = "#FEFEFE"; b5['bg'] = "#FEFEFE"; b7['bg'] = "#FEFEFE"
        else:
            b3['bg'] = "#54ADFF"; b5['bg'] = "#54ADFF"; b7['bg'] = "#54ADFF"
        return "player2"
    
    elif (b1['text'] != "" and b2['text'] != "" and b3['text'] != "" and
         b4['text']  != "" and b5['text'] != "" and b6['text'] != "" and
         b7['text']  != "" and b8['text'] != "" and b9['text'] != ""):
        return "tie"

    else:
        return False
#disable buttons function
def DisableButtons(ButtonList):
    for a in range(len(ButtonList)):
        ButtonList[a]['state'] = DISABLED
#enable buttons function
def EnableButtons(ButtonList):
    for a in range(len(ButtonList)):
        ButtonList[a]['state'] = NORMAL
# click function
def BtnClick(button):
    global START, player1_name, player2_name
    if START == True:
        if button['text'] == "":
            if turn['text'] == "{}{} Turn".format(player1_name, "'s"):
                button['text'] = "O"
                turn['text'] = "{}{} Turn".format(player2_name, "'s")
            else:
                button['text'] = "X"
                turn['text'] = "{}{} Turn".format(player1_name, "'s")
        check = WinCheck()
        if check != False:
            replay['text'] = "replay?"
            if check == "player1":
                text = "Congratulations, {} won!".format(player1_name)
                buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
                Remove = []
                for i in range(9):
                    if buttons[i]['bg'] == "#FEFEFE":
                        Remove.append(buttons[i])
            elif check == "player2":
                text = "Congratulations, {} won!".format(player2_name)
                buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
                Remove = []
                for i in range(9):
                    if buttons[i]['bg'] == "#FEFEFE":
                        Remove.append(buttons[i])
            else:
                text = "It is a tie!"
            turn['text'] = text

            if check == "player1" or check == "player2":
                for i in range(len(Remove)):
                    buttons.remove(Remove[i])
                DisableButtons(buttons)
#replay function
def Replay():
    Buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    EnableButtons(Buttons)
    for a in range(len(Buttons)):
        Buttons[a]['text'] = ""
        Buttons[a]['bg'] = "#0084FE"
        if sys.platform == "darwin":
            Buttons[a]['fg'] = "#606060"
        else:
            Buttons[a]['fg'] = "#FFFFFF"
    turn['text'] = "click on any button to start the game"
    replay['text'] = ""
    START = True
#buttons
if sys.platform == "darwin":
    b1 = Button(root, width = 3, height = 2, command = lambda:BtnClick(b1), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 40, "normal"))
    b2 = Button(root, width = 3, height = 2, command = lambda:BtnClick(b2), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 40, "normal"))
    b3 = Button(root, width = 3, height = 2, command = lambda:BtnClick(b3), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 40, "normal"))
    b4 = Button(root, width = 3, height = 2, command = lambda:BtnClick(b4), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 40, "normal"))
    b5 = Button(root, width = 3, height = 2, command = lambda:BtnClick(b5), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 40, "normal"))
    b6 = Button(root, width = 3, height = 2, command = lambda:BtnClick(b6), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 40, "normal"))
    b7 = Button(root, width = 3, height = 2, command = lambda:BtnClick(b7), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 40, "normal"))
    b8 = Button(root, width = 3, height = 2, command = lambda:BtnClick(b8), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 40, "normal"))
    b9 = Button(root, width = 3, height = 2, command = lambda:BtnClick(b9), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 40, "normal"))
    replay = Button(root, text = "Play", fg = "#0084FE", highlightbackground = "#FFFFFF", bg = "#FFFFFF", width = 30, height = 2, font = ("Helvetica", 15, "normal"), command = Replay, borderwidth = 0)
else:
    b1 = Button(root, width = 4, height = 2, command = lambda:BtnClick(b1), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 30, "normal"))
    b2 = Button(root, width = 4, height = 2, command = lambda:BtnClick(b2), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 30, "normal"))
    b3 = Button(root, width = 4, height = 2, command = lambda:BtnClick(b3), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 30, "normal"))
    b4 = Button(root, width = 4, height = 2, command = lambda:BtnClick(b4), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 30, "normal"))
    b5 = Button(root, width = 4, height = 2, command = lambda:BtnClick(b5), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 30, "normal"))
    b6 = Button(root, width = 4, height = 2, command = lambda:BtnClick(b6), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 30, "normal"))
    b7 = Button(root, width = 4, height = 2, command = lambda:BtnClick(b7), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 30, "normal"))
    b8 = Button(root, width = 4, height = 2, command = lambda:BtnClick(b8), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 30, "normal"))
    b9 = Button(root, width = 4, height = 2, command = lambda:BtnClick(b9), bg = "#0084FE", borderwidth = 0, state = DISABLED, font = ("Helvetica", 30, "normal"))
    replay = Button(root, text = "Play", fg = "#0084FE", highlightbackground = "#FFFFFF", bg = "#FFFFFF", width = 37, height = 2, font = ("Helvetica", 10, "normal"), command = Replay, borderwidth = 0)

b1.place(x = 0,     y = 0)
b2.place(x = 100,   y = 0)
b3.place(x = 200,   y = 0)
b4.place(x = 0,     y = 99)
b5.place(x = 100,   y = 99)
b6.place(x = 200,   y = 99)
b7.place(x = 0,     y = 198)
b8.place(x = 100,   y = 198)
b9.place(x = 200,   y = 198)
replay.place(x = 0, y = 358)
#label
if sys.platform == "darwin":
    turn = Label(root, text = "Please click play to start the game.", font = ("Helvetica", 15, "normal"), width = 33, height = 3, bg = "#FFFFFF", fg = "#C1C1C1")
    turn.place(x = 0, y = 300)
else:
    turn = Label(root, text = "Please click play to start the game.", font = ("Helvetica", 10, "normal"), width = 37, height = 3, bg = "#FFFFFF", fg = "#C1C1C1")
    turn.place(x = 0, y = 305)
#make the window can't be resizable 
root.resizable(False, False)
#window background color
root.configure(bg = '#FFFFFF')
root.mainloop()
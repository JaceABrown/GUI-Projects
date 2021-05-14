from tkinter import *
import random

top = Tk()
songList = []
myRoll = []

def addTrack():
    songList.append(E1.get())
    E1.delete(0, END)

def printList():
    print(songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text="Block 5 GUI projects")
    LMain.grid(column = 0, row=1)
    
    B1Main = Button(text = "week 1", bg = "white", command= week1)
    B1Main.grid(column= 1, row = 2)

    B2Main = Button(text = "week 2", bg = "white", command= week2)
    B2Main.grid(column= 1, row = 3)

    B3Main = Button(text = "week 3", bg = "white")
    B3Main.grid(column= 1, row = 4)


def week1():
    clearWindow()
    #this is a label widget
    L1 = Label(top, text="ourTunes")
    L1.grid(column= 0, row= 1)

    #this is an entry widget (for text entry)
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row = 2)


    B1 = Button(text = " + ", bg = "white", command= addTrack)
    B1.grid(column= 1, row = 2)

    B2 = Button(text = "playList", bg = "#d4850f", command = printList)
    B2.grid(column= 1, row = 1)

    B3 = Button(text="Export", bg= "#4940e6", command= exportList)
    B3.grid(column= 1, row = 3)

    B4 = Button(text="Main Menu", bg= "yellow", command= MainMeanu)
    B3.grid(column= 0, row = 3)

def week2():
    def rollDice():
        rollTime = E2W2.get()
        dieType = E1W2.get()
    
        clearWindow()

        for x in range(0, int(rollTimes)):
            myRoll.append(random.randint(1, int(dieType)))

        L4W2 = label (top, text= "Here are your roll")
        L4W2.grid(column= 0, row =1)

        L5W2 = label(top, text= "{}".format(myRolls))
        L4W2.grid(column= 0, row =1)
        
        B2W2 = button(text= "main Meanu", bg= "yellow",command = mainMeanu)
    
    clearWindow()

    L1W2 = Label(top, text="Dice Roller App")
    L1W2.grid(column= 0, row = 2)

    L2W2 = Label(top, text="# of Sides")
    L1W2.grid(column= 1, row = 2)
        
    L3W2 = Label(top, text="# of Rolls")
    L1W2.grid(column= 1, row = 2)
        
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column= 1, row = 2)
        
    E2W2 = Entry(top,bd = 5)
    E2W2.grid(column= 1, row = 2)
        
    B1W2 = Button(text= "Roll 'em!", bd = "yellow")

    
    Bclear = Button(text="clear", bg= "white" , command= clearWindow)
    Bclear.grid(column= 5, row = 20)
                    
    print(E1.get())


if __name__ == "__main__":
    mainMenu()
    top.mainloop()


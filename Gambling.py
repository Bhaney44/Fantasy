##Copyright Swan Lake 2020
## MAGA
import csv
from tkinter import *
import tkinter.messagebox as box

master = Tk()

#First Interface - earch entry

#Game
label0 = Label(master, text = 'Home', relief = 'groove', width = 12)
Entry0 = Entry(master, relief = 'groove', width = 12)
label5 = Label(master, text = 'Away', relief = 'groove', width = 12)
Entry17 = Entry(master, relief = 'groove', width = 12)

#Bovada
label1 = Label(master, text = 'Bovada', relief = 'groove', width = 12)
Entry1 = Entry(master, relief = 'groove', width = 12)
Entry2 = Entry(master, relief = 'groove', width = 12)
Entry3 = Entry(master, relief = 'groove', width = 12)
Entry4 = Entry(master, relief = 'groove', width = 12)

#BetTD
label2 = Label(master, text = 'BetTD', relief = 'groove', width = 12)
Entry5 = Entry(master, relief = 'groove', width = 12)
Entry6 = Entry(master, relief = 'groove', width = 12)
Entry7 = Entry(master, relief = 'groove', width = 12)
Entry8 = Entry(master, relief = 'groove', width = 12)

#Fan Duel
label3 = Label(master, text = 'Fan Duel', relief = 'groove', width = 12)
Entry9 = Entry(master, relief = 'groove', width = 12)
Entry10 = Entry(master, relief = 'groove', width = 12)
Entry11 = Entry(master, relief = 'groove', width = 12)
Entry12 = Entry(master, relief = 'groove', width = 12)

#Pinnacle
label4 = Label(master, text = 'Pinnacle', relief = 'groove', width = 12)
Entry13 = Entry(master, relief = 'groove', width = 12)
Entry14 = Entry(master, relief = 'groove', width = 12)
Entry15 = Entry(master, relief = 'groove', width = 12)
Entry16 = Entry(master, relief = 'groove', width = 12)

#write to file function
def write():
    
    #Define Variavles
    Game = str(Number.get())
    Bovada = str(Title.get())
    BetTD = str(Date.get())
    Fand_Duel = str(CPCs.get())
    Pinnacle = str(Abstracts.get())
    
    #Openfile
    with open('Swan_Lake.csv', 'a') as csvfile:
    #define fieldnames
        fieldnames = ['Game', 'Bovada', 'BetTD', 'Fand_Duel', 'Pinnacle']
    #define writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #Write
        writer.writerow({'Game': Game, 'Bovada':Bovada, 'BetTD':BetTD, 'Fand_Duel':Fand_Duel, 'Pinnacle':Pinnacle})

#Button to run write
b1 = Button(master, text = 'Enter Information', relief = 'groove', width = 25, command=write)

#function two to clear the entry widgets
def clear():
    Number.delete(0, END)
    Title.delete(0, END)
    Date.delete(0, END)
    CPCs.delete(0, END)
    Abstracts.delete(0, END)
                        
#button to run function clear
b2 = Button(master, text = 'Store New Word', relief = 'groove', width = 25, command=clear)

#Geometry
label0.grid( row = 1, column = 1, padx = 10 )
Entry0.grid( row = 2, column = 1, padx = 10 )
label5.grid( row = 3, column = 1, padx = 10 )
Entry17.grid( row = 4, column = 1, padx = 10 )

#Bovada
label1.grid( row = 1, column = 2, padx = 10 )
Entry1.grid( row = 2, column = 2, padx = 10 )
Entry2.grid( row = 3, column = 2, padx = 10 )
Entry3.grid( row = 4, column = 2, padx = 10 )
Entry4.grid( row = 5, column = 2, padx = 10 )

#BetTD
label2.grid( row = 1, column = 3, padx = 10 )
Entry5.grid( row = 2, column = 3, padx = 10 )
Entry6.grid( row = 3, column = 3, padx = 10 )
Entry7.grid( row = 4, column = 3, padx = 10 )
Entry8.grid( row = 5, column = 3, padx = 10 )

#Fan Duel
label3.grid( row = 1, column = 4, padx = 10 )
Entry9.grid( row = 2, column = 4, padx = 10 )
Entry10.grid( row = 3, column = 4, padx = 10 )
Entry11.grid( row = 4, column = 4, padx = 10 )
Entry12.grid( row = 5, column = 4, padx = 10 )

#Pinnacle
label4.grid( row = 1, column = 5, padx = 10 )
Entry13.grid( row = 2, column = 5, padx = 10 )
Entry14.grid( row = 3, column = 5, padx = 10 )
Entry15.grid( row = 4, column = 5, padx = 10 )
Entry16.grid( row = 5, column = 5, padx = 10 )

b1.grid( row = 1, column = 6, columnspan = 2)
b2.grid( row = 2, column = 6, columnspan = 2)

#Static Properties
master.title('Swan Lake')

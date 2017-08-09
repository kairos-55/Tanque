from tkinter import *

master = Tk()

def callback():
    print("click!")

b = Button(master, text="OK", command=callback)
b.pack()

mainloop()

'''
Created on 20/04/2017

@author: Alejo
'''

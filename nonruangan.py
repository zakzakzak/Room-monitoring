from Tkinter import *
import ruangan
win = ruangan.win

class nonruangan:
    def __init__(self, cols, rows, colspan, rowspans, height, width, teks, wrn):
        lab = Label(win,  font=('courier',10),text = teks, width = width, height=height, bg = wrn)
        lab.grid(row = rows, column = cols, columnspan = colspan, rowspan = rowspans, sticky=N+S+E+W )
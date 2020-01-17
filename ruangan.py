import Tkinter
from Tkinter import *
global win
win = Tk()

class ruangan:
    global list_keluhan
    list_keluhan = []

    def __init__(self, cols, rows, colspan, rowspans, height, width, nama):
        self.nama = nama
        self.warnaArr = ["#2ecc71", "#3498db", "#e74c3c", "#f1c40f", "#e67e22"]

        self.warnaNow = 0
        # inisialisasi tombol ruangan
        self.tombol = Button(win, fg="white", font=('Helvetica', 10, 'bold'), text=nama, width=width, height=height,
                             bg=self.warnaArr[self.warnaNow], command=self.popup, borderwidth=1,
                             relief=RIDGE)
        self.tombol.grid(row=rows, column=cols, columnspan=colspan, rowspan=rowspans, sticky=N + S + E + W)
        self.t = None

    def popup(self):
        # inisialisasi pop up
        x = win.winfo_pointerx()
        y = win.winfo_pointery()

        if y > 550:
            y = y - 220
        self.t = Tk()
        self.t.overrideredirect(1)
        self.t.geometry('%dx%d+%d+%d' % (250, 220, x, y))

        self.t.config(bg="#2c3e50")
        self.t.bind("<FocusOut>", self.destroy2)
        self.t.wm_title("Pesanan")
        self.lb1 = Label(self.t, width=2, bg="#2c3e50")
        self.lb1.grid(row=1, column=0)
        self.lb2 = Label(self.t, width=2, bg="#2c3e50")
        self.lb2.grid(row=1, column=2)
        self.lb3 = Label(self.t, height=1, bg="#2c3e50")
        self.lb3.grid(row=0, column=0, columnspan=3)

        self.msg = Text(self.t, bg="#34495e", width=25, height=10, relief=FLAT, border=0)
        self.msg.insert(INSERT, "Pesen 1 kursi dan 1 proyektor")

        self.msg.config(fg="white")
        self.msg.grid(row=1, column=1)

        self.btn = Button(self.t, text="Process", command=self.destroy1, font=('Helvetica', 10), bg="#f1c40f",
                          fg="#34495e", anchor=E, border=0)

        self.btn.grid(row=2, column=0, columnspan=3)
        self.msg.config(state=DISABLED)

    def destroy2(self):
        self.t.destroy()
        self.t = None

    def destroy1(self):
        for item in list_keluhan:
            if item[0] == self.nama:
                    item[1].send("Respon")
                    list_keluhan.remove(item)
            print item[0]
        self.t.destroy()
        self.t = None


    def changeColor(self,color):
        self.tombol.config(bg = self.warnaArr[color])
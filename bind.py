from tkinter import *


class Inteface:
    def __init__(self):

        self.entry = Entry(width=20, bg="purple", fg="yellow")
        self.list = Listbox(bg="darkblue", fg="yellow")
        self.sroll = Scrollbar(command=self.list.yview)

        self.entry.bind("<Return>", self.go_to_list)
        self.list.bind("<Double-Button-1>", self.go_to_entry)
        self.list.config(yscrollcommand=self.sroll.set)

        self.sroll.pack(side=RIGHT, fill=Y)
        self.entry.pack()
        self.list.pack()

    def go_to_list(self, info):
        x = self.entry.get().split()
        if x:
            for i in x:
                self.list.insert(END, i)
        self.entry.delete(0, END)

    def go_to_entry(self, info):
        select = self.list.curselection()
        self.entry.insert(END, self.list.get(select) + " ")
        self.list.delete(select)


root = Tk()
i = Inteface()

root.mainloop()

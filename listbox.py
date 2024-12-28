from tkinter import *


class Interface:
    def __init__(self, info, main):
        self.frame = Frame(main, bg="black")
        self.button_left = Button(
            self.frame, text="<<<", width=7, command=self.take_left, bg="darkgrey"
        )
        self.button_right = Button(
            self.frame, text=">>>", width=7, command=self.take_right, bg="darkgrey"
        )
        self.left_box = Listbox(
            self.frame, selectmode=EXTENDED, bg="darkblue", fg="yellow"
        )
        self.right_box = Listbox(
            self.frame, selectmode=EXTENDED, bg="darkgreen", fg="yellow"
        )

        for i in info:
            self.left_box.insert(0, i)

        self.frame.pack(expand=1)
        self.left_box.pack(side=LEFT)
        self.right_box.pack(side=RIGHT)
        self.button_left.pack(expand=1, anchor=S)
        self.button_right.pack(expand=1, anchor=N)

    def take_left(self):
        select = list(self.right_box.curselection())
        select.reverse()
        for i in select:
            self.left_box.insert(0, self.right_box.get(i))
        for i in select:
            self.right_box.delete(i)

    def take_right(self):
        select = list(self.left_box.curselection())
        select.reverse()
        for i in select:
            self.right_box.insert(0, self.left_box.get(i))
        for i in select:
            self.left_box.delete(i)


root = Tk()
root.title("Interface")

i = Interface(["banana", "apple", "cherry", "grape", "watermelon"], root)

root.mainloop()

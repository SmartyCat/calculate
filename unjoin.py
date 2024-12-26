from tkinter import *


class Unjoin:
    def __init__(self, main):
        main.title("Unjoin")
        main["bg"] = "darkgrey"
        self.frame = Frame(main)
        self.label_left = Label(self.frame, width=10, bg="blue", fg="yellow")
        self.label_right = Label(self.frame, width=10, bg="purple", fg="yellow")
        self.entry = Entry(width=20, bg="darkgreen", fg="yellow")

        self.button = Button(self.frame, text="Unjoin", command=self.unjoin)

        self.frame.pack(padx=10, pady=10)
        self.label_left.pack(side=LEFT, fill=Y)
        self.button.pack(side=LEFT)
        self.label_right.pack(side=LEFT, fill=Y)
        self.entry.pack()

    def unjoin(self):
        text = self.entry.get()
        if len(text) > 0:
            lst = text.split()
            if len(lst) > 1:
                self.label_left["text"] = lst[0]
                self.label_right["text"] = lst[1:]
            else:
                self.label_left["text"] = lst[0]
                self.label_right["text"] = "Empty"
        else:
            self.label_left["text"] = "Empty"
            self.label_right["text"] = "Empty"


root = Tk()


u = Unjoin(root)

root.mainloop()

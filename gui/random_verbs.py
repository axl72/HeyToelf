import tkinter as tk



class Label(tk.Label):
    def __init__(self,widget, size, text):
        tk.Label.__init__(self, widget, text=text, fg="black", font=("consolas", size),
                height=4, width=(len(text)+5))
        self.pack()

class Entry(tk.Entry):
    def __init__(self, widget):
        tk.Entry.__init__(self, widget, width=20)
        self.pack()

class Button(tk.Button):
    def __init__(self, widget, text, command=lambda:print("The button was pressed")):
        tk.Button.__init__(self, widget, text=text, command=command)
        self.pack(pady=10)

        

if __name__ == "__main__":
    pass

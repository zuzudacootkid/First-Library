from tkinter import*

class Starter:

    def __init__(self, parent):

        self.start_frame = Frame(parent, bg="pink", padx=150, pady=180)
        self.start_frame.grid(row=1, column=3)






root = Tk()
root.title("Virtual Library")
root.mainloop()



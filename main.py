from tkinter import*
import urllib.request





class Starter:

    def __init__(self, parent):

        self.start_frame = Frame(parent, bg="pink", padx=150, pady=180)
        self.start_frame.grid(row=1, column=3)


        self.heading_label = Label (self.start_frame, text = "Virtual library ct", bg="gray85", font=("montserrat", "12", "bold") )
        self.heading_label.grid(row=1,column=3)
      


      






root = Tk()
root.title("Virtual Library")
root.mainloop()




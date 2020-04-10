from tkinter import *
from PIL import ImageTk, Image
import math

class OrderProg:

    def __init__(self, root):

        self.root = root
        self.frame = Frame(self.root)

        self.images = {
            "image_logo": ImageTk.PhotoImage(Image.open("images/crumpetorium_logo.jpg"))
        }
        Label(self.root, image=self.images["image_logo"], bg="white").grid(row=0, columnspan=3)

        self.textentry("testing", 0)
        self.textentry("testing", 1)
        self.textentry("testing", 2)

    def textentry(self, labeltext, entrynum):

        # work out which row
        textentryrow = math.ceil((entrynum+1)/3)
        print(textentryrow)

        Entry(self.root, width=40, bg="white").grid(row=textentryrow, column=entrynum)
        Label(self.root, text=labeltext).grid(row=textentryrow+1, column=entrynum)




def main():
    # create Tk instance
    root = Tk()
    # set program title
    root.title("Crumpetorium order list")
    #create instance
    orderprog = OrderProg(root)
    # run event loop
    root.mainloop()

if __name__ == "__main__":
    main()
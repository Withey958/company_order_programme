from tkinter import *


class OrderProg:

    def __init__(self, root):

        self.root = root
        self.frame = Frame(self.root)



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
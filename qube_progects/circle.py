from tkinter import Canvas, Frame, Tk, BOTH


def main():
    root = Tk()
    c = Canvas(width=450, height=300, bg = 'red')
    c.pack()
    circle = c.create_oval(150, 150,50,50, width = 1, outline='grey')
    root.mainloop()


if __name__ == '__maine__':
    main()
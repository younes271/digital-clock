import time
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style

class DigitalClock(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.time1 = ''
        self.time()

    def initUI(self):
        self.parent.title("Digital Clock")
        Style().configure("TFrame", background="#333")
        self.pack(fill=BOTH, expand=1)
        self.timeLabel = Label(self, background="#333", foreground="#fff", font=("Helvetica", 48))
        self.timeLabel.pack()

    def time(self):
        time2 = time.strftime('%H:%M:%S')
        if time2 != self.time1:
            self.time1 = time2
            self.timeLabel.config(text=time2)
        self.timeLabel.after(200, self.time)

def main():
    root = Tk()
    clock = DigitalClock(root)
    clock.mainloop()

if __name__ == '__main__':
    main()

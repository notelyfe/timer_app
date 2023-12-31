from tkinter import *
from playsound import playsound
from tkinter import messagebox
import time
import os

root = Tk()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Timer:
    def __init__(self, root):

        self.root = root
        root.title("Timer Application")
        root.geometry("420x430")
        root.config(bg="#000")
        root.resizable(False, False)
        self.time = 0
        self.running = False

        # creating root frame for timer
        rootFrame = Frame(root, bg = "#000", pady=10, padx=80)
        rootFrame.grid(row=0, column=0)
        title = Label(rootFrame, text="Timer Application", font="arial 16 bold", bg="#000", fg="white", justify=CENTER, width=15, padx=5, pady=5)
        title.grid(row=0, column=0)

        # entry value frame
        entryFrame = Frame(root, bg="#000", pady=10, padx=10 )
        entryFrame.grid(row=1, column=0)
        
        #time labels
        self.secLabel = Label(entryFrame, text="Seconds", font="arial 12 bold", bg="#000", fg="white", padx=10, pady=10, width=8)
        self.secLabel.grid(row=0, column=0)

        self.minLabel = Label(entryFrame, text="Minutes", font="arial 12 bold", bg="#000", fg="white", padx=10, pady=10, width=8)
        self.minLabel.grid(row=1, column=0)

        self.hrsLabel = Label(entryFrame, text="Hours", font="arial 12 bold", bg="#000", fg="white", padx=10, pady=10, width=8)
        self.hrsLabel.grid(row=2, column=0)

        # taking input
        self.secVal = StringVar()
        secEntry = Entry(entryFrame, textvariable=self.secVal, width=5, font="arial 12")
        secEntry.grid(row=0, column=1)

        self.minVal = StringVar()
        minEntry = Entry(entryFrame, textvariable=self.minVal, width=5, font="arial 12")
        minEntry.grid(row=1, column=1)

        self.hrsVal = StringVar()
        hrsEntry = Entry(entryFrame, textvariable=self.hrsVal, width=5, font="arial 12")
        hrsEntry.grid(row=2, column=1)

        # counter and button frame
        mainFrame = Frame(root, bg = "#000", pady=5, padx=80)
        mainFrame.grid(row=3, column=0)

        timerFrame = Frame(mainFrame, bg = "#000", pady=10)
        timerFrame.grid(row=1, column=0)

        self.btnFrame = Frame(mainFrame, bg = "#000", pady=10)
        self.btnFrame.grid(row=2, column=0)

        self.timer = Label(timerFrame, text="00:00:00", font="arial 16 bold", bg="#000", fg="white", justify=CENTER, width=15)
        self.timer.grid(row=0, column=0)

        self.btnStart = Button(self.btnFrame, text="Start", font="arial 14 bold", bg="green", fg="white", command=self.Start)
        self.btnStart.grid(row=0, column=0)

        self.btnStop = Button(self.btnFrame, text="Stop", font="arial 14 bold", bg="red", fg="white", command=self.Stop)
        self.btnStop.grid(row=0, column=1)

    def Start(self):

        seconds = self.secVal.get()
        minutes = self.minVal.get()
        hours = self.hrsVal.get()

        if seconds == "":
            seconds = 0
        if minutes == "":
            minutes = 0
        if hours == "":
            hours = 0

        if int(seconds) >= 60:
            playsound(resource_path("error.mp3"))
            messagebox.showerror("Error","Error!! Can't set seconds greater than 59.")
            self.secVal.set("")

        elif int(minutes) >= 60:
            playsound(resource_path("error.mp3"))
            messagebox.showerror("Error","Error!! Can't set Minutes greater than 59.")
            self.minVal.set("")

        elif int(hours) >= 25:
            playsound(resource_path("error.mp3"))
            messagebox.showerror("Error","Error!! Can't set hours greater than 24.")
            self.hrsVal.set("")
        
        else:

            self.btnStart.config(text="Pause", command=self.pause, bg="yellow", fg="black")

            self.running = True
            self.secVal.set("")
            self.minVal.set("")
            self.hrsVal.set("")
            self.time = int(hours)*3600 + int(minutes)*60 + int(seconds)
            self.update_timer()

    def Stop(self):
        self.running = False
        self.timer.config(text="00:00:00")

    def update_timer(self):

        self.running = True

        while self.time > -1 and self.running == True:

            newSec = self.time % 60
            newMin = self.time // 60
            newHrs = self.time // 3600

            self.timer.config(text="{:02d}:{:02d}:{:02d}".format(newHrs, newMin, newSec))
            self.root.update()
            time.sleep(1)

            if self.time == 0:
                playsound(resource_path("alarm.mp3"))
                messagebox.showinfo("Info","Times up...")
                self.btnStart.config(text="Start", command=self.Start, bg="green", fg="white")


            self.time -= 1

    def pause(self):
        self.btnStart.config(text="Start", command=self.update_timer, bg="green", fg="white")
        self.running = False

timer = Timer(root)
root.mainloop()
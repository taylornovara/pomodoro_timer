"""

A simple Pomodoro Timer app using tkinter for the GUI

"""
import tkinter

# Constants
PINK = "#FFC3C3"
LITE_RED = "#FF8C8C"
RED = "#FF5D5D"
YELLOW = "#FFE3A9"
FONT_NAME = ""
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25

# Creates program window
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50)

# Creates our background image and sets it to the center of the window
canvas = tkinter.Canvas(width=200, height=224)
img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=img)
canvas.pack()

# Keeps program window open
window.mainloop()


"""

A simple Pomodoro Timer app using tkinter for the GUI

"""
import tkinter

# Constants
PINK = "#FFC3C3"
LITE_RED = "#FF8C8C"
RED = "#FF5D5D"
YELLOW = "#FFE3A9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25

# Creates program window
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=LITE_RED)

# Title
title_label = tkinter.Label(text='TIMER', bg=LITE_RED, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

# Creates our background image and txt. Sets both to the center of the window
canvas = tkinter.Canvas(width=200, height=224, bg=LITE_RED, highlightthickness=0)
img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = tkinter.Button(text="Start", font=(FONT_NAME, 18), bd=0)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 18), bd=0)
reset_button.grid(column=2, row=2)

# Check Marks
check_marks = tkinter.Label(text="✓", bg=LITE_RED, font=(FONT_NAME, 50))
check_marks.grid(column=1, row=3)

# Keeps program window open
window.mainloop()

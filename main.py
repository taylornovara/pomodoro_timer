"""

A simple Pomodoro Timer app using tkinter for the GUI

"""
import tkinter
import math

# Constants
PINK = "#FFC3C3"
LITE_RED = "#FF8C8C"
RED = "#FF5D5D"
YELLOW = "#FFE3A9"
GREEN = '#59CE8F'
FONT_NAME = ""
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0


# Functions

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 15
    short_break_sec = SHORT_BREAK_MIN * 5
    long_break_sec = LONG_BREAK_MIN * 10

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Long Break", fg=GREEN, bg=LITE_RED, font=(FONT_NAME, 40))
    elif reps % 2 == 0:
        countdown(work_sec)
        title_label.config(text="Work", fg=RED, bg=LITE_RED, font=(FONT_NAME, 40))
    elif reps % 2 != 0:
        countdown(short_break_sec)
        title_label.config(text="Short Break", fg=YELLOW)


def countdown(count):
    minute = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer, text=f"{minute}:{seconds}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


def reset_timer():
    window.after_cancel()


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
timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = tkinter.Button(text="Start", font=(FONT_NAME, 18), bd=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 18), bd=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check Marks
check_marks = tkinter.Label(bg=LITE_RED, font=(FONT_NAME, 50))
check_marks.grid(column=1, row=3)

# Keeps program window open
window.mainloop()

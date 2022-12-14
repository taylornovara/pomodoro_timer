"""

A simple Pomodoro Timer app using tkinter for the GUI. Did this work?

"""
import tkinter
import math

# Constants
PINK = "#FFC3C3"
LITE_RED = "#FF8C8C"
RED = "#FF5D5D"
YELLOW = "#FFE3A9"
GREEN = '#59CE8F'
WHITE = '#ffffff'
FONT_NAME = ""
# 25 minutes
WORK_MIN = 25
# 5 minutes
SHORT_BREAK_MIN = 5
# 15 minutes
LONG_BREAK_MIN = 15
reps = 0
timer = None


# Functions

def start_timer():
    """Starts the timer countdown based on the number of reps."""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Long Break", fg=GREEN, bg=LITE_RED, font=(FONT_NAME, 40))
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Short Break", fg=YELLOW)
    elif reps % 2 != 0:
        countdown(work_sec)
        title_label.config(text="Work", fg=RED, bg=LITE_RED, font=(FONT_NAME, 40))


def countdown(count):
    """A function that receives the time and counts down to zero. Restarts as soon as it hits zero.
    """
    # Stores the minutes and seconds into their own variables.
    minute = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        window.bell()
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        # Divide reps by 2 to get the number of work sessions, add a check mark to marks, and configure check_marks
        # label.
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


def reset_timer():
    """Reset all the check marks, text back to TIMER, and stop timer."""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER", fg=WHITE)
    check_marks.config(text="")
    global reps
    reps = 0


# Creates program window
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=LITE_RED)
window.resizable(False, False)

# Title
title_label = tkinter.Label(text='TIMER', fg=WHITE, bg=LITE_RED, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

# Creates our background image and txt, sets both to the center of the window. Adds tomato icon
canvas = tkinter.Canvas(width=200, height=224, bg=LITE_RED, highlightthickness=0)
img = tkinter.PhotoImage(file="tomato_img.png")
icon = tkinter.PhotoImage(file="tomato_icon.png")
window.iconphoto(False, icon)
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = tkinter.Button(text="Start", font=(FONT_NAME, 18), bd=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 18), bd=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check Marks
check_marks = tkinter.Label(bg=LITE_RED, fg=RED, font=(FONT_NAME, 40))
check_marks.grid(column=1, row=3)

# Keeps program window open
window.mainloop()

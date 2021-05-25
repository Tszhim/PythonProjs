from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
cycle_step = 1
reset = False


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global reset
    reset = True


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_begin():
    timer_label.config(text="Work!")
    countdown(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time):
    global cycle_step
    global reset

    # When reset button is pressed, clear all existing variables to start the timer over.
    if reset:
        time = 0
        cycle_step = 0
        reset = False

    # Updating time on canvas.
    min_left = math.floor(time / 60)
    sec_left = time % 60
    if sec_left < 10:
        sec_left = f"0{sec_left}"
    canvas.itemconfig(time_remaining, text=f"{min_left}:{sec_left}")

    # When timer hits 0, renew with next cycle.
    if time > 0:
        window.after(1000, countdown, time - 1)
    else:
        cycle_step = cycle_step + 1
        if cycle_step % 8 == 0:
            timer_label.config(text="Rest!")
            check_mark_update()
            countdown(LONG_BREAK_MIN * 60)
        elif cycle_step % 2 == 1:
            timer_label.config(text="Work!")
            check_mark_update()
            countdown(WORK_MIN * 60)
        else:
            timer_label.config(text="Break!")
            check_mark_update()
            countdown(SHORT_BREAK_MIN * 60)

# Updates check marks to indicate number of pomodoros finished.
def check_mark_update():

    # Printing number instead of check marks on screen after 30 sessions as to not overflow out of the window.
    if cycle_step > 30:
        session_tracker.config(text="Pomodoros Finished: " + str(math.floor((cycle_step - 1) / 2)))
    else:
        checks = ""
        for i in range(0, math.floor((cycle_step - 1) / 2)):
            checks = checks + "✔"
        session_tracker.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
# Window setup.
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas and timer setup.
canvas = Canvas(width=220, height=250, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(110, 125, image=tomato)
time_remaining = canvas.create_text(110, 135, text="00:00", font=(FONT_NAME, 20, "normal"), fill="white")

# Label displaying whether it is currently a work or break period.
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)

# Shows checks or number (after 30 checks) to indicate number of completed sessions.
session_tracker = Label(text="", font=(FONT_NAME, 10, "normal"), fg=GREEN, bg=YELLOW)

# Start and reset buttons for user.
start_button = Button(text="Start", fg="white", bg=PINK, command=timer_begin)
reset_button = Button(text="Reset", fg="white", bg=PINK, command=timer_reset)

# Grid formatting of elements.
timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
session_tracker.grid(row=3, column=1)

window.mainloop()

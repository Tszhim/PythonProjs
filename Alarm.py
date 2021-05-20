import threading
import time
from tkinter import *
import tkinter.font
from datetime import datetime
from playsound import playsound


class Alarm():
    def __init__(self):
        # root config
        self.root = Tk()
        self.root.title("Alarms")

        # greeting label
        self.greetingFont = tkinter.font.Font(family="Helvetica", size=13)
        self.label_greeting = Label(self.root, text="", font=self.greetingFont)
        self.label_greeting.pack()
        self.update_greeting()

        # add_alarm button
        self.add_alarm = Button(self.root, text="+ Add an alarm", command=self.prompt_alarmInfo)
        self.add_alarm.pack()

        self.root.mainloop()

    def update_greeting(self):
        curr_time = datetime.now()
        curr = curr_time.strftime("%H:%M:%S %p")
        if 0 < curr_time.hour < 12:
            curr = "Good Morning: " + curr
        elif 12 <= curr_time.hour < 16:
            curr = "Good Afternoon: " + curr
        elif 16 <= curr_time.hour < 21:
            curr = "Good Evening: " + curr
        elif 21 <= curr_time.hour < 24:
            curr = "Good Night: " + curr
        else:
            curr = "It is currently " + curr

        self.label_greeting.configure(text=curr)
        self.root.after(1000, self.update_greeting)

    def add_hr(self, label_hour):
        curr = label_hour["text"]
        if curr == "12":
            label_hour["text"] = "1"
        else:
            new_curr = str(int(curr) + 1)
            label_hour["text"] = new_curr

    def subtract_hr(self, label_hour):
        curr = label_hour["text"]
        if curr == "1":
            label_hour["text"] = "12"
        else:
            new_curr = str(int(curr) - 1)
            label_hour["text"] = new_curr

    def add_min(self, label_minute):
        curr = label_minute["text"]
        if curr[0] == "0":
            curr = curr[-1]

        if curr == "59":
            label_minute["text"] = "00"
        else:
            new_curr = int(curr) + 1
            new_curr_str = str(new_curr)

            if new_curr < 10:
                label_minute["text"] = "0" + new_curr_str
            else:
                label_minute["text"] = new_curr_str

    def subtract_min(self, label_minute):
        curr = label_minute["text"]
        if curr[0] == "0":
            curr = curr[-1]

        if curr == "0":
            label_minute["text"] = "59"
        else:
            new_curr = int(curr) - 1
            new_curr_str = str(new_curr)
            if new_curr < 10:
                label_minute["text"] = "0" + new_curr_str
            else:
                label_minute["text"] = new_curr_str

    def AMPM(self, label_AMPM, input):
        if input == "AM":
            label_AMPM["text"] = "AM"
        else:
            label_AMPM["text"] = "PM"

    def set(self, input_window, label_hour, label_minute, label_AMPM):
        hr = label_hour["text"]
        minute = label_minute["text"]
        AMPM = label_AMPM["text"]

        if AMPM == "PM":
            alter = int(hr) + 12
            if alter == 24:
                hr = "0"
            else:
                hr = str(alter)

        concat = hr + ":" + minute
        input_window.destroy()

        self.prompt_alarm(concat)

    def prompt_alarmInfo(self):
        input_window = Toplevel(self.root)
        label_instruct = Label(input_window, text="Set Alarm Time:")

        timeFont = tkinter.font.Font(family="Helvetica", size=10)
        label_hour = Label(input_window, text="12", font=timeFont)
        label_colon = Label(input_window, text=":", font=timeFont)
        label_minute = Label(input_window, text="00", font=timeFont)
        label_AMPM = Label(input_window, text="AM", font=timeFont)
        label_fill = Label(input_window, text="     ")

        button_hour_add = Button(input_window, text="+", font=timeFont, command=lambda: self.add_hr(label_hour))
        button_hour_subtract = Button(input_window, text="-", font=timeFont, command=lambda: self.subtract_hr(label_hour))
        button_minute_add = Button(input_window, text="+", font=timeFont, command=lambda: self.add_min(label_minute))
        button_minute_subtract = Button(input_window, text="-", font=timeFont, command=lambda: self.subtract_min(label_minute))
        button_AMtoPM = Button(input_window, text="PM", font=timeFont, command=lambda: self.AMPM(label_AMPM, "PM"))
        button_PMtoAM = Button(input_window, text="AM", font=timeFont, command=lambda: self.AMPM(label_AMPM, "AM"))
        button_set = Button(input_window, text="Set", font=timeFont, command=lambda: self.set(input_window, label_hour, label_minute, label_AMPM))

        label_instruct.grid(row=0, column=2)
        button_hour_add.grid(row=1, column=0)
        button_minute_add.grid(row=1, column=2)
        button_PMtoAM.grid(row=1, column=3)
        label_hour.grid(row=2, column=0)
        label_colon.grid(row=2, column=1)
        label_minute.grid(row=2, column=2)
        label_AMPM.grid(row=2, column=3)
        label_fill.grid(row=2, column=4)
        button_set.grid(row=2, column=5)
        button_hour_subtract.grid(row=3, column=0)
        button_minute_subtract.grid(row=3, column=2)
        button_AMtoPM.grid(row=3, column=3)

        self.root.mainloop()

    def prompt_alarm(self, concat):
        alarm_thread = threading.Thread(target=self.make_alarm, args=(concat,))
        alarm_thread.start()

    def make_alarm(self, alarm_time):
        while True:
            curr_time = datetime.now().strftime("%H:%M")
            if alarm_time == curr_time:
                # insert choice of alarm sound/music
                playsound('C:\\Users\\falco\\PycharmProjects\\AlarmApp\\viator.wav')
                break
            else:
                time.sleep(5)


instance = Alarm()

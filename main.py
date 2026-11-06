from tkinter import *
import time
SPEED_VALUE= 0.00
COUNT_MIN= 3.00

#-------------------------- FUNCTIONS ------------------------------------------------

def start_timer():
    global COUNT_MIN
    if COUNT_MIN > 0:
        COUNT_MIN -= 1/60
        time_label.config(text=f"{COUNT_MIN:.2f} min")
        window.after(1000, start_timer)
    else:
        time_label.config(text="Time's up!")


#-------------------------- WINDOW  ------------------------------------------------

window= Tk()
window.minsize(width=600, height=300)
window.title("Typing Speed Tester")

#-------------------------- LABELS ------------------------------------------------

time_label= Label(text=COUNT_MIN)
time_label.grid(column=0,row=1)
text_area = Entry(window, width=40)
text_area.grid(column=0,row=0,padx=5,pady=15)
speed_label= Label(text="Speed")
speed_label.grid(column=1, row=1)
speed_value= Label(text=f"{SPEED_VALUE} wpm ")
speed_value.grid(column=2, row=1)

#-------------------------- BUTTONS ------------------------------------------------
start_btn= Button(text="start", command=start_timer)
start_btn.grid(column=2, row=2)

window.mainloop()
# TODO: 2. typing input area
# TODO: 3. count typed words
# TODO: 4. count time
# TODO: 5. calculate w/m
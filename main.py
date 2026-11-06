from tkinter import *
SPEED_VALUE= 0.00


def start_timer():
    pass

window= Tk()
window.minsize(width=600, height=300)
window.title("Typing Speed Tester")

speed_label= Label(text="Speed")
speed_label.grid(column=1, row=1)
speed_value= Label(text=f"{SPEED_VALUE} wpm ")
speed_value.grid(column=2, row=1)

start_btn= Button(text="start", command=start_timer)
start_btn.grid(column=2, row=2)
window.mainloop()

# TODO: 2. typing input area
# TODO: 3. count typed words
# TODO: 4. count time
# TODO: 5. calculate w/m


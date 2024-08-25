from tkinter import *

root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=100)
canvas  = Canvas(width=400, height=444)

tomato_img = PhotoImage(file="./assets/tomato.png")
canvas.create_image(200, 222, image=tomato_img)
canvas.pack()



root.mainloop()
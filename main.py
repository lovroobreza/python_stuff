from tkinter import *

root = Tk()
root.title("Password manager")
root.minsize(width=500, height=600)
root.configure(padx=30, pady=30)

canvas = Canvas()
canvas.configure()

logo_image=PhotoImage(file="./assets/logo.png")

canvas.create_image(200,200,image=logo_image)

root.mainloop()
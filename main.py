from tkinter import *

root = Tk()
root.title("Lovro")
root.configure(background="white")
root.config(padx=20, pady=20)




def miles_to_km():
   miles = float(input.get())
   km = miles * 1.7
   km_label.config(text=f"{km}")

input = Entry(width=7)

miles_label = Label(text="Miles")

is_equal_label = Label(text="Is equal")

km_label = Label(text="0")

km_text = Label(text="Kilmoeters")

button = Button(text="Calulcate button", command=miles_to_km)


input.grid(column=1, row=0)

miles_label.grid(column=2, row=0)

is_equal_label.grid(column=0, row=1)

km_label.grid(column=1, row=1)

km_text.grid(column=2, row=1)

button.grid(column=1, row=2)
                   
root.mainloop()
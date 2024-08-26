from tkinter import *
import string, random, math
from tkinter import messagebox

# root
root = Tk()
root.title("Password manager")
root.configure(padx=20, pady=30)

# canvas
canvas = Canvas(width=200)
logo_image = PhotoImage(file="./assets/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1,row=0)

# website
website_input = Entry(width=35)
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
website_input.grid(column=1, row=1, columnspan=2)

# email
email_input = Entry(width=35)
email_label = Label(text="Email")
email_label.grid(column=0, row=2)
email_input.grid(column=1, row=2, columnspan=2)

email_input.insert(0, "obreza.lovro@gmail.com")

# password
def getLetter():
    return random.choice(string.ascii_letters)
def getNumber():
    return math.ceil(random.random() * 9)

def generate_password():
    generated_pass = ""
    for _ in range(1,9):
        if random.random() > 0.5:
            generated_pass += getLetter()
        else:
            generated_pass += str(getNumber())
    print(generated_pass)
    password_input.delete(0, END)
    password_input.insert(0, generated_pass)

password_input = Entry(width=21)
password_label = Label(text="Password")
password_button = Button(text="Generate Password", command=generate_password)
password_label.grid(column=0, row=3)
password_input.grid(column=1, row=3)
password_button.grid(column=2, row=3)


# add button
def add_password():
    with open("./files/passwords.txt", "a") as data_file:
        w = website_input.get()
        e = email_input.get()
        p = password_input.get()
        if w == "" or e == "" or p == "":
            messagebox.showerror(title="Empty fields", message="Fill out empty fields")
            return

        is_ok = messagebox.askokcancel(title=w, message="You sure you want to add those details?")
        if is_ok:
            data_file.write(f"{w} | {e} | {p}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)

add_button=Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

root.mainloop()
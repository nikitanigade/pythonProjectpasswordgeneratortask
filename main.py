import random
from tkinter import messagebox
from tkinter import *

def generate_password():
  try:
    repeat = int(repeat_entry.get())
    length = int(length_entry.get())
  except:
    messagebox.showerror(message="Please key in the required inputs")
    return

  if repeat == 1:
    password = random.sample(character_string,length)
  else:
    password = random.choices(character_string,k=length)
  password=''.join(password)
  password_v = StringVar()
  password="Created password: "+str(password)
  password_v.set(password)
  password_label = Entry(password_gen, bd=0, bg="pink", textvariable=password_v, state="readonly")
  password_label.place(x=40,y=240, height=50, width=320)


character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

password_gen  = Tk()
password_gen.geometry("450x400")
password_gen.title("Random Password Generator")

title_label = Label(password_gen, text="Password Generator", font=('Ubuntu Mono',20,"bold"))
title_label.pack()

length_label = Label(password_gen, text="Enter length of password: ",font=('Ubuntu Mono',12,"bold"))
length_label.place(x=50,y=80)
length_entry = Entry(password_gen, width=5)
length_entry.place(x=260,y=80)

repeat_label = Label(password_gen, text="Repetition? 1: no repetition, 2: otherwise: ",font=('Ubuntu Mono',12,"bold"))
repeat_label.place(x=50,y=140)
repeat_entry = Entry(password_gen, width=5)
repeat_entry.place(x=380,y=140)
password_button = Button(password_gen, text="Generate Password", command=generate_password)
password_button.place(x=150,y=200)
password_gen.mainloop()

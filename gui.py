from tkinter import *
from tkinter import messagebox
#from PIL import Image, ImageTk

root = Tk()
root.title("Movie Renting Service")
root.geometry("1280x720")
#img = Image.open("C:\Users\Viniele\Desktop\faculta\computer science class\Assignment_6_8\images\logo.png")
#photo = ImageTk.Photo(img)

def funct_butt_1():
   messagebox.showinfo("","Do not")

def funct_butt_2():
   messagebox.showinfo("","Push")

def funct_butt_3():
   messagebox.showinfo("","Button 4 , ever !!!")

def funct_butt_4():
   messagebox.showinfo("","U fucking asshole")

top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text="Button 1", fg="red", command= funct_butt_1)
button2 = Button(top_frame, text="Button 2", fg="blue", command= funct_butt_2)
button3 = Button(top_frame, text="Button 3", fg="green", command= funct_butt_3)
button4 = Button(bottom_frame, text="Button 4", fg="purple", command= funct_butt_4)

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)


root.mainloop()
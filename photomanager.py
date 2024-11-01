import cv2 
import customtkinter as tk
from tkinter import messagebox
t=tk.CTk()
t.iconbitmap("imgh.ico")
tk.set_appearance_mode('dark')
f1=tk.CTkEntry(t,font=(t,70),width=450)
def view():
    try:
     f3=str(f1.get())
     imag=cv2.imread(f3)
     height=imag.shape[0]
     width=imag.shape[1]
     cv2.imshow(f"{height}x{width}",imag)
     cv2.waitKey(0)
     f1.delete(0,tk.END)
    except:
        messagebox.askokcancel("Так кажется","ты сделал что-то не так")

def what():
    messagebox.showwarning("01.11.2024 ","by Ninalin")
f=tk.CTkButton(t,text="Просмотреть",fg_color="green",font=(t,70),command=view)
f2=tk.CTkButton(t,text="?",fg_color="white",font=(t,40),bg_color="black",hover_color="white",command=what)
t.title("Фото просмотарщик 1.0")
f.place(x=450,y=350)
f1.place(x=450,y=250)
f2.place(x=0,y=0)
t.mainloop()

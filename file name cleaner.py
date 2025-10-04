#A proggrame to delete a specific text from a folder  
import os
import customtkinter as ctk
from customtkinter import *
from tkinter import *
import re
from tkinter import filedialog



programme = CTk()
ctk.set_appearance_mode("Dark")


def correct_input():
   global input_correct_or_not
   x="done successfully"
   input_correct_or_not = CTkLabel(programme, text=x, height=6, width=200,font=("Cascadia Mono",19))
   input_correct_or_not.place(x=30,y=120)
def fail_input():
   x="Valid input"
   global input_correct_or_not
   input_correct_or_not = CTkLabel(programme, text=x, height=6, width=200,font=("Cascadia Mono",20))
   input_correct_or_not.place(x=30,y=120)
def no_file_input():
   global input_correct_or_not
   x="NO File Found"
   input_correct_or_not = CTkLabel(programme, text=x, height=6, width=200,font=("Cascadia Mono",20))
   input_correct_or_not.place(x=30,y=120)

def path_input():
    global path
    input_path.delete(0, 'end')
    nah = os.getcwd() 
    dr = filedialog.askdirectory(parent=programme, initialdir= nah, title='Please select a directory')
    input_path.insert(0, dr)
    path = input_path.get()
    return None




def delete_fun():
    path = input_path.get()
    textdel = input_text.get()
    located_or_not = os.path.isdir(path)
    if located_or_not == False:
       fail_input()
    else :
        file = os.listdir(path)
        for item in file:
            if not re.search(textdel, item):
             no_file_input()
            else:
             old_path = os.path.join(path,item)
             new_name = item.replace(textdel, "")
             new_path = os.path.join(path,new_name)
             os.rename(old_path, new_path)
             correct_input()







input_path = CTkEntry(programme,width=300,height=30,font=("Cascadia Mono",15))
input_text = CTkEntry(programme,width=300,height=30,font=("Cascadia Mono",15))
ok_buttom = CTkButton(programme,command=lambda:[delete_fun()] ,text="OK",fg_color="#7224e3",hover_color="#352c42",font=("Cascadia Mono",15))
dr_buttom = CTkButton(programme,command=lambda:[path_input()], text="...",fg_color="#7224e3",hover_color="#352c42",font=("Cascadia Mono",15))
input_path.place(x=10,y=20)
input_text.place(x=10,y=60)
ok_buttom.place(x=320,y=60)
dr_buttom.place(x=320,y=20)
programme.title("AZIZ")
programme.geometry("480x200")
programme.mainloop()
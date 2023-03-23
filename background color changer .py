from tkinter import* 
import random

root=Tk()
root.title("random color")
root.geometry("600x400")

color = {"colors" : '"maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"', 
         "Key" : "Colours"}

def random(): 
    random_number = random.randint(0,7)
    color[colors][random_number]
    root.configure(background=color)
    
btn = Button(root, text="change color", command = random)
btn.place(relx = 0.5, rely=0.5, anchor=CENTER) 

root.mainloop()
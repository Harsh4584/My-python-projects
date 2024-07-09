from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest = "Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb1.get()
    d = comb2.get()
    msg = sor.get(1.0,END)
    textget = change(text = msg,src=s,dest=d)
    des.delete(1.0,END)
    des.insert(END,textget)





root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='orange')

lab = Label(root,text="Translator",font=("Time New Roman",40,"bold"))
lab.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab = Label(root,text="Enter Text ",font=("Time New Roman",20,"bold"),bg="orange")
lab.place(x=100,y=100,height=20,width=300)

sor = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor.place(x=10,y=130,height=150,width=480)

list = list(LANGUAGES.values())

comb1 = ttk.Combobox(frame,value=list)
comb1.place(x=10,y=300,height=40,width=150)
comb1.set("english")

button = Button(frame,text="Translate",relief=RAISED,command=data)
button.place(x=170,y=300,height=40,width=150)

comb2 = ttk.Combobox(frame,value=list)
comb2.place(x=330,y=300,height=40,width=150)
comb2.set("english")

lab = Label(root,text="Output",font=("Time New Roman",20,"bold"),bg="orange")
lab.place(x=100,y=360,height=30,width=300)

des = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
des.place(x=10,y=400,height=150,width=480)

root.mainloop()
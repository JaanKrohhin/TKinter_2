from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import scrolledtext
from tkinter.messagebox import *
#import fileinput
from random import choice
from random import randint
def text_():
	text_list=["Button","Click","Money","Meow","Fire","Rawr"]
	a=choice(text_list)
	btn.configure(text=a)
def size():
	a=randint(10,30)
	btn.configure(font=f"Times_New_Roman {a}")
help=["CadetBlue","Crimson","Yellow","Lightgray"]
def op():
	file=open(askopenfilename(),"r")
	f=""
	for line in file:
		f+=line.strip("(){}")
	txt_box.insert(0.0,f)
	file.close
def sv():
	file=asksaveasfile(mode="w",defaultextension=((".txt"),(".docx")),filetypes=(("Notepad",".txt"),("Word",".docx")))
	t=txt_box.get(0.0,END)#fileinput.input(file)
	file.write(t)
	file.close()
def ex():
	if askyesno("Exit","Yeet/No Yeet"):
		showinfo("Exit","It got yeeted")
		scr.destroy()
	else:
		showinfo("Nein")
scr=Tk()
scr.geometry("400x300")
scr.title("TKinter elements")
tabs=ttk.Notebook(scr)
#list_=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eight"]
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text="1")
tabs.add(tab2,text="2")
tabs.add(tab3,text="3")
tabs.add(tab4,text="4")

#for j in range(8):
#	a=eval("tab"+str(j))
#	a=Frame(tabs)
#	tabs.add(a,text=list_[j])

btn=Button(scr,text="Click",font="Times_New_Roman 14")

M=Menu(scr)
scr.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="BG Colours",menu=m1)
m1.add_command(label="Yellow",command=lambda:scr.config(bg="Yellow"))
m1.add_command(label="Purple",command=lambda:scr.config(bg="Purple"))
m1.add_command(label="Blue",command=lambda:scr.config(bg="CadetBlue"))
m2=Menu(M,tearoff=2)
M.add_cascade(label="Button",menu=m2)
m2.add_command(label="Create",command=lambda:btn.pack(fill="both"))
m2.add_command(label="Random name",command=text_)
m2.add_command(label="Random letter size",command=size)
m2.add_command(label="Random Background",command=lambda:btn.config(bg=choice(help)))
m2.add_command(label="Delete",command=lambda:btn.pack_forget())

btn1=Button(tab1,text="Open",font="Times_New_Roman 14",command=op)
btn2=Button(tab1,text="Save",font="Times_New_Roman 14",command=sv)
btn3=Button(tab1,text="Exit",font="Times_New_Roman 14",command=ex)
#txt_box=Text(tab1,width=40,height=5)
txt_box=scrolledtext.ScrolledText(tab1,height=5,width=40)
txt_box.grid(row=0,column=0,columnspan=3)

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
tabs.pack(fill="both")
scr.mainloop()

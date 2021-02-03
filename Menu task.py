from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import scrolledtext
from random import randint,choice
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import sqrt
import os

colours=["BlueViolet","Brown","CadetBlue","Crimson","ForestGreen","Gold","Sienna","Violet","RoyalBlue","LightGray"]
rng=choice(colours)
ask={}
name=""
score=0
help=False
bg_=choice(colours)
def roots(a,b,c):
    D=b**2-4*a*c
    with open("variables.txt","w") as file:
        file.write(f"D={b}**2-4*{a}*{c}\n")
    with open("variables.txt","a") as f:
        if D>0:
            x1=(-1*b+sqrt(D))/(2*a)
            x2=(-1*b-sqrt(D))/(2*a)
            f.write(f"D>0\n\nThere are 2 roots for this equation\n\nx1={x1}\nx2={x2}")
            x=[x1,x2]
        elif D==0:
            x1=(-1*b)/(2*a)
            f.write(f"D=0\n\nThere roots are equal for this equation\nx1=x2={x1}")
            x=[x1]
        else:
            f.write(f"D<0\n\nThere no roots for this equation")
            x=False
        return x
def solve(event):
    friend=True
    try:
        a=float(enta.get())
    except:
        TypeError
        showinfo("Error","'a' is not a valid number")
        friend=False
    try:
        b=float(entb.get())
    except:
        TypeError
        showinfo("Error","'b' is not a valid number")
        friend=False
    try:
        c=float(entc.get())
    except:
        TypeError
        showinfo("Error","'c' is not a valid number")
        friend=False
    if friend==False:
        pass
    else:
        answer=roots(a,b,c)
        if type(answer)==list:
            if btn1.winfo_ismapped()==0:
                btn1.grid(column=0,columnspan=2,row=4)
        elif type(answer)!=list:
            if btn1.winfo_ismapped()==1:
                btn1.grid_forget()
        lines=""
        with open("variables.txt","r") as f:
            for i in f.readlines():
                lines+=i.strip("{}()")
            lbl.configure(text=lines,justify=LEFT)
def graph(event):
    a=float(enta.get())
    b=float(entb.get())
    c=float(entc.get())
    answer=roots(a,b,c)
    if len(answer)==2:
        answer.sort()
        x=np.arange(answer[0],answer[1]+0.01,0.01)
    elif len(answer)==1:
        x=np.array(answer[0])
    y=a*x**2+b*x+c
    plt.xticks(np.arange(-15,16,3))
    plt.yticks(np.arange(-15,16,3))
    plt.grid(axis="both",c="black",lw=2,alpha=0.5)
    plt.grid(True)
    plt.plot(x,y,color=f"{rng}",lw=3)
    plt.show()

def update_stuff(ask):
    with open("q&a.txt","r",encoding="utf-8") as file:
        for line in file:
            friend=[i.strip("\n") for i in line.split(":")]
            ask[friend[0]]=friend[1]
            friend.clear()
    return ask
def questions():
    scr.geometry("1050x550")
    ask_copy=list(ask)
    btn_quiz.pack_forget()
    for o in entries:
        o.delete(0,END)
    for i in labels:
        for j in entries:
            if labels.index(i)==entries.index(j):
                if labels.index(i)==0 and entries.index(j)==0:
                    i.configure(text="What is your name?",font="Times_New_Roman 14")
                else:
                    k=randint(0,len(ask_copy)-1)
                    i.configure(text=ask_copy[k])
                    ask_copy.pop(k)
                i.pack(fill="both")
                j.pack()
    btn_quiz.configure(text="Confirm answers",command=confirm)
    btn_quiz.pack()
def confirm():
    global help
    for i in entries:
        value=i.get()
        if len(value)==0:
            showerror("Error",f"You didnt write anything in question #{entries.index(i)+1}")
            break
        else:
            global score,name
            if entries.index(i)==0:
                name=value
            elif entries.index(i)==5:
                help=True
                if value.lower()==ask[labels[entries.index(i)].cget("text")]:#widgets=dict, text=key, cget just gets the value of the key
                    score+=1
            else:
                if value.lower()==ask[labels[entries.index(i)].cget("text")]:#widgets=dict, text=key, cget just gets the value of the key
                    score+=1
    if help:
        for j in labels,entries:
            for k in j:
                k.pack_forget()
        btn_quiz.pack_forget()
        lbl1.configure(text=f"Your score is {score} out of 5",font=f"Times_New_Roman 40")
        btn_quiz.configure(text="End Quiz",command=sort_)
        lbl1.pack()
        btn_quiz.pack()
def sort_():
    global name
    friend1=[]
    friend2=[]
    friend1.append(name)
    friend2.append(str(score))
    if score>=3:
        with open("passed.txt","r",encoding="utf-8") as f:
            for i in f:
                o=i.split(":")
                friend1.append(o[0])
                friend2.append(o[1].strip("\n"))
        for k in range(0,len(friend1)):
            print(friend1,friend2,friend2[k],int(friend2[k]),sep="\n")
            for j in range(0,len(friend1)):
                if int(friend2[k])>int(friend2[j]):
                    help_=friend2[k]
                    friend2[k]=friend2[j]
                    friend2[j]=help_
                
                    help_=friend1[k]
                    friend1[k]=friend1[j]
                    friend1[j]=help_
        with open("passed.txt","w",encoding="utf-8") as f:
            for i in range(len(friend1)):
                f.write(friend1[i]+":"+friend2[i]+"\n")

    else:
        with open("failed.txt","r",encoding="utf-8") as f:
            friend=[f"{name}:{str(score)}"]
            for line in f:
                friend.append(line.strip("\n"))
        friend.sort()
        with open("failed.txt","w",encoding="utf-8") as f:
            for i in range(len(friend)):
                f.write(friend[i]+"\n")
    lbl1.pack_forget()
    btn_quiz.configure(text="Start Quiz",command=questions)
    btn_quiz.pack(fill="both")
    scr.geometry("400x180")
def passed():
    help_=""
    global txt
    txt.delete(0.0,END)
    with open("passed.txt","r",encoding="utf-8") as f:
        for i in f:
            help_+=i.strip("(){}")
        help_=help_.replace(":"," ")
        txt.insert(0.0,help_)
def failed():
    global txt
    help_=""
    txt.delete(0.0,END)
    with open("failed.txt","r",encoding="utf-8") as f:
        for i in f:
            help_+=i.strip("(){}")
        help_=help_.replace(":"," ")
        txt.insert(0.0,help_)
def addd():
    global txt1_a,txt2_a
    q=txt1_a.get(0.0,END)
    q=q.strip("\n")
    a=txt2_a.get()
    with open("q&a.txt","a",encoding="utf-8") as f:
        f.write(f"{q}:{a}")
    txt1_a.delete(0.0,END)
    txt2_a.delete(0,END)
def admin():
    root=Tk()
    root.title("Admin")
    root.configure(bg=bg_)
    root.geometry("250x300")
    tabs=ttk.Notebook(root)

    tab1=Frame(tabs)
    tabs.add(tab1,text="Lists")
    global txt
    txt=scrolledtext.ScrolledText(tab1,height=15,width=30)
    btn_passed=Button(tab1,text="Passed list",command=passed,width=27,bg=bg_)
    btn_failed=Button(tab1,text="Failed list",command=failed,width=27,bg=bg_)
    btn_passed.pack()
    btn_failed.pack()
    txt.pack()

    global txt1_a,txt2_a
    tab2=Frame(tabs)
    tabs.add(tab2,text="Add Question")
    lbl1_a=Label(tab2,text="Question",width=10)
    txt1_a=scrolledtext.ScrolledText(tab2,height=5,font="Times_New_Roman 14",width=25,bg=bg_)
    txt2_a=Entry(tab2,font="Times_New_Roman 14",bg=bg_)
    lbl2_a=Label(tab2,text="Answer",width=10)
    btn_a=Button(tab2,text="Add",width=10,command=addd)

    lbl1_a.grid(row=0,column=1,columnspan=2)
    txt1_a.grid(row=1,column=0,columnspan=4)
    lbl2_a.grid(row=2,column=1,columnspan=2)
    txt2_a.grid(row=3,column=0,columnspan=4)
    btn_a.grid(row=4,column=1,columnspan=2)
    tabs.pack(fill="both")
    root.mainloop()
def change_to_1(event):
    if lbl2.winfo_ismapped()==0:
        scr.geometry("400x180")
    else:
        scr.geometry("1050x550")
def change_to_2(event):
    scr.geometry("600x240")
#---------------------------------------------------------------------
#First tab+actual menu
ask=update_stuff(ask)
scr=Tk()
scr.configure(bg=bg_)
scr.title("The Super Duper Menu")
scr.geometry("400x180")
tab=ttk.Notebook(scr)
tab1_m=Frame(tab)
tab.add(tab1_m,text="Pokemon Quiz")
tab1_m.bind("<Button-1>",change_to_1)
tab2_m=Frame(tab)
tab.add(tab2_m,text="Square Exuations")
tab2_m.bind("<Button-1>",change_to_2)
lbl1=Label(tab1_m,text="What is your name",font="Times_New_Roman 14",bg=bg_)
lbl2=Label(tab1_m,font="Times_New_Roman 14",bg=bg_)
lbl3=Label(tab1_m,font="Times_New_Roman 14",bg=bg_)
lbl4=Label(tab1_m,font="Times_New_Roman 14",bg=bg_)
lbl5=Label(tab1_m,font="Times_New_Roman 14",bg=bg_)
lbl6=Label(tab1_m,font="Times_New_Roman 14",bg=bg_)
ent1=Entry(tab1_m,font="Times_New_Roman 14",bg=bg_)
ent2=Entry(tab1_m,font="Times_New_Roman 14",bg=bg_)
ent3=Entry(tab1_m,font="Times_New_Roman 14",bg=bg_)
ent4=Entry(tab1_m,font="Times_New_Roman 14",bg=bg_)
ent5=Entry(tab1_m,font="Times_New_Roman 14",bg=bg_)
ent6=Entry(tab1_m,font="Times_New_Roman 14",bg=bg_)
labels=[lbl1,lbl2,lbl3,lbl4,lbl5,lbl6]
entries=[ent1,ent2,ent3,ent4,ent5,ent6]
for com in labels:
    com.bind("<Button-1>",change_to_1)
btn_quiz=Button(tab1_m,text="Start Quiz",font="Times_New_Roman 14",bg=bg_,command=questions)
btn_quiz.pack(fill="both")
m=Menu(scr)
scr.config(menu=m)
m1=Menu(m,tearoff=1)
m.add_cascade(label="Settings",menu=m1)
m1.add_command(label="Admin Menu",command=admin)
#--------------------------------------------------------------------------------------
#Second tab that is about square equations
colours=["BlueViolet","Brown","CadetBlue","Crimson","ForestGreen","Gold","Sienna","Violet","Black","RoyalBlue"]
rng=choice(colours)
enta=Entry(tab2_m,width=15,fg="Orange",font="Ariel 14",bd=5)
entb=Entry(tab2_m,width=15,fg="Orange",font="Ariel 14",bd=5)
entc=Entry(tab2_m,width=15,fg="Orange",font="Ariel 14",bd=5)

btn=Button(tab2_m,width=20,text="Solve",font="Ariel 14",bd=5)
btn1=Button(tab2_m,width=20,text="Graph",font="Ariel 14",bd=5)

lbl=Label(tab2_m,width=34,height=7,bg="LightGray",fg="Orange",bd=5,anchor=NW,text="The solution will be posted here",font="Ariel 14",justify=CENTER)
lbl
lbla=Label(tab2_m,width=5,bg="LightGray",fg="Orange",bd=5,anchor=NW,text="a=",font="Ariel 14",justify=CENTER)
lblb=Label(tab2_m,width=5,bg="LightGray",fg="Orange",bd=5,anchor=NW,text="b=",font="Ariel 14",justify=CENTER)
lblc=Label(tab2_m,width=5,bg="LightGray",fg="Orange",bd=5,anchor=NW,text="c=",font="Ariel 14",justify=CENTER)
btn1.bind("<Button-1>",graph)
btn.bind("<Button-1>",solve)
for meh in lbl,lbla,lblb,lblc:
    meh.bind("<Button-1>",change_to_2)
enta.grid(column=1,row=0)
entb.grid(column=1,row=1)
entc.grid(column=1,row=2)
btn.grid(column=0,columnspan=2,row=3)
lbl.grid(column=2,row=0,rowspan=4)
lbla.grid(column=0,row=0)
lblb.grid(column=0,row=1)
lblc.grid(column=0,row=2)

tab.pack(fill="both")
scr.mainloop()
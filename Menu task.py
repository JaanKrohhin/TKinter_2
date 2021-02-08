from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import scrolledtext
from random import randint,choice
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import sqrt

colours=["BlueViolet","Brown","CadetBlue","Crimson","ForestGreen","Gold","Sienna","Violet","RoyalBlue","LightGray"]
bg_=choice(colours)
score=0
ask={}
name=""
help_=0
var=[]
#Quiz functions------------------------------------------------------
def update_stuff(ask):
    with open("q&a.txt","r",encoding="utf-8-sig") as file:
        for line in file:
            friend=[i.strip("\n") for i in line.split(":")]
            ask[friend[0]]=friend[1]
            friend.clear()
    return ask
def questions():
    global ask_copy,btn_quiz,k,help_,var
    ent1.delete(0,END)

    ask_copy=list(ask)
    k=randint(0,len(ask_copy))
    var.append(ask_copy[k])

    btn_quiz.pack_forget()
    scr.geometry("1050x200")
    if help_==0:
        lbl1.configure(text="What is your name?")
    else:
        lbl1.configure(text=k)
    btn_quiz.configure(text="Confirm answer",command=confirm)
    lbl1.grid(row=0,column=0,columnspan=4)
    ent1.grid(row=1,column=1,columnspan=2)
    btn_quiz.grid(row=2,column=1,columnspan=2)
def confirm():
    global score,help_,ask_copy,var
    print("\n",ask_copy,"\n",var)
    athing=False
    value=ent1.get()
    for i in "pass":
        if len(value)==0:
            showerror("Error","You didn't write an answer")
            break
        else:
            if help_==0:
                name=value
                help_+=1
            elif help_==5:
                athing=True
                if value.lower()==ask[k]:
                    score+=1
            else:
                if value.lower()==ask[k]:
                    score+=1
                ask_copy.pop(ask_copy.index(k))
            ent1.delete(0,END)
            questions()
    if athing:
        ent1.grid_forget()
        lbl1.configure(text=f"Your score is {score}/5 ")
        btn_quiz.configure(text="End Quiz",command=sort_)
def sort_():
    pass
    #global name
    #friend1=[]
    #friend2=[]
    #friend1.append(name)
    #friend2.append(str(score))
    #if score>=3:
    #    with open("passed.txt","r",encoding="utf-8") as f:
    #        for i in f:
    #            o=i.split(":")
    #            friend1.append(o[0])
    #            friend2.append(o[1].strip("\n"))
    #    for k in range(0,len(friend1)):
    #        print(friend1,friend2,friend2[k],int(friend2[k]),sep="\n")
    #        for j in range(0,len(friend1)):
    #            if int(friend2[k])>int(friend2[j]):
    #                help_=friend2[k]
    #                friend2[k]=friend2[j]
    #                friend2[j]=help_
                
    #                help_=friend1[k]
    #                friend1[k]=friend1[j]
    #                friend1[j]=help_
    #    with open("passed.txt","w",encoding="utf-8") as f:
    #        for i in range(len(friend1)):
    #            f.write(friend1[i]+":"+friend2[i]+"\n")

    #else:
    #    with open("failed.txt","r",encoding="utf-8") as f:
    #        friend=[f"{name}:{str(score)}"]
    #        for line in f:
    #            friend.append(line.strip("\n"))
    #    friend.sort()
    #    with open("failed.txt","w",encoding="utf-8") as f:
    #        for i in range(len(friend)):
    #            f.write(friend[i]+"\n")
    #lbl1.pack_forget()
    #btn_quiz.grid_forget()
    #btn_quiz.configure(text="Start Quiz",command=questions)
    #btn_quiz.pack(fill="both")
    #scr.geometry("400x180")

##def addd():
#    global txt1_a,txt2_a,ask
#    q=txt1_a.get(0.0,END)
#    q=q.strip("\n")
#    a=txt2_a.get()
#    with open("q&a.txt","a",encoding="utf-8") as f:
#        f.write(f"{q}:{a}\n")
#    txt1_a.delete(0.0,END)
#    txt2_a.delete(0,END)
#    ask=update_stuff(ask)
#Miscellaneous
#---------------------------------------------------------------------
#First tab+actual menu
ask=update_stuff(ask)
scr=Tk()
scr.configure(bg=bg_)
scr.title("The Super Duper Menu")
scr.geometry("400x180")
scr.iconbitmap("Logo.ico")
tab=ttk.Notebook(scr)
tab1_m=Frame(tab)
tab.add(tab1_m,text="Pokemon Quiz")

lbl1=Label(tab1_m,text="What is your name",font="Times_New_Roman 14",bg=bg_)
ent1=Entry(tab1_m,font="Times_New_Roman 14",bg=bg_)
btn_quiz=Button(tab1_m,text="Start Quiz",font="Times_New_Roman 14",bg=bg_,command=questions)
btn_quiz.pack(fill="both")


tab.pack(fill="both")
scr.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import scrolledtext
from random import randint,choice
ask={}
name=""
score=0
help=False
colours=["cadetblue","crimson","orange","lightgray","forestgreen"]
bg_=choice(colours)
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
                if i.get().lower()==ask[labels[entries.index(i)].cget("text")]:#widgets=dict, text=key, cget just gets the value of the key
                    score+=1
            else:
                if i.get().lower()==ask[labels[entries.index(i)].cget("text")]:#widgets=dict, text=key, cget just gets the value of the key
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
    print(name)
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
    scr.geometry("400x400")
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
    help_=""
    txt.delete(0.0,END)
    with open("failed.txt","r",encoding="utf-8") as f:
        for i in f:
            help_+=i.strip("(){}")
        help_=help_.replace(":"," ")
        txt.insert(0.0,help_)
def admin():
    root=Tk()
    root.title("Admin")
    root.geometry("200x300")
    tabs=ttk.Notebook(scr)

    tab1=Frame(tabs)
    tabs.add(tab1,text="Lists")
    btn_passed=Button(tab1,text="Passed list",command=passed,width=27)
    btn_failed=Button(tab1,text="Failed list",command=failed,width=27)
    tab1.pack(fill="both")
    btn_passed.pack()
    btn_failed.pack()
    txt.pack()

    tab2=Frame(tabs)
    tabs.add(tab2,text="Add Question")
    ent1_a=Entry(tab2,width=27)
    entry2_a=Entry(tab2,width=27)
    ent1_a.grid(row=0,column=0)


    root.mainloop()
ask=update_stuff(ask)
scr=Tk()
scr.configure(bg=bg_)
scr.title("Quiz")
scr.geometry("450x350")
tabs=ttk.Notebook(scr)
lbl1=Label(scr,text="What is your name",font="Times_New_Roman 14",bg=bg_)
lbl2=Label(scr,font="Times_New_Roman 14",bg=bg_)
lbl3=Label(scr,font="Times_New_Roman 14",bg=bg_)
lbl4=Label(scr,font="Times_New_Roman 14",bg=bg_)
lbl5=Label(scr,font="Times_New_Roman 14",bg=bg_)
lbl6=Label(scr,font="Times_New_Roman 14",bg=bg_)
ent1=Entry(scr,font="Times_New_Roman 14",bg=bg_)
ent2=Entry(scr,font="Times_New_Roman 14",bg=bg_)
ent3=Entry(scr,font="Times_New_Roman 14",bg=bg_)
ent4=Entry(scr,font="Times_New_Roman 14",bg=bg_)
ent5=Entry(scr,font="Times_New_Roman 14",bg=bg_)
ent6=Entry(scr,font="Times_New_Roman 14",bg=bg_)
labels=[lbl1,lbl2,lbl3,lbl4,lbl5,lbl6]
entries=[ent1,ent2,ent3,ent4,ent5,ent6]

btn_quiz=Button(scr,text="Start Quiz",font="Times_New_Roman 14",bg=bg_,command=questions)
btn_quiz.pack(fill="both")
m=Menu(scr)
scr.config(menu=m)
m1=Menu(m,tearoff=1)
m.add_cascade(label="File",menu=m1)
m1.add_command(label="Admin Menu",command=admin)

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import webbrowser
from random import choice
ask={}
def update_stuff():
    with open("q&a.txt","r",encoding="utf-8") as file:
        for line in file:
            friend=[i.strip("\n") for i in line.split(":")]
            ask[friend[0]]=friend[1]
            friend.clear()
def questions():
    btn_quiz.pack_forget()
    for i in labels:
        for j in entries:
            if labels.index(i)==entries.index(j):
                if labels.index(i)==0 and entries.index(j)==0:
                    i.configure(text="What is your name?")
                k=choice(list(ask_copy))
                i.configure(text=k)
                i.pack(fill="both")
                j.pack()
    btn_quiz.configure()
def sort_correct(name,score):
    friend1=[]
    friend2=[]
    friend1.append(name)
    friend2.append(str(score))
    with open("passed.txt","r",encoding="utf-8") as f:
        for line in f:
            o=line.split(":")
            friend1.append(o[0])
            friend2.append(o[1].strip("\n"))
    for k in range(0,len(friend1)):
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
def sort_failed(name,score):
    with open("failed.txt","r",encoding="utf-8") as f:
        help_=[f"{name}:{str(score)}"]
        for line in f:
            help_.append(line.strip("\n"))
    help_.sort()
    with open("failed.txt","w",encoding="utf-8") as f:
        for i in range(len(help_)):
            f.write(help_[i]+"\n")

ask=update_stuff()
scr=Tk()
scr.title("Quiz")
scr.geometry("400x300")
scr.title("Super Duper Menu Of Awesomeness")

tabs=ttk.Notebook(scr)

ask={}
lbl1=Label(scr,font="Times_New_Roman 14")
lbl2=Label(scr,font="Times_New_Roman 14")
lbl3=Label(scr,font="Times_New_Roman 14")
lbl4=Label(scr,font="Times_New_Roman 14")
lbl5=Label(scr,font="Times_New_Roman 14")
lbl6=Label(scr,font="Times_New_Roman 14")
ent1=Entry(scr,font="Times_New_Roman 14")
ent2=Entry(scr,font="Times_New_Roman 14")
ent3=Entry(šcr,font="Times_New_Roman 14")
ent4=Entry(scr,font="Times_New_Roman 14")
ent5=Entry(scr,font="Times_New_Roman 14")
ent6=Entry(scr,font="Times_New_Roman 14")
labels=[lbl1,lbl2,lbl3,lbl4,lbl5,lbl6]
entries=[ent1,ent2,ent3,ent4,ent5,ent6]

btn_quiz=Button(scr,text="Start Quiz",font="Times_New_Roman 14",command=questions)
btn_quiz.pack(fill="both")

scr.mainloop()



#name=input("\nWhat is your name ,friendo?\n=>")
#c=0
#score=0
#print(f"{name}, that's a lovely name!")
#print(f"\nLet us start our quiz {name}!")
#c,ask_copy=question(ask_copy,name)
#score
#print(f"\nYour score is {score}/5")
#if score>=3:
#    print(f"You passed! Congratulations {name}!")
#    sort_correct(name,score)
#else:
#    print(f"Sorry to say it {name}, but you have failed the quiz. Better luck next time!")
#    sort_failed(name,score)
#M=Menu(scr)
#scr.config(menu=M)
#m1=Menu(M,tearoff=1)
#M.add_cascade(label="BG Colours",menu=m1)
#m1.add_command(label="Yellow",command=lambda:scr.config(bg="Yellow"))
#m1.add_command(label="Purple",command=lambda:scr.config(bg="Purple"))
#m1.add_command(label="Blue",command=lambda:scr.config(bg="CadetBlue"))
#m2=Menu(M,tearoff=2)
#M.add_cascade(label="Button")
#m2.add_command(label="Create")
#m2.add_command(label="Random name")
#m2.add_command(label="Random letter size")
#m2.add_command(label="Random Background")
#m2.add_command(label="Delete")
#txt_box=Text(tab1,height=5,width=40)
#txt_box.grid(row=0,column=0,columnspan=3)

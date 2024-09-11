from tkinter import *
from tkinter import messagebox
import os
root=Tk()

root.title("Zero-Cross game")
root.geometry("250x300")

messagebox.showinfo("showinfo", "Welcome,\nThis is the game of Zero and Cross")
messagebox.showinfo("showinfo", "There is the only two team Team A and Team B\nTeam A is Zero and Team B is One")
A=""
B=""
c=1

t=""
def fun(x):
    global A,B,a,c,t
    if x==0:
        B['bg']="red"
    if x==1 and "1" not in t:
        b1['fg']='white'
        if c==1:
            b1['bg']='blue'
            c=0
            
            b1['text']="X"
            A=A+"1"
        else:
            b1['bg']='green'
            c=1
            b1['text']="O"
            B=B+"1"
        t=t+"1"
    elif x==2 and "2" not in t:
        b2['fg']='white'
        t=t+"2"
        if c==1:
            b2['bg']='blue'
            c=0
            b2['text']="X"
            A=A+"2"
        else:
            b2['bg']='green'
            c=1
            b2['text']="O"
            B=B+"2"
        
    elif x==3 and "3" not in t:
       b3['fg']='white'
       t=t+"3"
       if c==1:
            b3['bg']='blue'
            c=0
            b3['text']="X"
            A=A+"3"
       else:
            b3['bg']='green'
            c=1
            b3['text']="O"
            B=B+"3"
        
    elif x==4 and "4" not in t:
       b4['fg']='white'
       t=t+"4"
       if c==1:
            b4['bg']='blue'
            c=0
            b4['text']="X"
            A=A+"4"
       else:
            b4['bg']='green'
            c=1
            b4['text']="O"
            B=B+"4"
        
    elif x==5 and "5" not in t:

       b5['fg']='white'
       if c==1:
            b5['bg']='blue'
            c=0
            b5['text']="X"
            A=A+"5"
       else:
            b5['bg']='green'
            c=1
            b5['text']="O"
            B=B+"5"

       t=t+"5"
    elif x==6 and "6" not in t:

       b6['fg']='white'
       if c==1:
            b6['bg']='blue'
            c=0
            b6['text']="X"
            A=A+"6"
       else:
            b6['bg']='green'
            c=1
            b6['text']="O"
            B=B+"6"
       t=t+"6"
    elif x==7 and "7" not in t:
       b7['fg']='white'
       if c==1:
            b7['bg']='blue'
            c=0
            b7['text']="X"
            A=A+"7"
       else:
            b7['bg']='green'
            c=1
            b7['text']="O"
            B=B+"7"
       t=t+"7"
    elif x==8 and "8" not in t:

       b8['fg']='white'
       if c==1:
            b8['bg']='blue'
            c=0
            b8['text']="X"
            A=A+"8"
       else:
            b8['bg']='green'
            c=1
            b8['text']="O"
            B=B+"8"
       t=t+"8"
    elif x==9 and "9" not in t:
       b9['fg']='white'
       if c==1:
            b9['bg']='blue'
            c=0
            b9['text']="X"
            A=A+"9"
       else:
            b9['bg']='green'
            c=1
            b9['text']="O"
            B=B+"9"
       t=t+"9"
    
    if ("1" in A and "2" in A and "3" in A) or ("4" in A and "5" in A and "6" in A) or ("7" in A and "8" in A and "9" in A) or ("1" in A and "5" in A and "9" in A) or ("3" in A and "5" in A and "7" in A) or ("1" in A and "4" in A and "7" in A) or ("2" in A and "5" in A and "8" in A) or("3" in A and "6" in A and "9" in A):
        messagebox.showinfo("Result", "Congrats\nTeam A is win")
        
    if ("1" in B and "2" in B and "3" in B) or ("4" in B and "5" in B and "6" in B) or ("7" in B and "8" in B and "9" in B) or ("1" in B and "5" in B and "9" in B) or ("3" in B and "5" in B and "7" in B) or ("1" in B and "4" in B and "7" in B) or ("2" in B and "5" in B and "8" in B) or("3" in B and "6" in B and "9" in B):\
       messagebox.showinfo("Result", "Congrats\nTeam B is win")
     

b1=Button(root,text="---",height="5",width="10",bg="red",command=lambda:fun(1))
b1.place(x=0,y=0)

b2=Button(root,text="---",height="5",width="10",bg="red",command=lambda:fun(2))
b2.place(x=81,y=0)

b3=Button(root,text="---",height="5",width="10",bg="red",command=lambda:fun(3))
b3.place(x=162,y=0)

b4=Button(root,text="---",height="5",width="10",bg="red",command=lambda:fun(4))
b4.place(x=0,y=87)

b5=Button(root,text="---",height="5",width="10",bg="red",command=lambda:fun(5))
b5.place(x=81,y=87)

b6=Button(root,text="---",height="5",width="10",bg="red",command=lambda:fun(6))
b6.place(x=162,y=87)

b7=Button(root,text="---",height="5",width="10",bg="red",command=lambda:fun(7))
b7.place(x=0,y=174)

b8=Button(root,text="---",height="5",width="10",bg="red",command=lambda:fun(8))
b8.place(x=81,y=174)

b9=Button(root,text="---",height="5",width="10",bg="red",command=lambda:fun(9))
b9.place(x=162,y=174)

l=Label(root,text="Turn is",font=("Arial",10,"bold"))
l.place(x=0,y=(174+87))

l1=Label(root,text="Team A",font=("Arial",10,"bold"))
l1.place(x=0,y=(174+87+18))


root.mainloop()







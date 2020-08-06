import tkinter.messagebox
from tkinter import *

root=Tk()
root.geometry("1350x750")
root.title("tictactoe")
root.configure(bg="cadet blue")

Topframe=Frame(root,bg="cadet blue",pady=2,width=1350,height=100,relief=RIDGE)
Topframe.grid(row=0,column=0)

tltlabel=Label(Topframe,text=" ADVANCED TICTACTOE GAME ",font=('arial',50,'bold'),bd=21,bg="cadet blue",fg="cornsilk",justify=CENTER)
tltlabel.grid(row=0,column=0)


mainframe=Frame(root,bg="powder blue",pady=2,width=1350,height=600,relief=RIDGE)
mainframe.grid(row=1,column=0)

leftframe=Frame(mainframe,bg="cadet blue",bd=10,width=750,height=500,padx=10,pady=2,relief=RIDGE)
leftframe.pack(side=LEFT)
rightframe=Frame(mainframe,bg="cadet blue",bd=10,width=600,height=500,padx=10,pady=2,relief=RIDGE)
rightframe.pack(side=RIGHT)

rightframe1=Frame(rightframe,bg="cadet blue",bd=10,width=600,height=200,padx=10,pady=2,relief=RIDGE)
rightframe1.grid(row=0,column=0)
rightframe2=Frame(rightframe,bg="cadet blue",bd=10,width=600,height=200,padx=10,pady=2,relief=RIDGE)
rightframe2.grid(row=1,column=0)

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)


buttons= StringVar()
click=True

def checker(buttons):
    global click
    if buttons["text"]=="" and click== True:
       buttons["text"]="X"
       click=False
       scorekeeper()
    elif buttons["text"]=="" and click==False:
       buttons["text"]="O"
       click=True
       scorekeeper()

def scorekeeper():
    if button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X":
       button1.configure(bg="yellow")
       button2.configure(bg="yellow")
       button3.configure(bg="yellow")
       n= float(PlayerX.get())
       score=(n+1)
       PlayerX.set(score)
       tkinter.messagebox.showinfo("Winner X","yoy have just won a game")
    if button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X":
       button4.configure(bg="yellow")
       button5.configure(bg="yellow")
       button6.configure(bg="yellow")
       n= float(PlayerX.get())
       score=(n+1)
       PlayerX.set(score)
       tkinter.messagebox.showinfo("Winner X","yoy have just won a game")
    if button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X":
       button7.configure(bg="yellow")
       button8.configure(bg="yellow")
       button9.configure(bg="yellow")
       n= float(PlayerX.get())
       score=(n+1)
       PlayerX.set(score)
       tkinter.messagebox.showinfo("Winner X","yoy have just won a game")
    if button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X":
       button1.configure(bg="yellow")
       button4.configure(bg="yellow")
       button7.configure(bg="yellow")
       n= float(PlayerX.get())
       score=(n+1)
       PlayerX.set(score)
       tkinter.messagebox.showinfo("Winner X","yoy have just won a game")
    if button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X":
       button2.configure(bg="yellow")
       button5.configure(bg="yellow")
       button8.configure(bg="yellow")
       n= float(PlayerX.get())
       score=(n+1)
       PlayerX.set(score)
       tkinter.messagebox.showinfo("Winner X","yoy have just won a game")
    if button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X":
       button3.configure(bg="yellow")
       button6.configure(bg="yellow")
       button9.configure(bg="yellow")
       n= float(PlayerX.get())
       score=(n+1)
       PlayerX.set(score)
       tkinter.messagebox.showinfo("Winner X","yoy have just won a game")
    if button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X":
       button1.configure(bg="yellow")
       button5.configure(bg="yellow")
       button9.configure(bg="yellow")
       n= float(PlayerX.get())
       score=(n+1)
       PlayerX.set(score)
       tkinter.messagebox.showinfo("Winner X","yoy have just won a game")
    if button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X":
       button3.configure(bg="yellow")
       button5.configure(bg="yellow")
       button7.configure(bg="yellow")
       n= float(PlayerX.get())
       score=(n+1)
       PlayerX.set(score)
       tkinter.messagebox.showinfo("Winner X","yoy have just won a game")

    
    if button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O":
       button1.configure(bg="red")
       button2.configure(bg="red")
       button3.configure(bg="red")
       n= float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       tkinter.messagebox.showinfo("Winner O","yoy have just won a game")
    if button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O":
       button4.configure(bg="red")
       button5.configure(bg="red")
       button6.configure(bg="red")
       n= float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       tkinter.messagebox.showinfo("Winner O","yoy have just won a game")
    if button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O":
       button8.configure(bg="red")
       button9.configure(bg="red")
       button7.configure(bg="red")
       n= float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       tkinter.messagebox.showinfo("Winner O","yoy have just won a game")
    if button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O":
       button1.configure(bg="red")
       button4.configure(bg="red")
       button7.configure(bg="red")
       n= float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       tkinter.messagebox.showinfo("Winner O","yoy have just won a game")
    if button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O":
       button2.configure(bg="red")
       button5.configure(bg="red")
       button8.configure(bg="red")
       n= float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       tkinter.messagebox.showinfo("Winner O","yoy have just won a game")
    if button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O":
       button6.configure(bg="red")
       button9.configure(bg="red")
       button3.configure(bg="red")
       n= float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       tkinter.messagebox.showinfo("Winner O","yoy have just won a game")
    if button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O":
       button1.configure(bg="red")
       button5.configure(bg="red")
       button9.configure(bg="red")
       n= float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       tkinter.messagebox.showinfo("Winner O","yoy have just won a game")
    if button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O":
       button7.configure(bg="red")
       button5.configure(bg="red")
       button3.configure(bg="red")
       n= float(PlayerO.get())
       score=(n+1)
       PlayerO.set(score)
       tkinter.messagebox.showinfo("Winner O","yoy have just won a game")
    

def reset():
    button1['text']=""
    button2['text']=""
    button3['text']=""
    button4['text']=""
    button5['text']=""
    button6['text']=""
    button7['text']=""
    button8['text']=""
    button9['text']=""


    button1.configure(bg="gainsboro")
    button2.configure(bg="gainsboro")
    button3.configure(bg="gainsboro")
    button4.configure(bg="gainsboro")
    button5.configure(bg="gainsboro")
    button6.configure(bg="gainsboro")
    button7.configure(bg="gainsboro")
    button8.configure(bg="gainsboro")
    button9.configure(bg="gainsboro")


def newgame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)

lblPlayerX=Label(rightframe1,text= " Player X:",bg="cadet blue",font='Times 45 bold',padx=2,pady=2)
lblPlayerX.grid(row=0,column=0,sticky=W)
txtPlayerX=Entry(rightframe1,font='Times 45 bold',textvariable=PlayerX,width=14,justify=LEFT).grid(row=0,column=1)


lblPlayerO=Label(rightframe1,text= " Player O:",bg="cadet blue",font='Times 45 bold',padx=2,pady=2)
lblPlayerO.grid(row=1,column=0,sticky=W)
txtPlayerO=Entry(rightframe1,font='Times 45 bold',textvariable=PlayerO,width=14,justify=LEFT).grid(row=1,column=1)





button1=Button(leftframe,text="",height=3,width=8,font='Times 26 bold',bg="gainsboro",relief=RIDGE,command=lambda: checker(button1))
button1.grid(row=1,column=0,sticky=N+E+W+S)

button2=Button(leftframe,text="",height=3,width=8,font='Times 26 bold',bg="gainsboro",relief=RIDGE,command=lambda: checker(button2))
button2.grid(row=1,column=1,sticky=N+E+W+S)

button3=Button(leftframe,text="",height=3,width=8,font='Times 26 bold',bg="gainsboro",relief=RIDGE,command=lambda: checker(button3))
button3.grid(row=1,column=2,sticky=N+E+W+S)

button4=Button(leftframe,text="",height=3,width=8,font='Times 26 bold',bg="gainsboro",relief=RIDGE,command=lambda: checker(button4))
button4.grid(row=2,column=0,sticky=N+E+W+S)

button5=Button(leftframe,text="",height=3,width=8,font='Times 26 bold',bg="gainsboro",relief=RIDGE,command=lambda: checker(button5))
button5.grid(row=2,column=1,sticky=N+E+W+S)

button6=Button(leftframe,text="",height=3,width=8,font='Times 26 bold',bg="gainsboro",relief=RIDGE,command=lambda: checker(button6))
button6.grid(row=2,column=2,sticky=N+E+W+S)

button7=Button(leftframe,text="",height=3,width=8,font='Times 26 bold',bg="gainsboro",relief=RIDGE,command=lambda: checker(button7))
button7.grid(row=3,column=0,sticky=N+E+W+S)


button8=Button(leftframe,text="",height=3,width=8,font='Times 26 bold',bg="gainsboro",relief=RIDGE,command=lambda: checker(button8))
button8.grid(row=3,column=1,sticky=N+E+W+S)

button9=Button(leftframe,text="",height=3,width=8,font='Times 26 bold',bg="gainsboro",relief=RIDGE,command=lambda: checker(button9))
button9.grid(row=3,column=2,sticky=N+E+W+S)



button_new=Button(rightframe2,text=" NEW GAME ",font='Times 26 bold',height=3,width=25,bg="gainsboro",relief=RIDGE,command=newgame)
button_new.grid(row=0,column=0)

button_reset=Button(rightframe2,text=" RESET ",font='Times 26 bold',height=3,width=25,bg="gainsboro",relief=RIDGE,command=reset)
button_reset.grid(row=1,column=0)


root.mainloop()
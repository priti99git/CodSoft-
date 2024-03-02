from tkinter import *

expression=""

def press(num):
    global expression

    expression = expression +str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)    
        expression=""
    except:
        equation.set("error") 
        expression=""

def clear():
    global expression
    expression=""
    equation.set("")


if __name__=="__main__":
    gui=Tk()
    gui.configure(background="navyblue")
    gui.title("Simple Calculator")
   
    gui.geometry("311x200")
    equation=StringVar()
    expression_field=Entry(gui,textvariable=equation,borderwidth=3)
    expression_field.grid(columnspan=6,ipadx=100,pady=5,padx=4)

    button1=Button(gui,text='1',fg='black',bg='light blue',command=lambda: press(1),height=1,width=8)
    button1.grid(row=2,column=0,pady=2)

    button1=Button(gui,text='2',fg='black',bg='light blue',command=lambda: press(2),height=1,width=8)
    button1.grid(row=2,column=1,pady=2)

    button1=Button(gui,text='3',fg='black',bg='light blue',command=lambda: press(3),height=1,width=8)
    button1.grid(row=2,column=2,pady=2)

    button1=Button(gui,text='4',fg='black',bg='light blue',command=lambda: press(4),height=1,width=8)
    button1.grid(row=3,column=0,pady=2)

    button1=Button(gui,text='5',fg='black',bg='light blue',command=lambda: press(5),height=1,width=8)
    button1.grid(row=3,column=1,pady=2)

    button1=Button(gui,text='6',fg='black',bg='light blue',command=lambda: press(6),height=1,width=8)
    button1.grid(row=3,column=2,pady=2)

    button1=Button(gui,text='7',fg='black',bg='light blue',command=lambda: press(7),height=1,width=8)
    button1.grid(row=4,column=0,pady=2)

    button1=Button(gui,text='8',fg='black',bg='light blue',command=lambda: press(8),height=1,width=8)
    button1.grid(row=4,column=1,pady=2)

    button1=Button(gui,text='9',fg='black',bg='light blue',command=lambda: press(9),height=1,width=8)
    button1.grid(row=4,column=2,pady=2)

    button1=Button(gui,text='0',fg='black',bg='light blue',command=lambda: press(0),height=1,width=8)
    button1.grid(row=5,column=0,pady=2)

    plus=Button(gui,text='+',fg='black',bg='light blue',command=lambda: press("+"),height=1,width=8)
    plus.grid(row=2,column=3,pady=2)

    minus=Button(gui,text='-',fg='black',bg='light blue',command=lambda: press("-"),height=1,width=8)
    minus.grid(row=3,column=3,pady=2)

    multiply=Button(gui,text='*',fg='black',bg='light blue',command=lambda: press("*"),height=1,width=8)
    multiply.grid(row=4,column=3,pady=2)

    divide=Button(gui,text='/',fg='black',bg='light blue',command=lambda: press("/"),height=1,width=8)
    divide.grid(row=5,column=3,pady=2)
       
    decimal=Button(gui,text='.',fg='black',bg='light blue',command=lambda: press("."),height=1,width=8)
    decimal.grid(row=5,column=1,pady=2)

    equal=Button(gui,text='=',fg='black',bg='white',command=equalpress,height=1,width=8)
    equal.grid(row=6,column=0,pady=2)

    clear=Button(gui,text='C',fg='black',bg='yellow',command=clear,height=1,width=8)
    clear.grid(row=6,column=1,pady=2)
    
    decimal=Button(gui,text='%',fg='black',bg='light blue',command=lambda: press("%"),height=1,width=8)
    decimal.grid(row=5,column=2,pady=2)


gui.mainloop()
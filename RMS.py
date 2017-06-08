from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title('Restaurant Management System')

text_Input = StringVar()
operator=""

Tops =Frame(root, width=1600,height=100,bg='powder blue',relief=SUNKEN)
Tops.pack(side=TOP)

f1 =Frame(root, width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 =Frame(root, width=300,height=700,bg='powder blue',relief=SUNKEN)
f2.pack(side=RIGHT)
#==========TIME====================
localtime = time.asctime(time.localtime(time.time()))
#=================SYSTEM INFO=================
labelinfo = Label(Tops,font=('Arial',50,'bold'),text='Restaurant Management System',fg='Steel Blue',bd=10,anchor='w')
labelinfo.grid(row=0,column=0)
labelinfo = Label(Tops,font=('Arial',20,'bold'),text=localtime,fg='Steel Blue',bd=10,anchor='w')
labelinfo.grid(row=1,column=0)


#==================CALCULATOR=================

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnresult():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = sumup

def Ref():
    x = random.randint(29087, 679890)
    randomRef = str(x)
    rand.set(randomRef)

    CoF = 0 if fries.get()=="" else float(fries.get())
    CoB =  0 if burger.get()=="" else float(burger.get())
    Cocm = 0 if cheesem.get()=="" else float(cheesem.get())
    Cocp = 0 if chillyp.get()=="" else float(chillyp.get())
    Cop = 0 if pizza.get()=="" else float(pizza.get())
    Copa = 0 if pasta.get()=="" else float(pasta.get())
    Coit = 0 if icedtea.get()=="" else float(icedtea.get())
    Cocc = 0 if coldcoffee.get()=="" else float(coldcoffee.get())

    costof_fries = CoF * 90.0
    costof_burger = CoB * 60.0
    costof_cheesemeal = Cocm * 80.0
    costof_chillypotato = Cocp * 120.0
    costof_pizza = Cop * 220.0
    costof_pasta= Copa * 80.0
    costof_icedtea = Coit * 95.0
    costof_coldcoffee = Cocc * 150.0

    Costof_meal = 'Rs',str('%.2f' %(costof_fries + costof_burger + costof_cheesemeal + costof_chillypotato + costof_pizza+ costof_pasta + costof_icedtea + costof_coldcoffee))

    pay_tax = ((costof_fries + costof_burger + costof_cheesemeal + costof_chillypotato + costof_pizza + costof_pasta + costof_icedtea + costof_coldcoffee)*0.3)

    Total_cost = ((costof_fries + costof_burger + costof_cheesemeal + costof_chillypotato + costof_pizza  + costof_pasta + costof_icedtea + costof_coldcoffee))


    Ser_charge = ((costof_fries + costof_burger + costof_cheesemeal + costof_chillypotato + costof_pizza   + costof_pasta + costof_icedtea + costof_coldcoffee)/99)

    Service = 'Rs', str('%.2f'% Ser_charge)

    OverallCost  = 'Rs', str('%.2f' % (pay_tax + Total_cost + Ser_charge))

    Paidtax = 'Rs' , str ('%.2f'% pay_tax)

    costofmeal.set(Costof_meal)
    servicec.set(Service)
    statetax.set(Paidtax)
    subtotal.set(Costof_meal)
    totalcost.set(OverallCost)




def qExit():
    root.destroy()

def Reset():
    rand.set("")
    fries.set("")
    burger.set("")
    cheesem.set("")
    chillyp.set("")
    pizza.set("")
    pasta.set("")
    icedtea.set("")
    costofmeal.set("")
    coldcoffee.set("")
    servicec.set("")
    statetax.set("")
    subtotal.set("")
    totalcost.set("")

textdisplay = Entry(f2,font=('Arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg='powder blue',justify='right')
textdisplay.grid(columnspan=4)

btn7 = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='7',bg='powder blue',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8 = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='8',bg='powder blue',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9 = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='9',bg='powder blue',command=lambda:btnClick(9)).grid(row=2,column=2)
btn4 = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='4',bg='powder blue',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5 = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='5',bg='powder blue',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6 = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='6',bg='powder blue',command=lambda:btnClick(6)).grid(row=3,column=2)
btn1 = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='1',bg='powder blue',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2 = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='2',bg='powder blue',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3 = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='3',bg='powder blue',command=lambda:btnClick(3)).grid(row=4,column=2)
addition = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='+',bg='powder blue',command=lambda:btnClick('+')).grid(row=2,column=3)
minus = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='-',bg='powder blue',command=lambda:btnClick('-')).grid(row=3,column=3)
multiply = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='*',bg='powder blue',command=lambda:btnClick('*')).grid(row=4,column=3)
divide = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='/',bg='powder blue',command=lambda:btnClick('/')).grid(row=5,column=3)
btn0 = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='0',bg='powder blue',command=lambda:btnClick(0)).grid(row=5,column=1)
result = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='=',bg='powder blue',command=lambda:btnresult()).grid(row=5,column=2)
reset = Button(f2,fg='black',font=('Arial',20,'bold'),padx=16,pady=16,bd=8,text='C',bg='powder blue',command=lambda:btnClearDisplay()).grid(row=5,column=0)


#==================other entries=======================
rand = StringVar()
fries = StringVar()
burger = StringVar()
cheesem = StringVar()
chillyp= StringVar()
pizza= StringVar()
pasta  = StringVar()

reference = Label(f1,font=('Arial',16,'bold'),text='Reference:',fg='Steel Blue',bd=16,anchor='w')
reference.grid(row=0,column=0)
textref = Entry(f1,font=('Arial',16,'bold'),textvariable=rand,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textref.grid(row=0,column=1)

largefries = Label(f1,font=('Arial',16,'bold'),text='Large Fries:',fg='Steel Blue',bd=16,anchor='w')
largefries.grid(row=1,column=0)
textlf = Entry(f1,font=('Arial',16,'bold'),textvariable=fries,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textlf.grid(row=1,column=1)

Burger = Label(f1,font=('Arial',16,'bold'),text='Burger:',fg='Steel Blue',bd=16,anchor='w')
Burger.grid(row=2,column=0)
textbr = Entry(f1,font=('Arial',16,'bold'),textvariable=burger,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textbr.grid(row=2,column=1)

Pizza = Label(f1,font=('Arial',16,'bold'),text='Pizza:',fg='Steel Blue',bd=16,anchor='w')
Pizza.grid(row=3,column=0)
textpz = Entry(f1,font=('Arial',16,'bold'),textvariable=pizza,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textpz.grid(row=3,column=1)

Cheese_meal = Label(f1,font=('Arial',16,'bold'),text='Cheese meal:',fg='Steel Blue',bd=16,anchor='w')
Cheese_meal.grid(row=4,column=0)
textcm = Entry(f1,font=('Arial',16,'bold'),textvariable=cheesem,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textcm.grid(row=4,column=1)

Chilly_potato = Label(f1,font=('Arial',16,'bold'),text='Chilly Potato:',fg='Steel Blue',bd=16,anchor='w')
Chilly_potato.grid(row=5,column=0)
textcp = Entry(f1,font=('Arial',16,'bold'),textvariable=chillyp,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textcp.grid(row=5,column=1)

Pasta = Label(f1,font=('Arial',16,'bold'),text='Pasta:',fg='Steel Blue',bd=16,anchor='w')
Pasta.grid(row=6,column=0)
textp = Entry(f1,font=('Arial',16,'bold'),textvariable=pasta,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textp.grid(row=6,column=1)

#===============================Restaurantinfo2==================

icedtea = StringVar()
costofmeal = StringVar()
coldcoffee = StringVar()
servicec = StringVar()
statetax= StringVar()
subtotal = StringVar()
totalcost= StringVar()

Iced_tea = Label(f1,font=('Arial',16,'bold'),text='Iced Tea:',fg='Steel Blue',bd=16,anchor='w')
Iced_tea.grid(row=0,column=2)
textit = Entry(f1,font=('Arial',16,'bold'),textvariable=icedtea,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textit.grid(row=0,column=3)

Cost_of_meal = Label(f1,font=('Arial',16,'bold'),text='Cost of Meal:',fg='Steel Blue',bd=16,anchor='w')
Cost_of_meal.grid(row=2,column=2)
textcom = Entry(f1,font=('Arial',16,'bold'),textvariable=costofmeal,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textcom.grid(row=2,column=3)

Cold_coffee = Label(f1,font=('Arial',16,'bold'),text='Cold Coffee:',fg='Steel Blue',bd=16,anchor='w')
Cold_coffee.grid(row=1,column=2)
textcc = Entry(f1,font=('Arial',16,'bold'),textvariable=coldcoffee,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textcc.grid(row=1,column=3)

Service_charge = Label(f1,font=('Arial',16,'bold'),text='Service Charge:',fg='Steel Blue',bd=16,anchor='w')
Service_charge.grid(row=3,column=2)
textsc = Entry(f1,font=('Arial',16,'bold'),textvariable=servicec,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textsc.grid(row=3,column=3)

State_tax = Label(f1,font=('Arial',16,'bold'),text='State Tax:',fg='Steel Blue',bd=16,anchor='w')
State_tax.grid(row=4,column=2)
textst = Entry(f1,font=('Arial',16,'bold'),textvariable=statetax,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textst.grid(row=4,column=3)

Sub_Total = Label(f1,font=('Arial',16,'bold'),text='Sub Total:',fg='Steel Blue',bd=16,anchor='w')
Sub_Total.grid(row=5,column=2)
textsut = Entry(f1,font=('Arial',16,'bold'),textvariable=subtotal,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
textsut.grid(row=5,column=3)

Total_cost = Label(f1,font=('Arial',16,'bold'),text='Total Cost:',fg='Steel Blue',bd=16,anchor='w')
Total_cost.grid(row=6,column=2)
texttc = Entry(f1,font=('Arial',16,'bold'),textvariable=totalcost,fg='Steel Blue',bd=10,insertwidth=4,bg='white',justify='right')
texttc.grid(row=6,column=3)

#==============================BUTTONS===========================

btnTotal = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('Arial',16,'bold'),width=10,text='Total',bg='powder blue',command=Ref).grid(row=8,column=1)

btnexit = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('Arial',16,'bold'),width=10,text='Exit',bg='powder blue',command=qExit).grid(row=8,column=2)

btnreset = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('Arial',16,'bold'),width=10,text='Reset',bg='powder blue',command=Reset).grid(row=8,column=3)

root.mainloop()












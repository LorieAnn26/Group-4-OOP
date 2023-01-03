from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import mysql.connector
import mysql.connector as mysql
from datetime import datetime
import time;


class Customer:
    def __init__(self,root):
        self.root = root
        self.root.title("Uncle George Cafe Ordering System")
        self.root.geometry("1915x1000")
        self.root.config(background='tan')


        #grid bg
        ABC = Frame(self.root, bg='#592c17', bd=20, relief=RIDGE)
        ABC.grid()
        ABC1 = Frame(ABC, bd=14, width=2050, height=300, relief=RIDGE, bg='black')
        ABC1.grid(row=0, column=0, columnspan=4, sticky=W)
        ABC2 = Frame(ABC, bd=10, width=400, height=488, padx=10, relief=RIDGE, bg='black')
        ABC2.grid(row=1, column=0, sticky=W)
        ABC3 = Frame(ABC2, bd=10, width=370, height=340, relief=RIDGE, bg='#b16d3c')
        ABC3.grid(row=0, column=0, sticky=W)
        ABC4 = Frame(ABC2, bd=14, width=370, height=120, padx=10, relief=RIDGE, bg='#592c17')
        ABC4.grid(row=1, column=0, columnspan=4, sticky=W)
        ABC5 = Frame(ABC, bd=10, width=500, height=490,  padx=2, pady=3, relief=RIDGE, bg='#b16d3c')
        ABC5.grid(row=1, column=1, sticky=W)
        ABC6 = Frame(ABC, bd=12, width=470, height=488, relief=RIDGE, bg='black')
        ABC6.grid(row=1, column=2, sticky=W)
        ABC7 = Frame(ABC6, bd=14, width=370, height=340, relief=RIDGE, bg='#b16d3c')
        ABC7.grid(row=0, column=0, sticky=W)
        ABC8 = Frame(ABC6, bd=14, width=370, height=120, relief=RIDGE, bg='#b16d3c')
        ABC8.grid(row=1, column=0, columnspan=4, sticky=W)
        ABC9 = Frame(ABC6, bd=14, width=460, height=488, relief=RIDGE, bg='#b16d3c')
        ABC9.grid(row=2, column=0, sticky='nsew')


        #date, time, title
        Date1 = StringVar()
        Time1 = StringVar()
        Date1.set(time.strftime("%d/%m/%y"))
        Time1.set(time.strftime("%H:%M:%S"))

        self.lblTitle = Label(ABC1, textvariable=Date1, font=('arial',32,'bold'), pady=9,
                              bd=5, bg='black', fg='white').grid(row=0,column=0)

        self.lblTitle = Label(ABC1, text='\tUncle George Cafe\t', font=('arial',62,'bold'), pady=9,
                              bd=5, bg='black', fg='white').grid(row=0,column=1)

        self.lblTitle = Label(ABC1, textvariable=Time1, font=('arial',32,'bold'), pady=9,
                              bd=5, bg='black', fg='white').grid(row=0,column=2)


        #frappes
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()

        E_Skyway = StringVar()
        E_Windblown = StringVar()
        E_Super_Sonic = StringVar()
        E_Realtop = StringVar()
        E_Phenomenal = StringVar()
        E_Silver_Story = StringVar()
        E_Bulldozer = StringVar()
        E_Empire_King = StringVar()
        E_Sky_Dancer = StringVar()
        E_Triple_Crown = StringVar()
        E_Graceful_Lady = StringVar()
        E_Hagdan_Bato = StringVar()

        E_Skyway.set('0')
        E_Windblown.set('0')
        E_Super_Sonic.set('0')
        E_Realtop.set('0')
        E_Phenomenal.set('0')
        E_Silver_Story.set('0')
        E_Bulldozer.set('0')
        E_Empire_King.set('0')
        E_Sky_Dancer.set('0')
        E_Triple_Crown.set('0')
        E_Graceful_Lady.set('0')
        E_Hagdan_Bato.set('0')

        def chkSkyway():
            if (var1.get()==1):
                self.txtSkyway.configure(state='readonly')
                self.txtSkyway.focus()
                self.txtSkyway.delete('0',END)
                E_Skyway.set("0")
            elif var1.get()==0:
                self.txtSkyway.configure(state=DISABLED)
                self.txtSkyway.set('0')

        def chkWindblown():
            if (var2.get()==1):
                self.txtWindblown.configure(state='readonly')
                self.txtWindblown.focus()
                self.txtWindblown.delete('0',END)
                E_Windblown.set("0")
            elif var2.get()==0:
                self.txtWindblown.configure(state=DISABLED)
                self.txtWindblown.set('0')

        def chkSuper_Sonic():
            if (var3.get()==1):
                self.txtSuper_Sonic.configure(state='readonly')
                self.txtSuper_Sonic.focus()
                self.txtSuper_Sonic.delete('0',END)
                E_Super_Sonic.set("0")
            elif var3.get()==0:
                self.txtSuper_Sonic.configure(state=DISABLED)
                self.txtSuper_Sonic.set('0')

        def chkRealtop():
            if (var4.get()==1):
                self.txtRealtop.configure(state='readonly')
                self.txtRealtop.focus()
                self.txtRealtop.delete('0',END)
                E_Realtop.set("0")
            elif var4.get()==0:
                self.txtRealtop.configure(state=DISABLED)
                self.txtRealtop.set('0')

        def chkPhenomenal():
            if (var5.get()==1):
                self.txtPhenomenal.configure(state='readonly')
                self.txtPhenomenal.focus()
                self.txtPhenomenal.delete('0',END)
                E_Phenomenal.set("0")
            elif var5.get()==0:
                self.txtPhenomenal.configure(state=DISABLED)
                self.txtPhenomenal.set('0')

        def chkSilver_Story():
            if (var6.get()==1):
                self.txtSilver_Story.configure(state='readonly')
                self.txtSilver_Story.focus()
                self.txtSilver_Story.delete('0',END)
                E_Silver_Story.set("0")
            elif var6.get()==0:
                self.txtSilver_Story.configure(state=DISABLED)
                self.txtSilver_Story.set('0')

        def chkBulldozer():
            if (var7.get()==1):
                self.txtBulldozer.configure(state='readonly')
                self.txtBulldozer.focus()
                self.txtBulldozer.delete('0',END)
                E_Bulldozer.set("0")
            elif var7.get()==0:
                self.txtBulldozer.configure(state=DISABLED)
                self.txtBulldozer.set('0')

        def chkEmpire_King():
            if (var8.get()==1):
                self.txtEmpire_King.configure(state='readonly')
                self.txtEmpire_King.focus()
                self.txtEmpire_King.delete('0',END)
                E_Empire_King.set("0")
            elif var8.get()==0:
                self.txtEmpire_King.configure(state=DISABLED)
                self.txtEmpire_King.set('0')

        def chkSky_Dancer():
            if (var9.get()==1):
                self.txtSky_Dancer.configure(state='readonly')
                self.txtSky_Dancer.focus()
                self.txtSky_Dancer.delete('0',END)
                E_Sky_Dancer.set("0")
            elif var9.get()==0:
                self.txtSky_Dancer.configure(state=DISABLED)
                self.txtSky_Dancer.set('0')

        def chkTriple_Crown():
            if (var10.get()==1):
                self.txtTriple_Crown.configure(state='readonly')
                self.txtTriple_Crown.focus()
                self.txtTriple_Crown.delete('0',END)
                E_Triple_Crown.set("0")
            elif var10.get()==0:
                self.txtTriple_Crown.configure(state=DISABLED)
                self.txtTriple_Crown.set('0')

        def chkGraceful_Lady():
            if (var11.get()==1):
                self.txtGraceful_Lady.configure(state='readonly')
                self.txtGraceful_Lady.focus()
                self.txtGraceful_Lady.delete('0',END)
                E_Graceful_Lady.set("0")
            elif var11.get()==0:
                self.txtGraceful_Lady.configure(state=DISABLED)
                self.txtGraceful_Lady.set('0')

        def chkHagdan_Bato():
            if (var12.get()==1):
                self.txtHagdan_Bato.configure(state='readonly')
                self.txtHagdan_Bato.focus()
                self.txtHagdan_Bato.delete('0',END)
                E_Hagdan_Bato.set("0")
            elif var12.get()==0:
                self.txtHagdan_Bato.configure(state=DISABLED)
                self.txtHagdan_Bato.set('0')

        self.lblFrappes = Label (ABC5, font=('arial',20,'bold'), text= 'FRAPPES', height=2, bd=2, fg='black', bg='#b16d3c', justify='right')
        self.lblFrappes.grid(row=0, column=0,columnspan=6, sticky='nsew')

        self.Skywayimg = PhotoImage(file="Skyway.png")
        self.Skyway = Checkbutton(ABC5, image=self.Skywayimg, text="Skyway\n P 129.00", variable=var1, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkSkyway)
        self.Skyway.grid(row=1,column=0)
        self.txtSkyway = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Skyway, state=DISABLED, bd=8, width=10)
        self.txtSkyway.grid(row=2, column=0, pady = (2, 25))

        self.WindBlownimg = PhotoImage(file="Windblown.png")
        self.Windblown = Checkbutton(ABC5, image=self.WindBlownimg, text='Windblown\n P 129.00', variable=var2, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkWindblown)
        self.Windblown.grid(row=1,column=1)
        self.txtWindblown = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Windblown, state=DISABLED, bd=8, width=10)
        self.txtWindblown.grid(row=2, column=1, pady = (2, 25))

        self.Super_Sonicimg = PhotoImage(file="SuperSonic.png")
        self.Super_Sonic = Checkbutton(ABC5, image=self.Super_Sonicimg, text='Super Sonic\n P 129.00', variable=var3, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkSuper_Sonic)
        self.Super_Sonic.grid(row=1,column=2)
        self.txtSuper_Sonic = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Super_Sonic, state=DISABLED, bd=8, width=10)
        self.txtSuper_Sonic.grid(row=2, column=2, pady = (2, 25))

        self.Realtopimg = PhotoImage(file="Realtop.png")
        self.Realtop = Checkbutton(ABC5, image=self.Realtopimg, text='Realtop\n P 129.00', variable=var4, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkRealtop)
        self.Realtop.grid(row=1, column=3)
        self.txtRealtop = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Realtop, state=DISABLED, bd=8, width=10)
        self.txtRealtop.grid(row=2, column=3, pady = (2, 25))

        self.Phenomenalimg = PhotoImage(file="Phenomenal.png")
        self.Phenomenal = Checkbutton(ABC5, image=self.Phenomenalimg, text='Phenomenal\n P 129.00', variable=var5, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkPhenomenal)
        self.Phenomenal.grid(row=1, column=4)
        self.txtPhenomenal = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Phenomenal, state=DISABLED, bd=8, width=10)
        self.txtPhenomenal.grid(row=2, column=4, pady = (2, 25))

        self.Silver_Storyimg = PhotoImage(file="SilverStory.png")
        self.Silver_Story = Checkbutton(ABC5, image=self.Silver_Storyimg, text='Silver Story\n P 139.00', variable=var6, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkSilver_Story)
        self.Silver_Story.grid(row=1, column=5)
        self.txtSilver_Story = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Silver_Story, state=DISABLED, bd=8, width=10)
        self.txtSilver_Story.grid(row=2, column=5, pady = (2, 25))

        self.Bulldozerimg = PhotoImage(file="Bulldozer.png")
        self.Bulldozer = Checkbutton(ABC5,image=self.Bulldozerimg, text='Bulldozer\n P 139.00', variable=var7, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkBulldozer)
        self.Bulldozer.grid(row=4, column=0)
        self.txtBulldozer = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Bulldozer, state=DISABLED, bd=8, width=10)
        self.txtBulldozer.grid(row=5, column=0, pady = (2, 25))

        self.Empire_Kingimg = PhotoImage(file="EmpireKing.png")
        self.Empire_King = Checkbutton(ABC5, image=self.Empire_Kingimg, text='Empire King\n P 139.00', variable=var8, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkEmpire_King)
        self.Empire_King.grid(row=4, column=1)
        self.txtEmpire_King = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Empire_King, state=DISABLED, bd=8, width=10)
        self.txtEmpire_King.grid(row=5, column=1, pady = (2, 25))

        self.Sky_Dancerimg = PhotoImage(file="SkyDancer.png")
        self.Sky_Dancer = Checkbutton(ABC5, image=self.Sky_Dancerimg, text='Sky Dancer\n P 139.00', variable=var9, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkSky_Dancer)
        self.Sky_Dancer.grid(row=4, column=2)
        self.txtSky_Dancer = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Sky_Dancer, state=DISABLED, bd=8, width=10)
        self.txtSky_Dancer.grid(row=5, column=2, pady = (2, 25))

        self.Triple_Crownimg = PhotoImage(file="TripleCrown.png")
        self.Triple_Crown = Checkbutton(ABC5, image=self.Triple_Crownimg, text='Triple Crown\n P 139.00', variable=var10, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkTriple_Crown)
        self.Triple_Crown.grid(row=4, column=3)
        self.txtTriple_Crown = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Triple_Crown, state=DISABLED, bd=8, width=10)
        self.txtTriple_Crown.grid(row=5, column=3, pady = (2, 25))

        self.Graceful_Ladyimg = PhotoImage(file="GracefulLady.png")
        self.Graceful_Lady = Checkbutton(ABC5, image=self.Graceful_Ladyimg, text='Graceful Lady\n P 139.00', variable=var11, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkGraceful_Lady)
        self.Graceful_Lady.grid(row=4, column=4)
        self.txtGraceful_Lady = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Graceful_Lady, state=DISABLED, bd=8, width=10)
        self.txtGraceful_Lady.grid(row=5, column=4, pady = (2, 25))

        self.Hagdan_Batoimg = PhotoImage(file="HagdanBato.png")
        self.Hagdan_Bato = Checkbutton(ABC5, image=self.Hagdan_Batoimg, text='Hagdan Bato\n P 139.00', variable=var12, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkHagdan_Bato)
        self.Hagdan_Bato.grid(row=4, column=5)
        self.txtHagdan_Bato = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=1000, textvariable=E_Hagdan_Bato, state=DISABLED, bd=8, width=10)
        self.txtHagdan_Bato.grid(row=5, column=5, pady = (2, 25))


        #payment info
        CustomerRef = StringVar()
        TotalQuantity = StringVar()
        TotalCost = StringVar()
        MOP = StringVar()
        Payment = StringVar()
        TotalChange = StringVar()

        self.lblPaymentInfo = Label (ABC3, font=('arial',20,'bold'), text= 'PAYMENT\n INFORMATION', height=3, bd=2, fg='black', bg='#b16d3c')
        self.lblPaymentInfo.grid(row=0, column=0, columnspan=2, sticky='nsew')

        CustomerRef.set(random.randint(19800,9875648))

        self.lblCus_Ref = Label (ABC3, font=('arial',12,'bold'), text='Customer Ref:', bd=2, fg='black', bg='#b16d3c')
        self.lblCus_Ref.grid(row=1, column=0, sticky=W)
        self.txtCus_Ref = Entry (ABC3, font=('arial',12,'bold'),textvariable=CustomerRef, state='readonly', width=15)
        self.txtCus_Ref.grid(row=1, column=1,pady=3, padx=20)

        self.lblTotalQuantity = Label (ABC3, font=('arial',12,'bold'), text='Total Quantity', bd=2, fg='black', bg='#b16d3c')
        self.lblTotalQuantity.grid(row=2, column=0, sticky=W)
        self.txtTotalQuantity = Entry (ABC3, font=('arial',12,'bold'),textvariable=TotalQuantity, state='readonly', width=15)
        self.txtTotalQuantity.grid(row=2, column=1,pady=3, padx=20)

        self.lblTotalCost = Label (ABC3, font=('arial',12,'bold'), text='Total Cost', bd=2, fg='black', bg='#b16d3c')
        self.lblTotalCost.grid(row=3, column=0, sticky=W)
        self.txtTotalCost = Entry (ABC3, font=('arial',12,'bold'),textvariable=TotalCost,state='readonly', width=15)
        self.txtTotalCost.grid(row=3, column=1,pady=3, padx=20)

        self.lblMOP = Label (ABC3, font=('arial',12,'bold'), text='Mode of Payment:', padx=2, fg='black', bg='#b16d3c')
        self.lblMOP.grid(row=4, column=0, sticky=W)
        self.cboMOP = ttk.Combobox (ABC3, textvariable=MOP, state='readonly', font=('arial',12,'bold'), width=13)
        self.cboMOP ['value']=('','Cash','GCash','COD')
        self.cboMOP.current(0)
        self.cboMOP.grid(row=4, column=1,pady=3, padx=20)

        #payment input
        operator='' #7+9
        def buttonClick(numbers): #9
            global operator
            operator = operator+numbers
            self.txtPayment.delete(0,END)
            self.txtPayment.insert(END,operator)
        
        def clear():
            global operator
            operator=''
            self.txtPayment.delete(0,END)

        self.lblPayment = Label(ABC3, font=('arial', 12, 'bold'), text='Payment:', padx=2, fg='black', bg='#b16d3c')
        self.lblPayment.grid(row=5, column=0, sticky=W)
        self.txtPayment = Entry(ABC3, font=('arial', 12, 'bold'), textvariable=Payment, state='normal', width=15)
        self.txtPayment.grid(row=5, column=1, pady=3, padx=20)

        
        button7=Button(ABC4,text='7',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=7,height=2
                    ,command=lambda:buttonClick('7'))
        button7.grid(row=1,column=0)
        
        button8=Button(ABC4,text='8',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=6,height=2
                    ,command=lambda:buttonClick('8'))
        button8.grid(row=1,column=1)
        
        button9=Button(ABC4,text='9',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=7,height=2
                    ,command=lambda:buttonClick('9'))
        button9.grid(row=1,column=2)
        
        button4=Button(ABC4,text='4',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=7,height=2
                    ,command=lambda:buttonClick('4'))
        button4.grid(row=2,column=0)
        
        button5=Button(ABC4,text='5',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=6,height=2
                    ,command=lambda:buttonClick('5'))
        button5.grid(row=2,column=1)
        
        button6=Button(ABC4,text='6',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=7,height=2
                    ,command=lambda:buttonClick('6'))
        button6.grid(row=2,column=2)
        
        button1=Button(ABC4,text='1',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=7,height=2
                    ,command=lambda:buttonClick('1'))
        button1.grid(row=3,column=0)
        
        button2=Button(ABC4,text='2',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=6,height=2
                    ,command=lambda:buttonClick('2'))
        button2.grid(row=3,column=1)
        
        button3=Button(ABC4,text='3',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=7,height=2
                    ,command=lambda:buttonClick('3'))
        button3.grid(row=3,column=2)
        
        buttonClear=Button(ABC4,text='On/Clear',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=14,height=2
                        ,command=clear)
        buttonClear.grid(row=4,column=0, columnspan=2)
        
        button0=Button(ABC4,text='0',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=7,height=2
                    ,command=lambda:buttonClick('0'))
        button0.grid(row=4,column=2)


        #reciept
        self.txtReciept = Text(ABC7, height=33, width=57, bd=10, font=('arial',9,'bold'))
        self.txtReciept.grid(row=0,column=0)


        #prices and computation
        def PrintReceipt():
            self.txtReciept.delete(1.0,END)
            CustomerRef.set(random.randint(19800,9875648))
            Item1 = int(E_Skyway.get())
            Item2 = int(E_Windblown.get())
            Item3 = int(E_Super_Sonic.get())
            Item4 = int(E_Realtop.get())
            Item5 = int(E_Phenomenal.get())
            Item6 = int(E_Silver_Story.get())
            Item7 = int(E_Bulldozer.get())
            Item8 = int(E_Empire_King.get())
            Item9 = int(E_Sky_Dancer.get())
            Item10 = int(E_Triple_Crown.get())
            Item11 = int(E_Graceful_Lady.get())
            Item12 = int(E_Hagdan_Bato.get())

            Frappe1 = Item1*129
            Frappe2 = Item2*129
            Frappe3 = Item3*129
            Frappe4 = Item4*129
            Frappe5 = Item5*129
            Frappe6 = Item6*139
            Frappe7 = Item7*139
            Frappe8 = Item8*139
            Frappe9 = Item9*139
            Frappe10 = Item10*139
            Frappe11 = Item11*139
            Frappe12 = Item12*139

            Q_Skyway = StringVar()
            Q_Windblown = StringVar()
            Q_Super_Sonic = StringVar()
            Q_Realtop = StringVar()
            Q_Phenomenal = StringVar()
            Q_Silver_Story = StringVar()
            Q_Bulldozer = StringVar()
            Q_Empire_King = StringVar()
            Q_Sky_Dancer = StringVar()
            Q_Triple_Crown = StringVar()
            Q_Graceful_Lady = StringVar()
            Q_Hagdan_Bato = StringVar()

            Q_Skyway.set(Frappe1)
            Q_Windblown.set(Frappe2)
            Q_Super_Sonic.set(Frappe3)
            Q_Realtop.set(Frappe4)
            Q_Phenomenal.set(Frappe5)
            Q_Silver_Story.set(Frappe6)
            Q_Bulldozer.set(Frappe7)
            Q_Empire_King.set(Frappe8)
            Q_Sky_Dancer.set(Frappe9)
            Q_Triple_Crown.set(Frappe10)
            Q_Graceful_Lady.set(Frappe11)
            Q_Hagdan_Bato.set(Frappe12)

            NoOfFrappes = Item1+Item2+Item3+Item4+Item5+Item6+Item7+Item8+Item9+Item10+Item11+Item12
            TotalQuantity.set(NoOfFrappes)
            PriceOfFrappes = (Frappe1+Frappe2+Frappe3+Frappe4+Frappe5+Frappe6+Frappe7+Frappe8+Frappe9+Frappe10+Frappe11+Frappe12)
            Cost = PriceOfFrappes
            TotalCost.set(Cost)
            Date2 = StringVar()
            Time2 = StringVar()
            Date2.set(time.strftime("%d/%m/%y"))
            Time2.set(time.strftime("%H:%M:%S"))
            Pay = Payment
            Pay = (Payment.get())
            Pay = int(Pay)
            Change = Pay - Cost
            TotalChange.set(Change)



            self.txtReciept.insert(END,'\t\t        Uncle George Cafe\n')
            self.txtReciept.insert(END,'\t1476 Vicente Cruz St. Corner Dimasalang Rd.,\n\t\t        Manila, Philippines\n\n')
            self.txtReciept.insert(END,'CustomerRef: \t'+CustomerRef.get()+'\n')
            self.txtReciept.insert(END, Date2.get() + '\t\t\t\t\t' + Time2.get() + '\n')
            self.txtReciept.insert(END, '------------------------------------------------------------------------------------------------')
            self.txtReciept.insert(END,'\nItems\t\t\t\t\t'+'Cost\n')
            if E_Skyway.get()!='0':
                self.txtReciept.insert(END,E_Skyway.get()+' Skyway \t\t\t\t\t'+Q_Skyway.get()+'\n')
            if E_Windblown.get()!='0':
                self.txtReciept.insert(END,E_Windblown.get()+' Windblown \t\t\t\t\t'+Q_Windblown.get()+'\n')
            if E_Super_Sonic.get()!='0':
                self.txtReciept.insert(END,E_Super_Sonic.get()+' Super Sonic \t\t\t\t\t'+Q_Super_Sonic.get()+'\n')
            if E_Realtop.get()!='0':
                self.txtReciept.insert(END,E_Realtop.get()+' Realtop \t\t\t\t\t'+Q_Realtop.get()+'\n')
            if E_Phenomenal.get()!='0':
                self.txtReciept.insert(END,E_Phenomenal.get()+' Phenomenal \t\t\t\t\t'+Q_Phenomenal.get()+'\n')
            if E_Silver_Story.get()!='0':
                self.txtReciept.insert(END,E_Silver_Story.get()+' Silver Story \t\t\t\t\t'+Q_Silver_Story.get()+'\n')
            if E_Bulldozer.get()!='0':
                self.txtReciept.insert(END,E_Bulldozer.get()+' Bulldozer \t\t\t\t\t'+Q_Bulldozer.get()+'\n')
            if E_Empire_King.get()!='0':
                self.txtReciept.insert(END,E_Empire_King.get()+' Empire King \t\t\t\t\t'+Q_Empire_King.get()+'\n')
            if E_Sky_Dancer.get()!='0':
                self.txtReciept.insert(END,E_Sky_Dancer.get()+' Sky Dancer \t\t\t\t\t'+Q_Sky_Dancer.get()+'\n')
            if E_Triple_Crown.get()!='0':
                self.txtReciept.insert(END,E_Triple_Crown.get()+' Triple Crown \t\t\t\t\t'+Q_Triple_Crown.get()+'\n')
            if E_Graceful_Lady.get()!='0':
                self.txtReciept.insert(END,E_Graceful_Lady.get()+' Graceful Lady \t\t\t\t\t'+Q_Graceful_Lady.get()+'\n')
            if E_Hagdan_Bato.get()!='0':
                self.txtReciept.insert(END,E_Hagdan_Bato.get()+' Hagdan Bato \t\t\t\t\t'+Q_Hagdan_Bato.get()+'\n')
            self.txtReciept.insert(END,'------------------------------------------------------------------------------------------------')
            self.txtReciept.insert(END, '\nTotal Quantity: \t\t\t\t\t' + str(TotalQuantity.get()))
            self.txtReciept.insert(END, '\nTotal Cost: \t\t\t\t\t' + 'Php ' + str(TotalCost.get()))
            self.txtReciept.insert(END, '\nMode of Payment: \t\t\t\t\t' + str(MOP.get()))
            self.txtReciept.insert(END, '\nPayment: \t\t\t\t\t' + 'Php ' + (Payment.get()))
            self.txtReciept.insert(END, '\nChange: \t\t\t\t\t' + 'Php ' + (TotalChange.get()))
            self.txtReciept.insert(END,'\n------------------------------------------------------------------------------------------------')
            self.txtReciept.insert(END,'\n\n\t        This serves as your official receipt.\n\t           Thank you! Please come again.\n\n       For feedback message us @ Uncle George Cafe - Sampaloc\n')


        #reset
        def Reset():
            self.txtReciept.delete('1.0',END)
            E_Skyway.set('0')
            E_Windblown.set('0')
            E_Super_Sonic.set('0')
            E_Realtop.set('0')
            E_Phenomenal.set('0')
            E_Silver_Story.set('0')
            E_Bulldozer.set('0')
            E_Empire_King.set('0')
            E_Sky_Dancer.set('0')
            E_Triple_Crown.set('0')
            E_Graceful_Lady.set('0')
            E_Hagdan_Bato.set('0')

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)

            self.txtSkyway.configure(state=DISABLED)
            self.txtWindblown.configure(state=DISABLED)
            self.txtSuper_Sonic.configure(state=DISABLED)
            self.txtRealtop.configure(state=DISABLED)
            self.txtPhenomenal.configure(state=DISABLED)
            self.txtSilver_Story.configure(state=DISABLED)
            self.txtBulldozer.configure(state=DISABLED)
            self.txtEmpire_King.configure(state=DISABLED)
            self.txtSky_Dancer.configure(state=DISABLED)
            self.txtTriple_Crown.configure(state=DISABLED)
            self.txtGraceful_Lady.configure(state=DISABLED)
            self.txtHagdan_Bato.configure(state=DISABLED)

            CustomerRef.set("0")
            TotalQuantity.set("0")
            TotalCost.set("0")
            MOP.set("")
            Payment.set("0")

        # save and print receipt
        def Save():
            r_CustomerReference = CustomerRef.get()
            r_Date = Date1.get()
            r_Time = Time1.get()
            r_TQuantity = TotalQuantity.get()
            r_TCost = TotalCost.get()
            r_Modeofpayment = MOP.get()
            r_Payment = Payment.get()
            r_TotalChange = TotalChange.get()

            mysqldb = mysql.connect(host="localhost", port="3306", user="root", password="", database="orderingsystemug")
            cursor = mysqldb.cursor()
            sql = "INSERT INTO `sales` (Reference_No,Date,Time,Total_Quantity,Total_Cost,Mode_of_Payment,Payment,Total_Change) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (r_CustomerReference, r_Date, r_Time, r_TQuantity, r_TCost, r_Modeofpayment, r_Payment, r_TotalChange)
            cursor.execute(sql, val)
            mysqldb.commit()
            tkinter.messagebox.showinfo("Uncle George Cafe Ordering System", "Receipt has been saved!")

            mysqldb.close()

        #sales
        def Sales():
            root2 = Tk()
            root2.geometry("1915x1000")
            root2.config(background='tan')
            mysqldb = mysql.connect(host="localhost", port="3306", user="root", password="", database="orderingsystemug")
            cursor = mysqldb.cursor()
            cursor.execute("SELECT * FROM sales")
            i = 0
            ABCD = Frame(root2, bg='#592c17', bd=20, relief=RIDGE)
            ABCD.grid()
            ABCD1 = Frame(ABCD, bd=10, width=1800, height=200, relief=RIDGE, bg='black')
            ABCD1.grid(row=0, column=0, columnspan=8, sticky='N')
            ABCD2 = Frame(root2, bd=5, width=1800, height=2, relief=RIDGE, bg='black')
            ABCD2.grid(row=3, column=0, sticky='S', pady = (5,0))


            self.lblTitle = Label(ABCD1, text='\t\t   Sales\t\t\t', font=('arial', 62, 'bold'), pady=9, bd=5, bg='black', fg='white', anchor = 'n').grid(row=0, column=1)


            e = Label(ABCD, width=19, text='Customer Ref No.', font=('arial', 14, 'bold'), borderwidth=2, relief='ridge', anchor='n', bg='tan')
            e.grid(row=1, column=0, pady = (5,0))
            e = Label(ABCD, width=19, text='Date', font=('arial', 14, 'bold'), borderwidth=2, relief='ridge', anchor='n', bg='tan')
            e.grid(row=1, column=1, pady = (5,0))
            e = Label(ABCD, width=19, text='Time', font=('arial', 14, 'bold'), borderwidth=2, relief='ridge', anchor='n', bg='tan')
            e.grid(row=1, column=2, pady = (5,0))
            e = Label(ABCD, width=19, text='Total Quantity', font=('arial', 14, 'bold'), borderwidth=2, relief='ridge', anchor='n', bg='tan')
            e.grid(row=1, column=3, pady = (5,0))
            e = Label(ABCD, width=19, text='Total Cost', font=('arial', 14, 'bold'), borderwidth=2, relief='ridge', anchor='n', bg='tan')
            e.grid(row=1, column=4, pady = (5,0))
            e = Label(ABCD, width=19, text='Mode of Payment', font=('arial', 14, 'bold'), borderwidth=2, relief='ridge', anchor='n', bg='tan')
            e.grid(row=1, column=5, pady = (5,0))
            e = Label(ABCD, width=19, text='Payment', font=('arial', 14, 'bold'), borderwidth=2, relief='ridge', anchor='n', bg='tan')
            e.grid(row=1, column=6, pady = (5,0))
            e = Label(ABCD, width=19, text='Change', font=('arial', 14, 'bold'), borderwidth=2, relief='ridge', anchor='n', bg='tan')
            e.grid(row=1, column=7, pady = (5,0))
            i = 2
            for sales in cursor:
                for j in range(len(sales)):
                    e = Entry(ABCD, width=20, font=('arial', 14, 'bold'), justify=CENTER, borderwidth=2, bg='blanched almond', fg='#592c17')
                    e.grid(row=i, column=j)
                    e.insert(END, sales[j])
                i = i + 1

            def Exit2():
                Exit = tkinter.messagebox.askyesno('Uncle George Cafe Sales','Are you sure you want to exit?')
                if Exit > 0:
                    root2.destroy()
                    return

            # Button for closing
            self.Exit = Button(ABCD2, bd=1, fg='black', font=('arial', 15, 'bold'), width=20, height=2,
                                  bg='blanched almond', text='Exit', command=Exit2,).grid(row=3, column=4)


        #exit
        def Exit():
            Exit = tkinter.messagebox.askyesno('Uncle George Cafe Ordering System','Are you sure you want to exit?')
            if Exit > 0:
                root.destroy()
                return


        #total, reset, exit buttons
        self.btnReset = Button(ABC8, bd=5, fg='black', font=('arial',16,'bold'), width=15, height=2,
                                bg='tan', text='Reset', command=Reset).grid(row=0,column=0)

        self.btnTotal = Button(ABC8, bd=5, fg='black', font=('arial',16,'bold'), width=15, height=2,
                                bg='tan', text='Total', command=PrintReceipt).grid(row=0,column=1)

        self.btnSave = Button(ABC9, bd=5, fg='black', font=('arial', 16, 'bold'), width=31, height=2,
                              bg='tan', text='Save & Print Receipt', command=Save).grid(row=2, column=0)

        self.btnSales = Button(ABC2, padx=14, pady=7, bd=5, fg='black', font=('arial', 16, 'bold'), width=23, height=2,
                               bg='tan', text='Sales', command=Sales).grid(row=2, column=0)

        self.btnExit = Button(ABC2, padx=14, pady=7, bd=5, fg='black', font=('arial',16,'bold'), width=23, height=2,
                                bg='tan', text='Exit', command=Exit).grid(row=3,column=0)



if __name__=='__main__':
    root = Tk()
    application = Customer (root)
    root.mainloop()


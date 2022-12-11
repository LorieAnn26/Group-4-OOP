from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
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
        ABC3 = Frame(ABC2, bd=10, width=400, height=340, relief=RIDGE, bg='#b16d3c')
        ABC3.grid(row=0, column=0, sticky=W)
        ABC4 = Frame(ABC2, bd=14, width=370, height=120, padx=10, relief=RIDGE, bg='#592c17')
        ABC4.grid(row=1, column=0, columnspan=4, sticky=W)
        ABC5 = Frame(ABC, bd=10, width=460, height=490,  padx=2, pady=3, relief=RIDGE, bg='#b16d3c')
        ABC5.grid(row=1, column=1, sticky=W)
        ABC6 = Frame(ABC, bd=12, width=460, height=488, relief=RIDGE, bg='black')
        ABC6.grid(row=1, column=2, sticky=W)
        ABC7 = Frame(ABC6, bd=14, width=370, height=340, relief=RIDGE, bg='#b16d3c')
        ABC7.grid(row=0, column=0, sticky=W)
        ABC8 = Frame(ABC6, bd=14, width=370, height=120, relief=RIDGE, bg='#b16d3c')
        ABC8.grid(row=1, column=0, columnspan=4, sticky=W)
        ABC9 = Frame(ABC6, bd=14, width=460, height=488, relief=RIDGE, bg='#b16d3c')
        ABC9.grid(row=2, column=0, sticky=W)


        #date, time, title
        Date1 = StringVar()
        Time1 = StringVar()
        Date1.set(time.strftime("%d/%m/%y"))
        Time1.set(time.strftime("%H:%M:%S"))

        self.lblTitle = Label(ABC1, textvariable=Date1, font=('arial',30,'bold'), pady=9,
                              bd=5, bg='black', fg='white').grid(row=0,column=0)

        self.lblTitle = Label(ABC1, text='\tUncle George Cafe\t', font=('arial',62,'bold'), pady=9,
                              bd=5, bg='black', fg='white').grid(row=0,column=1)

        self.lblTitle = Label(ABC1, textvariable=Time1, font=('arial',30,'bold'), pady=9,
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
                self.txtSkyway.configure(state=NORMAL)
                self.txtSkyway.focus()
                self.txtSkyway.delete('0',END)
                E_Skyway.set("")
            elif var1.get()==0:
                self.txtSkyway.configure(state=DISABLED)
                self.txtSkyway.set('0')

        def chkWindblown():
            if (var2.get()==1):
                self.txtWindblown.configure(state=NORMAL)
                self.txtWindblown.focus()
                self.txtWindblown.delete('0',END)
                E_Windblown.set("")
            elif var2.get()==0:
                self.txtWindblown.configure(state=DISABLED)
                self.txtWindblown.set('0')

        def chkSuper_Sonic():
            if (var3.get()==1):
                self.txtSuper_Sonic.configure(state=NORMAL)
                self.txtSuper_Sonic.focus()
                self.txtSuper_Sonic.delete('0',END)
                E_Super_Sonic.set("")
            elif var3.get()==0:
                self.txtSuper_Sonic.configure(state=DISABLED)
                self.txtSuper_Sonic.set('0')

        def chkRealtop():
            if (var4.get()==1):
                self.txtRealtop.configure(state=NORMAL)
                self.txtRealtop.focus()
                self.txtRealtop.delete('0',END)
                E_Realtop.set("")
            elif var4.get()==0:
                self.txtRealtop.configure(state=DISABLED)
                self.txtRealtop.set('0')

        def chkPhenomenal():
            if (var5.get()==1):
                self.txtPhenomenal.configure(state=NORMAL)
                self.txtPhenomenal.focus()
                self.txtPhenomenal.delete('0',END)
                E_Phenomenal.set("")
            elif var5.get()==0:
                self.txtPhenomenal.configure(state=DISABLED)
                self.txtPhenomenal.set('0')

        def chkSilver_Story():
            if (var6.get()==1):
                self.txtSilver_Story.configure(state=NORMAL)
                self.txtSilver_Story.focus()
                self.txtSilver_Story.delete('0',END)
                E_Silver_Story.set("")
            elif var6.get()==0:
                self.txtSilver_Story.configure(state=DISABLED)
                self.txtSilver_Story.set('0')

        def chkBulldozer():
            if (var7.get()==1):
                self.txtBulldozer.configure(state=NORMAL)
                self.txtBulldozer.focus()
                self.txtBulldozer.delete('0',END)
                E_Bulldozer.set("")
            elif var7.get()==0:
                self.txtBulldozer.configure(state=DISABLED)
                self.txtBulldozer.set('0')

        def chkEmpire_King():
            if (var8.get()==1):
                self.txtEmpire_King.configure(state=NORMAL)
                self.txtEmpire_King.focus()
                self.txtEmpire_King.delete('0',END)
                E_Empire_King.set("")
            elif var8.get()==0:
                self.txtEmpire_King.configure(state=DISABLED)
                self.txtEmpire_King.set('0')

        def chkSky_Dancer():
            if (var9.get()==1):
                self.txtSky_Dancer.configure(state=NORMAL)
                self.txtSky_Dancer.focus()
                self.txtSky_Dancer.delete('0',END)
                E_Sky_Dancer.set("")
            elif var9.get()==0:
                self.txtSky_Dancer.configure(state=DISABLED)
                self.txtSky_Dancer.set('0')

        def chkTriple_Crown():
            if (var10.get()==1):
                self.txtTriple_Crown.configure(state=NORMAL)
                self.txtTriple_Crown.focus()
                self.txtTriple_Crown.delete('0',END)
                E_Triple_Crown.set("")
            elif var10.get()==0:
                self.txtTriple_Crown.configure(state=DISABLED)
                self.txtTriple_Crown.set('0')

        def chkGraceful_Lady():
            if (var11.get()==1):
                self.txtGraceful_Lady.configure(state=NORMAL)
                self.txtGraceful_Lady.focus()
                self.txtGraceful_Lady.delete('0',END)
                E_Graceful_Lady.set("")
            elif var11.get()==0:
                self.txtGraceful_Lady.configure(state=DISABLED)
                self.txtGraceful_Lady.set('0')

        def chkHagdan_Bato():
            if (var12.get()==1):
                self.txtHagdan_Bato.configure(state=NORMAL)
                self.txtHagdan_Bato.focus()
                self.txtHagdan_Bato.delete('0',END)
                E_Hagdan_Bato.set("")
            elif var12.get()==0:
                self.txtHagdan_Bato.configure(state=DISABLED)
                self.txtHagdan_Bato.set('0')

        self.Skywayimg = PhotoImage(file="Skyway.png")
        self.Skyway = Checkbutton(ABC5, image=self.Skywayimg, text="Skyway\n P 129.00", variable=var1, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkSkyway)
        self.Skyway.grid(row=1,column=0)
        self.txtSkyway = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Skyway, state='readonly', bd=8, width=10)
        self.txtSkyway.grid(row=2, column=0)

        self.WindBlownimg = PhotoImage(file="Windblown.png")
        self.Windblown = Checkbutton(ABC5, image=self.WindBlownimg, text='Windblown\n P 129.00', variable=var2, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkWindblown)
        self.Windblown.grid(row=1,column=1)
        self.txtWindblown = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Windblown, state='readonly', bd=8, width=10)
        self.txtWindblown.grid(row=2, column=1)

        self.Super_Sonicimg = PhotoImage(file="SuperSonic.png")
        self.Super_Sonic = Checkbutton(ABC5, image=self.Super_Sonicimg, text='Super Sonic\n P 129.00', variable=var3, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkSuper_Sonic)
        self.Super_Sonic.grid(row=1,column=2)
        self.txtSuper_Sonic = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Super_Sonic, state='readonly', bd=8, width=10)
        self.txtSuper_Sonic.grid(row=2, column=2)

        self.Realtopimg = PhotoImage(file="Realtop.png")
        self.Realtop = Checkbutton(ABC5, image=self.Realtopimg, text='Realtop\n P 129.00', variable=var4, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkRealtop)
        self.Realtop.grid(row=1, column=3)
        self.txtRealtop = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Realtop, state='readonly', bd=8, width=10)
        self.txtRealtop.grid(row=2, column=3)

        self.Phenomenalimg = PhotoImage(file="Phenomenal.png")
        self.Phenomenal = Checkbutton(ABC5, image=self.Phenomenalimg, text='Phenomenal\n P 129.00', variable=var5, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkPhenomenal)
        self.Phenomenal.grid(row=1, column=4)
        self.txtPhenomenal = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Phenomenal, state='readonly', bd=8, width=10)
        self.txtPhenomenal.grid(row=2, column=4)

        self.Silver_Storyimg = PhotoImage(file="SilverStory.png")
        self.Silver_Story = Checkbutton(ABC5, image=self.Silver_Storyimg, text='Silver Story\n P 139.00', variable=var6, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkSilver_Story)
        self.Silver_Story.grid(row=1, column=5)
        self.txtSilver_Story = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Silver_Story, state='readonly', bd=8, width=10)
        self.txtSilver_Story.grid(row=2, column=5)

        self.Bulldozerimg = PhotoImage(file="Bulldozer.png")
        self.Bulldozer = Checkbutton(ABC5,image=self.Bulldozerimg, text='Bulldozer\n P 139.00', variable=var7, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkBulldozer)
        self.Bulldozer.grid(row=4, column=0)
        self.txtBulldozer = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Bulldozer, state='readonly', bd=8, width=10)
        self.txtBulldozer.grid(row=5, column=0)

        self.Empire_Kingimg = PhotoImage(file="EmpireKing.png")
        self.Empire_King = Checkbutton(ABC5, image=self.Empire_Kingimg, text='Empire King\n P 139.00', variable=var8, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkEmpire_King)
        self.Empire_King.grid(row=4, column=1)
        self.txtEmpire_King = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Empire_King, state='readonly', bd=8, width=10)
        self.txtEmpire_King.grid(row=5, column=1)

        self.Sky_Dancerimg = PhotoImage(file="SkyDancer.png")
        self.Sky_Dancer = Checkbutton(ABC5, image=self.Sky_Dancerimg, text='Sky Dancer\n P 139.00', variable=var9, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkSky_Dancer)
        self.Sky_Dancer.grid(row=4, column=2)
        self.txtSky_Dancer = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Sky_Dancer, state='readonly', bd=8, width=10)
        self.txtSky_Dancer.grid(row=5, column=2)

        self.Triple_Crownimg = PhotoImage(file="TripleCrown.png")
        self.Triple_Crown = Checkbutton(ABC5, image=self.Triple_Crownimg, text='Triple Crown\n P 139.00', variable=var10, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkTriple_Crown)
        self.Triple_Crown.grid(row=4, column=3)
        self.txtTriple_Crown = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Triple_Crown, state='readonly', bd=8, width=10)
        self.txtTriple_Crown.grid(row=5, column=3)

        self.Graceful_Ladyimg = PhotoImage(file="GracefulLady.png")
        self.Graceful_Lady = Checkbutton(ABC5, image=self.Graceful_Ladyimg, text='Graceful Lady\n P 139.00', variable=var11, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkGraceful_Lady)
        self.Graceful_Lady.grid(row=4, column=4)
        self.txtGraceful_Lady = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Graceful_Lady, state='readonly', bd=8, width=10)
        self.txtGraceful_Lady.grid(row=5, column=4)

        self.Hagdan_Batoimg = PhotoImage(file="HagdanBato.png")
        self.Hagdan_Bato = Checkbutton(ABC5, image=self.Hagdan_Batoimg, text='Hagdan Bato\n P 139.00', variable=var12, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan', relief=RIDGE, command=chkHagdan_Bato)
        self.Hagdan_Bato.grid(row=4, column=5)
        self.txtHagdan_Bato = Spinbox(ABC5, font=('arial',17,'bold'), from_=0, to_=100, textvariable=E_Hagdan_Bato, state='readonly', bd=8, width=10)
        self.txtHagdan_Bato.grid(row=5, column=5)


        #payment info
        PaymentInfo = StringVar()
        CustomerRef = StringVar()
        TotalQuantity = StringVar()
        TotalCost = StringVar()
        MOP = StringVar()
        Payment = StringVar()


        self.lblPaymentInfo = Label (ABC3, font=('arial',20,'bold'), text= 'Payment Information', bd=2, fg='black', bg='#b16d3c', justify='right')
        self.lblPaymentInfo.grid(row=0, column=0,columnspan=2, sticky=W)

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
        self.cboMOP = ttk.Combobox (ABC3,textvariable=MOP, state='readonly', font=('arial',12,'bold'), width=13)
        self.cboMOP ['value']=('','Cash','GCash','COD')
        self.cboMOP.current(0)
        self.cboMOP.grid(row=4, column=1,pady=3, padx=20)

        self.lblPayment = Label(ABC3, font=('arial', 12, 'bold'), text='Payment:', padx=2, fg='black', bg='#b16d3c')
        self.lblPayment.grid(row=5, column=0, sticky=W)
        self.txtPayment = Entry(ABC3, font=('arial', 12, 'bold'), textvariable=Payment, state='normal', width=15)
        self.txtPayment.grid(row=5, column=1, pady=3, padx=20)

        operator='' #7+9
        def buttonClick(numbers): #9
            global operator
            operator=operator+numbers
            calculatorField.delete(0,END)
            calculatorField.insert(END,operator)
        
        def clear():
            global operator
            operator=''
            calculatorField.delete(0,END)
        
        def answer():
            global operator
            result=str(eval(operator))
            calculatorField.delete(0,END)
            calculatorField.insert(0,result)
            operator=''
        
        
        calculatorField=Entry(ABC4,font=('arial',14,'bold'),width=26,bd=4)
        calculatorField.grid(row=0,column=0,columnspan=4)
        
        button7=Button(ABC4,text='7',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4,
                    command=lambda:buttonClick('7'))
        button7.grid(row=1,column=0)
        
        button8=Button(ABC4,text='8',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4,
                    command=lambda:buttonClick('8'))
        button8.grid(row=1,column=1)
        
        button9=Button(ABC4,text='9',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4
                    ,command=lambda:buttonClick('9'))
        button9.grid(row=1,column=2)
        
        buttonPlus=Button(ABC4,text='+',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=5
                        ,command=lambda:buttonClick('+'))
        buttonPlus.grid(row=1,column=3)
        
        button4=Button(ABC4,text='4',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4
                    ,command=lambda:buttonClick('4'))
        button4.grid(row=2,column=0)
        
        button5=Button(ABC4,text='5',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4
                    ,command=lambda:buttonClick('5'))
        button5.grid(row=2,column=1)
        
        button6=Button(ABC4,text='6',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4
                    ,command=lambda:buttonClick('6'))
        button6.grid(row=2,column=2)
        
        buttonMinus=Button(ABC4,text='-',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=5
                        ,command=lambda:buttonClick('-'))
        buttonMinus.grid(row=2,column=3)
        
        button1=Button(ABC4,text='1',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4
                    ,command=lambda:buttonClick('1'))
        button1.grid(row=3,column=0)
        
        button2=Button(ABC4,text='2',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4
                    ,command=lambda:buttonClick('2'))
        button2.grid(row=3,column=1)
        
        button3=Button(ABC4,text='3',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4
                    ,command=lambda:buttonClick('3'))
        button3.grid(row=3,column=2)
        
        buttonMult=Button(ABC4,text='*',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=5
                        ,command=lambda:buttonClick('*'))
        buttonMult.grid(row=3,column=3)
        
        buttonAns=Button(ABC4,text='Ans',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4,
                        command=answer)
        buttonAns.grid(row=4,column=0)
        
        buttonClear=Button(ABC4,text='Clear',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4
                        ,command=clear)
        buttonClear.grid(row=4,column=1)
        
        button0=Button(ABC4,text='0',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=4
                    ,command=lambda:buttonClick('0'))
        button0.grid(row=4,column=2)
        
        buttonDiv=Button(ABC4,text='/',font=('arial',14,'bold'),fg='white',bg='black',bd=6,width=5,
                        command=lambda:buttonClick('/'))
        buttonDiv.grid(row=4,column=3)

        #reciept
        self.txtReciept = Text(ABC7, height=35, width=55, bd=10, font=('arial',9,'bold'))
        self.txtReciept.grid(row=0,column=0)


        #Prices and computation
        def costOfItem():
            CustomerRef.set(random.randint(19800,9875648))
            Item1 = float(E_Skyway.get())
            Item2 = float(E_Windblown.get())
            Item3 = float(E_Super_Sonic.get())
            Item4 = float(E_Realtop.get())
            Item5 = float(E_Phenomenal.get())
            Item6 = float(E_Silver_Story.get())
            Item7 = float(E_Bulldozer.get())
            Item8 = float(E_Empire_King.get())
            Item9 = float(E_Sky_Dancer.get())
            Item10 = float(E_Triple_Crown.get())
            Item11 = float(E_Graceful_Lady.get())
            Item12 = float(E_Hagdan_Bato.get())

            PriceOfFrappes = (Item1*129)+(Item2*129)+(Item3*129)+(Item4*129)+(Item5*129)+(Item6*139)+(Item7*139)+(Item8*139)+(Item9*139)+(Item10*139)+(Item11*139)+(Item12*139)
            TCost = ("Php " + str('%.2f'%PriceOfFrappes))
            TotalCost.set(TCost)
            Date2 = StringVar()
            Time2 = StringVar()
            Date2.set(time.strftime("%d/%m/%y"))
            Time2.set(time.strftime("%H:%M:%S"))


            self.txtReciept.insert(END,'\t\t        Uncle George Cafe\n')
            self.txtReciept.insert(END,'\t1476 Vicente Cruz St. Corner Dimasalang Rd.,\n\t\t        Manila, Philippines\n\n')
            self.txtReciept.insert(END,'CustomerRef: \t'+CustomerRef.get()+'\n')
            self.txtReciept.insert(END, Date2.get() + '\t\t\t\t\t    ' + Time2.get() + '\n')
            self.txtReciept.insert(END, '------------------------------------------------------------------------------------------------')
            self.txtReciept.insert(END,'\nItem\t\t\t\t'+'Quantity\n')
            self.txtReciept.insert(END,'Skyway: \t\t\t\t'+E_Skyway.get()+'\n')
            self.txtReciept.insert(END,'Windblown: \t\t\t\t'+E_Windblown.get()+'\n')
            self.txtReciept.insert(END,'Super Sonic: \t\t\t\t'+E_Super_Sonic.get()+'\n')
            self.txtReciept.insert(END,'Realtop: \t\t\t\t'+E_Realtop.get()+'\n')
            self.txtReciept.insert(END,'Phenomenal: \t\t\t\t'+E_Phenomenal.get()+'\n')
            self.txtReciept.insert(END,'Silver Story: \t\t\t\t'+E_Silver_Story.get()+'\n')
            self.txtReciept.insert(END,'Bulldozer: \t\t\t\t'+E_Bulldozer.get()+'\n')
            self.txtReciept.insert(END,'Empire King: \t\t\t\t'+E_Empire_King.get()+'\n')
            self.txtReciept.insert(END,'Sky Dancer: \t\t\t\t'+E_Sky_Dancer.get()+'\n')
            self.txtReciept.insert(END,'Triple Crown: \t\t\t\t'+E_Triple_Crown.get()+'\n')
            self.txtReciept.insert(END,'Graceful Lady: \t\t\t\t'+E_Graceful_Lady.get()+'\n')
            self.txtReciept.insert(END,'Hagdan Bato: \t\t\t\t'+E_Hagdan_Bato.get()+'\n')
            self.txtReciept.insert(END,'------------------------------------------------------------------------------------------------\n')
            self.txtReciept.insert(END, '\nTotal Quantity: \t\t\t\t')
            self.txtReciept.insert(END, '\nTotal Cost: \t\t\t\t\t   ' + str(TotalCost.get()))
            self.txtReciept.insert(END, '\nMode of Payment: \t\t\t\t\t       ' + str(MOP.get()))
            self.txtReciept.insert(END, '\nPayment: \t\t\t\t\t       ' + str(Payment.get()))
            self.txtReciept.insert(END, '\nChange: \t\t\t\t\t\n\n')
            self.txtReciept.insert(END,'------------------------------------------------------------------------------------------------')
            self.txtReciept.insert(END,'\n\n\t        This serves as your official receipt.\n\t           Thank you! Please come again.\n\n       For feedback message us @ Uncle George Cafe - Sampaloc\n')


        #Reset
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

            CustomerRef.set("")
            TotalCost.set("")
            MOP.set("")
            Payment.set("")

        # Sales
        def Sales():
                self.txtReciept = Text(ABC7, height=35, width=55, bd=10, font=('arial', 9, 'bold'))
                self.txtReciept.grid(row=0, column=0)

        #Exit
        def Exit():
            Exit = tkinter.messagebox.askyesno('Uncle George Cafe Ordering System','Are you sure you want to exit?')
            if Exit > 0:
                root.destroy()
                return

        # Save and Print Receipt
        def Save():
            self.txtReciept = Text(ABC7, height=35, width=55, bd=10, font=('arial', 9, 'bold'))
            self.txtReciept.grid(row=0, column=0)

        #total, reset, exit buttons
        self.btnReset = Button(ABC8, bd=5, fg='black', font=('arial',16,'bold'), width=15, height=2,
                                bg='tan', text='Reset', command=Reset).grid(row=0,column=0)

        self.btnTotal = Button(ABC8, bd=5, fg='black', font=('arial',16,'bold'), width=14, height=2,
                                bg='tan', text='Total', command=costOfItem).grid(row=0,column=1)

        self.btnSave = Button(ABC9, bd=5, fg='black', font=('arial', 16, 'bold'), width=30, height=2,
                              bg='tan', text='Save & Print Receipt', command=Save).grid(row=2, column=0)

        self.btnSales = Button(ABC2, padx=14, pady=7, bd=5, fg='black', font=('arial', 16, 'bold'), width=23, height=2,
                               bg='tan', text='Sales', command=Sales).grid(row=2, column=0)

        self.btnExit = Button(ABC2, padx=14, pady=7, bd=5, fg='black', font=('arial',16,'bold'), width=23, height=2,
                                bg='tan', text='Exit', command=Exit).grid(row=2,column=0)



if __name__=='__main__':
    root = Tk()
    application = Customer (root)
    root.mainloop()


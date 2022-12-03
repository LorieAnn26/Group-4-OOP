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
        ABC1 = Frame(ABC, bd=14, width=2050, height=300, padx=10, relief=RIDGE, bg='black')
        ABC1.grid(row=0, column=0, columnspan=4, sticky=W)
        ABC2 = Frame(ABC, bd=14, width=400, height=488, padx=10, relief=RIDGE, bg='black')
        ABC2.grid(row=1, column=0, sticky=W)
        ABC3 = Frame(ABC2, bd=14, width=370, height=340, padx=10, relief=RIDGE, bg='tan')
        ABC3.grid(row=0, column=0, sticky=W)
        ABC4 = Frame(ABC2, bd=14, width=370, height=120, padx=10, relief=RIDGE, bg='#592c17')
        ABC4.grid(row=1, column=0, columnspan=4, sticky=W)
        ABC6 = Frame(ABC, bd=14, width=460, height=488, padx=10, relief=RIDGE, bg='black')
        ABC6.grid(row=1, column=1, sticky=W)
        ABC7 = Frame(ABC6, bd=14, width=370, height=340, padx=10, relief=RIDGE, bg='#592c17')
        ABC7.grid(row=0, column=0, sticky=W)
        ABC8 = Frame(ABC6, bd=14, width=370, height=120, padx=10, relief=RIDGE, bg='#592c17')
        ABC8.grid(row=1, column=0, columnspan=4, sticky=W)
        

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


       #customer info 
        CustomerInfo = StringVar()
        CustomerRef = StringVar()


        self.lblCustomerInfo = Label (ABC3, font=('arial',30,'bold'), text= 'Frappes',height = 1, fg='black', bg='tan', justify='right')
        self.lblCustomerInfo.grid(row=0, column=0, sticky=W)
        
        CustomerRef.set(random.randint(19800,9875648))
        
        self.lblCus_Ref = Label (ABC4, font=('arial',15,'bold'), text='Customer Ref:', padx=3, fg='white', bg='#592c17')
        self.lblCus_Ref.grid(row=1, column=0)
        self.txtCus_Ref = Entry (ABC4, font=('arial',14,'bold'),textvariable=CustomerRef, width=20)
        self.txtCus_Ref.grid(row=1, column=1,pady=3, padx=20)
       

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


        self.Skyway = Checkbutton(ABC3, text='Skyway', variable=var1, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkSkyway)
        self.Skyway.grid(row=1, sticky=W)
        self.txtSkyway = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left',state=DISABLED)
        self.txtSkyway.grid(row=1, column=1)

        self.Windblown = Checkbutton(ABC3, text='Windblown', variable=var2, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkWindblown)
        self.Windblown.grid(row=2, sticky=W)
        self.txtWindblown = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Windblown, bd=8, width=20, justify='left',state=DISABLED)
        self.txtWindblown.grid(row=2, column=1)

        self.Super_Sonic = Checkbutton(ABC3, text='Super Sonic', variable=var3, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkSuper_Sonic)
        self.Super_Sonic.grid(row=3, sticky=W)
        self.txtSuper_Sonic = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Super_Sonic, bd=8, width=20, justify='left',state=DISABLED)
        self.txtSuper_Sonic.grid(row=3, column=1)

        self.Realtop = Checkbutton(ABC3, text='Realtop', variable=var4, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkRealtop)
        self.Realtop.grid(row=4, sticky=W)
        self.txtRealtop = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Realtop, bd=8, width=20, justify='left',state=DISABLED)
        self.txtRealtop.grid(row=4, column=1)

        self.Phenomenal = Checkbutton(ABC3, text='Phenomenal', variable=var5, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkPhenomenal)
        self.Phenomenal.grid(row=5, sticky=W)
        self.txtPhenomenal = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Phenomenal, bd=8, width=20, justify='left',state=DISABLED)
        self.txtPhenomenal.grid(row=5, column=1)

        self.Silver_Story = Checkbutton(ABC3, text='Silver Story', variable=var6, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkSilver_Story)
        self.Silver_Story.grid(row=6, sticky=W)
        self.txtSilver_Story = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Silver_Story, bd=8, width=20, justify='left',state=DISABLED)
        self.txtSilver_Story.grid(row=6, column=1)

        self.Bulldozer = Checkbutton(ABC3, text='Bulldozer', variable=var7, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkBulldozer)
        self.Bulldozer.grid(row=1, column=2, sticky=W)
        self.txtBulldozer = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Bulldozer, bd=8, width=20, justify='left',state=DISABLED)
        self.txtBulldozer.grid(row=1, column=3)

        self.Empire_King = Checkbutton(ABC3, text='Empire King', variable=var8, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkEmpire_King)
        self.Empire_King.grid(row=2, column=2, sticky=W)
        self.txtEmpire_King = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Empire_King, bd=8, width=20, justify='left',state=DISABLED)
        self.txtEmpire_King.grid(row=2, column=3)

        self.Sky_Dancer = Checkbutton(ABC3, text='Sky Dancer', variable=var9, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkSky_Dancer)
        self.Sky_Dancer.grid(row=3, column=2, sticky=W)
        self.txtSky_Dancer = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Sky_Dancer, bd=8, width=20, justify='left',state=DISABLED)
        self.txtSky_Dancer.grid(row=3, column=3)

        self.Triple_Crown = Checkbutton(ABC3, text='Triple Crown', variable=var10, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkTriple_Crown)
        self.Triple_Crown.grid(row=4, column=2, sticky=W)
        self.txtTriple_Crown = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Triple_Crown, bd=8, width=20, justify='left',state=DISABLED)
        self.txtTriple_Crown.grid(row=4, column=3)

        self.Graceful_Lady = Checkbutton(ABC3, text='Graceful Lady', variable=var11, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkGraceful_Lady)
        self.Graceful_Lady.grid(row=5, column=2, sticky=W)
        self.txtGraceful_Lady = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Graceful_Lady, bd=8, width=20, justify='left',state=DISABLED)
        self.txtGraceful_Lady.grid(row=5, column=3)

        self.Hagdan_Bato = Checkbutton(ABC3, text='Hagdan Bato', variable=var12, onvalue=1, offvalue=0,font=('arial',15,'bold'), bg='tan', command=chkHagdan_Bato)
        self.Hagdan_Bato.grid(row=6, column=2, sticky=W)
        self.txtHagdan_Bato = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Hagdan_Bato, bd=8, width=20, justify='left',state=DISABLED)
        self.txtHagdan_Bato.grid(row=6, column=3)
        

	#tax, subtotal, total cost
        Sum = StringVar()
        TotalCost = StringVar()

        
        self.lblSum = Label (ABC4, font=('arial',30,'bold'), text='Total', fg='white', bg='#592c17', justify='right')
        self.lblSum.grid(row=0, column=0, sticky=W)
        
        self.lblTotalCost = Label (ABC4, font=('arial',15,'bold'), text='Total Cost', bd=2, fg='white', bg='#592c17')
        self.lblTotalCost.grid(row=1, column=2, sticky=W)
        self.txtTotalCost = Entry (ABC4, font=('arial',13,'bold'),textvariable=TotalCost, bd=7, width=19)
        self.txtTotalCost.grid(row=1, column=3,pady=3, padx=10)

	#reciept
        self.txtReciept = Text(ABC7, height=23, width=50, bd=10, font=('arial',15,'bold'))
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
            TCost = 'P', str('%.2f'%PriceOfFrappes)
            TotalCost.set(TCost)

            self.txtReciept.insert(END,'\t\tUncle George Cafe\n')
            self.txtReciept.insert(END,'\t\t\n')
            self.txtReciept.insert(END,'CustomerRef: \t'+CustomerRef.get()+'\n')
            self.txtReciept.insert(END,'Items\t\t\t\t'+'Cost of Items\n')
            self.txtReciept.insert(END,'Skyway: \t\t\t\t           '+E_Skyway.get()+'\n')
            self.txtReciept.insert(END,'Windblown: \t\t\t\t           '+E_Windblown.get()+'\n')
            self.txtReciept.insert(END,'Super Sonic: \t\t\t\t           '+E_Super_Sonic.get()+'\n')
            self.txtReciept.insert(END,'Realtop: \t\t\t\t           '+E_Realtop.get()+'\n')
            self.txtReciept.insert(END,'Phenomenal: \t\t\t\t           '+E_Phenomenal.get()+'\n')
            self.txtReciept.insert(END,'Silver Story: \t\t\t\t           '+E_Silver_Story.get()+'\n')
            self.txtReciept.insert(END,'Bulldozer: \t\t\t\t           '+E_Bulldozer.get()+'\n')
            self.txtReciept.insert(END,'Empire King: \t\t\t\t           '+E_Empire_King.get()+'\n')
            self.txtReciept.insert(END,'Sky Dancer: \t\t\t\t           '+E_Sky_Dancer.get()+'\n')
            self.txtReciept.insert(END,'Triple Crown: \t\t\t\t           '+E_Triple_Crown.get()+'\n')
            self.txtReciept.insert(END,'Graceful Lady: \t\t\t\t           '+E_Graceful_Lady.get()+'\n')
            self.txtReciept.insert(END,'Hagdan Bato: \t\t\t\t           '+E_Hagdan_Bato.get()+'\n')

            self.txtReciept.insert(END,'\nTotal Cost: \t\t\t\t'+str(TotalCost.get()))
            

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
            Name.set("")
            Address.set("")
            Contact.set("")
            Payment.set("")
            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")


        #Exit
        def Exit():
            Exit = tkinter.messagebox.askyesno('Uncle George Cafe Ordering System','Are you sure you want to exit?')
            if Exit > 0:
                root.destroy()
                return
                

        #total, reset, exit buttons
        self.btnReset = Button (ABC8, padx=14, pady=7, bd=5, fg='black', font=('arial',20,'bold'), width=9, height=2,
                                bg='tan', text='Reset', command=Reset).grid(row=0,column=0)

        self.btnTotal = Button (ABC8, padx=14, pady=7, bd=5, fg='black', font=('arial',20,'bold'), width=9, height=2,
                                bg='tan', text='Total', command=costOfItem).grid(row=0,column=1)

        self.btnExit = Button (ABC8, padx=14, pady=7, bd=5, fg='black', font=('arial',20,'bold'), width=8, height=2,
                                bg='tan', text='Exit', command=Exit).grid(row=0,column=2)


        
if __name__=='__main__':
    root = Tk()
    application = Customer (root)
    root.mainloop()
    

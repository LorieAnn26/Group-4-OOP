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
        self.root.geometry("1350x750")
        self.root.config(background='tan')


        #grid bg
        ABC = Frame(self.root, bg='tan', bd=20, relief=RIDGE)
        ABC.grid()
        ABC1 = Frame(ABC, bd=14, width=1350, height=100, padx=10, relief=RIDGE, bg='brown')
        ABC1.grid(row=0, column=0, columnspan=4, sticky=W)
        ABC2 = Frame(ABC, bd=14, width=450, height=488, padx=10, relief=RIDGE, bg='brown')
        ABC2.grid(row=1, column=0, sticky=W)
        ABC3 = Frame(ABC, bd=14, width=450, height=488, padx=10, relief=RIDGE, bg='tan')
        ABC3.grid(row=1, column=1, sticky=W)
        ABC4 = Frame(ABC, bd=14, width=460, height=488, padx=10, relief=RIDGE, bg='brown')
        ABC4.grid(row=1, column=2, sticky=W)
        ABC5 = Frame(ABC4, bd=14, width=370, height=340, padx=10, relief=RIDGE, bg='tan')
        ABC5.grid(row=0, column=0, sticky=W)
        ABC6 = Frame(ABC4, bd=14, width=370, height=120, padx=10, relief=RIDGE, bg='tan')
        ABC6.grid(row=1, column=0, columnspan=4, sticky=W)


        #date, time, title
        Date1 = StringVar()
        Time1 = StringVar()
        Date1.set(time.strftime("%d/%m/%y"))
        Time1.set(time.strftime("%H:%M:%S"))

        self.lblTitle = Label(ABC1, textvariable=Date1, font=('times',31,'bold'), pady=9,
                              bd=5, bg='brown', fg='white').grid(row=0,column=0)
        
        self.lblTitle = Label(ABC1, text='\tUncle George Cafe\t\t', font=('times',40,'bold'), pady=9,
                              bd=5, bg='brown', fg='white').grid(row=0,column=1)

        self.lblTitle = Label(ABC1, textvariable=Time1, font=('times',31,'bold'), pady=9,
                              bd=5, bg='brown', fg='white').grid(row=0,column=2)


        #customer info 
        CustomerRef = StringVar()
        Name = StringVar()
        Address = StringVar()
        Contact = StringVar()
        Payment = StringVar()
        Orders = StringVar()
        
        self.lblCus_Ref = Label (ABC2, font=('arial',12,'bold'), text='Customer Ref:', padx=2, fg='white', bg='brown')
        self.lblCus_Ref.grid(row=0, column=0)
        self.txtCus_Ref = Entry (ABC2, font=('arial',12,'bold'),textvariable=CustomerRef, width=20)
        self.txtCus_Ref.grid(row=0, column=1,pady=3, padx=20)

        self.lblName = Label (ABC2, font=('arial',12,'bold'), text='Name:', padx=2, pady=2, fg='white', bg='brown')
        self.lblName.grid(row=1, column=0)
        self.txtName = Entry (ABC2, font=('arial',12,'bold'), textvariable=Name, width=20)
        self.txtName.grid(row=1, column=1,pady=3, padx=20)

        self.lblAddress = Label (ABC2, font=('arial',12,'bold'), text='Address:', padx=2, pady=2, fg='white', bg='brown')
        self.lblAddress.grid(row=2, column=0)
        self.txtAddress = Entry (ABC2, font=('arial',12,'bold'),textvariable=Address, width=20)
        self.txtAddress.grid(row=2, column=1,pady=3, padx=20)
        
        self.lblContact = Label (ABC2, font=('arial',12,'bold'), text='Contact:', padx=2, pady=2, fg='white', bg='brown')
        self.lblContact.grid(row=3, column=0)
        self.txtContact = Entry (ABC2, font=('arial',12,'bold'),textvariable=Contact, width=20)
        self.txtContact.grid(row=3, column=1,pady=3, padx=20)

        self.lblPayment = Label (ABC2, font=('arial',12,'bold'), text='Payment:', padx=2, fg='white', bg='brown')
        self.lblPayment.grid(row=4, column=0)
        self.cboPayment = ttk.Combobox (ABC2,textvariable=Payment, state='readonly', font=('arial',12,'bold'), width=18)
        self.cboPayment ['value']=('','Cash','GCash','COD')
        self.cboPayment.current(0)
        self.cboPayment.grid(row=4, column=1,pady=3, padx=20)


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

        self.Skyway = Checkbutton(ABC3, text='Skyway', variable=var1, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Skyway.grid(row=0, sticky=W)
        self.txtSkyway = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left')
        self.txtSkyway.grid(row=0, column=1)

        self.Windblown = Checkbutton(ABC3, text='Windblown', variable=var2, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Windblown.grid(row=1, sticky=W)
        self.txtWindblown = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left')
        self.txtWindblown.grid(row=1, column=1)

        self.Super_Sonic = Checkbutton(ABC3, text='Super Sonic', variable=var3, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Super_Sonic.grid(row=2, sticky=W)
        self.txtSuper_Sonic = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left',state=DISABLED)
        self.txtSuper_Sonic.grid(row=2, column=1)

        self.Realtop = Checkbutton(ABC3, text='Realtop', variable=var1, onvalue=4, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Realtop.grid(row=3, sticky=W)
        self.txtRealtop = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left',state=DISABLED)
        self.txtRealtop.grid(row=3, column=1)

        self.Phenomenal = Checkbutton(ABC3, text='Phenomenal', variable=var1, onvalue=5, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Phenomenal.grid(row=4, sticky=W)
        self.txtPhenomenal = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left',state=DISABLED)
        self.txtPhenomenal.grid(row=4, column=1)

        self.Silver_Story = Checkbutton(ABC3, text='Silver Story', variable=var6, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Silver_Story.grid(row=5, sticky=W)
        self.txtSilver_Story = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left',state=DISABLED)
        self.txtSilver_Story.grid(row=5, column=1)

        self.Bulldozer = Checkbutton(ABC3, text='Bulldozer', variable=var7, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Bulldozer.grid(row=6, sticky=W)
        self.txtBulldozer = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left',state=DISABLED)
        self.txtBulldozer.grid(row=6, column=1)

        self.Empire_King = Checkbutton(ABC3, text='Empire King', variable=var8, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Empire_King.grid(row=7, sticky=W)
        self.txtEmpire_King = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left',state=DISABLED)
        self.txtEmpire_King.grid(row=7, column=1)

        self.Sky_Dancer = Checkbutton(ABC3, text='Sky Dancer', variable=var9, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Sky_Dancer.grid(row=8, sticky=W)
        self.txtSky_Dancer = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left',state=DISABLED)
        self.txtSky_Dancer.grid(row=8, column=1)

        self.Triple_Crown = Checkbutton(ABC3, text='Triple Crown.', variable=var10, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Triple_Crown.grid(row=9, sticky=W)
        self.txtTriple_Crown = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left',state=DISABLED)
        self.txtTriple_Crown.grid(row=9, column=1)

        self.Graceful_Lady = Checkbutton(ABC3, text='Graceful Lady', variable=var11, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Graceful_Lady.grid(row=10, sticky=W)
        self.txtGraceful_Lady = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left',state=DISABLED)
        self.txtGraceful_Lady.grid(row=10, column=1)

        self.Hagdan_Bato = Checkbutton(ABC3, text='Hagdan Bato', variable=var12, onvalue=1, offvalue=0,font=('arial',12,'bold'), bg='tan')
        self.Hagdan_Bato.grid(row=11, sticky=W)
        self.txtHagdan_Bato = Entry(ABC3, font=('arial',12,'bold'), textvariable=E_Skyway, bd=8, width=20, justify='left',state=DISABLED)
        self.txtHagdan_Bato.grid(row=11, column=1)


        #reciept
        self.txtReciept = Text(ABC5, height=20, width=43, bd=10, font=('arial',9,'bold'))
        self.txtReciept.grid(row=0,column=0)


        #Exit
        def Exit():
            Exit = tkinter.messagebox.askyesno('Uncle George Cafe Ordering System','Are you sure you want to exit?')
            if Exit > 0:
                root.destroy()
                return
            

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
                

        #total, reset, exit buttons
        self.btnReset = Button (ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial',16,'bold'), width=5, height=2,
                                bg='tan', text='Reset').grid(row=0,column=0)

        self.btnTotal = Button (ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial',16,'bold'), width=5, height=2,
                                bg='tan', text='Total').grid(row=0,column=1)

        self.btnExit = Button (ABC6, padx=14, pady=7, bd=5, fg='black', font=('arial',16,'bold'), width=5, height=2,
                                bg='tan', text='Exit', command=Exit).grid(row=0,column=2)


        
if __name__=='__main__':
    root = Tk()
    application = Customer (root)
    root.mainloop()
    

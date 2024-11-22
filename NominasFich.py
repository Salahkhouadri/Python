from tkinter import *
class Nominas:
    def __init__(self,root):
        self.root = Toplevel(root)
        self.root.title("Nominas")
        self.root.columnconfigure([0, 1, 2, 3, 4, 5, 6,7], weight=1) 
        self.root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16], weight=0) 
        self.root.geometry("1300x600")
        self.root.configure(padx=30,pady=30)
        self.create_nomina()
        self.root.mainloop()

    def create_nomina(self):
        Label(self.root, text="Codigo", font=("Arial", 12,"bold")).grid(row=0, column=0,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Apellidos y Nombre", font=("Arial", 12,"bold")).grid(row=0, column=1,columnspan=7, sticky="nsew",padx=20,pady=5)
        entri1 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,))
        entri2 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10))
        entri1.grid(row=1, column=0,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri2.grid(row=1, column=1,columnspan=7, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri2.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")


        ##Second Row##
        Label(self.root, text="Fecha Inicio", font=("Arial", 12,"bold")).grid(row=2, column=0,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Fecha Nacimiento", font=("Arial", 12,"bold")).grid(row=2, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Direccion", font=("Arial", 12,"bold")).grid(row=2, column=2,columnspan=7, sticky="nsew",padx=20,pady=5)
        entri3 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri4 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri5 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))

        entri3.grid(row=3, column=0,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri4.grid(row=3, column=1,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri5.grid(row=3, column=2,columnspan=7, sticky="nsew",padx=20,pady=5,ipady=5) 

        entri3.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        entri4.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        entri5.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")


        ####Tercera Row####
        Label(self.root, text="NIF", font=("Arial", 12,"bold")).grid(row=4, column=0,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Datos Bancarios", font=("Arial", 12,"bold")).grid(row=4, column=1,columnspan=4, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Numero afiliacion SS", font=("Arial", 12,"bold")).grid(row=4, column=5,columnspan=3, sticky="nsew",padx=20,pady=5)
        entri6 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri7 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri8 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))

        entri6.grid(row=5, column=0,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri7.grid(row=5, column=1,columnspan=4, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri8.grid(row=5, column=5,columnspan=3, sticky="nsew",padx=20,pady=5,ipady=5) 

        entri6.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        entri7.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        entri8.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")

        ####Quinto Row####
        Label(self.root, text="Salario Bruto", font=("Arial", 12,"bold")).grid(row=8, column=0,columnspan=1, sticky="nsew",padx=20,pady=20)
        Label(self.root, text="Numero Pagas", font=("Arial", 12,"bold")).grid(row=8, column=2,columnspan=1, sticky="nsew",padx=20,pady=20)
        entri9 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri10 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri9.grid(row=8, column=1,columnspan=1, sticky="nsew",padx=20,pady=20,ipady=5) 
        entri10.grid(row=8, column=3,columnspan=1, sticky="nsew",padx=20,pady=20,ipady=5) 

        entri9.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        entri10.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")

        hr = Frame(self.root, height=1, bg="black") 
        hr.grid(row=9, column=0, columnspan=8, sticky="ew", padx=20,pady=(0,10))  

        ####Sexto Row####
        Label(self.root, text="SALARIO MES", font=("Arial", 12,"bold")).grid(row=10, column=0,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="%IRPF", font=("Arial", 12,"bold")).grid(row=10, column=2,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Rentencion IRPF", font=("Arial", 12,"bold")).grid(row=10, column=5,columnspan=1, sticky="nsew",padx=20,pady=5)
        entri11 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri12 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri13 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))

        entri11.grid(row=10, column=1,columnspan=1, sticky="nsew",padx=20,pady=10,ipady=5) 
        entri12.grid(row=10, column=3,columnspan=1, sticky="nsew",padx=20,pady=10,ipady=5) 
        entri13.grid(row=10, column=6,columnspan=2, sticky="nsew",padx=20,pady=10,ipady=5) 

        entri11.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")
        entri12.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")

        ####Septimo Row####
        Label(self.root, text="PRORROTA PAGAS", font=("Arial", 12,"bold")).grid(row=12, column=0,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="SEG. SOCIAL", font=("Arial", 12,"bold")).grid(row=12, column=2,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="DEDUCCION SS", font=("Arial", 12,"bold")).grid(row=12, column=5,columnspan=1, sticky="nsew",padx=20,pady=5)
        entri14 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri15 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri16 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))

        entri14.grid(row=12, column=1,columnspan=1, sticky="nsew",padx=20,pady=10,ipady=5) 
        entri15.grid(row=12, column=3,columnspan=1, sticky="nsew",padx=20,pady=10,ipady=5) 
        entri16.grid(row=12, column=6,columnspan=2, sticky="nsew",padx=20,pady=10,ipady=5) 

        entri15.config(state=DISABLED, disabledbackground="#BCDEFF",disabledforeground="black")

        Label(self.root, text="MENSAJES VALIDACION",fg="red", font=("Arial", 12,"bold"), bd=1, relief="solid", wraplength=650).grid(row=14, column=0,columnspan=4, sticky="nsew",padx=20,pady=10,ipady=10)
        Label(self.root, text="A PERCIBIR", font=("Arial", 12,"bold")).grid(row=14, column=5,columnspan=1, sticky="nsew",padx=20,pady=5)
        entri17 = Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri17.grid(row=14, column=6,columnspan=2, sticky="nsew",padx=20,pady=10,ipady=5) 
        entri17.config(state=DISABLED, disabledbackground="#838383",disabledforeground="black")

        Button(self.root, text="Cargar Empleado",font=("Arial", 15,"bold"), bd=1, relief="solid", background="#FFFF99").grid(row=15, column=1,columnspan=2, sticky="nsew",padx=20,pady=10)
        Button(self.root, text="CALCULAR",font=("Arial", 15,"bold"), bd=1, relief="solid", background="#FFFF99").grid(row=15, column=5,columnspan=1, sticky="nsew",padx=20,pady=10)
        Button(self.root, text="IMPRIMIR",font=("Arial", 15,"bold"), bd=1, relief="solid", background="#FFFF99").grid(row=15, column=6,columnspan=1, sticky="nsew",padx=20,pady=10)

        
from tkinter import *
class Altas:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Altas")
        self.root.columnconfigure([0, 1, 2, 3, 4, 5, 6,7], weight=1) 
        self.root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10], weight=0) 
        self.root.resizable(1, 0)
        self.create_gui()
        self.root.mainloop()
        
    def create_gui(self):
        ####Primera Row####
        Label(self.root, text="Apellidos y Nombre", font=("Arial", 12,"bold")).grid(row=0, column=0,columnspan=8, sticky="nsew",padx=20,pady=5)
        entri1 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri1.grid(row=1, column=1,columnspan=6, sticky="nsew",padx=20,pady=5,ipady=5) 

    
        ####Segunda Row####
        Label(self.root, text="Fecha Inicio", font=("Arial", 12,"bold")).grid(row=2, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Fecha Nacimiento", font=("Arial", 12,"bold")).grid(row=2, column=2,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Direccion", font=("Arial", 12,"bold")).grid(row=2, column=3,columnspan=4, sticky="nsew",padx=20,pady=5)
        entri2 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri3 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri4 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri2.grid(row=3, column=1,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri3.grid(row=3, column=2,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri4.grid(row=3, column=3,columnspan=4, sticky="nsew",padx=20,pady=5,ipady=5) 

        ####Tercera Row####
        Label(self.root, text="NIF", font=("Arial", 12,"bold")).grid(row=4, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Datos Bancarios", font=("Arial", 12,"bold")).grid(row=4, column=2,columnspan=3, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Numero afiliacion SS", font=("Arial", 12,"bold")).grid(row=4, column=5,columnspan=2, sticky="nsew",padx=20,pady=5)
        entri5 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri6 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri7 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri5.grid(row=5, column=1,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri6.grid(row=5, column=2,columnspan=3, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri7.grid(row=5, column=5,columnspan=2, sticky="nsew",padx=20,pady=5,ipady=5) 

        ####Cuarta Row####
        Label(self.root, text="Genero", font=("Arial", 12,"bold")).grid(row=6, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Departarmento", font=("Arial", 12,"bold")).grid(row=6, column=2,columnspan=3, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Puesto", font=("Arial", 12,"bold")).grid(row=6, column=5,columnspan=2, sticky="nsew",padx=20,pady=5)
        entri8 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri9 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri10 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri8.grid(row=7, column=1,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri9.grid(row=7, column=2,columnspan=3, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri10.grid(row=7, column=5,columnspan=2, sticky="nsew",padx=20,pady=5,ipady=5) 

        ####Quinto Row####
        Label(self.root, text="Telefono", font=("Arial", 12,"bold"), anchor="w").grid(row=8, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Salario Mensual", font=("Arial", 12,"bold"), anchor="w").grid(row=8, column=3,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="IRPF", font=("Arial", 12,"bold"), anchor="w").grid(row=8, column=5,columnspan=1, sticky="nsew",padx=20,pady=5)
        entri8 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri9 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri10 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"), justify="center")
        entri8.grid(row=8, column=2,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri9.grid(row=8, column=4,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri10.grid(row=8, column=6,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri10.insert(0, "10%")
        entri10.config(state="readonly")


        ####Sexto Row####
        Label(self.root, text="Email", font=("Arial", 12,"bold"), anchor="w").grid(row=9, column=1,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Pagas Extra", font=("Arial", 12,"bold"), anchor="w").grid(row=9, column=3,columnspan=1, sticky="nsew",padx=20,pady=5)
        Label(self.root, text="Seg. Social", font=("Arial", 12,"bold"), anchor="w").grid(row=9, column=5,columnspan=1, sticky="nsew",padx=20,pady=5)
        entri11 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri12 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"))
        entri13 = Entry(self.root, bd=1, relief="solid",font=("Arial", 10,"bold"), justify="center")
        entri11.grid(row=9, column=2,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri12.grid(row=9, column=4,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri13.grid(row=9, column=6,columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5) 
        entri13.insert(0, "6.4%")
        entri13.config(state="readonly")

        ####Septimo Row####
        Label(self.root, text="MENSAJES VALIDACION",fg="red", font=("Arial", 12,"bold"), bd=1, relief="solid").grid(row=10, column=1,columnspan=4,rowspan=2, sticky="nsew",padx=20,pady=10,ipady=10)
        Button(self.root, text="Guardar", bd=1, relief="solid", background="#FFFF99", font=("Arial",12, "bold")).grid(row=10, column=5,columnspan=2, rowspan=1,sticky="nsew",padx=20,pady=5,ipady=10) 
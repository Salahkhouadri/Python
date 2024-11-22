from tkinter import *

class Bajas:
    def __init__(self, root):
        self.root = Toplevel(root)
        self.root.title("Bajas")
        self.root.columnconfigure([0, 1], weight=1)
        self.root.rowconfigure([0, 1, 2, 3], weight=0)
        self.root.geometry("500x350")
        self.root.resizable(1,0)
        self.create_bajas()
        self.root.mainloop()
        
    def create_bajas(self):
        Label(self.root, text="Codigo Empleado", font=("Arial",12, "bold")).grid(row=0, column=0, columnspan=1, sticky="nsew",pady=(50,10))
        entri1= Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri1.grid(row=1, column=0, columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5)

        Label(self.root, text="Fecha Baja", font=("Arial",12, "bold")).grid(row=0, column=1, columnspan=1, sticky="nsew",pady=(50,10))
        entri2= Entry(self.root, bd=1, relief="solid",font=("Arial", 12))
        entri2.grid(row=1, column=1, columnspan=1, sticky="nsew",padx=20,pady=5,ipady=5)

        Label(self.root, text="MENSAJES VALIDACION", font=("Arial",12, "bold"),fg="red", bd=1, relief="solid").grid(row=2, column=0, columnspan=2, sticky="nsew",padx=60,pady=20,ipady=20)

        Button(self.root, text="Confirmar", bd=1, relief="solid",background="#FFFF99", font=("Arial",12, "bold")).grid(row=3, column=0, columnspan=2,pady=5,ipadx=30,ipady=10)



    
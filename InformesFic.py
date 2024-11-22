from tkinter import *
class Informes:
    def __init__(self,root):
        self.root = Toplevel(root)
        self.root.title("Informes")
        self.root.columnconfigure([0, 1, 2, 3], weight=1) 
        self.root.rowconfigure([0, 1, 2, 3, 4, 5], weight=1) 
        self.root.configure(padx=50,pady=50)
        self.root.geometry("1500x600")
        self.crea_informes()
        self.root.mainloop()

    def crea_informes(self):
        Label(self.root, text="EMPLEADOS\nALTA", font=("Arial",15,"bold"), pady=10).grid(row=0, column=0)
        Label(self.root, text="EMPLEADOS\nBAJA", font=("Arial",15,"bold"), pady=10).grid(row=0, column=1)
        Label(self.root, text="MEDIA\nEDADES", font=("Arial",15,"bold"), pady=10).grid(row=0, column=2)
        Label(self.root, text="RETRIBUCION\nMEDIA", fg="Blue", font=("Arial",15,"bold"), pady=10).grid(row=0, column=3)

        entri1 =Entry(self.root,bd=1, relief="solid", justify="center", font=("Arial",15))
        entri2 =Entry(self.root,bd=1, relief="solid", justify="center", font=("Arial",15))
        entri3 =Entry(self.root,bd=1, relief="solid", justify="center", font=("Arial",15))
        entri4 =Entry(self.root,bd=1, relief="solid", justify="center", font=("Arial",18))

        entri1.grid(row=1, column=0,ipady=25,ipadx=25)
        entri2.grid(row=1, column=1,ipady=25,ipadx=25)
        entri3.grid(row=1, column=2,ipady=25,ipadx=25)
        entri4.grid(row=1, column=3,ipady=30,ipadx=40)

        entri1.config(state="readonly")
        entri2.config(state="readonly")
        entri3.config(state="readonly")
        entri4.config(state="readonly")

        ###Segunda Row####
        Label(self.root, text="%MUJERES", font=("Arial",15),pady=20).grid(row=2, column=0)
        Label(self.root, text="%MUJERES", font=("Arial",15),pady=20).grid(row=2, column=1)
        Label(self.root, text="MUJERES", font=("Arial",15),pady=20).grid(row=2, column=2)
        Label(self.root, text="MUJERES", fg="#94B8FF", font=("Arial",15,"bold"),pady=20).grid(row=2, column=3)

        entri5 =Entry(self.root,bd=1, relief="solid", font=("Arial",15))
        entri6 =Entry(self.root,bd=1, relief="solid", font=("Arial",15))
        entri7 =Entry(self.root,bd=1, relief="solid", font=("Arial",15))
        entri8 =Entry(self.root,bd=1, relief="solid", font=("Arial",15))

        entri5.grid(row=3, column=0,ipady=25,ipadx=25)
        entri6.grid(row=3, column=1,ipady=25,ipadx=25)
        entri7.grid(row=3, column=2,ipady=25,ipadx=25)
        entri8.grid(row=3, column=3,ipady=25,ipadx=25)


        entri5.config(state="readonly")
        entri6.config(state="readonly")
        entri7.config(state="readonly")
        entri8.config(state="readonly")

        ###Segunda Row####
        Label(self.root, text="%HOMBRES", font=("Arial",15),pady=20).grid(row=4, column=0)
        Label(self.root, text="%HOMBRES", font=("Arial",15),pady=20).grid(row=4, column=1)
        Label(self.root, text="HOMBRES", font=("Arial",15),pady=20).grid(row=4, column=2)
        Label(self.root, text="HOMBRES", fg="#94B8FF", font=("Arial",15,"bold"),pady=20).grid(row=4, column=3)

        entri9 =Entry(self.root,bd=1, relief="solid", font=("Arial",15))
        entri10 =Entry(self.root,bd=1, relief="solid", font=("Arial",15))
        entri11 =Entry(self.root,bd=1, relief="solid", font=("Arial",15))
        entri12 =Entry(self.root,bd=1, relief="solid", font=("Arial",15))

        entri9.grid(row=5, column=0,ipady=25,ipadx=25)
        entri10.grid(row=5, column=1,ipady=25,ipadx=25)
        entri11.grid(row=5, column=2,ipady=25,ipadx=25)
        entri12.grid(row=5, column=3,ipady=25,ipadx=25)


        entri9.config(state="readonly")
        entri10.config(state="readonly")
        entri11.config(state="readonly")
        entri12.config(state="readonly")
        
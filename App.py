from tkinter import *
from AltasFich import Altas 
from BajasFic import Bajas
from InformesFic import Informes
from NominasFich import Nominas

def launch_altas():
    Altas(root)
def launch_bajas():
    Bajas(root)
    
def launch_informes():
    Informes(root)

def launch_nominas():
    Nominas(root)
    
root = Tk()
root.title("GUI Example")


root.columnconfigure([0, 1], weight=1) 
root.rowconfigure([0, 1, 2, 3], weight=1) 

root.geometry("500x500")
root.resizable(0, 0)

#AQUI EL HEAD
header_label = Label(root, text="Nominator+", font=("Arial", 16))
header_label.grid(row=0, column=0, columnspan=2)  


try:
    image = PhotoImage(file="Face.png").subsample(8)
except TclError:
    print("Error: No se pudo cargar la imagen 'Face.png'.")
    image = None 
image_label = Label(root, image=image)
image_label.grid(row=1, column=0, columnspan=2, sticky="nsew") 

button1 = Button(root, text="ALTAS")
button2 = Button(root, text="BAJAS")
button3 = Button(root, text="INFORMES")
button4 = Button(root, text="NOMINAS")


button1.config(background="#FFFF99", border=2, font=("Arial", 12),bd=1, relief="solid",command=launch_altas)
button2.config(background="#FFFF99", border=2, font=("Arial", 12),bd=1, relief="solid",command=launch_bajas)
button3.config(background="#FFFF99", border=2, font=("Arial", 12),bd=1, relief="solid",command=launch_informes)
button4.config(background="#FFFF99", border=2, font=("Arial", 12),bd=1, relief="solid",command=launch_nominas)



button1.grid(row=2, column=0,ipadx=75,ipady=10) 
button2.grid(row=2, column=1,ipadx=75,ipady=10) 
button3.grid(row=3, column=0,ipadx=60,ipady=10)  
button4.grid(row=3, column=1,ipadx=60,ipady=10) 


root.mainloop()

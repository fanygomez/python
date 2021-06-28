from tkinter import *

raiz = Tk()
raiz.title("Test1")
# raiz.resizable()
#Desactivar redimencionar
# raiz.resizable(0,0)
# Redimencionar a lo ancho
# raiz.resizable(1,0)
# Agregar imagen
# raiz.iconbitmap("gato.ico")
# la raiz se va adapter al tamaño de su contenedor interno ( frame)
# raiz.geometry("650x350")

# Canbiar color de fondoo
raiz.config(bg="blue")
#Crear frame
miFrame = Frame()
#Empaquetar frames
# miFrame.pack(side="left",anchor="n")
# miFrame.pack(fill="x")
# miFrame.pack(fill="y",expand="True")
# miFrame.pack(fill="both",expand="True")
miFrame.pack()
miFrame.config(bg="red")
#Agregar tamañano al frame
miFrame.config(width="650",height="650")
miFrame.config(bd=35)
# miFrame.config(relief="groove")
miFrame.config(relief="sunken")
miFrame.config(cursor="hand2")
raiz.mainloop()
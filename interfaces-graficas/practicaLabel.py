from tkinter import *
#Permite imagenes .png, gif para hacer uso de otro formato se tiene que cargar otro modulos
root = Tk()
root.title("Test2")
miFrame = Frame(root,width = 500, height=400)
miFrame.pack()
# miImagen = PhotoImage(file="mouse.gif")
# Label(miFrame,imagen=miImagen).place(x=100,y=200)
Label(miFrame, text="Hola mundo!!", fg="red",font=("Comic Sans MS",20)).place(x=100,y=200)

root.mainloop()
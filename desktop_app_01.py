# se importa la libreria tkinter con todas sus fuciones

from tkinter import *
from tkinter import messagebox

# =============================
# funciones de la app
# =============================
def calcular():
    messagebox.showinfo("MINICALCULADORA", "Hizo click en calcular")
    s=int(a.get())+int(b.get())
    r=int(a.get())-int(b.get())
    m=int(a.get())*int(b.get())
    d=int(a.get())/int(b.get())
    t=int(a.get())%int(b.get())
    mod=int(a.get())//int(b.get())
    p=int(a.get())**int(b.get())
    t_resultados.insert(INSERT, f"{a.get()} + {b.get()} = {s}\n")
    t_resultados.insert(INSERT, f"{a.get()} - {b.get()} = {r}\n")
    t_resultados.insert(INSERT, f"{a.get()} x {b.get()} = {m}\n")
    t_resultados.insert(INSERT, f"{a.get()} / {b.get()} = {d}\n")
    t_resultados.insert(INSERT, f"{a.get()} % {b.get()} = {t}\n")
    t_resultados.insert(INSERT, f"{a.get()} // {b.get()} = {mod}\n")
    t_resultados.insert(INSERT, f"{a.get()} ** {b.get()} = {p}\n")

def borrar():
    messagebox.showinfo("MINICALCULADORA", "Los datos serán borrados")
    a.set("")
    b.set("")
    t_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("MINICALCULADORA", "La app se cerrará")
    ventana_principal.destroy()

# =============================
# ventana principal
# =============================

# se declara una variable llamada ventana_principal que adquiere las caracteristicas de un objeto Tk()

ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas Uis Socorro")

# tamaño de la ventana
ventana_principal.geometry("500x450")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg="gray", width=480, height=250)

a = StringVar()
b = StringVar()

# ====================================
# frame entrada datos
# ====================================

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10,y=200)

bt_calcular=Button(frame_operaciones, text="CALCULAR", command=calcular)
bt_calcular.place(x=45, y=35)

bt_borrar=Button(frame_operaciones, text="BORRAR", command=borrar)
bt_borrar.place(x=200, y=35)

bt_salir=Button(frame_operaciones, text="SALIR", command=salir)
bt_salir.place(x=360, y=35)

frame_operaciones_2 = Frame(ventana_principal)
frame_operaciones_2.config(bg="white", width=480, height=180)
frame_operaciones_2.place(x=10,y=10)
logo = PhotoImage(file= "img/logo.png")
lb_logo = Label(frame_operaciones_2, image=logo, bg= "white")
lb_logo.place (x=11, y=40)

lb_titulo = Label(frame_operaciones_2, text="MINICALCULADORA")
lb_titulo.config(bg="white", fg="green", font=("gabriola", 20))
lb_titulo.place(x=275, y=30)

lb_a =Label(frame_operaciones_2, text="A : ")
lb_a.config(bg="white", fg="green", font=("courier", 20))
lb_a.place(x=255, y=80)

entry_a = Entry(frame_operaciones_2, textvariable=a)
entry_a.config(bg="white", fg="green", font=("courier", 20))
entry_a.focus_set()
entry_a.place(x=305, y=82)

lb_b =Label(frame_operaciones_2, text="B : ")
lb_b.config(bg="white", fg="green", font=("courier", 20))
lb_b.place(x=255, y=120)

entry_b = Entry(frame_operaciones_2, textvariable=b)
entry_b.config(bg="white", fg="green", font=("courier", 20))
entry_b.place(x=305, y=122)
# ====================================
# frame resultados
# ====================================

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=130)
frame_resultados.place(x=10,y=310)

t_resultados=Text(frame_resultados)
t_resultados.config(bg="white", fg="green",font=("gabriola, 20"))
t_resultados.place(x=10, y=10, width=460, height=110)

# run
# se ejecuta la funcion (metodo) mainloop() de la clase Tk a traves de la instancia ventana_principal, 
# este metodo despliega una ventana siemple en la pantalla y queda a la espera de lo que el usuario haga
# cada accion del usuario se conoce como evento. El metodo mainloop() es un bucle "infinito"

ventana_principal.mainloop()
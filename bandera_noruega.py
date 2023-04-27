# se importa la libreria tkinter con todas sus fuciones

from tkinter import *

# =============================
# funciones de la app
# =============================

# =============================
# ventana principal
# =============================

# se declara una variable llamada ventana_principal que adquiere las caracteristicas de un objeto Tk()

ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas Uis Socorro")

# tamaño de la ventana
ventana_principal.geometry("800x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg="red")

# ====================================
# frame entrada datos
# ====================================

frame_operaciones_1 = Frame(ventana_principal)
frame_operaciones_1.config(bg="white", width=800, height=40)
frame_operaciones_1.place(x=0,y=160)

# ====================================
# frame resultados
# ====================================

frame_resultados_1 = Frame(ventana_principal)
frame_resultados_1.config(bg="blue", width=800, height=80)
frame_resultados_1.place(x=0,y=200)

frame_resultados_2 = Frame(ventana_principal)
frame_resultados_2.config(bg="white", width=800, height=40)
frame_resultados_2.place(x=0,y=280)

frame_resultados_3 = Frame(ventana_principal)
frame_resultados_3.config(bg="white", width=40, height=800)
frame_resultados_3.place(x=200,y=280)

frame_resultados_4 = Frame(ventana_principal)
frame_resultados_4.config(bg="blue", width=80, height=800)
frame_resultados_4.place(x=240,y=200)

frame_resultados_5 = Frame(ventana_principal)
frame_resultados_5.config(bg="white", width=40, height=800)
frame_resultados_5.place(x=320,y=280)

frame_resultados_6 = Frame(ventana_principal)
frame_resultados_6.config(bg="white", width=40, height=200)
frame_resultados_6.place(x=320,y=0)

frame_resultados_7 = Frame(ventana_principal)
frame_resultados_7.config(bg="blue", width=80, height=300)
frame_resultados_7.place(x=240,y=0)

frame_resultados_8 = Frame(ventana_principal)
frame_resultados_8.config(bg="white", width=40, height=200)
frame_resultados_8.place(x=200,y=0)
# run
# se ejecuta la funcion (metodo) mainloop() de la clase Tk a traves de la instancia ventana_principal, 
# este metodo despliega una ventana siemple en la pantalla y queda a la espera de lo que el usuario haga
# cada accion del usuario se conoce como evento. El metodo mainloop() es un bucle "infinito"

ventana_principal.mainloop()
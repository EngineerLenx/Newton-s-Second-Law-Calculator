from tkinter import *
from tkinter import ttk
#Ventana
root = Tk()
root.title("Calculadora Segunda Ley de Newton")
root.geometry("400x300")
root.config(bg = "dark gray")
root.resizable(0, 0)
root.iconphoto(False, PhotoImage(file='C:/Users/luern/Downloads/1024Ton618.png'))

#Entrada de datos (masa, aceleración, fuerza)
ent_fuerza = ttk.Entry(root, width= 11)
ent_fuerza.place(x = 80, y = 100)
ent_masa = ttk.Entry(root, width= 11)
ent_masa.place(x = 80, y = 150)
ent_aceleracion = ttk.Entry(root, width= 11)
ent_aceleracion.place(x = 80, y = 200)

#Funcion decisivo
def Calw():
    opc = ComboIn.get()
    if opc == "Fuerza":
        c_fuerza()
    if opc == "Masa":
        c_masa()
    if opc == "Aceleración":
        c_aceleracion()

#Funciones del calculo
def c_fuerza():
    ent_fuerza.insert(0, "x")
    try:
        masa = ent_masa.get()
        masa = float(masa)
        aceleracion = ent_aceleracion.get()
        aceleracion = float(aceleracion)
        fuerza = masa*aceleracion
        ley_resultado.config(text = '{:.5}'.format(fuerza))
        ley_uni_resultado.config(text = "N")
    except ValueError:
        pass

def c_masa():
    try:
        fuerza = ent_fuerza.get()
        fuerza = float(fuerza)
        aceleracion = ent_aceleracion.get()
        aceleracion = float(aceleracion)
        masa = fuerza / aceleracion
        ley_resultado.config(text = '{:.5}'.format(masa))
        ley_uni_resultado.config(text = "Kg")
    except ValueError:
        pass
    
def c_aceleracion():
    try:
        fuerza = ent_fuerza.get()
        fuerza = float(fuerza)
        masa = ent_masa.get()
        masa = float(masa)
        aceleracion = fuerza / masa
        ley_resultado.config(text = '{:.5}'.format(aceleracion))
        ley_uni_resultado.config(text = "m/s^2")
    except ValueError:
        pass

#Funcion para eliminar datos
def clean_all():
    ent_masa.delete(0, END)
    ent_masa.insert(0, " ")
    ent_aceleracion.delete(0, END)
    ent_aceleracion.insert(0, " ")
    ent_fuerza.delete(0, END)
    ent_fuerza.insert(0, " ")
    ley_resultado.config(text = "")
    ley_uni_resultado.config(text = "")

#Label del Título
titulo = Label(root, text = "SEGUNDA LEY DE NEWTON")
titulo.config(bg = "dark gray", font = ("consolas", 22))
titulo.place(x = 30)

#Label de fuerza, masa, aceleracion
lbl_fuerza = Label(root, text = "Fuerza", bg = "dark gray").place(x = 22.5, y = 100)
lbl_masa = Label(root, text = "Masa", bg = "dark gray").place(x = 25, y = 150)
lbl_aceleracion = Label(root, text = "Aceleracion", bg = "dark gray").place(x = 10, y = 200 )

#Label de las unidades
lbl_ufuerza = Label(root, text = "N", bg = "dark gray").place(x = 145, y = 100)
lbl_umasa = Label(root, text = "Kg", bg = "dark gray").place(x = 145, y = 150)
lbl_uaceleracion = Label(root, text = "m/s^2", bg = "dark gray").place(x = 145, y = 200)

#Label de Salida (muestra el resultado)
ley_resultado = ttk.Label(root, text = "", width = 10)
ley_resultado.place(x = 220, y = 150)

#Label unidad del resultado
ley_uni_resultado = ttk.Label(root, text = "", width = 6)
ley_uni_resultado.place(x = 270, y = 150)

#Label indicador del resultado
ind_re = Label(root, text = "Resultado:", bg = "dark gray")
ind_re.place(x = 220, y = 120)

#Combobox que contiene lo que se quiere calcular
ComboIn = ttk.Combobox(root, width= 10, state = "readonly")
ComboIn.place(x = 60 , y = 45)
ComboIn["values"] = ("Fuerza", "Masa", "Aceleración")
ComboIn.current(0)

#Botón del cálculo
button = ttk.Button(root, text = "Calcular", command = Calw, width=10)
button.place(x = 220, y = 220)

#Botón de borrado
clean = ttk.Button(root, text="Borrar", command = clean_all, width = 7)
clean.place(x = 320, y = 220)

#Ejecución de la ventana, siempre al final del código.
root.mainloop()
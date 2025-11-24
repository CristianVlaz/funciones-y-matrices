import tkinter as tk
from tkinter import ttk 

from negocio.negocio_pacientes import obtener_pacientes_para_gui

def funcion_boton_listar():
   
    print("\n¡Botón 'Listar Pacientes' presionado!")

    # 1. Limpiamos la tabla (por si tenía datos de antes)
    for i in tree_pacientes.get_children():
        tree_pacientes.delete(i)

    # 2. Obtenemos los datos del "cerebro"
    lista_pacientes = obtener_pacientes_para_gui()

    # 3. Insertamos los datos en la tabla (Treeview)
    if lista_pacientes:
        for p in lista_pacientes:
            tree_pacientes.insert(
                "", 
                "end", 
                text=p.id, 
                values=(p.rut_paciente, p.nombre_paciente, p.telefono) 
            )
    else:
        print("No se encontraron pacientes (revisa la terminal).")


# ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión Hospital (G4)")
ventana.geometry("700x500") # La hicimos más grande

# --- 4. Creación del Frame de Controles (Botones y Etiquetas)

# Un frame para los controles
frame_controles = ttk.Frame(ventana, padding="10")
frame_controles.pack(side='top', fill='x') # Se pega arriba

# Etiqueta
etiqueta_titulo = ttk.Label(frame_controles, text="Gestión de Pacientes", font=("Helvetica", 16))
etiqueta_titulo.pack(side='left', padx=10)

# Botón
boton_listar = ttk.Button(
    frame_controles, 
    text="Actualizar Lista de Pacientes",
    command=funcion_boton_listar
)
boton_listar.pack(side='right', padx=10)

# --- 5. Creación del Frame de la Tabla de Pacientes 

# Un frame para la tabla
frame_tabla = ttk.Frame(ventana, padding="10")
frame_tabla.pack(side='bottom', fill='both', expand=True)

# Creamos la tabla (Treeview)
tree_pacientes = ttk.Treeview(
    frame_tabla, 
    columns=("RUT", "Nombre", "Teléfono"),
    show='headings' # Oculta la columna de IDs automáticos
)

# Definimos las cabeceras
tree_pacientes.heading("RUT", text="RUT del Paciente")
tree_pacientes.heading("Nombre", text="Nombre Completo")
tree_pacientes.heading("Teléfono", text="Teléfono")

# Definimos el ancho de las columnas
tree_pacientes.column("RUT", width=100)
tree_pacientes.column("Nombre", width=250)
tree_pacientes.column("Teléfono", width=100)

tree_pacientes.pack(fill='both', expand=True) # Dibuja la tabla

# --- 6. Iniciar el bucle de la aplicación ---
ventana.mainloop()

#Este es el comienzo de la interfaz grafica que se trabajará más adelante. Contiene una ventana principal con un botón para listar pacientes y una tabla para mostrar los datos de los pacientes obtenidos desde la capa de negocio.
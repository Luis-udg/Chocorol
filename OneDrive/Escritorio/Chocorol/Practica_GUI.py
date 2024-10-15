import tkinter as tk
from tkinter import filedialog, messagebox
import re

def create_gui():
    global text_area
    window = tk.Tk()
    window.title("Decoder")
    window.geometry("700x600")

    boton1 = tk.Button(window, text="Importar archivo", command=import_file)
    boton1.pack(pady=10)

    boton2 = tk.Button(window, text="Decodificar", command=analyze_text)
    boton2.pack(pady=10)

    boton3 = tk.Button(window, text="Guardar archivo", command=save_file)
    boton3.pack(pady=10)

    text_area = tk.Text(window, wrap=tk.WORD, height=20, width=80)
    text_area.pack(pady=10)

    window.mainloop()

def import_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Archivos de texto", "*.txt")],
        title="Selecciona un archivo"
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)
        global current_file
        current_file = file_path

def analyze_text():
    content = text_area.get("1.0", tk.END)
    lines = content.strip().split("\n")
    decoded_lines = []

    for line in lines:
        decoded_line = ensambladorAbinario(line) 
        decoded_lines.append(decoded_line)

    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, "\n".join(decoded_lines))

def ensambladorAbinario(instruccionEnsamblador):
    operaciones={
        'AND'   :'000',
        'OR'    :'001',
        'SUMA'  :'010',
        'RESTA' :'011',
        'RESTA' :'011',
        'MENORQ':'100',
        'LEER'  :'111'
    }
    direccionesMemoria={
        "0":'00000',
        '1':'00001',
        '2':'00010',
        '3':'00011',
        '4':'00100',
        '5':'00101',
        '6':'00110',
        '7':'00111'
    }
    partes=instruccionEnsamblador.split()
    operacion=partes[0]
    opAluBinario=operaciones.get(operacion)
    patron = re.compile(r'\$([0-9]+)')
    resultados = patron.findall(instruccionEnsamblador)
    dirMemoriaB = direccionesMemoria.get(resultados[0])
    if operacion == 'LEER' :
        MC='10'
        dir1Lectura = "00000"
        dir2Lectura = "00010"
    else:
        MC='01'
        dir1Lectura = direccionesMemoria.get(resultados[1])
        dir2Lectura = direccionesMemoria.get(resultados[2])
    
    return MC+dir1Lectura+opAluBinario+dir2Lectura+dirMemoriaB

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")],
        title="Guardar archivo como"
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            content = text_area.get("1.0", tk.END)
            f.write(content.strip())
        messagebox.showinfo("Éxito", "Archivo guardado correctamente.")

create_gui()
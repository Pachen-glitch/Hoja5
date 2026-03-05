from tkinter import *
import simulador 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
"""Simulador de Procesos con Interfaz Gráfica en Tkinter
Jorge Martinez 2026
Hecho en Python 3.10
Este programa simula la ejecución de procesos en un sistema con recursos limitados (RAM y CPU).
Permite configurar el número de procesos, el intervalo de llegada, la capacidad de RAM, el
número de CPUs y las instrucciones por turno. Además, incluye un experimento para analizar el tiempo promedio en función del número de procesos.

se usaron las librerías SimPy para la simulación, NumPy para el cálculo de estadísticas y Matplotlib para la visualización de resultados. La interfaz gráfica se construyó con Tkinter, permitiendo al usuario interactuar fácilmente con el simulador y visualizar los resultados de manera clara.
"""

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Procesos")
        self.geometry("300x300")
        self.bg="#B47E7E"
        self.configure(bg=self.bg)
        #  Labels e Inputs

        Label(self, text="Procesos", bg=self.bg).pack()
        self.entry_procesos = Entry(self)
        self.entry_procesos.insert(0, "50")
        self.entry_procesos.pack()

        Label(self, text="Intervalo", bg=self.bg).pack()
        self.entry_intervalo = Entry(self)
        self.entry_intervalo.insert(0, "10")
        self.entry_intervalo.pack()

        Label(self, text="RAM", bg=self.bg).pack()
        self.entry_ram = Entry(self)
        self.entry_ram.insert(0, "100")
        self.entry_ram.pack()

        Label(self, text="CPUs", bg=self.bg).pack()
        self.entry_cpu = Entry(self)
        self.entry_cpu.insert(0, "1")
        self.entry_cpu.pack()

        Label(self, text="Instrucciones", bg=self.bg).pack()
        self.entry_instrucciones = Entry(self)
        self.entry_instrucciones.insert(0, "3")
        self.entry_instrucciones.pack()

        #  Botón
        Button(self, text="Ejecutar", bg="#8B4513", command=self.ejecutar).pack(pady=5)
        Button(self, text="Ejecutar Experimento", 
       bg="#5A8F7B", 
       command=self.ejecutar_experimento).pack(pady=5)

        #  Resultado
        self.label_resultado = Label(self, text="", bg=self.bg)
        self.label_resultado.pack()
    def ejecutar(self):# ejecuta solo lo que se pide 
        try:
            procesos = int(self.entry_procesos.get())
            intervalo = float(self.entry_intervalo.get())
            ram = int(self.entry_ram.get())
            cpu = int(self.entry_cpu.get())
            instrucciones_por_turno = int(self.entry_instrucciones.get())

            prom, des = simulador.correr_simulacion(
                procesos,
                intervalo,
                ram,
                cpu,
                instrucciones_por_turno
            )

            self.label_resultado.config(
                text=f"Tiempo Promedio: {prom:.2f}\nDesviación: {des:.2f}"
            )

        except Exception as e:
            self.label_resultado.config(text="Error en los datos")
    def ejecutar_experimento(self):# ejecuta con 50,100,150,200 procesos y grafica el resultado
        try:
            intervalo = float(self.entry_intervalo.get())
            ram = int(self.entry_ram.get())
            cpu = int(self.entry_cpu.get())
            procesos = int(self.entry_procesos.get())  
            instrucciones = int(self.entry_instrucciones.get()) #Instrucciones por turno fijo para el experimento   CPU

            cantidades, promedios = simulador.experimento(
                intervalo,
                ram,
                cpu,
                instrucciones
            )

            # Crear nueva ventana
            ventana_grafica = Toplevel(self)
            ventana_grafica.title("Resultados del Experimento")
            ventana_grafica.geometry("600x400")

            fig, ax = plt.subplots()
            ax.plot(cantidades, promedios)
            ax.set_xlabel("Número de procesos")
            ax.set_ylabel("Tiempo promedio")
            ax.set_title("Tiempo promedio vs Procesos")

            canvas = FigureCanvasTkAgg(fig, master=ventana_grafica)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=BOTH, expand=True)

        except Exception as e:
            print(e)
            self.label_resultado.config(text="Error en experimento")
            
a=App()
a.mainloop()

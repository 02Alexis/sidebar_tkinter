import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FormGraphicsDesign():
    def __init__(self, main_panel):
        figure = Figure(figsize=(8, 6), dpi=100)
        ax1 = figure.add_subplot(211)
        ax2 = figure.add_subplot(212)

        figure.subplots_adjust(hspace=0.4)
        self.graphic1(ax1)
        self.graphic2(ax2)

        canvas = FigureCanvasTkAgg(figure, master=main_panel)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def graphic1(self, ax):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]

        ax.bar(x, y, label="Gráfica 1", color="blue", alpha=0.7)

        ax.set_title("Gráfico 1 - Gráfico de barras")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")        
        ax.legend()

        # Añadir etiquetas a cada barra
        for i, v in enumerate(y):
            ax.text(x[i] - 0.1, v + 0.1, str(v), color="black")

        ax.grid(axis='y', linestyle='--', alpha=0.7)   

    def graphic2(self, ax):
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 1, 2, 1]

        ax.plot(x, y, label="Gráfica 2", color="green")

        ax.set_title("Gráfico 2")
        ax.set_xlabel("Eje X", fontsize=12)
        ax.set_ylabel("Eje Y", fontsize=12)        
        ax.plot(x, y, label="Gráfica 2", color="green", linestyle='--', marker='o')
        ax.annotate('Punto importante', xy=(3, 1), xytext=(3.5, 1.5), arrowprops=dict(facecolor='blue', shrink=0.05))
        ax.set_xlim(0, 6) # Establece los límites del eje x
        ax.set_ylim(0, 3) # Establece los límites del eje y
        ax.grid(True, linestyle='--', alpha=0.6)      
        ax.legend()


import tkinter as tk
from tkinter import font
from config import COLOR_HOVER, COLOR_LATERAL_BAR, COLOR_MAIN_BOSY, COLOR_UPPER_BAR
import util.util_window as util_window
import util.util_image as util_image

class FormMasterDesign(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.logo = util_image.read_image("./img/KIRITO.webp", (560, 136))
        self.profile = util_image.read_image("./img/perfil.jpg", (100, 100))
        self.icon = util_image.read_image("./img/profile.jpg", (32, 32)) 
        self.config_window()
        self.panels()

    def config_window(self):
        # configuración inicial de la ventana
        self.title("Sidebar")
        self.iconphoto(True, self.icon)
        w, h = 1024, 600
        self.geometry("%dx%d+0+0" % (w, h))
        util_window.center_window(self, w, h)

    def panels(self):
        # creación paneles barra superiror, menu lateral y cuerpo principal
        self.superior_bar = tk.Frame(
            self, bg=COLOR_UPPER_BAR, height=50
        )
        self.superior_bar.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_LATERAL_BAR, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.principal_body = tk.Frame(
            self, bg=COLOR_MAIN_BOSY
        )
        self.principal_body.pack(side=tk.RIGHT, fill='both', expand=True)

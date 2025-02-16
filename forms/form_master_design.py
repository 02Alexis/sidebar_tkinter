import tkinter as tk
from tkinter import font
from config import COLOR_HOVER, COLOR_LATERAL_BAR, COLOR_MAIN_BOSY, COLOR_UPPER_BAR
import util.util_window as util_window
import util.util_image as util_image

class FormMasterDesign(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.logo = util_image.read_image("./img/KIRITO.webp", (560, 136))
        self.profile = util_image.read_image("./img/logo.png", (100, 100))
        self.icon = util_image.read_image("./img/profile.jpg", (32, 32)) 
        self.config_window()
        self.panels()
        self.upper_bar_controls()
        self.sidebar_controls()

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

    def upper_bar_controls(self):
        #configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12) 
        
        #Etiqueta de titulo
        self.labeltitle = tk.Label(self.superior_bar, text="Alexis")
        self.labeltitle.config(fg="#ffffff", font=(
            "Roboto", 15
        ), bg=COLOR_UPPER_BAR, pady=10, width=16)
        self.labeltitle.pack(side=tk.LEFT)

        #Botón menu lateral
        self.btnmenulateral = tk.Button(self.superior_bar, text="\uf0c9", font=font_awesome,
                                bd=0, bg=COLOR_UPPER_BAR, fg="white")
        self.btnmenulateral.pack(side=tk.LEFT)

        #Etiqueta de información
        self.labeltitle = tk.Label(
            self.superior_bar, text="Dev Full Stack")
        self.labeltitle.config(fg="#ffffff", font=(
            "Roboto", 15
        ), bg=COLOR_UPPER_BAR, padx=10, width=20)
        self.labeltitle.pack(side=tk.RIGHT)

    def sidebar_controls(self):
        # configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family="FontAwesome", size=15)

        # Etiqueta de perfil
        self.labelprofile = tk.Label(
            self.menu_lateral, image=self.profile, bg=COLOR_LATERAL_BAR
        )
        self.labelprofile.pack(side=tk.TOP, pady=10)

        # Botón del menu lateral
        self.btndashbord = tk.Button(self.menu_lateral)
        self.btnprofile = tk.Button(self.menu_lateral)
        self.btnpicture = tk.Button(self.menu_lateral)
        self.btninfo = tk.Button(self.menu_lateral)
        self.btnsettings = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Dashboard", "\uf109", self.btndashbord),
            ("Profile", "\uf007", self.btnprofile),
            ("Picture", "\uf03e", self.btnpicture),
            ("Info", "\uf129", self.btninfo),
            ("Settings", "\uf013", self.btnsettings),
        ]

        for text, icon, button in buttons_info:
            self.config_btn_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)

    def config_btn_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f" {icon}   {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_LATERAL_BAR, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos enter y leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_HOVER, fg="white")

    def on_leave(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_LATERAL_BAR, fg="white")


import tkinter as tk
import util.util_window as util_window
import util.util_image as util_image

class FormInfoDesign(tk.Toplevel):

    def __init__(self) -> None:
        super().__init__()
        self.icon = util_image.read_image("./img/profile.jpg", (32, 32))
        self.config_window()
        self.buildwidgets()

    def config_window(self):
        # Configuración incial de la ventana
        self.title("Sidebar")
        self.iconphoto(True, self.icon)
        w, h = 400, 100
        util_window.center_window(self, w, h)

    def buildwidgets(self):
        self.labelVersion = tk.Label(self, text="Versión: 1.0")
        self.labelVersion.config(fg="#000000", font=(
            "Roboto", 15
        ), pady=10, width=20)
        self.labelVersion.pack()

        self.labelAuthor = tk.Label(self, text="Autor: Alexis Tamayo")
        self.labelAuthor.config(fg="#000000", font=(
            "Roboto", 15
        ), pady=10, width=20)
        self.labelAuthor.pack()
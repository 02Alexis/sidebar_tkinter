import tkinter as tk
import util.util_window as util_window
import util.util_image as util_image
from config import COLOR_MAIN_BOSY

class FormBuildSiteDesign():
    def __init__(self, main_panel, logo):
        self.upper_bar = tk.Frame(main_panel)
        self.upper_bar.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.lower_bar = tk.Frame(main_panel)
        self.lower_bar.pack(side=tk.BOTTOM, fill="both", expand=True)

        self.labelTitle = tk.Label(self.upper_bar, text="Página en Contrucción")
        self.labelTitle.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_MAIN_BOSY)
        self.labelTitle.pack(side=tk.TOP, fill="both", expand=True)

        self.labelimage = tk.Label(self.lower_bar, image=logo)
        self.labelimage.place(x=0, y=0, relwidth=1, relheight=1)
        self.labelimage.config(fg="#fff", font=("Roboto", 10), bg=COLOR_MAIN_BOSY)

def center_window(window, application_width, application_height):
    # Obtener las dimensiones de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Calcular las coordenadas x e y para centrar la ventana
    x = int((screen_width/2) - (application_width /2))
    y = int((screen_height/2) - (application_height /2))
    window.geometry(f"{application_width}x{application_height}+{x}+{y}")
    
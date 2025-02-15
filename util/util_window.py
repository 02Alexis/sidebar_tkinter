def center_window(window, application_width, application_long):
    window_width = window.winfo_screenwidth()
    window_long = window.winfo_screenheight()
    x = int((window_width/2) - (window_long/2))
    y = int((window_long/2) - (window_width/2))
    return window.geometry(f"{application_width}x{application_long+{x}+{y}}")
    
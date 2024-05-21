from tkinter import *
import os
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("Shutdown App")
st.geometry("450x450")
st.config(bg="#30D5C8")

# Define styles
button_style = {
    "font": ("Arial", 12),
    "relief": RAISED,
    "bg": "#FF5733",
    "fg": "white",
    "activebackground": "#45a049",
    "activeforeground": "white",
    "cursor": "hand2"
}

restart_button = Button(st, text="Restart", **button_style, command=restart)
restart_button.place(relx=0.5, rely=0.2, anchor=CENTER, width=120, height=40)

restart_time_button = Button(st, text="Restart in 20s", **button_style, command=restart_time)
restart_time_button.place(relx=0.5, rely=0.4, anchor=CENTER, width=120, height=40)

logout_button = Button(st, text="Log Out", **button_style, command=logout)
logout_button.place(relx=0.5, rely=0.6, anchor=CENTER, width=120, height=40)

shutdown_button = Button(st, text="Shut Down", **button_style, command=shutdown)
shutdown_button.place(relx=0.5, rely=0.8, anchor=CENTER, width=120, height=40)

st.mainloop()

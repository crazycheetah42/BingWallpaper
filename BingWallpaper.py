# Author of Bing Wallpaper backend: Maximilian Muth <mail@maxi-muth.de>
# Author of GUI: crazycheetah42 (https://github.com/crazycheetah42)
# Original source for Windows and Linux can be found here: https://github.com/mammuth/bing-wallpaper
# Description: Downloads the Bing picture of the Day and sets it as wallpaper (Windows). Comes with a nice GUI.

import tkinter as tk
from tkinter import ttk, messagebox
import bw
from pathlib import Path
import os, shutil
import win32com.client

# Here is where the GUI coding starts

root = tk.Tk()
root.geometry("500x350")
root.wm_title("Bing Wallpaper")
root.iconbitmap("icon.ico")

app_heading = ttk.Label(root, text="Bing Wallpaper", font=("Segoe UI", 30))
app_heading.pack()

space_lbl = ttk.Label(root, text="", font=("Segoe UI", 5))
space_lbl.pack()

welcome_text = ttk.Label(root, text="Welcome to Bing Wallpaper! In this app you can get the latest daily wallpaper from Bing, and tweak some settings.", wraplength=500, font=("Segoe UI", 12))
welcome_text.pack()

space_lbl = ttk.Label(root, text="", font=("Segoe UI", 5))
space_lbl.pack()

set_wall_btn = ttk.Button(root, text="Download and Set Wallpaper", command=bw.download_wallpaper)
set_wall_btn.pack()

space_lbl = ttk.Label(root, text="", font=("Segoe UI", 10))
space_lbl.pack()

settings_header = ttk.Label(root, text="Settings", font=("Segoe UI", 25))
settings_header.pack()


link = ttk.Label(root, text="Click here to find out how to make this program automatically run daily", foreground="blue", cursor="hand2")
link.pack(pady=20)

def open_docs(event):
    import webbrowser
    webbrowser.open("https://github.com/crazycheetah42/BingWallpaper/blob/main/README.md#run-daily")
link.bind("<Button-1>", open_docs)

if __name__ == "__main__":
    root.mainloop()

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


# Function to get the path to the Startup folder
def get_startup_folder():
    """Returns the path to the Windows Startup folder for the current user."""
    return Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"

# Function to create a shortcut in the Startup folder
def create_startup_shortcut():
    """Creates a shortcut in the Windows Startup folder pointing to setwall.exe."""
    user_directory = os.environ['USERPROFILE']
    print(user_directory)
    exe_path = Path(__file__).parent / f"{user_directory}\AppData\Local\Programs\BingWallpaper\setwall.exe"  # Path to the executable
    startup_folder = get_startup_folder()
    shortcut_path = startup_folder / "BingWallpaper.lnk"    # Shortcut path

    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(str(shortcut_path))
        shortcut.TargetPath = str(exe_path)                 # Set target to setwall.exe
        shortcut.WorkingDirectory = str(exe_path.parent)    # Set working directory
        shortcut.Save()
    except Exception as e:
        messagebox.showerror("Failed to create shortcut", "Bing Wallpaper was unable to create a startup entry")

# Function to remove the shortcut from the Startup folder
def remove_startup_shortcut():
    """Removes the BingWallpaper shortcut from the Windows Startup folder."""
    shortcut_path = get_startup_folder() / "BingWallpaper.lnk"
    try:
        if shortcut_path.exists():
            shortcut_path.unlink()
        else:
            print("")
    except Exception as e:
        messagebox.showerror("Failed to remove shortcut", "Bing Wallpaper was unable to remove the startup entry. The file resides in the shell:startup folder.")

# Function to toggle the Run on Startup setting
def toggle_startup():
    if startup_checked.get():
        create_startup_shortcut()
    else:
        remove_startup_shortcut()

# Initialize the Run on Startup checkbox
startup_checked = tk.BooleanVar()
# Check if the shortcut already exists in the Startup folder
startup_checked.set((get_startup_folder() / "BingWallpaper.lnk").exists())

run_on_startup = ttk.Checkbutton(root, text="Run on startup", 
                                 variable=startup_checked, 
                                 command=toggle_startup,
                                 width=13)
run_on_startup.pack()


link = ttk.Label(root, text="Click here to find out how to make this program automatically run daily", foreground="blue", cursor="hand2")
link.pack(pady=20)

def open_docs(event):
    import webbrowser
    webbrowser.open("https://github.com/crazycheetah42/BingWallpaper/blob/main/README.md#run-daily")
link.bind("<Button-1>", open_docs)

if __name__ == "__main__":
    root.mainloop()

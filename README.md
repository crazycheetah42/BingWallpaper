# BingWallpaper
BingWallpaper (crazycheetah42) is a GUI wrapper for <a href="https://github.com/mammuth/bing-wallpaper">BingWallpaper (Mammuth)</a> for Windows. Written in Python and tkinter.

# Run Daily
The app can be run daily. All you have to do is create a task in Task Scheduler.
<br>
![image](https://github.com/user-attachments/assets/0111c6c4-b23e-4e30-8af8-a4dc22d74c78)
<br>
Then set these settings in the Trigger tab.
<br>
![image](https://github.com/user-attachments/assets/f3e4802d-696c-4853-86e7-48e3fef8b7b8)
<br>
Then set the app set_wall.exe as the Action in the Action tab. set_wall.exe will be in the folder you extracted this app to. Usually, the path will be "C:\Program Files\BingWallpaper\set_wall.exe". If you used the portable version with the zip, set_wall.exe is in the folder you extracted it to. Change the "Start In" folder to "%USERPROFILE%\Pictures", which will be C:\Users\Your User Name\Pictures (unless you changed it, then make it D:\Pictures for example)
<br>
![image](https://github.com/user-attachments/assets/b6a668ad-41b4-42a7-b6af-a39229a38abd)
<br>
Go to Conditions and uncheck "Start only if computer is on AC power".
Go to Settings and uncheck "Stop the task if it runs longer than 3 days".
Click OK. The Task should be created successfully.

There is a weird bug with PyInstaller, which is the module that compiles my code into an executable. Windows Defender (mostly on Windows 10) will flag it as a virus. However, I can guarantee that it's not a virus (all the code is here), and you just have to allow the file to run.
<br>
# Support me
If you appreciate this project and want to donate, please donate to this venmo account:
<br>
<img src="https://github.com/user-attachments/assets/b7f46d54-715c-49d0-9a90-ee14f5b4271f" height=207 width=207>

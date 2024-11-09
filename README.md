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

In case you get Windows Defender screaming at you about threats in my program, all the source code is available here and it seems to be a consistent issue with pyinstaller. I haven't had this on Windows 11 systems, but more often on Windows 10 systems.

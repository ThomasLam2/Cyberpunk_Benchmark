import os
import subprocess
import time

import vgamepadfunc
from vgamepadfunc import vg
from pywinauto import Application

#Connect gamepad 360
gamepad = vg.VX360Gamepad()
print("360 GAMEPAD IN")
time.sleep(1)

#Open Redlauncher
os.chdir(r'C:\Program Files (x86)\Steam\steamapps\common\Cyberpunk 2077')
subprocess.Popen("REDprelauncher.exe")

time.sleep(3)

#Open Cyberpunk 2077
os.chdir(r'C:\Program Files (x86)\Steam\steamapps\common\Cyberpunk 2077\bin\x64')
subprocess.Popen("Cyberpunk2077.exe") #Open the game


time.sleep(30) #Wait for game to load

subprocess.call(["taskkill","/F","/IM","REDlauncher.exe"])

#Game Should now be ON

#Starting the app
app = Application(backend="uia")
#app.start(r"C:/Program Files/Microsoft Office/root/Office16/EXCEL.exe")
app.connect(path=r"C:\Program Files (x86)\Steam\steamapps\common\Cyberpunk 2077\bin\x64")

#Focus on Window
win = app.window(title_re='.*Cyberpunk2077')


#Skip Intro
vgamepadfunc.pressb()

#Go to Main menue
time.sleep(3)
vgamepadfunc.pressstart()

#Go to Options
time.sleep(2)
vgamepadfunc.pressdown(4)
vgamepadfunc.pressa()

#Go to Graphics
vgamepadfunc.pressrightshoulder(3)

#Start Benchmark
time.sleep(1)
vgamepadfunc.pressx()



#Benchmark Should be Running
time.sleep(110)

#Turn off Application
#print("Shutting off Application ")
subprocess.call(["taskkill","/F","/IM","Cyberpunk2077.exe"])
print("application closed")









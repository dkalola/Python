#--lib import--
import os
from termcolor import colored
import re
from gtts import gTTS
#--local import--
from playsound import playsound
from pyfiles import CMDS
from pyfiles import GRAPHICS as gp



path_27="C:/Python27/Scripts"
path_38="C:/Python38/Scripts"
reqdes = "D:/PYTHON/LIB_INSTALL/TXT files"
pyv = 38
pyvpath = f"C:/Python{pyv}/python.exe"


os.system("cd C:/Users/DELL")
os.system('mkdir sounds')
os.system('mkdir pyfiles')
os.system("CLS")
gp.graphics()




while(True):
 
	status = True
	sel = input(colored("$~ ",'red') + colored("PYTHON: ",'green'))
	if(sel == "exit"):
		break
	CMDS.cmds(sel,path_27,path_38,pyvpath)

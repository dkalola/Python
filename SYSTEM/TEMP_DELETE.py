import os, shutil
from win10toast import ToastNotifier 
import psutil
from playsound import playsound
from termcolor import colored

print("Do no close.. ")

n = ToastNotifier() 

folder = 'C:/Users/DELL/AppData/Local/Temp'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(colored('Failed to delete %s. Reason: %s' % (file_path, e),'red'))

folder2 = 'C:/Windows/Temp'
for filename in os.listdir(folder2):
    file_path = os.path.join(folder2, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(colored('Failed to delete %s. Reason: %s' % (file_path, e),'red'))

n.show_toast("SYSTEM", "Successfully Cleaned Temp Folders", duration = 5) 
n.show_toast("SYSTEM", f"CPU Usage {psutil.cpu_percent()}", duration = 5)
n.show_toast("SYSTEM", f"RAM Usage {psutil.virtual_memory()[2]}", duration = 5)



playsound('D:/PYTHON/SOUNDS/dont-think-so.mp3')

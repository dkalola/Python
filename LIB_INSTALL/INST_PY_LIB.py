import os
from termcolor import colored

def graphics():
	print(colored(
	'''
	 _         _ _ _ _ _     _ _ _                _ _ _ _ _    _ _     __     _ _ _ _     _ _ _ _ _
	| |       |_ _   _ _|  | _ _ _''             |_ _   _ _|  |   \   |  |   /       |   |_ _   _ _|
	| |           | |      | |    \ \                | |      |    \  |  |   |   ----        | |
	| |           | |      | |_ _ / /     _ _        | |      |     \ |  |   \    \          | |
	| |           | |      | |_ _ :      |_ _|       | |      |  |\  \|  |    \    \         | |
	| |           | |      | |    \ \                | |      |  | \     |     \    \        | |
	| |_ _ _   _ _| |_ _   | |_ _ / /             _ _| |_ _   |  |  \    |    ----   |       | |
	| _ _ _ | |_ _ _ _ _|  | _ _ _''             |_ _ _ _ _|  |__|   \_ _|   |_ _ _  /       |_|
	''','cyan'))

#-----------------------------------------------------------
def install():
	ans = input(colored("To install for both versions type(b) else(n): ",'green'))
	if(str(ans) == 'b'):
		name = input(colored("Enter the name of Lib: ",'green'))
		os.system("cd "+path_27)
		print ("installing for Python27 "+name)
		os.system("pip install "+name)
		os.system("cd "+path_38)
		print()
		print ("installing for Python38 "+name)
		os.system("pip install "+name)
		
	else:	
		a = input(colored("Enter the Python version(27 or 38): ",'green'))
		if(int(a) == 27):
			os.system("cd "+path_27)
			name = input(colored("Enter the name of Lib: ",'green'))
			print ("installing "+name)
			os.system("pip install "+name,'yellow')
			


		if(int(a) == 38):
			os.system("cd "+path_38)
			name = input(colored("Enter the name of Lib: ",'green'))
			print ("installing "+name)
			os.system("pip install "+name,'yellow')

	os.system('pip freeze > Requirements.txt')
	print('Updated the Requirements file')
	os.system("pause")	

def installtxt(string):
	ans = input(colored("To install in both versions type(b) else(n): ",'green'))
	if(str(ans) == 'b'):
		os.system("cd "+path_27)
		print ("installing for Python27 from "+string)
		os.system("pip install -r "+string,'yellow')
		os.system("cd "+path_38)
		print ("installing from "+string)
		os.system("pip install -r "+string,'yellow')
		os.system("pause")
	else:
		a = input(colored("Enter the Python version(27 or 38): ",'green'))
		if(int(a) == 27):
			os.system("cd "+path_27)
			print ("installing from "+string)
			os.system("pip install -r "+string,'yellow')
			os.system("pause")


		if(int(a) == 38):
			os.system("cd "+path_38)
			print ("installing from "+str)
			os.system("pip install -r "+str,'yellow')
			os.system("pause")
#-----------------------------------------------------------


path_27="C:/Python27/Scripts"
path_38="C:/Python38/Scripts"

os.system("cd C:/Users/DELL")



while(True):
	os.system("cls")
	graphics()
	path = "D:/PYTHON/LIB_INSTALL/TXT files"
	status = False
	  
	# Getting the list of directories 
	dir = os.listdir(path) 


	# Checking if the list is empty or not 
	if len(dir) == 0: 
	    status = False 
	    install()
	else: 
		status = True
		sel = input(colored("Would you like to install files(I) or update Requirements file(R)?: ",'green'))

		if(sel.lower() == "r"):
			os.system('pip freeze > Requirements.txt')
			print(colored('Updated the Requirements file','magenta'))
			f = open("Requirements.txt", "r")
			print()
			print(colored(f.read(), 'magenta'))
			os.system("pause")
		if(sel.lower() == "i"):
			install()


		
	






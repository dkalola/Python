import os

#-----------------------------------------------------------
def install():
	ans = input("To install for both versions type(b) else(n): ")
	if(str(ans) == 'b'):
		name = input("Enter the name of Lib: ")
		os.system("cd "+path_27)
		print ("installing for Python27 "+name)
		os.system("pip install "+name)
		os.system("cd "+path_38)
		print()
		print ("installing for Python38 "+name)
		os.system("pip install "+name)
		
	else:	
		a = input("Enter the Python version(27 or 38): ")
		if(int(a) == 27):
			os.system("cd "+path_27)
			name = input("Enter the name of Lib: ")
			print ("installing "+name)
			os.system("pip install "+name)
			


		if(int(a) == 38):
			os.system("cd "+path_38)
			name = input("Enter the name of Lib: ")
			print ("installing "+name)
			os.system("pip install "+name)

	os.system('pip freeze > Requirements.txt')
	print('Updated the Requirements file')
	os.system("pause")	

def installtxt(string):
	ans = input("To install in both versions type(b) else(n): ")
	if(str(ans) == 'b'):
		os.system("cd "+path_27)
		print ("installing for Python27 from "+string)
		os.system("pip install -r "+string)
		os.system("cd "+path_38)
		print ("installing from "+string)
		os.system("pip install -r "+string)
		os.system("pause")
	else:
		a = input("Enter the Python version(27 or 38): ")
		if(int(a) == 27):
			os.system("cd "+path_27)
			print ("installing from "+string)
			os.system("pip install -r "+string)
			os.system("pause")


		if(int(a) == 38):
			os.system("cd "+path_38)
			print ("installing from "+str)
			os.system("pip install -r "+str)
			os.system("pause")
#-----------------------------------------------------------


path_27="C:/Python27/Scripts"
path_38="C:/Python38/Scripts"

os.system("cd C:/Users/DELL")



while(True):
	os.system("cls")
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
		sel = 'n' #input("Would you like to install from the txt files?(Y/N): ")

		if(sel.lower() == "y"):
			print("Here's what we found: ")
			for i in range(0,len(dir)):
				print(str(i)+" = "+dir[i])
			ans = input("Select the txt file by the indicted number: ")
			file = dir[int(ans)]
			installtxt(file)
		if(sel.lower() == "n"):
			install()


		
	






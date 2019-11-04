#Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory. 
import os
#Your program will prompt the user for the directory they would like to save the file in as well as the name of the file. 
print("Welcome. This is your address book program.")
flag1=0
while flag1 ==0:  
	directoryName=input ("Please enter the directory name you would like to use:")
	print("Please wait while directory is being validated....")
	if os.path.isdir(directoryName): #will check for directory existence and will respond accordingly
		flag1=1
		print('Directory' + directoryName + 'exists')
	else:
		flag1=0
		print("This directory does not exist. Please enter a new directory name.")
#prompt the user for their name, address, and phone number
fileName= input("Please enter the file name you would like to use in a .txt file format.")
entryName=input("Please enter the person's name:")
entryAddress=input("Please ennter their address:")
entryPhone=input("Please enter their phone number:")
#Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user. 
try:
	print("Please wait while file is being written....")
	with open(fileName, 'w') as fileHandle:
		fileHandle.write(entryName + "," + entryAddress + "," + entryPhone)
		print("Your file" + fileName + "was created.")
except:
	print("There was an error when trying to save.")
#Once the data has been written your program should read the file you just wrote to the file system and display the file contents to the user for validation purposes.
try:
	print("Please wait while file is read....") 
	with open(fileName, 'r') as fileHandle:
		fileData= fileHandle.readline()
		print(fileData)
except:
	print("There was an error.")

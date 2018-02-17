#A simple python program to list all content of a Directory
import os
print('********************** Designed By Techie vivek ***************************************')
print('\n')
path=input('----------> Please Enter the Full path of Directory/Folder you are looking for <--------------------------')
os.chdir(path)
for foldername,subfolders,filenames in os.walk(os.getcwd()):
    print('This is where we are ********'+os.path.basename(foldername).upper()+'**********')
    print('*******************************************************************************************')
    print('Sub-Folders inside %s is :'%(os.path.basename(foldername)))
    for folder in subfolders:
        print(folder)
    print('Files inside %s is :' %(os.path.basename(foldername)))
    for file in filenames:
        print(file)

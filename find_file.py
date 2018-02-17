import os,subprocess
print('*******************************Designed By Techie Vivek*****************************8')
path=input('Enter the Full path of Directory or Folder you are looking for')
file=input('Enter the Filename you are looking for')
os.chdir(path)
for foldername,subfolder,filename in os.walk(os.getcwd()):
    for files in filename:
        if(files==file):
            filepath=os.path.join(foldername,files)
            print('Found Files with Matching Names %s'%filepath)
            os.chdir(os.path.dirname(filepath))
            subprocess.Popen(['start',file],shell=True)



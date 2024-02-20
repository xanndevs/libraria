import os

#This line ensures that we are running the script in the correct directory so the relative path definition doesn't go wrong 
os.chdir("\\".join(os.path.realpath(__file__).split("\\")[:-1]))

#Installs the required packages
os.system("pip install -r ./requirements.txt")
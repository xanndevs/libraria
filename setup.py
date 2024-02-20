from os import chdir, system, path

#This line ensures that we are running the script in the correct directory so the relative path definition doesn't go wrong 
chdir("\\".join(path.realpath(__file__).split("\\")[:-1]))

#Installs the required packages
system("pip install -r ./requirements.txt")
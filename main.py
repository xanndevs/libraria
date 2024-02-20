import os

#This line ensures that we are running the script in the correct directory so the relative path definition doesn't go wrong 
os.chdir("\\".join(os.path.realpath(__file__).split("\\")[:-1]))

#I am too lazy to actually create a main.py so I am going to use the test script and get away with it :D
os.system("py -m libraria.tests.test_libraria")

from os import chdir, system, path

#This line ensures that we are running the script in the correct directory so the relative path definition doesn't go wrong 
chdir("\\".join(path.realpath(__file__).split("\\")[:-1]))

#I am too lazy to actually create a main.py so I am going to use the test script and get away with it :D
system("py -m libraria.tests.test_libraria")

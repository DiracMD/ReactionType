import numpy as np 
import matplotlib.pyplot as plt
import os


with open("bonds.reaxc.reaction") as data:
    new = []
    for line in data:
        nline = str(line.split()[0])
        sline = line.split()[1].split("->")
        if sline[0] == "[H]C([H])=C([H])[H]":
            #reactantname = "C2H4R" + ".txt"
            #os.mknod('/mnt/e/sub/decane/dodecane/3750/ff08/2400K/reactype/' + reactantname)
            f = open("C2H4R.txt","w")
            print(line,file=f)
        #if sline[1] == "[H]C([H])=C([H])[H]" :
        #   print(line, file=.txt)

        


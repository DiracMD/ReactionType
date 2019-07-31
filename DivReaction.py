""" initial import the reference modules and library """
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

import os

"""define the molecule to research"""
molecule = "C2H4"
reactantname = "C2H4" + "R.csv"                                                    
# e.g.[H]C[H]=C([H])[H].
os.mknod('/mnt/e/sub/decane/dodecane/3750/ff08/2400K/reactype/' + reactantname)
productname = "C2H4" + "P.csv" 
os.mknod('/mnt/e/sub/decane/dodecane/3750/ff08/2400K/reactype/' + productname)
# e.g.[H]C[H]=C([H])[H].

""" read the reaction file """
with open("bonds.reaxc.reaction") as data:
    new = [] 
    for line in data:
        nline = str(line.split()[0])
        sline = line.split()[1].split("->")
        sline.insert(0, nline)
        new.append(sline)
    reactions = new
    for reaction in reactions:
        f1 = open(reactantname, "a")
        f2 = open(productname, "a")
        if reaction[1] == "[H]C([H])=C([H])[H]":
            print(reaction[0] + "," + reaction[1] + "," + reaction[2], file = f1)
        if reaction[2] == "[H]C([H])=C([H])[H]":
            print(reaction[0] + "," + reaction[1] + "," + reaction[2], file = f2)

    

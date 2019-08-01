""" initial import the reference modules and library """
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import openbabel
import rdkit 
import os

product = pd.read_csv("./C2H4P.csv", header=None)
reactant = pd.read_csv("./C2H4R.csv", header=None)

for j in range(len(reactant)):
    for i in range(len(product)):
        if reactant[2][j] == product[1][i]:
            print(str(reactant[0][j])+","+str(reactant[2][j])+"->"+str(reactant[2][j])
            +"   "+ str(product[0][i])+" "+str(product[1][i])+"->"+str(product[2][i]))

#for x in range(0,20):
    #z=df[0][x]
    #y.append(z)
"""
plt.bar(x, height = y, width=0.8)
plt.show()
"""
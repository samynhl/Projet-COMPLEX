import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

M = np.array([[0,1,1,0,0,0],
             [1,0,0,1,1,0],
             [1,0,0,1,0,0],
             [0,1,1,0,1,0],
             [0,1,0,1,0,1],
             [0,0,0,0,1,0],
             [0,0,0,0,0,0]])

print(M.shape)
index = np.random.choice(M.shape[0], 1) 
print(index)

# Rajouter une ligne de fustion
# Tirage de l'arête aléatoire
# Fusion en temps lineaire et selectione en temps lineaire


# Sélection aléatoire d'une arête parmi m arêtes

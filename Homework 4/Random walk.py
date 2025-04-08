import random
import matplotlib.pyplot as plt

def randomwalk(n):
    x = 0
    start = x
    xposition = [start]
    probabilities = [-1, 1]
    for i in range(1, n + 1):
        x += random.choice(probabilities)
        xposition.append(x)
    
    return xposition

print(randomwalk(1000))

    
    
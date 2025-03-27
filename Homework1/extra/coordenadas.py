#Converter coodenadas cartesianas para polares
import numpy as np

r = (x, y)

def cartesianas_para_polares(r):
  rho = np.sqrt(x**2 + y**2)
  phi = np.arctan2(x, y)
  return (rho, phi)

cartesianas_para_polares (r)
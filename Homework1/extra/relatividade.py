#Tempo que a espaçonave leva para chegar na terra em m/s

import numpy as np

def spacecraft_time(space, velocity):
    c = 299792458
    lorentz_factor = np.sqrt(1 - (velocity**2/c**2))

    time_1 = space/velocity*lorentz_factor
    return time_1


space = 400000000
velocity = 269000000
time = spacecraft_time(space, velocity)
print(time)
import matplotlib.pyplot as plt

import numpy as np


Ts = 30;   # signal interval

end = 150; # signal end point

n = 11


x = np.linspace(-end , end, num=n) # signal vector


# TODO: revise this array to your results
print(x)
y = np.array([-10.204 , -11.081, -11.958, -10.364, -5.899, 0.000, 5.899, 9.885, 11.560, 13.553, 11.958]) # speed vector
## y = np.array([10.204,11.081,11.958,10.364,5.899,0.000, 5.899, 9.885, 11.560, 13.553, 11.958]) # speed vector


z = np.polyfit(x, y, 2) # Least squares polynomial fit, and return the coefficients.


goal = -10.204             # if we want to let the servo run at 7 cm/sec

                     # equation : z[0]*x^2 + z[1]*x + z[2] = goal

z[2] -= goal         # z[0]*x^2 + z[1]*x + z[2] - goal = 0


result = np.roots(z) # Return the roots of a polynomial with coefficients given


# output the correct one

if (0 <= result[0]) and (result[0] <= end):

    print(result[0])

else:

    print(result[1])
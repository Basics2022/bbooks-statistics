"""


With X,Z i.i.d, X,Y have correlation corr_XY,

  Y = corr_XY * X + ( 1 - corr_XY**2 )**.5 * Z


2025-06-10

"""

import numpy as np
import matplotlib.pyplot as plt

#> Seed for random number generator
np.random.seed(1234)

#> Params of the script
rng_label = 'Normal'      #
rng_params = { 'mu': 0., 'sigma': 1., 'nt': 1000 }
corr_XY = .7


#> List of random number generators: functions and parameters
rgen_list = {
    'Bernoulli': { 'generator': np.random.default_rng().choice, 'params': {}, \
                   'write_params': lambda mu, sigma, nt: {'a':[mu-sigma, mu+sigma], 'p':[.5, .5], 'size': nt}  },
    'Normal':    { 'generator': np.random.default_rng().normal, 'params': {}, \
                   'write_params': lambda mu, sigma, nt: {'loc': mu, 'scale': sigma, 'size': nt}  }
}

rgen = rgen_list[rng_label]  #> Choose random number generator


#> Build correlated random variables
#> X,Z i.i.d
X = rgen['generator']( **rgen['write_params'](**rng_params) )
Z = rgen['generator']( **rgen['write_params'](**rng_params) )

Y = corr_XY * X + ( 1. - corr_XY**2 )**.5 * Z


#> Sampling
n_samples_v = [ 25, 50, 100 ]

data = { 
    'X': {}
    'Y': {}
}

    



#> Plot random numbers
fig, ax = plt.subplots(1,1, figsize=(5,5))
ax.plot(X,Y, 'o')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid()








plt.show()

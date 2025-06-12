#> Import libraries

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

# Parameters
#> Time
Tfin = 1000.                              # final time
dt   = 1                                  # reference dt

#> Random number generators of increments, with different probability density
rgen_list = {
    'Bernoulli': { 'generator': np.random.default_rng().choice, 'params': {}, \
      'write_params': lambda mu, sigma, nt: {'a':[mu-sigma, mu+sigma], 'p':[.5, .5], 'size': nt}  },
    'Normal':    { 'generator': np.random.default_rng().normal, 'params': {}, \
      'write_params': lambda mu, sigma, nt: {'loc': mu, 'scale': sigma, 'size': nt}  }
}

#> Select normal distribution for increments
rgen = rgen_list['Normal']

#> N. realizations
n_realizations = 1000

#> Colors for plot
colors = cm.tab10.colors

data_g = []

for i in np.arange(n_realizations):

    #> n. of time-steps
    n_timesteps = int( Tfin / dt )

    #> Increments: i.i.d. ~ dBrownian = white noise*dt, dw = xi*dt
    mu, sigma = 0., 1./np.sqrt(dt)
    params = rgen['write_params'](mu, sigma, n_timesteps)
    xi = rgen['generator'](**params);  dwi = xi * dt
    # mu, sigma = 0., np.sqrt(dt)
    # params = rgen['write_params'](mu, sigma, n_timesteps)
    # xi = rgen['generator'](**params);  dwi = xi

    #> Cumulative sum of increments: Wiener process (Browninan motion)
    # wi[i+1] = wi[i] + dwi[i]
    wi = np.insert( np.cumsum(dwi), 0, 0., axis=0 )

    #> Realization
    data_g += [{
        'timevector': np.arange(n_timesteps+1) * dt,
        'whitenoise': dwi,
        'wiener': wi,
        'linecolor': colors[0]
    }]

#> Statistics
stat_mean = np.sum([  d['wiener'] for d in data_g ], axis=0) / n_realizations
stat = {
    'mean': stat_mean,
    'var' : np.sum([ (d['wiener']-stat_mean)**2 for d in data_g], axis=0) / n_realizations
}

fig, ax = plt.subplots(1,1, figsize=(6,6))
iline, nbold = 0, 2
lw, lwthin = 1., .1
for d in data_g[::10]:
    if ( iline >= nbold ):  lw = lwthin
    ax.plot(d['timevector'], d['wiener'], color=d['linecolor'], linewidth=lw)
    iline += 1

ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_xlim(-dt, Tfin)
ax.set_ylim(-3.0*np.sqrt(Tfin), 3.0*np.sqrt(Tfin))
ax.grid()


#> Sample correlation
n_samples_v = [ 50, 100, 200 ]

for n_samples in n_samples_v:
    print(n_samples)

plt.show()


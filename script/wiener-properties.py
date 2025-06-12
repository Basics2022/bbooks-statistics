#> Import libraries

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from scipy.stats import norm


def sample_to_pdf(x, bins=100, density=True):
  """ evaluate pdf, from histogram, and normalizing with uniform integration rule """
  hist, bin_edges = np.histogram(x, bins=bins, density=True)   # get data from histogram
  bin_cen = 0.5 * ( bin_edges[:-1] + bin_edges[1:] )           # bin center
  d_bin = bin_edges[1:] - bin_edges[:-1]                       # bin width
  pdf = hist / np.sum(hist * d_bin)                            # normalization to get int pdf = 1

  return hist, bin_cen  # pdf, bin_cen


#> Set seed, for reproducibility
np.random.seed(1234)   # seed, not working

# Parameters ---------------------------------------------------------------------
#> Time
Tfin = 1000.                              # final time
dt   = 1                                  # reference dt
n_timesteps = int( Tfin / dt )

#> Parameters of the rng, 
rng_label = 'Normal'
mu, sigma = 0., 1. # 1./np.sqrt(dt)

#> Random number generators of increments, with different probability density
rng_list = {
    'Bernoulli': { 'generator': np.random.default_rng().choice, 'params': {}, \
      'write_params': lambda mu, sigma, nt: {'a':[mu-sigma, mu+sigma], 'p':[.5, .5], 'size': nt}  },
    'Normal':    { 'generator': np.random.default_rng().normal, 'params': {}, \
      'write_params': lambda mu, sigma, nt: {'loc': mu, 'scale': sigma, 'size': nt}  }
}

#> Select normal distribution for increments
rng = rng_list[rng_label]

#> N. realizations
n_realizations = 10000 # 5000  # 1000  # 10000

#> Colors for plot
colors = cm.tab10.colors

data_g = []

#> Sample realizations of the Wiener process
for i in np.arange(n_realizations):

    #> Increments: i.i.d. ~ dBrownian = white noise*dt, dw = xi*dt
    params = rng['write_params'](mu, sigma, n_timesteps)
    xi = rng['generator'](**params);  dwi = xi

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


#> Properties
#> 1. P(M(t)>a) = 1 - \phi(a/sqrt(t))
# tv1 = [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 ]
tv1 = [ 200, 400, 600, 800, 1000 ]
mv = []
mvs = []

for t in tv1:
    #> Append to mv, the vector of max W(t) of the realizations
    maxW = [ np.max(data['wiener'][:t]) for data in data_g ]
    mvs += [ np.sort(maxW) ]
    mv += [ maxW ]

cdf = np.arange(len(maxW)) / len(maxW)

fig, ax = plt.subplots(3, len(tv1)+1, figsize=(3*(len(tv1)+1), 3*3))
for i in range(len(tv1)):
    p, x = sample_to_pdf(mv[i], bins=100) # 30)
    dx = x[1] - x[0]
    Pcum = np.cumsum(p[::-1])[::-1] * dx
    ax[0,i].plot(x, p,)
    ax[1,i].plot(x, Pcum, )
    ax[2,i].plot(mvs[i], cdf)
    ax[1,i].set_xlabel("a")
    ax[0,i].set_title(f"t:{tv1[i]}")
    for j in range(3): ax[j,i].grid()
    if ( i == 0 ): 
        ax[0,i].set_ylabel("p(a)")
        ax[1,i].set_ylabel("P(M(t)>a)")

    ax[0,len(tv1)].plot(x/np.sqrt(tv1[i]), p*np.sqrt(tv1[i]))
    ax[1,len(tv1)].plot(x/np.sqrt(tv1[i]), Pcum, marker='x')

ax[0,len(tv1)].grid()
ax[1,len(tv1)].grid();  ax[1,len(tv1)].set_xlabel('${a/\sqrt{t}}$')
ax[0,len(tv1)].set_title("Non-dimensional")

xx = np.arange(0,4,.1)
yy = norm.cdf(xx)
ax[1,len(tv1)].plot(xx, 2. - 2.*yy, '--', color='black')

#> Plots
#> Realizations
fig, ax = plt.subplots(1,1, figsize=(6,6))
iline, nbold = 0, 2
lw, lwthin = 1., .05
for d in data_g[::10]:
    if ( iline >= nbold ):  lw = lwthin
    ax.plot(d['timevector'], d['wiener'], color=d['linecolor'], linewidth=lw)
    iline += 1

ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_xlim(-dt, Tfin)
ax.set_ylim(-3.0*np.sqrt(Tfin), 3.0*np.sqrt(Tfin))
ax.grid()

plt.show()


import numpy as np
import matplotlib.pyplot  as plt
from matplotlib.ticker import MultipleLocator
# two arrays
x = np.array([0.053, 0.042, 0.029, 0.025, 0.017, 0.010, 0.008, 0.002], float)
F = np.array([3.55, 2.96, 2.31, 2.01, 1.50, 1.02, 0.697, 0.226],float)

planets_densities = np.array([5.43,	5.20,	5.51,	3.34,	3.93,	1.33,	0.69,	1.32,	1.64,	1.86], float)
planets_radii = np.array([2440,6052,6371,1738,3390,69910,58230,25360,24620,1187],float)
planets_labels = ["Me","Ve","Ea","Mo","Ma","Ju","Sa","Ur","Ne","Pl"]

moons_densities = np.array([1.90,1.76,3.53,2.99,1.94,1.85,1.15,1.61,0.96,1.47,1.23,1.88,1.09,1.20,1.70,1.40,1.71,1.63,1.20,2.05,1.20,1.70], float)
moons_radii = np.array([1738,11.1,6.2,1821,1565,2634,2403,199,249,530,560,764,2575,718,0.66,13.5,11.7,35.3,30.1,0.5,215,15.9], float)
moons_labels = ["Ph","De","Io","Eu","Ga","Ca","Mi","En","Te","Di","Rh",	"Ti","Ia","Mr","Ar","Um","Tt","Ob","Pr","Tr", "Nr","Ch"]

asteroids_densities = np.array([2.50,2.60,1.30,2.67,1.90,5.50,3.46,2.16], float)
asteroids_radii = np.array([6.1,15.8,26.4,9.69,0.32,50,263,473], float)
asteroids_labels = ["Ga",	"Id",	"Ma",	"Er",	"It",	"Lu",	"Vs",	"Ce"]
#print(len(asteroids_radii_native)==len(asteroids_log_radii) and len(moons_log_radii)==len(moons_radii_native) and len(planets_log_radii)==len(planets_radii_native))
#print(str(len(moons_log_radii)), ",", str(len(moons_radii_native)))

all_labels = planets_labels+moons_labels+asteroids_labels
all_densities = np.concatenate([planets_densities, moons_densities, asteroids_densities])
all_log_radii = np.concatenate([planets_radii, moons_radii, asteroids_radii])


fig, ax = plt.subplots()
ax.set_yscale('log')

# Major x-axis ticks every 1, minor ticks every 0.1
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.tick_params(which='minor', length=3)
ax.tick_params(which='major', length=6)
ax.grid(which='major', alpha=0.5)
ax.grid(which='minor', alpha=0.2, linestyle=':')
ax.set_xlim(0, round(np.max(all_densities)))
ax.set_title(label="Log–linear graph of planets, moons and asteroids radius against density.", loc='center')

# Plot the points
ax.plot(planets_densities, planets_radii,'.g')
ax.plot(moons_densities, moons_radii, '.r')
ax.plot(asteroids_densities, asteroids_radii, '.b')

# NOW add annotations to the axes
k = 0
for x, y in zip(all_densities, all_log_radii):
    label = "{:.2f}".format(y)
    ax.annotate(all_labels[k],  # Changed from plt.annotate to ax.annotate
                (x, y),
                textcoords="offset points",
                xytext=(0, 5),
                ha='center')
    k += 1

ax.set_xlabel("Density/10^3 kg m^-3")
ax.set_ylabel("Radius/km")
plt.show()
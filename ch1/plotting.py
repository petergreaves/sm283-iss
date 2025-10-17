import numpy as np
from sys import argv
import matplotlib.pyplot  as plt
import argparse
from matplotlib.ticker import MultipleLocator


parser = argparse.ArgumentParser("plotter")
parser.add_argument("--include_tma", help="whether to include TMA 1 planets a and b.")
args = parser.parse_args()


planets_densities = np.array([5.43,5.20,5.51,3.34,
                              3.93,1.33,0.69,1.32,
                              1.64,	1.86],float)

planets_radii = np.array([2440,6052,6371,1738,
                          3390,69910,58230,25360,
                          24620,1187],float)

planets_labels = ["Me-T","Ve-T","Ea-T","Mo-T",
                  "Ma-T","Ju-G","Sa-G","Ur-G",
                  "Ne-G","Pl-K"]


if args.include_tma:
    # then include A and B from TMA 1
    planets_densities = np.concatenate([planets_densities, np.array([1.25,5.32], float)])
    planets_radii=np.concatenate([planets_radii, np.array([(1.31*10**5)/2, 5550/2],float)])
    planets_labels =planets_labels+["A-G", "B-T"]


moons_densities = np.array([1.90,1.76,3.53,
                            2.99,1.94,1.85,1.15,
                            1.61,0.96,1.47,1.23,
                            1.88,1.09,1.20,1.70,
                            1.40,1.71,1.63,1.20,
                            2.05,1.20,1.70], float)
                            
moons_radii = np.array([11.1,6.2,1821,
                        1565,2634,2403,199,
                        249,530,560,764,
                        2575,718,236,579,
                        585,789,761,209,
                        1353,170,606],float)

moons_labels = ["Ph-M","De-M","Io-M","Eu-M","Ga-M","Ca-M","Mi-M","En-M","Te-M","Di-M","Rh-M",
                "Ti-M","Ia-M","Mr-M","Ar-M","Um-M","Tt-M","Ob-M","Pr-M","Tr-M", "Nr-M","Ch-M"]

asteroids_densities = np.array([2.50,2.60,1.30,2.67,1.90,3.40,3.46,2.16], float)
asteroids_radii = np.array([6.1,15.8,26.4,9.69,0.32,50,263,473], float)
asteroids_labels = ["Ga-A",	"Id-A",	"Ma-A",	"Er-A",	"It-A",	"Lu-A",	"Vs-A",	"Ce-A"]
#print(len(asteroids_radii_native)==len(asteroids_log_radii) and len(moons_log_radii)==len(moons_radii_native) and len(planets_log_radii)==len(planets_radii_native))
#print(str(len(moons_radii)), ",", str(len(moons_densities)), ",", str(len(moons_labels)))

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
ax.set_title(label="Planets, moons and asteroids radius against density.", loc='center')

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
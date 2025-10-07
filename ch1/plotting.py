import numpy as np
import matplotlib.pyplot  as plt
# two arrays
x = np.array([0.053, 0.042, 0.029, 0.025, 0.017, 0.010, 0.008, 0.002], float)
F = np.array([3.55, 2.96, 2.31, 2.01, 1.50, 1.02, 0.697, 0.226],float)

planets_densities = np.array([5.43,	5.20,	5.51,	3.34,	3.93,	1.33,	0.69,	1.32,	1.64,	1.86], float)
planets_log_radii = np.array([3.39,	3.78,	3.80,	3.24,	3.53,	4.84,	4.77,	4.40,	4.39,	3.07], float)
planets_labels = ["Me","Ve","Ea","Mo","Ma","Ju","Sa","Ur","Ne","Pl"]

moons_densities = np.array([1.90,1.76,3.53,2.99,1.94,1.85,1.15,1.61,0.96,1.47,1.23,1.88,1.09,1.20,1.70,1.40,1.71,1.63,1.20,2.05,1.20,1.70], float)
moons_log_radii = np.array([1.05,0.79,3.26,3.19,3.42,3.38,2.30,2.40,2.72,2.75,2.88,3.41,2.86,2.37,2.76,2.77,2.90,2.88,2.32,3.13,2.23,2.78], float)
moons_labels = ["Ph","De","Io","Eu","Ga","Ca","Mi","En","Te","Di","Rh",	"Ti","Ia","Mr","Ar","Um","Tt","Ob","Pr","Tr", "Nr","Ch"]

asteroids_densities = np.array([2.50,2.60,1.30,2.67,1.90,5.50,3.46,2.16], float)
asteroids_log_radii = np.array([0.785329835,1.198657087,1.421603927,0.986323777,-0.494850022,1.698970004,2.419955748,2.674861141], float)
asteroids_labels = ["Ga",	"Id",	"Ma",	"Er",	"It",	"Lu",	"Vs",	"Ce"]


all_labels = planets_labels+moons_labels+asteroids_labels

all_densities = np.concatenate([planets_densities, moons_densities, asteroids_densities])
all_log_radii = np.concatenate([planets_log_radii, moons_log_radii, asteroids_log_radii])

k=0
for x,y in zip(all_densities,
               all_log_radii):

    label = "{:.2f}".format(y)
    plt.annotate(all_labels[k], # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    k+=1



# Plot the points
plt.plot(planets_densities,planets_log_radii,'.g')
plt.plot(moons_densities,moons_log_radii,'.r')
plt.plot(asteroids_densities,asteroids_log_radii,'.b')

plt.xlabel("Density/kg m^-3")
plt.ylabel("Radius log(10)")
plt.show()
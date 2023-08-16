import numpy as np
import matplotlib.pyplot as plt

import matplotlib.patches as patch
#### First lets make the tricolor of Indian National Flag
#The green colour depicting the fertility, growth and auspiciousness of the land
green = patch.Rectangle((0,0), width=10, height=2, facecolor='#008000')
#The white color depicting peace and truth 
white = patch.Rectangle((0,2), width=10, height=2, facecolor='#ffffff') 
#The kesari color depicting the strength and courage of the country
kesari = patch.Rectangle((0,4), width=10, height=2, facecolor='#FF9933') 
fig,ax = plt.subplots()
ax.add_patch(green)
ax.add_patch(white)
ax.add_patch(kesari)
#### Now lets make the Ashok Chakra Chakra depicting that there is life in movement and death in stagnation
r=0.8
plt.plot(5,3, marker = 'o', markerfacecolor = '#000088ff', markersize = 10)
ashoka_chakra = plt.Circle((5, 3), r, color='#000088ff', fill=False, linewidth=7)
ax.add_artist(ashoka_chakra)

#### Continuing with adding small circles inside the edge of Chakra

chakra_circles_x = []
chakra_circles_y = []


for i in range(1,25):
    chakra_circles_x.append(5+(r-0.05) * np.cos(np.pi/24 + np.pi*i/12))
    chakra_circles_y.append(3+(r-0.05) * np.sin(np.pi/24 + np.pi*i/12))


plt.plot(chakra_circles_x, chakra_circles_y, 'o',
         markersize=4,
         markerfacecolor='#000088ff',
         markeredgecolor = '#000088ff')

#### And finally lets make the 24 spokes within the chakra
for i in range(0,24):
    x1 =  5 + r/2 * np.cos(np.pi*i/12 + np.pi/48)
    x2 =  5 + r/2 * np.cos(np.pi*i/12 - np.pi/48)
    y1 =  3 + r/2 * np.sin(np.pi*i/12 + np.pi/48)
    y2 =  3 + r/2 * np.sin(np.pi*i/12 - np.pi/48)
    x3 =  5 + r * np.cos(np.pi*i/12)
    y3 =  3 + r * np.sin(np.pi*i/12)
    ax.add_patch(patch.Polygon([[5,3], [x1,y1], [x3,y3],[x2,y2]], fill=True, closed=True, color='#000088ff'))

plt.axis('equal')

#### Kaboom!
plt.show()
print("Vande Mataram")

#And a quote by B. R. Ambedkar that till date resides in my heart 
print("\nWe are Indians, firstly and lastly.")
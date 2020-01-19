from math import sqrt
from skimage.feature import blob_log
from skimage.color import rgb2gray
from skimage import io

import matplotlib.pyplot as plt

image = io.imread("test2.jpg",as_gray=True)

#image en BW
image_gray = rgb2gray(image)
#choix de la méthode de reconnaissance des blobs
blobs_log = blob_log(image_gray, max_sigma=1, num_sigma=1, threshold=0.1)
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
#données esthétique pour le graphique
color = 'yellow'
title = 'Laplacian of Gaussian'

#création du graphique nécessaire à référencer les cercles sur l'image
fig, ax = plt.subplots(figsize=(20, 20))

#affichage du titre et de l'image sans mise en valeur des blobs
ax.set_title(title)
ax.imshow(image)

for blob in blobs_log :
    y, x, r = blob
    c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
    ax.add_patch(c)
    
#ax.set_axis_off() #si on veut pas les axes

plt.show()

from skimage.feature import blob_log
from skimage.color import rgb2gray
from skimage import io
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

inputmaxsigma = input("max sigma=  ") 
inputinsigma = input("min sigma=  ") 
inputthresholds = input("threshold= ")
inputthreshold = float(inputthresholds)
image = io.imread("bite.jpg",as_gray=False)


image_gray = rgb2gray(image)
blobs_log = blob_log(image_gray, max_sigma=inputmaxsigma, num_sigma=inputinsigma, threshold=inputthreshold)




color = 'yellow'
title = 'Laplacian of Gaussian'



fig, ax = plt.subplots(figsize=(20, 20))
ax.imshow(image)
yellow_circle = Line2D([0], [0],linewidth=0, linestyle=None, color=None, marker='o',markeredgecolor='y',markeredgewidth=2, label=len(blobs_log),markerfacecolor='w',
                         markersize=15),
ax.legend(handles=yellow_circle,loc='upper center', shadow=False, fontsize='15',title='Nombre de défaut(s) detecté(s) :',title_fontsize=15)
 
              
for blob in blobs_log :
    y, x, r = blob
    c = plt.Circle((x, y), r, color=color, linewidth=6, fill=False)
    ax.add_patch(c)
    ax.set_axis_off() #si on veut pas les axes

if blobs_log.size:
        plt.savefig("cesttoutbon.png")
        
        
    
    
plt.show()

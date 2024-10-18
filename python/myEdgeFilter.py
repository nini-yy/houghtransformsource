import numpy as np
import scipy    # For signal.gaussian function
from scipy.signal.windows import gaussian

from myImageFilter import myImageFilter

''' detecting edges:
        1. apply gaussian blue
        2. find sobel x and sobel y
        3. use sobel x and sobel y to find magnitude and direction
        4. using the direction apply NMS to decrease noise in magnitude
        5. output suppressed image '''

def myEdgeFilter(img0, sigma):
    # YOUR CODE HERE
    hsize = int(2 * np.ceil(3 * sigma) + 1)
    
    gauss1D = gaussian(hsize, sigma).reshape(hsize, 1)
    gauss = gauss1D @ gauss1D.T
    gauss = gauss/np.sum(gauss) # normalizing filter


    smoothimg = myImageFilter(img0, gauss)

    #np.fliplr(np.flipud(
    sobelX = np.array([[1, 0, -1],[2,0,-2],[1,0,-1]])
    sobelY = np.array([[1, 2, 1],[0,0,0],[-1,-2,-1]])
    
    imgx = myImageFilter(smoothimg, sobelX)
    imgy = myImageFilter(smoothimg, sobelY)

    imgmag = np.sqrt(imgx**2 + imgy**2) # vector magnitude?? setting different magnitudes??
    #imgmag = np.multiply(imgmag, 255.0 / imgmag.max())

    angles = np.rad2deg(np.arctan2(imgy, imgx)) # arctan based on coord -> turn into deg from radians
    angles[angles < 0] += 180 # weed out not under 180


    def non_maximum_suppression(image, angles):
        size = image.shape
        suppressed = np.zeros(size)
        for i in range(1, size[0] - 1):
            for j in range(1, size[1] - 1):
                if (0 <= angles[i, j] < 22.5) or (157.5 <= angles[i, j] <= 180):  #closest to 0 -> testing along x axis
                    value_to_compare = max(image[i, j - 1], image[i, j + 1])
                elif (22.5 <= angles[i, j] < 67.5):                              #closest to 45 -> testing along y = x
                    value_to_compare = max(image[i + 1, j + 1], image[i - 1, j - 1])
                elif (67.5 <= angles[i, j] < 112.5):                             #closest to 90 -> testing along y axis
                    value_to_compare = max(image[i - 1, j], image[i + 1, j])
                else:                                                            #closeset to 135 -> testing along y = -x
                    value_to_compare = max(image[i + 1, j - 1], image[i - 1, j + 1])
                
                if image[i, j] >= value_to_compare:
                    suppressed[i, j] = image[i, j]
                    
        #suppressed = np.multiply(suppressed, 255.0 / suppressed.max())
        return suppressed

    img1 = non_maximum_suppression(imgmag, angles)
    

    return img1
import numpy as np
import cv2  # For cv2.dilate function

def myHoughLines(H, nLines):

    #define a non max suppression for hough image
    def non_max_suppression(H):
        Hsup = np.zeros_like(H)
        rows, cols = H.shape
        
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                # take out a 3 by 3 area
                patch = H[i-1:i+2, j-1:j+2]
                
                # if center is max of 3x3, then set to middle
                if H[i, j] == np.max(patch):
                    Hsup[i, j] = H[i, j]
                else:
                    Hsup[i, j] = 0
                    
        return Hsup
    
    Hsup = non_max_suppression(H)

    rhos = []
    thetas = []
    
    for i in range(nLines):
        #find max in suppressed -> take the indexes
        idx = np.argmax(Hsup)
        rho_ind, theta_ind = np.unravel_index(idx, Hsup.shape)
        #add to list
        rhos.append(rho_ind)
        thetas.append(theta_ind)
        
        # set to 0 so we dont find the same line again
        Hsup[rho_ind, theta_ind] = 0
    
    return np.array(rhos), np.array(thetas)
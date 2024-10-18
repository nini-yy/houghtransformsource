import numpy as np
''' My version of probabilistic hough lines utilizes the rhoScale and rhoTheta outputted by myHoughTransform'''

def myHoughLineSegments(lineRho, lineTheta, Im, rhoScale, thetaScale):
    h = Im.shape[0]
    w = Im.shape[1]
    lines = []
    
    for rho_idx, theta_idx in zip(lineRho, lineTheta):

        #variables
        rho = rhoScale[rho_idx]
        theta = thetaScale[theta_idx]
        cost = np.cos(theta)
        sint = np.sin(theta)

        seglen = 3  # cv2 has minlength??? -- param??

        #iterating through each pixel
        for y in range(h):
            for x in range(w):
                # if pixel is edge
                if Im[y, x] > 0:  
                    # pix dist from edge
                    dist = abs(x * cost + y * sint - rho)
                    
                    # dist close enough -- param??
                    if dist < 1:  
                        x0 = int(x - seglen * (-sint))
                        y0 = int(y - seglen * cost)
                        xn = int(x + seglen * (-sint))
                        yn = int(y + seglen * cost)

                        # add to lines
                        lines.append(((x0, y0), (xn, yn)))
    
    return lines
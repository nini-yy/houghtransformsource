import numpy as np

def myHoughTransform(Im, rhoRes, thetaRes):
    h = Im.shape[0]
    w = Im.shape[1]
    
    # theta between [0, 2pi] incrementing by thetaRes
    thetamax = 2 * np.pi
    thetamin = 0
    thetaScale = np.arange(thetamin, thetamax, thetaRes)
    #print(len(thetaScale))
        
    # rho between [0, M] -- m is max distance in an image (diag)
    diaglen = int(np.sqrt(h**2 + w**2))
    rhoScale = np.arange(0, diaglen + 1, rhoRes)
    #print(len(rhoScale))
    
    # array for all sets of pairs
    imghough = np.zeros((len(rhoScale), len(thetaScale)), dtype=np.int32)
    
    # get edges -> thresh > 0
    edgepts = np.argwhere(Im > 0)
    
    for j, theta in enumerate(thetaScale):
        #if j % 10 == 0:
        #    print(j, theta)
        for y, x in edgepts:
            # p = x cos(t) + y sin(t)
            rho = x * np.cos(theta) + y * np.sin(theta)
            
            if rho >= 0: 
                rho_idx = np.argmin(np.abs(rhoScale - rho))
                
                imghough[rho_idx, j] += 1
    
    return imghough, rhoScale, thetaScale
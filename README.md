# houghtransformsource

The file main.ipynb includes the walkthrough and parameters I used to achieve the results I wanted for cv2.houghLinesP which uses cv2.canny in a OpenCV implementation.

*The other files include*
- myEdgeFilter.py which replaces cv2.Canny (however, you do need to apply thresholding after)
- myhoughLines.py which replaces cv2.houghLines
- myhoughLineSegments.py which replaces cv2.houghLinesP

In myEdgeFilter.py, we applied the edge detection algorithm. I ran this with sigma = 2. I found that running with this sigma value decreased the noise to the perfect amount where the gaussian blur did not interfere with the edges, but also allowed us to clean up the image. The image on the left is with only running myEdgeFilter, the one on the right is with a threshold value of 0.07.

MyHoughTransform takes three values, rhoRes, thetaRes, and the thresholded image. I found that with a too high rhoRes, it was not obtaining all the edges needed, especially for the curved aspect of the vase in this image, which I still found to be a problem despite lowering it to 2. Since the lines were fairly separate using π/90 was enough to be able to detect the edges with clarity and reduce noise. This function is used in my houghLines implementation. 

MyHoughLines takes the hough transform image and nLines. I found that 30 was a good value for nLines to be able to detect the finer edges in the vase while also not introducing too much noise.


**Some Final Thoughts**

The code worked decently well with this single set of parameters. However, I think that a different set of parameters would be a lot better for images that have a lot more going on such as image 6, 8 or 9. These would do better with a higher sigma or threshold value to decrease the noise caused by the textures in the environment. However, it performed well with images 1 through 5. I thought that the edge detection and thresholding cause the most problems as they are what affects the rest of the algorithm. If the edges are properly detected and thresholded, it allows the rest of the functions to perform fairly well. Of course, the rho resolution and theta resolution are also very important however they can be adjusted less across the board. I found that finding the right balance between sigma and threshold worked best to improve the performance as it decreased a lot of noise and allowed the rest of the algorithms to implement better. I also found that increasing the nLines allowed me to highlight more edges, especially when applying the HoughLinesP or myHoughSegments.

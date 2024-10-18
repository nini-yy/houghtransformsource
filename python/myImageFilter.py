import numpy as np

def myImageFilter(img0, h):
    imgheight, imgwid = img0.shape
    filheight, filwid = h.shape

    padheight = filheight // 2
    padwid = filwid // 2

    padimg = np.pad(img0, ((padheight, padheight), (padwid, padwid)), mode='edge')

    img1 = np.zeros((imgheight, imgwid))

    for i in range(imgheight):
        for j in range(imgwid):
            #conv = (np.sum(padimg[i:i + filheight, j:j + filwid] * h))
            region = padimg[i:i+filheight, j:j+filwid]
            img1[i, j] = np.sum(region*h)
            '''if conv < 0:
                img1[i][j] = 0
            elif conv > 255:
                img1[i][j] = 255
            else:
                img1[i][j] = conv'''

    return img1

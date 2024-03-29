import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messipyr.jpg',0)

template = cv2.imread('messi_face_template.jpg',0)
#template = cv2.GaussianBlur(template,(5,5),0)
#template=cv2.resize(template,(1081,1081),interpolation=cv2.INTER_AREA)

#img = cv2.GaussianBlur(img,(5,5),0)
img2 = img.copy()
w, h = template.shape[::-1]
print(template.shape[::-1])

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)
    print(method)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    #print(res)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val,max_val,min_loc,max_loc)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res)
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img)
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
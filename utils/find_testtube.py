import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def find_testtube(arquivo):
    img = cv.imread(arquivo, cv.IMREAD_COLOR)
    assert img is not None, "file could not be read, check with os.path.exists()"
    img2 = img.copy()
    template = cv.imread('temp_images/template.jpg', cv.IMREAD_COLOR)
    assert template is not None, "file could not be read, check with os.path.exists() 2"
    w, h, c = template.shape[::-1]
    
    new_img = cv.resize(img, (w, h))
    cv.imwrite('new_img.jpg', new_img)
    # Lista para armazenar as imagens geradas pela comparação
    images = []

    # All the 6 methods for comparison in a list
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
    'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    
    for meth in methods:
        new_img2 = new_img.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv.matchTemplate(new_img2,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv.rectangle(new_img2,top_left, bottom_right,(0, 255, 0), 2)

        # Armazenar a imagem resultante e a imagem original com o retângulo desenhado
        images.append((res, cv.cvtColor(new_img2, cv.COLOR_BGR2RGB)))
    
    return images

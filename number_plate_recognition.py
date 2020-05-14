def main():
    import numpy as np
    import cv2
    import imutils
    import sys
    import pytesseract
    import pandas as pd
    import time
    
    
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = cv2.imread("D:\\University of Colorado\\Subjects\\02_ML\\Project\\CarAcceptance\\Car Images\\Happy Case.jpg")
    img = imutils.resize(img, width=500)
    #cv2.imshow("Original Image", img)
    #cv2.waitKey(0)
    cv2.imwrite("Original Image.png", img)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Preprocess 1 - Grayscale Conversion", gray_img)
    #cv2.waitKey(0)
    cv2.imwrite("Preprocess 1 - Grayscale Conversion.png", gray_img)
    gray_img = cv2.bilateralFilter(gray_img, 11, 17, 17)
    cv2.imwrite("Preprocess 2 - Bilateral Filter.png", gray_img)
    #cv2.imshow("Preprocess 2 - Bilateral Filter", gray_img)
    #cv2.waitKey(0)
    c_edge = cv2.Canny(gray_img, 170, 200)
    cv2.imwrite("Preprocess 3 - Canny Edges.png", c_edge)
    #cv2.imshow("Preprocess 3 - Canny Edges", c_edge)
    #cv2.waitKey(0)
    cnt, new = cv2.findContours(c_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnt = sorted(cnt, key = cv2.contourArea, reverse = True)[:30]
    NumberPlateCount = None
    im2 = img.copy()
    cv2.drawContours(im2, cnt, -1, (0,255,0), 3)
    cv2.imwrite("Top 30 Contours.png", im2)
    #cv2.imshow("Top 30 Contours.png", im2)
    #cv2.waitKey(0)
    count = 0

    for c in cnt:
        perimeter = cv2.arcLength(c, True)      #Getting perimeter of each contour
        approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
        if len(approx) == 4:            #Selecting the contour with 4 corners/sides.
            NumberPlateCount = approx
            break
    
    masked = np.zeros(gray_img.shape,np.uint8)
    new_image = cv2.drawContours(masked,[NumberPlateCount],0,255,-1)
    new_image = cv2.bitwise_and(img,img,mask=masked)
    cv2.imwrite("4 - Final_Image.png",new_image)
    #cv2.imshow("4 - Final_Image",new_image)
    #cv2.waitKey(0)
    configr = ('-l eng --oem 1 --psm 3')
    text_no = pytesseract.image_to_string(new_image, config=configr)
    print(text_no)
    
    
    

if __name__ == '__main__':
    main()
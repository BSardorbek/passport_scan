import cv2
import pytesseract

import numpy as np
import math


#####################################

img = cv2.imread('a.jpg',0)
(height, width) = img.shape

#####################################

img_copy = img.copy()

img_canny = cv2.Canny(img_copy, 50, 100, apertureSize = 3)


img_hough = cv2.HoughLinesP(img_canny, 1, math.pi / 180, 100, minLineLength = 100, maxLineGap = 10)


(x, y, w, h) = (np.amin(img_hough, axis = 0)[0,0], np.amin(img_hough, axis = 0)[0,1],
np.amax(img_hough, axis = 0)[0,0] - np.amin(img_hough, axis = 0)[0,0],
np.amax(img_hough, axis = 0)[0,1] - np.amin(img_hough, axis = 0)[0,1])

img_roi = img_copy[y:y+h,x:x+w]

#####################################

(height, width) = img_roi.shape

img_roi_copy = img_roi.copy()
dim_mrz = (x, y, w, h) = (1, round((height*0.9)+1), width-3, round(height-(height*0.9))-2)

img_roi_copy = cv2.rectangle(img_roi_copy, (x, y-30), (x + w ,y + h),(0,0,0),2)

img_mrz = img_roi[y-36:y+h-13, x:x+w]


img_mrz = cv2.cvtColor(img_mrz, cv2.COLOR_BGR2RGB)
ret, img_mrz = cv2.threshold(img_mrz,127,255,cv2.THRESH_TOZERO)

mrz = pytesseract.image_to_string(img_mrz, config = r'--oem 3 --psm 6')

mrz = [line for line in mrz.split('\n')]
if mrz[0][0:2] == 'P<':
    lastname = mrz[0].split('<')[1][3:]
    print("lastname",lastname)
else:
    lastname = mrz[0].split('<')[0][5:]
    print("lastname",lastname)
firstname = [i for i in mrz[0].split('<<') if (i).isspace() == 0 and len(i) > 0 and i != "<"][1].partition('<')[0]
print("firstname",firstname)
print("mrz",mrz)
pp_no = mrz[1][:9]
print("pp_no",pp_no)
pinfl = mrz[1][28:42]
print("pinfl",pinfl)
###################################

img_roi_copy = img_roi.copy()
dim_lastname_chi = (x, y, w, h) = (455, 1210, 120, 70)
img_roi_copy = cv2.rectangle(img_roi_copy, (x, y), (x + w ,y + h),(0,0,0))


passport_dict = {'Passport No.': pp_no,
                 'First Name': firstname,
                 'Last Name': lastname,
                 'Pinfl':pinfl,
                }
print(passport_dict)
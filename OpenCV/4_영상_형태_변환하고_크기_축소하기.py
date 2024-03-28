# 4. 영상 형태 변환하고 크기 축소하기

import cv2 as cv
import sys

img = cv.imread('C:/Users/demon/Desktop/img(OpenCV)/soccer.jpg')

if img is None:
  sys.exit('파일이 존재하지 않음')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small=cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5)

cv.imwrite('soccer_gray.jpg', gray)
cv.imwrite('soccer_gray_small.jpg', gray_small)

cv.imshow('Color image',img)
cv.imshow('Gray image',gray)
cv.imshow('Gray image small',gray_small)

cv.waitKey()
cv.destroyAllWindows()

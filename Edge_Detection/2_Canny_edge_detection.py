import cv2 as cv

img = cv.imread('C:/Users/win/Desktop/soccer.JPG')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny1=cv.Canny(gray,50,150)
canny2=cv.Canny(gray,100,200)


cv.imshow('Original',gray)
cv.imshow('canny1',canny1)
cv.imshow('canny2',canny2)

cv.waitKey()
cv.destroyAllWindows()


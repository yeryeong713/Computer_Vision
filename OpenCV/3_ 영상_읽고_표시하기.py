# 3. 영상을 읽고 표시하기
import cv2 as cv
import sys

img = cv.imread('C:/Users/demon/Desktop/img(OpenCV)/soccer.jpg')

if img is None:
    sys.exit('파일이 존재하지 않음')

cv.imshow('Image Display',img)
print(img[0,0,0], img[0,0,1], img[0,0,2])

#Image Display라는 창을 키보드 입력이 들어올 때까지 켜놓기.
cv.waitKey()
cv.destroyAllWindows()

#Image Display 창이 꺼지면 img의 type과 shape을 출력함
print(type(img))
print(img.shape)

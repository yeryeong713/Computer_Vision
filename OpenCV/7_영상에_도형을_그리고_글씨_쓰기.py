#7. 영상에 도형을 그리고 글씨 쓰기
import cv2 as cv
import sys

img=cv.imread('C:/Users/demon/Desktop/img(OpenCV)/apples.jpg')

if img is None:
  sys.exit('파일을 찾을 수 없음')

# cv.rectangle(img,(290,780),(620,950),(0,0,225),2)
# cv.putText(img, 'mouse',(290,770), cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

def draw(event, x, y, flags, param):
  if event==cv.EVENT_LBUTTONDOWN:
    cv.rectangle(img,(x,y),(x+200,y+200),(0,0,225),2)
  elif event==cv.EVENT_RBUTTONDOWN:
    cv.rectangle(img,(x,y),(x+100,y+100),(255,0,0),2)

  cv.imshow('Draw',img)

cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

cv.setMouseCallback('Drawing',draw)

while(True):
  if cv.waitKey(1)==ord('q'):
    cv.destroyAllWindows()
    break

# cv.waitKey()
# cv.destroyAllWindows()

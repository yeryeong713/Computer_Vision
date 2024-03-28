#5. 웹 캠에서 비디오 읽기
#6. 비디오에서 수집한 영상 이어 붙이기

import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0, cv.CAP_DSHOW)


if not cap.isOpened():
  sys.exit('카메라 연결 실패')

frames=[]
while True:
  ret, frame = cap.read()

  if not ret:
    print('프레임 획득 실패 > 루프 나감')
    break

  cv.imshow('Video display', frame)

  key = cv.waitKey(1)
  if key==ord('c'):
    frames.append(frame)
  elif key==ord('q'):
    break

cap.release()
cv.destroyAllWindows()

if len(frames)>0:
  imgs=frames[0]
  for i in range(1, min(3, len(frames))):
    imgs=np.hstack((imgs, frames[i]))

  cv.imshow('collected images', imgs)

  cv.waitKey()
  cv.destroyAllWindows()

print(len(frames))
print(frames[0].shape)
print(type(imgs))
print(imgs.shpe)

import cv2
filepath ="luffy.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("nice one baby",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

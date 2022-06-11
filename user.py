import cv2
import os

while True:
	Fname = input("Name of your file[add '.jpg' at the end]:")
	flag = input("\n Press[1] for colored image or [0] for gray image:")
		
	if os.path.exists(Fname) and flag == '0':
		imge= cv2.imread(Fname, 0)
		cv2.imshow(Fname, imge)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break
	
	elif os.path.exists(Fname) and flag == '1':
		imge= cv2.imread(Fname, 1)
		cv2.imshow(Fname, imge)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break

	else:
		print(" File name is invalid......................")
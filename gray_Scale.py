import cv2
  
#Loading Image
image = cv2.imread("C:\\Users\\Rahul\\Desktop\\photoshoot\\Rahul_California_Trip.jpg")
  
# Checkif image is present on the disk or not
if image is None:  
    print("Could not open or find the image")

# convert color image to gray
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
 # Save result
cv2.imwrite("C:\\Users\\Rahul\\Desktop\\photoshoot\\imageGray.jpg", grayImage)
 
# Create a windows for display.
cv2.namedWindow("BGRImageWindow", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("GrayImageWindow", cv2.WINDOW_AUTOSIZE)
 
# Display image- Putting the image in the respective Windows
cv2.imshow("BGRImageWindow", image)
cv2.imshow("GrayImageWindow", grayImage)
 
# Wait for a keystroke in the window
cv2.waitKey(0)

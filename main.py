import cv2

image = cv2.imread('doguinho.webp')

print("Image width: ", end="")
print(image.shape[1])

print("Image height: ", end="")
print(image.shape[0])

print("Image channels: ", end="")
print(image.shape[2])

cv2.imshow("Cute dog", image)
cv2.waitKey(0)
#'cv2.waitkey(0)' ask for enter some character to close the window

(b, g, r) = image[0,0] #bgr order 

print("The pixel (0,0) have this colors: ")
print("Red:", r, "| Green:", g, "| Blue:", b)


image[0,0] = (255,0,0) #changes the pixel (0,0) color
cv2.imshow("Maybe a cute dog", image)
cv2.waitKey(0)

image[20:90, :] = (0,0,255) #put a red rectangle in the image
cv2.imshow("A different cute dog", image)
cv2.waitKey(0)

crop = image[150:350, 200:400] #cropping the dog image
cv2.imshow("A clipped dog and your cute tongue", crop)
cv2.waitKey(0)
 
image[20:90, :] = (0,0,0) #take off a red rectangle in the image
proportion = 100.0 / image.shape[1]
new_size = (100, int(image.shape[0] * proportion))
resized_image = cv2.resize(image, new_size, interpolation = cv2.INTER_AREA)
cv2.imshow("A little cute dog", resized_image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("A gray cute dog", gray)
cv2.waitKey(0)


import cv2
import pytesseract

#img = cv2.imread('breakingnews.png')
img = cv2.imread('images/airportSecurity.png')
text = pytesseract.image_to_string(img)
print(text)


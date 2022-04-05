import cv2
import pytesseract
from gtts import gTTS
import os
#img = cv2.imread('breakingnews.png')
img = cv2.imread('images/airportSecurity.png')
text = pytesseract.image_to_string(img)
print(text)
language = 'en'
myobj = gTTS(text=text, lang=language, slow=False)

myobj.save("reddit.mp3")



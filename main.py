import cv2
import pytesseract
from gtts import gTTS
import os
#img = cv2.imread('breakingnews.png')
filename = os.listdir('images/')
print(filename)
img = cv2.imread('images/ohboy.png')
text = pytesseract.image_to_string(img)
print(text)
language = 'en'
audio = gTTS(text=text, lang=language,tld="com.au", slow=False)

audio.save("audio/ohboy2.mp3")



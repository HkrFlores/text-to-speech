import cv2
import pytesseract
from gtts import gTTS
import os
#img = cv2.imread('breakingnews.png')
filesname = os.listdir('images/')
print(filesname)
language = 'en'


for file in filesname:
    filename = file.strip('.png')
    imagepath = 'images/' + file
    img = cv2.imread(imagepath)
    text = pytesseract.image_to_string(img)
    print(text)
    audio = gTTS(text=text, lang=language, slow=False)
    audiopath = 'audio/' + filename + '.mp3'
    print(audiopath)
    audio.save(audiopath)


print("Task completed")
# all this works without for loop
#img = cv2.imread('images/ohboy.png')
#text = pytesseract.image_to_string(img)
#print(text)
#language = 'en'
#audio = gTTS(text=text, lang=language,tld="com.au", slow=False)
#audio.save("audio/ohboy2.mp3")



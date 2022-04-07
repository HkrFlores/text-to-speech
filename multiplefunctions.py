import os
import cv2
import pytesseract
from gtts import gTTS

def convertToAudio(audiofilepath, textfile):
    print("saving audio")
    language = "en"
#    print(textfile)
    audio = gTTS(text=textfile, lang=language, slow=False)
    audio.save(audiofilepath)

def saveToText(text, filepath):
    print("savetotext")
    savedfile = open(filepath, "a")
    savedfile.write(text)
    savedfile.close()
    return savedfile

def openImageFromFolder(imagepath):
    print("openImage")
    img = cv2.imread(imagepath)
    imagetextsaved = pytesseract.image_to_string(img)
    return imagetextsaved

def mainCycle():
    imagepath = 'images/'
    textpath = 'text/'
    audiopath = 'audio/'
    fileinfolder = os.listdir(imagepath)
    print("main cycle")
    for file in fileinfolder:
        filename = file.strip('.png')
        imagetoopen = imagepath + file
        texttoopen = textpath + filename + '.txt'
        audiotoopen = audiopath + filename + '.mp3'
        textfromimage = openImageFromFolder(imagetoopen)
        savedText = saveToText(textfromimage, texttoopen)
#        textopen = open(texttoopen, "r")
#        print(textopen)
        convertToAudio(audiotoopen, textfromimage)

print("start main cycle")
mainCycle()
print("completed main cycle")
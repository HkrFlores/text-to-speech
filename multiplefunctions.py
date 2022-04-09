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
    print("audio saved")

def saveToText(text, filepath):
    print("savetotext")
    savedfile = open(filepath, "a")
    savedfile.write(text)
    savedfile.close()
    #print(savedfile)
    return True

def openImageFromFolder(imagepath):
    print("openImage")
    img = cv2.imread(imagepath)
    imagetextsaved = pytesseract.image_to_string(img)
    return imagetextsaved

def openTextFile(textpath):
    print("openText")
    textinfile = ""
    for line in open(textpath, 'r'):
        print(line)
        textinfile = textinfile+line
#    with open(textpath) as filetext:
#        for line in filetext:
#            textinfile = filetext.readline()

    print(textinfile)
    return textinfile

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
        if savedText:
            textToAudio = openTextFile(texttoopen)
            print(textToAudio)

        convertToAudio(audiotoopen, textToAudio)
        #convertToAudio(audiotoopen, textfromimage)

def readTextAndAudio():
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
        textToAudio = openTextFile(texttoopen)
        convertToAudio(audiotoopen, textToAudio)

print("start main cycle")
#mainCycle()
readTextAndAudio()

print("completed main cycle")
import os
import cv2
import pytesseract

def saveToText(text, filepath):
    print("savetotext")
    savedfile = open(filepath, "a")
    savedfile.write(text)
    savedfile.close()
#    return savedfile

def openImageFromFolder(imagepath):
    print("openImage")
    img = cv2.imread(imagepath)
    imagetextsaved = pytesseract.image_to_string(img)
    return imagetextsaved

def mainCycle():
    imagepath = 'images/outdatedtech.png'
    textpath = 'text/outdatedtech2.txt'
    print("main cycle")
    textfromimage = openImageFromFolder(imagepath)
    saveToText(textfromimage, textpath)

print("start main cycle")
mainCycle()
import cv2
import pytesseract
import os

filelist = os.listdir('images/')
print(filelist)

for file in filelist:
    stripword = file.strip(".png")
    imagepath = 'images/' + file
    newpath = 'images/' + stripword + '.mp3'
    print(newpath)
    savingfilename = 'text/' + stripword + '.txt'
    img = cv2.imread(imagepath)
    text = pytesseract.image_to_string(img)
    filename = open(savingfilename, "a")
    filename.write(text)
    filename.close()


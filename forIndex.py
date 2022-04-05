import os

filelist = os.listdir('images/')
print(filelist)

for file in filelist:
    #print(file)
    stripword = file.strip(".png")
    #print(stripword)
    newpath = 'images/' + stripword + '.mp3'
    print(newpath)






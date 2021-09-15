from os import listdir
from os.path import isfile, join

mypath = "audio\\"


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

fileNames = ["tags\\" + y + ".txt" for y in [x for x in [f.partition(".")[0] for f in onlyfiles] if len(x) > 0]]

for filename in fileNames:
    open(filename, "w")

print (str(fileNames))
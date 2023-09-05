import os

isoname = input("Iso Name: ")
isofilescon = input("Where Are The files?: ")

os.system("oscdimg.exe -m " + isofilescon + " " + isoname)
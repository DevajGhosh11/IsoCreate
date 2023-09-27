import os

isoname = input("Iso Name: ")
isofilescon = input("Where Are The files?: ")

os.system("oscdimg.exe -m " + isofilescon + " " + isoname)

isona2e = input("Iso Name: ")
isofil2escon = input("Where Are The files?: ")

os.system("oscdimg.exe -m " + isofil2escon + " " + isona2e)
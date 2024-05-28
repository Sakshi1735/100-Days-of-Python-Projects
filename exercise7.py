'''
Write a program to clear the clutter inside a folder on your computer. You should use os module to rename
all the png images from 1.png all way till n.png where n is the number of png files in that folder.
Do the same for other file formats.

asff.png -->1.png
jgsds.png -->2.png
khjbfk.png-->3.png
name.png-->4.png
'''

import os
files=os.listdir("clutterfolder")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutterfolder/{file}",f"clutterfolder/{i}.png")
        i=i+1
    print(file)

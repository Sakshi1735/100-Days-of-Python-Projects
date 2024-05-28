#seek() and tell()

'''with open('file.txt','r') as f:
    print(type(f))
    f.seek(10) #move to the 10th byte in the file
    print(f.tell()) #tell the current position of the cursor
    data = f.read(5) #read the next 5 bytes
    print(data )
'''


#truncate()
with open('file.txt','w') as f:
    f.write('Hello World')
    f.truncate(5) # keeping the size of the file to a particular size by truncating it.
with open('file.txt','r') as f:
    print(f.read())


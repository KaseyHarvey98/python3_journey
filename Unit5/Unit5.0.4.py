import os

def lister(path):
    for filename in os.listdir(path):
        newpath = os.path.join(path, filename)
        if os.path.isdir(newpath):
            print('***', filename)
            lister(newpath)
        else:
            print(filename)

lister('..')

import os
import sys


def fileAll(path):
    dirs = os.listdir(path)
    for item in dirs:
        itempath = path + item
        flag = os.path.isdir(itempath)
        if flag == True:
            fileAll(itempath + "/")
        else:
            flagfile = os.path.isfile(itempath)
            if flagfile == True:
                f = itempath.split('.')
                if f[-1] == 'jpg':
                    print(itempath)

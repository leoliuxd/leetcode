#!/bin/python
# -*- coding: UTF-8 -*-
import os

if __name__ == '__main__':
    pathDir = os.listdir('xunzhang')
    for allDir in pathDir:
        orginalDire = allDir
        allDir = allDir.replace('.',"@3x.")
        os.rename(os.path.join('./xunzhang/', orginalDire), os.path.join('./xunzhang/', allDir))
        print allDir

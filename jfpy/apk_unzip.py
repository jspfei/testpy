#!/usr/bin/python
# -*- coding: utf-8 -*-
import zipfile
def apk_un_zip(apkfile):
    filedir ='data/'
    r = zipfile.is_zipfile(apkfile)
    if r:
        fz = zipfile.ZipFile(apkfile,'r')
        for file in fz.namelist():
            #print(file)
            fz.extract(file,filedir)
    else:
        print "This file is not zip file"

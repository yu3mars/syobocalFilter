#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, codecs, requests
import config

savedir = config.savedir
url = config.url

def LocalLoad():
    oldics = codecs.open("syobocal.ics","r","utf-8").readlines()
    newics = codecs.open("newcal_local.ics","w","utf-8")
    repattern = re.compile("#\d+")
    isVevent = False
    toCollect = False
    strls = []
    for s in oldics:
        if(isVevent):
            if(s=="END:VEVENT\r\n"):
                isVevent = False
                if(toCollect):
                    strls.append(s)
                    for st in strls:
                        newics.writelines(st)
                    toCollect = False
                strls = []
            else:
                if(s.startswith("SUMMARY:")):
                    if(s.find("【新】")>=0 or s.find("【注】")>=0 or (s.find("【！】")>=0 and repattern.search(s)==None)):
                        toCollect = True
                strls.append(s)
        else:
            if(s == "BEGIN:VEVENT\r\n"):
                isVevent = True
                strls.append(s)
            else:
                newics.write(s)
    oldics.close()
    newics.close()

def UrlLoad():
    oldics = requests.get(url).text.splitlines()
    newics = codecs.open(savedir + "newcal.ics","w","utf-8")
    repattern = re.compile("#\d+")
    isVevent = False
    toCollect = False
    strls = []
    for s in oldics:
        if(isVevent):
            if(s=="END:VEVENT"):
                isVevent = False
                if(toCollect):
                    strls.append(s)
                    for st in strls:
                        newics.write(st)
                        newics.write("\r\n")
                    toCollect = False
                strls = []
            else:
                if(s.startswith("SUMMARY:")):
                    if(s.find("【新】")>=0 or s.find("【注】")>=0 or (s.find("【！】")>=0 and repattern.search(s)==None)):
                        toCollect = True
                strls.append(s)
        else:
            if(s == "BEGIN:VEVENT"):
                isVevent = True
                strls.append(s)
            else:
                newics.write(s)
                newics.write("\r\n")
    newics.close()

def main():
    #LocalLoad()
    UrlLoad()

if __name__ == '__main__':
    main()

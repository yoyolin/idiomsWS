# -*- coding: utf-8 -*-
import os, sys, glob, re
import pandas as pd

def main():
    dir = "E:\\Codes\\PycharmProjects\\idiomsWS\\idioms\\"

    #open all idioms files
    idioms_allfiles = {}
    for fileName in glob.glob(dir + '*.txt'):
        with open(fileName) as f:
            idioms = f.readlines()
            idioms_4word = [i  for i in idioms if len(i) == 13]
            f.close()
        idioms_count = int(re.findall(r'\d+', fileName)[0])
        idioms_allfiles[idioms_count] = idioms_4word

    #construct first three levels
    idioms_219 =  set(idioms_allfiles[219])
    idioms_276 = set(idioms_allfiles[276])
    idioms_634 = set(idioms_allfiles[634])
    junior = idioms_276 - idioms_219
    middle = idioms_219
    high = idioms_634 -  (junior|middle)
    print len(junior), len(middle), len(high)

    #save to csv
    idioms = list(junior) + list(middle) + list(high)
    level = [1]*len(junior) + [2]*len(middle)+[3]*len(high)
    idioms_levels = {"idioms":idioms, "level": level}
    idioms_df = pd.DataFrame( data = idioms_levels)
    idioms_df.to_csv("idioms_with_levels.csv",encoding='utf-8-sig')

if __name__ == "main":
    main()


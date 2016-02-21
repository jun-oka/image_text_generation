#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# from __future__ import print_function
# import argparse
# import os
# import sys
# import random

# import cv2
# import numpy as np
# from PIL import Image

# import chainer
# from chainer import cuda
# import chainer.functions as F
# from chainer.functions import caffe

#cvsから文章を取ってくる
import pandas as pd
from generate import wakati
import random
#import os
#sos.chdir("/Users/kano/Documents/python_practice/chainer/examples/image_text_generation_local/final_project")

# sys.path.append('/document_random_generate')

def make_random_text(label):

    #pandasでcsvを読み込み
    df = pd.read_csv('table01.csv', encoding="SHIFT-JIS")
    print(label)

    #カテゴリの行を選択
    df_selected = df[df['category'] == 'wig']
    df_selected_column = df_selected["text"]
    #print df_selected_column

    #dataFrameを配列に変換
    message = ""
    numpyMatrix = df_selected_column.as_matrix()
    for i in numpyMatrix:
        message += str(i.encode("utf-8"))
        wordlist = wakati(message)

    # Create table of Markov Chain
    markov = {}
    prev1 = ""
    prev2 = ""
    for word in wordlist:
        if prev1 and prev2:
            if not prev2 in markov:
                markov[prev2] = {}
            if not prev1 in markov[prev2]:
                markov[prev2][prev1] = []
            markov[prev2][prev1].append(word)
        prev2 = prev1
        prev1 = word

    # Generate Sentence
    count = 0
    prev2= random.choice(list(markov.keys()))
    prev1 = random.choice(list(markov[prev2].keys()))
    sentence = prev2 + prev1
    while count < 20:
        tmp = random.choice(markov[prev2][prev1])
        sentence += tmp
        prev2 = prev1
        prev1 = tmp
        count += 1

    print(sentence)
    #str_numpyMatrix = str(numpyMatrix)

    #print str_numpyMatrix 

    # tmp_message  = ""

    # for line in numpyMatrix:
    # 	tmp_message  += line[1]

    # message = str(tmp_message)
    # print message   
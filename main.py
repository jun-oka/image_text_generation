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
from generate import generate_sentence
import sys
import codecs

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# sys.path.append('/document_random_generate')

#pandasでcsvを読み込み
df = pd.read_csv('table01.csv',encoding='SHIFT-JIS')

#カテゴリの行を選択
df_selected = df[df['category'] == 'wig']
df_selected_column = df_selected["text"]
# print df_selected_column

#dataFrameを配列に変換
numpyMatrix = df_selected_column.as_matrix()
str_numpyMatrix = str(numpyMatrix)
# print str_numpyMatrix 

# tmp_message  = ""

# for line in numpyMatrix:
# 	tmp_message  += line[1]

# message = str(tmp_message)
# print message   

result = wakati(str_numpyMatrix)
sentence = generate_sentence(result)

# print result
print sentence
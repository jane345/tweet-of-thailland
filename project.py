from deepcut import DeepcutTokenizer
import deepcut
import csv
import string
import pandas as pd
import numpy as np

def tokenized_word(df):
    # token = df.map(deepcut.tokenize)
    token = deepcut.tokenize(df)
    tokenizer = DeepcutTokenizer(ngram_range=(1,1),stop_words='thai')
    # df['word']= token.map(tokenizer._word_ngrams)
    word = tokenizer._word_ngrams(token)
    #print(df)
    #df.to_csv('tokenizing.csv',index = None)
    return word
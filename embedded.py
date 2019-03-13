import string
import pandas as pd
import numpy as np
import gensim.models.keyedvectors as word2vec
from scipy import spatial


def avg_sentence_vector(sentence, model, num_features, index2word_set):
    words = sentence
    feature_vec = np.zeros((num_features), dtype=object ).T
    n_words = 0
    for word in words:
        if word in index2word_set:
            n_words += 1
            feature_vec = np.add(feature_vec, model[word])
    if (n_words > 0):
        feature_vec = np.divide(feature_vec, n_words)
    return feature_vec

def embedded_word(df):
    model = word2vec.KeyedVectors.load_word2vec_format('wiki.th.text.model')
    index2word_set = (model.wv.index2word)
    vec = avg_sentence_vector(sentence=df, model=model, num_features=400,index2word_set=index2word_set)
    # vec = df.map(lambda x: avg_sentence_vector(sentence=x, model=model, num_features=400,index2word_set=index2word_set)).apply(np.array)
    #s1_afv = avg_sentence_vector(df.split[0], model=model, num_features=400,index2word_set=index2word_set)
    return vec

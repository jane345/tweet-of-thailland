# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.svm import SVC
import project
import embedded
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
true = []
test = []
test_dataset = pd.read_csv('G:\\senior\\dataset\\testing.csv', encoding = 'utf8')
'''
print(0)
test_token = project.tokenized_word(test_dataset)
print(1)
test_embedded = embedded.embedded_word(test_token)
test_embedded.to_pickle("df_test")
print(2)
'''

test_embedded = pd.read_pickle("df_test")
true_label = test_dataset.sentiment.values.tolist()
test_data = test_embedded.word2vec.values.tolist()

#model = pickle.load(open("G:\\senior\\model\\svm_linear.pkl", 'rb'))
#model = pickle.load(open("G:\\senior\\model\\SVM_rbf_new2.pkl", 'rb'))
model = pickle.load(open("G:\\senior\\model\\SVM_linear_new2.pkl", 'rb'))

prob = model.predict_proba(test_data)

for i in range(len(test_data)):
    #print(test_dataset.tweet[i] , prob[i])
    label = np.array2string(np.argmax(prob[i]))
    proba = np.amax(prob)
    a = np.array2string(test_dataset.sentiment[i])
    true.append(a)
    test.append(label)

labels = ['0','1','2']
print(confusion_matrix(true,test,labels=labels))
print(accuracy_score(test,true))
print(classification_report(true, test, target_names=labels))

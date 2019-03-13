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
from sklearn.metrics import multilabel_confusion_matrix
true = []
test = []
test_dataset = pd.read_csv('G:\\senior\\dataset\\testing_1.csv', encoding = 'utf8')
'''
print(0)
test_token = project.tokenized_word(test_dataset)
print(1)

test_embedded = embedded.embedded_word(test_token)
test_embedded.to_pickle("df_test_newdataset")
print(2)
'''
test_embedded = pd.read_pickle("df_test_newdataset")
true_label = test_dataset.subject.values.tolist()
test_data = test_embedded.word2vec.values.tolist()
print(len(true_label))

for i in range(len(true_label)):
        if test_dataset.subject[i]== 0 :
            l = [1,0,0,0]
        elif test_dataset.subject[i]== 1 :
            l = [0,1,0,0]
        elif test_dataset.subject[i]== 2:
            l = [0,0,1,0]
        elif test_dataset.subject[i]== 3:
            l = [0,0,0,1]
        true.append(l)
true1 = np.asarray(true)
print(true1)


model = pickle.load(open("G:\\senior\\model\\subject_rbf_multi.pkl", 'rb'))
#prob = model.predict_proba(test_data)
predict = model.predict(test_data)
print(predict)
print(model.score(test_data, true1, sample_weight=None))
print(multilabel_confusion_matrix(true,test))

'''for i in range(len(test_data)):
    label = np.array2string(np.argmax(prob[i]))
    proba = np.amax(prob)
    a = np.array2string(test_dataset.subject[i])
    true.append(a)
    test.append(label)

labels = ['0','1','2','3']'''

'''
print(confusion_matrix(true1.argmax(axis=1),predict.argmax(axis=1)))
print(accuracy_score(predict,true1))
print(classification_report(true1,predict, target_names=labels))
'''
'''
print(confusion_matrix(true,test))
print(accuracy_score(test,true))
print(classification_report(true,test, target_names=labels))'''

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


model_sentiment = pickle.load(open("E:\\Senior_Project\\1_code\\deep\\website(vue)\\my-project\\SVM_linear_new.pkl", 'rb'))
model_subject = pickle.load(open("E:\\Senior_Project\\1_code\\deep\\website(vue)\\my-project\\subject_rbf_multi.pkl", 'rb'))
status = 'อาหารอร่อยมากกกกกกกกกกกกก'
token = project.tokenized_word(status)
embedded = embedded.embedded_word(token).reshape(1,-1)

predict_sentiment = model_sentiment.predict_proba(embedded)
predict_subject = model_subject.predict(embedded)

sentiment = np.array2string(np.argmax(predict_sentiment))
subject = np.array2string(np.argmax(predict_subject))



# -*- coding: utf-8 -*-
"""SupportVectorMachineModeling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cz_NbfelDBMXwVZZso2fbDqhhvQ7uVMe

## Support Vector Machine Modeling
"""

!pip install numpy
!pip install pandas
!pip install sklearn
!pip install statsmodels
!pip install matplotlib
!pip install seaborn

import matplotlib.pyplot as plt

# import random undersampling and other necessary libraries 
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
df = pd.read_csv("insurancedata.csv")
print(df.shape)
print(df.head())

"""## N : 0 / Y : 1 의 각각 비율 확인"""

df.SIU_CUST_YN.value_counts()

df.SIU_CUST_YN.value_counts(normalize=True).plot(kind='bar', color = "black")
print(df.SIU_CUST_YN.value_counts(normalize=True)*100)

"""## 데이터 추가정제

데이터에 맞춰서 하나만 실행
"""

#insurance data

df['SIU_CUST_YN'].replace('N', 0, inplace = True)
df['SIU_CUST_YN'].replace('Y', 1, inplace = True)
df['FP_CAREER'].replace('N', 0, inplace = True)
df['FP_CAREER'].replace('Y', 1, inplace = True)
df.drop(['Unnamed: 0'], axis=1, inplace = True)
df.drop(['TOTALPREM'], axis=1, inplace = True)

X = df.iloc[:,1:] # SIU_CUST_YN을 제외한 모든 cloumn
y = df.iloc[:,0] # SIU_CUST_YN

from collections import Counter
from sklearn.model_selection import train_test_split
# 트레이닝 데이터, 테스트 데이터 설정
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# 현재 트레이닝 데이터 확인
print("Before Sampling: ",Counter(y_train))

"""## OverSampling Test Module"""

from imblearn.over_sampling import SMOTE
# OverSampling 방법(SMOTE)
SMOTE = SMOTE()
# OverSampling 실행
X_train_SMOTE, y_train_SMOTE = SMOTE.fit_resample(X_train, y_train)
# OverSampling 결과 데이터 확인
print("Before Sampling: ",Counter(y_train))
print("After oversampling(SMOTE): ",Counter(y_train_SMOTE))

from imblearn.over_sampling import BorderlineSMOTE
# OverSampling 방법(BSMOTE)
BSMOTE = BorderlineSMOTE()
# OverSampling 실행
X_train_BSMOTE, y_train_BSMOTE = BSMOTE.fit_resample(X_train, y_train)
# OverSampling 결과 데이터 확인
print("Before Sampling: ",Counter(y_train))
print("After oversampling(BSMOTE)): ",Counter(y_train_BSMOTE))

from imblearn.over_sampling import ADASYN
# OverSampling 방법(ADASYN)
ADASYN = ADASYN()
# OverSampling 실행
X_train_ADASYN, y_train_ADASYN = ADASYN.fit_resample(X_train, y_train)
# OverSampling 결과 데이터 확인
print("Before Sampling: ",Counter(y_train))
print("After oversampling(ADASYN): ",Counter(y_train_ADASYN))

from imblearn.over_sampling import SVMSMOTE
# OverSampling 방법(SVMSMOTE)
SVMSMOTE = SVMSMOTE()
X_train_SVMSMOTE, y_train_SVMSMOTE = SVMSMOTE.fit_resample(X_train, y_train)
print("Before Sampling: ",Counter(y_train))
print("After oversampling(ADASYN): ",Counter(y_train_SVMSMOTE))

"""## Sampling 방식 선택"""

# 해당 변수를 설정해서 Sampling 방식 선택 후 머신러닝 실행
X_train_sampling = X_train_SVMSMOTE
y_train_sampling = y_train_SVMSMOTE

"""## 결과 확인"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_sampling = scaler.fit_transform(X_train_sampling)
X_test = scaler.transform(X_test)

# 기본svm
from sklearn.svm import SVC
model = SVC()
model.fit(X_train_sampling, y_train_sampling)

# sklearn에서 제공하는 score값
print(model.score(X_test, y_test))

print(model.predict(X_test))

predict_X = model.predict(X_test)

# 비중.
persentage = 0.5

from sklearn.metrics import confusion_matrix, accuracy_score,precision_score,recall_score,f1_score


print('Persentage : 0.5')
print('Just result')
print("---------------------------")
print('accuracy: %.2f' % accuracy_score(y_test, predict_X))
print('precision: %.2f' % precision_score(y_test, predict_X))
print('recall: %.2f' % recall_score(y_test, predict_X))
print('F1: %.2f' % f1_score(y_test, predict_X))

import seaborn as sns
confusion = confusion_matrix(y_true = y_test
                             , y_pred = predict_X)

plt.figure(figsize=(4, 3))
sns.heatmap(confusion, annot=True, annot_kws={'size':15}, cmap='OrRd', fmt='.10g')
plt.title('Confusion Matrix')
plt.show()

# rbf kernel 활용
from sklearn import svm
model = svm.SVC(kernel='rbf',gamma=10)
model.fit(X_train_sampling, y_train_sampling)

# sklearn에서 제공하는 score값
print(model.score(X_test, y_test))

print(model.predict(X_test))

predict_X = model.predict(X_test)

# 비중.
persentage = 0.5

from sklearn.metrics import confusion_matrix, accuracy_score,precision_score,recall_score,f1_score


print('Persentage : 0.5')
print('Just result')
print("---------------------------")
print('accuracy: %.2f' % accuracy_score(y_test, predict_X))
print('precision: %.2f' % precision_score(y_test, predict_X))
print('recall: %.2f' % recall_score(y_test, predict_X))
print('F1: %.2f' % f1_score(y_test, predict_X))

import seaborn as sns
confusion = confusion_matrix(y_true = y_test
                             , y_pred = predict_X)

plt.figure(figsize=(4, 3))
sns.heatmap(confusion, annot=True, annot_kws={'size':15}, cmap='OrRd', fmt='.10g')
plt.title('Confusion Matrix')
plt.show()

# poly kernel 활용
from sklearn import svm
model = svm.SVC(kernel='poly',degree=2) #degree는 차원수
model.fit(X_train_sampling, y_train_sampling)

# sklearn에서 제공하는 score값
print(model.score(X_test, y_test))

print(model.predict(X_test))

predict_X = model.predict(X_test)

# 비중.
persentage = 0.5

from sklearn.metrics import confusion_matrix, accuracy_score,precision_score,recall_score,f1_score


print('Persentage : 0.5')
print('Just result')
print("---------------------------")
print('accuracy: %.2f' % accuracy_score(y_test, predict_X))
print('precision: %.2f' % precision_score(y_test, predict_X))
print('recall: %.2f' % recall_score(y_test, predict_X))
print('F1: %.2f' % f1_score(y_test, predict_X))

import seaborn as sns
confusion = confusion_matrix(y_true = y_test
                             , y_pred = predict_X)

plt.figure(figsize=(4, 3))
sns.heatmap(confusion, annot=True, annot_kws={'size':15}, cmap='OrRd', fmt='.10g')
plt.title('Confusion Matrix')
plt.show()


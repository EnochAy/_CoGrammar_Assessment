#Load Libraries
import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import imblearn

#Load datasets
df1 = pd.read_csv("C:/Users/HP/Desktop/Co_Grammar/aug_train.csv")
df2 = pd.read_csv("C:/Users/HP/Desktop/Co_Grammar/aug_test.csv")

#Data Analysis and Visualization
df1.head()
df2.head()

df1.dtypes

df1.isnull().sum()

#Visualizations
#Churn vs. normal 
sns.countplot(df1.target)


#Frequency of each category separated by label
plt.figure(figsize=[15,18])
features = ['gender','relevent_experience','enrolled_university','education_level', 'major_discipline',
       'experience','company_size','company_type','last_new_job']
n=1
for f in features:
    plt.subplot(5,2,n)
    sns.countplot(x=f, hue='target', alpha=0.7, data=df1)
    plt.title("Countplot of {}  by target".format(f))
    n=n+1
plt.tight_layout()
plt.show()

np.array(df1.columns[df1.dtypes != object])


#2. Data Preprocessing
import copy
df_train=copy.deepcopy(df1)
df_test=copy.deepcopy(df2)

cols=np.array(df1.columns[df1.dtypes != object])
for i in df_train.columns:
    if i not in cols:
        df_train[i]=df_train[i].map(str)
        df_test[i]=df_test[i].map(str)
df_train.drop(columns=cols,inplace=True)
df_test.drop(columns=np.delete(cols,len(cols)-1),inplace=True)


df_train.columns



#Data Encoding
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict

# build dictionary function
cols=np.array(df1.columns[df1.dtypes != object])
d = defaultdict(LabelEncoder)

# only for categorical columns apply dictionary by calling fit_transform 
df_train = df_train.apply(lambda x: d[x.name].fit_transform(x))
df_test=df_test.apply(lambda x: d[x.name].transform(x))
df_train[cols]=df1[cols]
df_test[np.delete(cols,len(cols)-1)]=df1[np.delete(cols,len(cols)-1)]


df_train.dtypes

df_test.columns


import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns
style.use('ggplot')
sns.set_style('whitegrid')
plt.subplots(figsize = (12,7))
## Plotting heatmap. # Generate a mask for the upper triangle (taken from seaborn example gallery)
mask = np.zeros_like(df_train.corr().apply(abs), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(df_train.corr().apply(abs), cmap=sns.diverging_palette(20, 220, n=200), annot=True, mask=mask, center = 0, )
plt.title("Heatmap of all the Features of Train data set", fontsize = 25)



# visualizing the features with positive and negative correlation
f, axes = plt.subplots(nrows=3, ncols=3, figsize=(20,15))

f.suptitle('Features With High Correlation', size=35)
sns.boxplot(x="target", y="city", data=df_train, ax=axes[0,0])
sns.boxplot(x="target", y="gender", data=df_train, ax=axes[0,1])
sns.boxplot(x="target", y='relevent_experience', data=df_train, ax=axes[0,2])
sns.boxplot(x="target", y='enrolled_university', data=df_train, ax=axes[1,0])
sns.boxplot(x="target", y='education_level', data=df_train, ax=axes[1,1])
sns.boxplot(x="target", y='company_size', data=df_train, ax=axes[1,2])
sns.boxplot(x="target", y='company_type', data=df_train, ax=axes[2,0])
sns.boxplot(x="target", y='enrollee_id', data=df_train, ax=axes[2,1])
sns.boxplot(x="target", y='training_hours', data=df_train, ax=axes[2,2])


counts = df1.target.value_counts()
not_change = counts[0]
change = counts[1]
perc_not_change = not_change*100/ sum(counts)
perc_change = change*100/ sum(counts)
print('There were {} not_change ({:.2f}%) and {} change ({:.2f}%).'.format(not_change, perc_not_change, change, perc_change))


#From this we can clearly see that the target 0 is in majority which will effect our model so we will use SMOTE 
# (Synthetic Minority Over-sampling Technique) which will help us to create more synthetic data for the minority class 1 :)
# Dealing with Data Imbalance using SMOTE
X=df_train.drop(columns=['target']).values #Predictor Variables
y=df_train['target'].values #Response Variable




def oversample(X, y, ss=1):
    from collections import Counter
    from imblearn.over_sampling import SVMSMOTE
    from numpy import where

# summarize class distribution
    print("Original class distribution:")
    counter = Counter(y)
    print(counter)
    
# transform the dataset
    X, y = SVMSMOTE(sampling_strategy=ss,n_jobs=-1).fit_resample(X, y)
    
    print("Over sampling done using SVM SMOTE.\nNew class distribution is:")
# summarize the new class distribution
    counter = Counter(y)
    print(counter)
    
    return X, y

    X, y = oversample(X,y)
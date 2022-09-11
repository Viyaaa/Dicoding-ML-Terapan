# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FQYtFuBV4pRgECFfWaS-RIP0KUgVabbC

#### Melakukan setup untuk dapat mengunduh dataset secara langsung pada Kaggle
"""

! pip install kaggle

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
  
# Then move kaggle.json into the folder where the API expects to find it.
!mkdir -p ~/.kaggle/ && mv kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json

! kaggle datasets download -d wisnuanggara/daftar-harga-rumah

! unzip daftar-harga-rumah.zip

"""#### Melakukan import library"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

from sklearn.preprocessing import  OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

"""Mengimport dataset dan memasukkannya kedalam DataFrame"""

file_name = '/content/DATA RUMAH.xlsx'
df = pd.read_excel(file_name)

df

df.info()

"""Mengganti tipe beberapa data menjadi tipe object"""

df[['KT', 'KM', 'GRS']] = df[['KT', 'KM', 'GRS']].astype(str).astype(object)

df.info()

"""Membuat kolom baru berupa harga dalam satuan juta, dan membuang kolom nomor, nama rumah, dan harga"""

df['HARGA (JT)'] = df['HARGA']//1000000
df = df.drop(columns=['NO', 'HARGA', 'NAMA RUMAH'])
df

df.describe()

"""#### EDA"""

sns.boxplot(x=df['HARGA (JT)'])

sns.boxplot(x=df['LB'])

sns.boxplot(x=df['LT'])

"""Karena data memiliki outliers yang besar, maka digunakan teknik IQR untuk menangani outliers"""

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR=Q3-Q1
df=df[~((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))).any(axis=1)]
 
df.shape

df.hist(bins=50, figsize=(15,5))
plt.show()

categorical_features = ['KT', 'KM', 'GRS']

feature = categorical_features[0]
count = df[feature].value_counts()
percent = 100*df[feature].value_counts(normalize=True)
new_df = pd.DataFrame({'jumlah kamar tidur': count,
                   'persentase': percent.round(1)})
print(new_df)
count.plot(kind='bar', title=feature)

feature = categorical_features[1]
count = df[feature].value_counts()
percent = 100*df[feature].value_counts(normalize=True)
new_df = pd.DataFrame({'jumlah kamar mandi': count,
                   'persentase': percent.round(1)})
print(new_df)
count.plot(kind='bar', title=feature)

feature = categorical_features[2]
count = df[feature].value_counts()
percent = 100*df[feature].value_counts(normalize=True)
new_df = pd.DataFrame({'jumlah mobil yang muat dalam garasi': count,
                   'persentase': percent.round(1)})
print(new_df)
count.plot(kind='bar', title=feature)

cat_features = df.select_dtypes(include='object').columns.to_list()
 
for col in cat_features:
  sns.catplot(x=col, y="HARGA (JT)", kind="bar", dodge=False, height = 4, aspect = 3,  data=df, palette="Set3")
  plt.title("Rata-rata 'Harga' Relatif terhadap - {}".format(col))

sns.pairplot(df, diag_kind = 'kde')

"""Membuat heatmap untuk melihat korelasi pada fitur numerik"""

plt.figure(figsize=(6, 5))
correlation_matrix = df.corr().round(2)
 
# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=12)

"""Melakukan One Hot Encoding pada beberapa fitur kategorikal"""

df = pd.concat([df, pd.get_dummies(df['KT'], prefix='KT')],axis=1)
df = pd.concat([df, pd.get_dummies(df['KM'], prefix='KM')],axis=1)
df = pd.concat([df, pd.get_dummies(df['GRS'], prefix='GRS_MOBIL')],axis=1)
df.drop(['KT', 'KM', 'GRS'], axis=1, inplace=True)

df

sns.pairplot(df[['LT', 'LB']], plot_kws={"s": 2});

"""Membagi data menjadi train dan test"""

X = df.drop(["HARGA (JT)"],axis =1)
y = df["HARGA (JT)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""Melakukan standarisasi"""

numerical_features = ['LT', 'LB']
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

X_train[numerical_features].describe().round(2)

"""#### Membuat model"""

models = pd.DataFrame(index=['train_mse', 'test_mse'],
                      columns=['Boosting', 'RandomForest', 'knn'])

RF = RandomForestRegressor(n_estimators=150, max_depth=16, random_state=100)
RF.fit(X_train, y_train)
 
models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

boosting = AdaBoostRegressor(random_state=100, learning_rate=0.001, n_estimators=50)
boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

knn = KNeighborsRegressor(n_neighbors=13)
knn.fit(X_train, y_train)
 
models.loc['train_mse','knn'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)
models

X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

"""Membuat metrik MSE untuk menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai yang diprediksi"""

mse = pd.DataFrame(columns=['train', 'test'], index=['RF','Boosting', 'KNN'])
 
# Buat dictionary untuk setiap algoritma yang digunakan
model_dict = {'RF': RF, 'Boosting': boosting, 'KNN': knn}
 
# Hitung Mean Squared Error masing-masing algoritma pada data train dan test
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e4
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e4
 
# Panggil mse
mse

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

prediksi = X_test.iloc[:20].copy()
pred_dict = {'y_true':y_test[:20]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)
 
pd.DataFrame(pred_dict)

def render_predict_table(data, col_width=7.0, row_height=0.625, font_size=12,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
    predict_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
    predict_table.auto_set_font_size(False)
    predict_table.set_fontsize(font_size)

    for k, cell in predict_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax.get_figure(), ax

fig,ax = render_predict_table(pd.DataFrame(pred_dict), header_columns=0, col_width=2.5)
fig.savefig("table_predict.png")

x_ax = range(len(y_test[:25]))
plt.figure(figsize=(15,7))
plt.scatter(x_ax, y_test[:25], s=5, color="blue", label="original")
plt.plot(x_ax, boosting.predict(X_test.iloc[:25]), lw=0.8, color="red", label="predicted_Boost")
plt.plot(x_ax, knn.predict(X_test.iloc[:25]), lw=0.8, color="black", label="predicted_KNN")
plt.plot(x_ax, RF.predict(X_test.iloc[:25]), lw=0.8, color="green", label="predicted_RF")
plt.legend()
plt.show()
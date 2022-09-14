# Laporan Proyek Machine Learning - Grivia Trifosa Iskandar
## Domain Proyek

Teknologi memiliki peran besar dalam kehidupan manusia saat ini, termasuk salah satunya yaitu penggunaan Machine Learning untuk membantu manusia dalam menyelesaikan permasalahan komputasi yang rumit. Salah satu contohnya yaitu penggunaan Machine Learning untuk memprediksi harga rumah di Jakarta Selatan.

Menurut [Rahayuningtyas], rumah merupakan kebutuhan yang diperlukan bagi manusia sebagai tempat tinggal. Dalam kebutuhan untuk membeli rumah, terdapat beberapa aspek yang dapat dipertimbangkan untuk memberikan harga pada rumah. Dengan adanya penggunaan teknologi dalam memprediksi harga rumah, diharapkan agar dapat menghitung korelasi dari berbagai aspek-aspek pada rumah tersebut, sehingga dapat memberikan informasi mengenai harga rumah yang sesuai dengan keadaan. 

Berdasarkan [dataset] ini, akan dilatih model Machine Learning yang mampu untuk memprediksi harga rumah yang ada di Tebet, Jakarta Selatan. Penulis akan menyelesaikan permasalahan prediksi ini dengan model regressi, dan model akan menghasilkan harga rumah berdasarkan data yang telah dibagi menjadi data *train* dan data *test*.

## Business Understanding

### Problem Statements
- Apakah model dapat memprediksi harga rumah di daerah Tebet, Jakarta Selatan dengan baik?

### Goals
- Mengetahui model yang terbaik untuk memprediksi harga rumah di daerah Tebet, Jakarta Selatan

### Solution Statements
- Menggunakan EDA untuk dapat melihat fitur yang berkorelasi dan memiliki pengaruh terhadap harga rumah
- Menggunakan Model Machine Learning yang sesuai, yaitu regresi. Terdapat beberapa model yang akan digunakan untuk melihat model mana yang akan menghasilkan nilai prediksi harga rumah yang terbaik. Berikut model-model yang akan digunakan:
    - *K-Neighbors Regressor*
    - *AdaBoost Regressor*
    - *Random Forest Regressor*

## Data Understanding
[Dataset] yang digunakan ini diambil dari platform Kaggle yang dipublikasikan oleh Wisnu Anggara. [Dataset] ini terdiri dari 2 file *.xlsx* yaitu data untuk rumah yang ada di Jakarta Selatan dan data untuk rumah yang ada di Tebet, salah satu daerah di Jakarta Selatan. Berikut akses link menuju dataset www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah. Data pada tiap file dataset memiliki sekitar 1000 data. Proyek ini menggunakan file dataset untuk rumah yang ada di Tebet, dengan penjelasan fitur sebagai berikut.
- NO : nomor data.
- NAMA RUMAH : title rumah.
- HARGA : harga dari rumah.
- LB : jumlah luas bangunan.
- LT : jumlah luas tanah.
- KT : jumlah kamar tidur.
- KM : jumlah kamar mandi.
- GRS : jumlah kapasitas mobil dalam garasi.

Selain itu, dilakukan juga *Exploratory Data Analysis* (EDA) yang bertujuan untuk menghilangkan outliers, serta menampilkan korelasi antar data baik data kategorikal maupun data numerik.

Berikut merupakan visualisasi boxplot dari data numerik dari LT, LB, dan Harga (JT).

![Visualisasi BoxPlot Harga (JT)](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download.png)

![Visualisasi BoxPlot LB](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(1).png)

![Visualisasi BoxPlot LT](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(2).png)

Dapat dilihat dari ketiga gambar tersebut, semua fitur memiliki outliers. Oleh karena itu, digunakan metode *Interquartile Range* (IQR) untuk mengatasi outliers tersebut. Sehingga, nantinya data akan direduksi dan dieliminasi guna mengatasi outliers.

Selanjutnya, dilakukan *univariate analysis* untuk data kategorikal dan data numerik. 

![Visualisasi Data Kategorikal KT](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(4).png)

Dari gambar diatas dapat disimpulkan bahwa pada fitur KT (Jumlah Kamar Tidur), data terbanyak ditempati oleh 4 kamar tidur dan data tersedikit ditempati oleh 10 kamar tidur.

![Visualisasi Data Kategorikal KT](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(5).png)

Dari gambar diatas dapat disimpulkan bahwa pada fitur KM (Jumlah Kamar Mandi), data terbanyak ditempati oleh 3 kamar mandi dan data tersedikit ditempati oleh 10 kamar mandi.

![Visualisasi Data Kategorikal KT](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(6).png)

Dari gambar diatas dapat disimpulkan bahwa pada fitur GRS (Jumlah Mobil yang Muat Dalam Garasi), data terbanyak ditempati oleh 2 mobil dan data tersedikit ditempati oleh 6 mobil.

Visualisasi data numerik dilakukan dengan menggunakan plot histogram.

![Visualisasi Data Numerik](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(3).png)

Dari gambar diatas, dapat ditarik kesimpulan, yaitu:
- Pada data "Harga (JT)", data rumah kebanyakan terdapat direntang 2.500.000.000 hingga 5.000.000.000
- Distribusi data miring ke kanan (right skewed) yang dimana akan berdampak pada hasil prediksi model.

Selain itu, terdapat juga EDA *multivariate analysis* untuk data kategorikal dan data numerik.

![Visualisasi Data Kategorikal](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(7).png)
![Visualisasi Data Kategorikal](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(12).png)
![Visualisasi Data Kategorikal](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(13).png)

Dari data diatas, dapat disimpulkan:
- Data pada KT (Jumlah Kamar Tidur), jumlah kamar tidur 10 memiliki nilai yang rendah, sehingga dapat disimpulkan fitur KT memiliki pengaruh dampak yang kecil terhadap rata-rata harga.
- Data pada KT (Jumlah Kamar Mandi), jumlah kamar mandi 10 memiliki nilai yang mirip dengan nilai yang lain, sehingga dapat disimpulkan fitur KM memiliki pengaruh dampak yang kecil terhadap rata-rata harga.
- Data pada GRS (Jumlah Mobil yang Muat di Garasi), dimana 6 mobil yang muat di garasi memiliki nilai tertinggi dibanding yang lain, sehingga dapat disimpulkan fitur GRS memiliki dampak terhadap rata-rata harga.

Pada data numerik, digunakan pairplot untuk melihat hubungan antara data fitur dan data target.

![Visualisasi Data Kategorikal](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(8).png)

Dapat disimpulkan berdasarkan gambar diatas, bahwa fitur "LB" dan "LT" memiliki hubungan data yang positif dengan data "Price".

Serta terdapat juga heatmap yang bertujuan untuk memvisualisasikan korelasi antara fitur "LB" dan "LT" dengan data "Price" agar lebih mudah untuk dilihat dan dipahami.

![Visualisasi Data Kategorikal](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(9).png)

## Data Preparation
- Mengatasi outliers dengan menggunakan metode *Interquartile Range* (IQR) yang akan berdampak pada pengurangan data pada dataset.
- Melakukan one hot encoding pada data-data kategorikal dengan menggunakan fungsi *get_dummies* pada library Pandas, dimana data diubah menjadi bilangan biner.
- Membagi data menjadi data train dan data test dengan fungsi *train_test_split*. Pembagian data dilakukan sebanyak 80% untuk data train dan 20% untuk data test.
- Melakukan standarisasi untuk fitur numerik agar menghasilkan nilai standar deviasi sama dengan 1 dan mean sama dengan 0. Standarisasi dilakukan agar memudahkan algoritma dalam melakukan komputasi perhitungan.

## Modeling

- Berikut penjelasan beberapa algoritma yang membantu dalam pembuatan model Machine Learning, dimana algoritma yang diambil merupakan algoritma bertipe regresi.
    - **Random Forest**, merupakan salah satu algoritma populer yang digunakan karena kesederhanaannya dan memiliki stabilitas yang baik. 
    - **K-Neighbors Regressor**, merupakan salah satu algoritma yang didasari oleh K-Nearest Neighbors. Algoritma ini memiliki kelebihan yaitu dapat melakukan komputasi yang baik pada data yang bersifat non-linear. Namun algoritma ini juga memiliki kelemahan yaitu sensitif terhadap noise seperti missing value atau outliers. 
    - **AdaBoost**, merupakan singkatan dari Adaptive Boosting. Algoritma ini bertujuan untuk memberikan bobot lebih pada observasi yang tidak tepat atau disebut weak classification. 

- Berikut merupakan tahapan pembuatan model dengan beberapa algoritma yang berbeda.
    1. Sebelum membuat model, dilakukan dulu pembuatan DataFrame yang akan diisi dengan hasil MSE data train dan data test pada setiap algoritma. 
    2. Selanjutnya, dilakukan pembuatan model Random Forest dengan melakukan import library pada sklearn.ensemble yang mengambil fungsi RandomForestRegressor. Setelah itu membuat model dengan diisikan beberapa parameter seperti n_estimators=150, max_depth=16, dan random_state=100.
    3. Pada algoritma Boosting, melakukan import library sklearn.ensemble yang mengambil fungsi AdaBoostRegressor. Digunakan beberapa parameter seperti n_estimators=50, learning_rate=0.001, dan random_state=100.
    4. Pada tahapan ini, dilakukan import library sklearn.neighbors yang mengambil fungsi KNeighborsRegressor. Pada algoritma K-Neighbors Regressor, digunakan parameter n_neighbors=13.
    *Catatan: pada nilai yang terdapat pada tiap parameter diisi dengan angka acak dimana dilakukan *trial dan error* beberapa kali hingga mendapatkan nilai MSE yang terkecil dari hasil tersebut.

## Evaluation
Pada tahap evaluasi, digunakan Mean Squared Error (MSE) yang berfungsi untuk menghitung rata-rata jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi, serta memiliki formula sebagai berikut

![MSE Formula](https://www.gstatic.com/education/formulas2/472522532/en/mean_squared_error.svg)

MSE	=	mean squared error
n	=	jumlah dataset
Yi	=	nilai sebenarnya
Ŷi	=	nilai prediksi

Berikut merupakan hasil dari MSE yang dilakukan oleh ketiga model Machine Learning.

![Visualisasi Data Kategorikal](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(10).png)

Dapat dilihat pada gambar diatas, algoritma Random Forest memiliki nilai error yang paling kecil (berada di angka 52,6 untuk train dan 237 untuk test) dibandingkan kedua algoritma lainnya. Sedangkan untuk algoritma Boosting memiliki nilai error yang paling besar dibandingkan yang lainnya (berada di angka 317,32 untuk train dan 344,75 untuk test).

Selain itu terdapat juga tabel hasil prediksi model-model serta nilai aktual dan visualisasi plottingan yang menampilkan data test dengan data yang diprediksi oleh model Machine Learning. 

![Tabel Prediksi](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/table_predict.png)
![Visualisasi Data Kategorikal](https://raw.githubusercontent.com/Viyaaa/Dicoding-ML-Terapan/main/download%20(11).png)

Titik biru pada plot merupakan data test yang benar, dan garis plot berwarna merah diperuntukkan algoritma Boosting, garis hitam untuk algoritma KNN, dan garis hijau untuk algoritma Random Forest. Pada gambar diatas, dapat dilihat bahwa nilai prediksi untuk setiap algoritma tidak ada yang persis sama pada titik, yang ada hanya diantara diatas titik (artinya prediksi harga rumah lebih tinggi dari nilai aktual) atau dibawah titik (artinya prediksi harga rumah lebih rendah dari nilai aktual). Sebagai contoh, kita mengambil data pada titik ke-5, nilai aktualnya yaitu 2999, dan prediksi nilai yang paling mendekati titik yaitu prediksi model Random Forest di angka 2810,3, sedangkan prediksi model KNN di angka 3226,9 dan prediksi model Boosting di 3419,5.

## Kesimpulan
Pada proyek predictive analysis ini, dapat ditarik kesimpulan berdasarkan prediksi harga rumah yang ada di Tebet, Jakarta Selatan dengan menggunakan tiga model regresi Machine Learning, yaitu bahwa diantara Random Forest, K-Neighbors Regressor, dan AdaBoost, algoritma Random Forest lebih baik dibandingkan yang lainnya. Hal ini dapat dilihat dari nilai *Mean Squared Error* (MSE) yang dihasilkan lebih kecil dibandingkan yang lainnya. 


## Referensi
Febrion Rahayuningtyas, E., Novia Rahayu, F., Azhar, Y., &#38; Artikel, I. (2021). Prediksi Harga Rumah Menggunakan General Regression Neural Network. *Jurnal Informatika,8*(1), 59–66. https://ejournal.bsi.ac.id/ejurnal/index.php/ji/article/view/9036


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>
   [Dataset]: https://www.kaggle.com/datasets/wisnuanggara/daftar-harga-rumah
   [Wisnu Anggara]: https://www.kaggle.com/datasets/wisnuanggara/
   [Rahayuningtyas]: https://doi.org/10.31294/ji.v8i1.9036

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>


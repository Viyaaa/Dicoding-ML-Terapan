# Laporan Proyek Machine Learning - Grivia Trifosa Iskandar

### Project Overview
Pada zaman modern ini, teknologi telah berkembang dengan pesat, salah satunya yaitu untuk memberikan hiburan. Salah satu jenis hiburan yang bisa dinikmati oleh setiap orang yaitu menonton film melalui *smartphone* ataupun teknologi lainnya. Namun dengan banyaknya film sebagai hiburan, tentu tidak semua film dapat ditonton dan sesuai dengan minat setiap orang [[1]]. Untuk itulah dibuat sistem rekomendasi dengan *based-content filtering* dan *collaborative filtering*.

Berdasarkan [dataset] *Movie Lens*, akan dilakukan pembuatan model berdasarkan *content-based* dan *collaborative filtering* berdasarkan genre film yang ada.

### Business Understanding
#### Problem Statements
- Bagaimana cara membuat sistem rekomendasi berdasarkan genre film lainnya yang serupa?
- Bagaimana cara membuat sistem rekomendasi berdasarkan rating yang telah diberikan oleh *user* yang pernah menonton?
 
#### Goals
- Menghasilkan rekomendasi sejumlah film yang sesuai dengan genre film.
- Menghasilkan rekomendasi sejumlah film yang sesuai dengan preferensi pengguna berdasarkan rating yang telah diberikan sebelumnya.

#### Solution Statements
- Sistem rekomendasi akan menggunakan teknik *content-based filtering* untuk memberikan rekomendasi berdasarkan genre film yang serupa, dengan menggunakan *cosine similarity* untuk melihat kemiripan antar film serta *tf-idf vectorizer* untuk merepresentasikan fitur penting dari tiap kategori film.
- Selain itu, sistem rekomendasi juga akan menggunakan *collaborative filtering* untuk memberikan rekomendasi berdasarkan rating yang diberikan oleh user lain yang pernah menonton, dengan menggunakan *class RecommenderNet*.

### Data Understanding
[Dataset] yang digunakan ini diambil dari platform Kaggle yang dipublikasikan oleh Shubham Mehta. Dataset ini terdiri dari 4 file .csv, namun yang akan digunakan pada proyek kali ini hanya file movies.csv dan ratings.csv. Berikut merupakan akses link untuk dataset https://www.kaggle.com/datasets/shubhammehta21/movie-lens-small-latest-dataset. 

Data movie pada movies.csv berjumlah sebanyak 9742, sedangkan untuk ratings.csv memiliki rating sebanyak 100836. Berikut variabel-variabel yang terdapat pada movies.csv dan ratings.csv:
- **movies.csv**:
    - movieId: id pada film
    - title: judul film
    - genres: jenis ragam film
- **ratings.csv**:
    - userId: id user yang memberi rating pada film
    - movieId: id pada film
    - rating: nilai rating untuk film
    - timestamp: stempel waktu mewakili detik sejak (UTC) 1 Januari, 1970
- **links.csv**:
    - movieId: id pada film
    - imdbId: id film yang ada di website http://www.imdb.com/
    - tmbdId: id film yang ada di website https://www.themoviedb.org/
- **tags.csv**:
    - userId: id user yang memberi tag pada film
    - movieId: id pada film
    - tag: metadata yang dibuat pengguna tentang film
    - timestamp: stempel waktu mewakili detik sejak (UTC) 1 Januari, 1970

Berikut beberapa visualisasi hasil *Exploratory Data Analysis*(EDA) dari data movie dan data rating.

![movie info](https://i.ibb.co/chT5rPV/movie-info.png)

Dari gambar diatas, dapat dilihat bahwa terdapat 9742 data pada data movies. Hal ini sesuai dengan yang dideskripsikan pada platform Kaggle.

![rating info](https://i.ibb.co/5K0YK1s/rating-info.png)

Dari gambar diatas, dapat dilihat terdapat 100836 data rating.

![genres](https://i.ibb.co/591sX9m/genres-2.png)

Dari gambar diatas, dapat dilihat bahwa genre film terbanyak jatuh pada genre drama, yang dilanjutkan dengan komedi, dan thriller.

### Data Preparation
1. **Mengecek Nilai Null**. 
    Dilakukan pengecekan apakah terdapat nilai null pada fitur-fitur di data movie dan data rating.

    ![movie null](https://i.ibb.co/4Jrz1wK/movie-isnull.png)

    ![rating null](https://i.ibb.co/DWTbWy8/rating-isnull.png)

    Dari hasil diatas, dapat disimpulkan bahwa baik pada data movie dan data rating tidak memiliki nilai null.

2. ***Drop Duplicate* pada Judul Film**
    Selain itu, ternyata terdapat judul film yang sama dan lebih dari satu. Oleh karena itu, dilakukan juga penghapusan data judul yang sama pada data movie sehingga nantinya model dapat merekomendasikan film dengan baik.

    ![movie drop duplicates](https://i.ibb.co/5WZnzkQ/movie-drop-dup.png)

    Jumlah data movie dari penghapusan duplikasi judul menjadi sebanyak 9737 data.

#### Collaborative Filtering
1. Pada *Collaborative Filtering*, dilakukan *encoding* data untuk data user dengan data rating yang lalu nantinya data hasil encoding akan digabung kedalam satu DataFrame untuk training dan validasi.
2. Data kemudian dibagi menjadi data train dan data test dengan train_test_split sebanyak 80:20.

### Modeling
#### Content Based Filtering
Teknik *Content-Based filtering* merupakan teknik yang merekomendasikan sesuatu berdasarkan dengan item yang sudah populer sebelumnya. Misalnya jika terdapat seseorang yang menyukai film baru yang bergenre komedi, sistem dapat merekomendasikan film bergenre yang sama.

##### Kelebihan dan Kelemahan pada Teknik Content-Based Filtering
Kelebihan dari teknik ini yaitu sistem rekomendasi ini dapat merekomendasikan suatu item yang bahkan belum pernah di-rate oleh satu orang pun. Namun, terdapat juga kelemahan pada sistem ini yaitu item yang disajikan hanyalah item-item yang mirip ataupun sama dengan item sebelumnya sehingga hal ini menunjukkan tidak terlalu adanya variasi.

##### Tahapan Pemodelan dengan *Content-Based filtering*
Pada teknik *Content-Based filtering*, dilakukan penggunaan fungsi *tfidfvectorizer* yang bertujuan untuk mengambil fitur-fitur penting yang ada pada fitur genre movie. Setelah itu, data ditransformasikan menjadi bentuk matriks.

Setelah itu, digunakan fungsi *Cosine Similarity* dari library sklearn untuk mencari derajat kesamaan film sehingga film yang nantinya direkomendasikan akan memiliki kesamaan dalam segi genre, dan akan dilanjutkan dengan membuat fungsi sistem rekomendasi bernama *movie_recommendations()*. Pada fungsi ini, terdapat beberapa parameter antara lain yaitu:
- *movie_title*: nama film.
- *similarity_data*: disini diisi dengan nilai *default* yaitu *dataframe cosine similarity* yang sudah dibuat sebelumnya. 
- *items*: nama dan fitur yang akan dipakai untuk mendefinisikan kesamaan pada *movie_title*, dalam hal ini adalah data nama film dan data genrenya.
- *k*: banyaknya rekomendasi yang akan ditampilkan.

Pada fungsi *movie_recommendations()*, fungsi pertama kali akan mengambil data menggunakan argpartition, yang dimana akan mengambil sejumlah nilai k dari derajat kesamaan yang sudah dideklarasikan sebelumnya. Selanjutnya, dilakukan pengambilan data dengan kesamaan yang paling tinggi/besar, dan melakukan drop data film yang dijadikan acuan untuk mencari rekomendasi agar data film tidak akan ditampilkan.

Berikut merupakan beberapa contoh dari sistem rekomendasi dengan teknik *content-based filtering*.
Dari gambar dibawah ini, sistem menampilkan rekomendasi film yang mirip dengan film The Conjuring (2013)
![Film](https://i.ibb.co/dpK6XV7/conjuring.png)

![Gambar Pertama](https://i.ibb.co/D155ChS/download.png)

Dari gambar dibawah ini, sistem menampilkan rekomendasi film yang mirip dengan film The Jungle Book (1967)
![Film](https://i.ibb.co/ByjCWfn/junglebook.png)

![Gambar Kedua](https://i.ibb.co/vXSQzYn/download-1.png)

Dari gambar dibawah ini, sistem menampilkan rekomendasi film yang mirip dengan film Alvin and the Chipmunks: The Squeakquel (2009)
![Film](https://i.ibb.co/BjdNf7b/Alvin.png)

![Gambar Ketiga](https://i.ibb.co/RN0CNjf/download-2.png)

Dapat terlihat dari beberapa hasil rekomendasi yang ditampilkan diatas bahwa film-film yang direkomendasikan memiliki genre yang sama dengan genre film yang ditonton.

#### Collaborative Filtering
Pada teknik *Collaborative Filtering* mengusung konsep dimana sistem akan merekomendasikan item berdasarkan prediksi item yang mungkin disukai oleh pengguna. Pada teknik ini, salah satunya yaitu memanfaatkan deep learning yang akan memprediksi keluaran berupa rekomendasi film yang disukai berdasarkan film yang pernah dirating oleh user sebelumnya.

##### Kelebihan dan Kelemahan pada Teknik Collaborative Filtering
Kelebihan yang dimiliki oleh teknik ini yaitu dapat merekomendasikan item bahkan dalam kondisi dimana analisis data sulit dilakukan. Namun, terdapat juga kelemahan pada teknik ini yaitu membutuhkan data rating agar sistem dapat merekomendasikan item.

##### Tahapan Pemodelan dengan Collaborative Filtering
Teknik *Collaborative Filtering* memerlukan data yaitu data rating dari user lain. Setelah data movie dan data rating telah melalui tahap data preparation seperti encoding dan pembagian training dan validasi, dilakukan pembuatan class RecommenderNet. Pada model RecommenderNet dilakukan beberapa tuning pada hyperparameter untuk mendapatkan hasil terbaik pada model. Setelah itu, model akan dicompile dengan menggunakan Binary Crossentropy untuk menghitung loss function, Adam sebagai optimizer, serta RMSE sebagai metriks evaluasi. Berikut output dari proses training dengan batch_size sebesar 32 dan epochs sebanyak 25.

![training](https://i.ibb.co/dcDsq1V/training-model.png)

Berikut merupakan beberapa contoh dari sistem rekomendasi dengan teknik *collaborative filtering*.
Dari gambar dibawah ini, sistem menampilkan 5 rekomendasi film berdasarkan user 594 yang pernah memberikan rating tinggi pada beberapa film yang serupa.

![Film](https://i.ibb.co/TRgYHfV/collab.png)

### Evaluation
#### Content-Based Filtering
Pada teknik *content-based filtering*, metrik evaluasi yang digunakan yaitu metrik presisi. Dari metrik ini, akan dihitung berdasarkan rekomendasi item film yang memiliki genre yang sesuai dengan film.  Berikut rumus dari metrik presisi:

![rumus metrik presisi](https://hasty.ai/media/pages/docs/mp-wiki/metrics/accuracy/fcbf093d04-1653642321/11.png)

Yang dimana:
- *Accuracy*: Nilai akurasi
- *Number of correct predictions*: Banyaknya jumlah data yang benar
- *Total number of predictions*: Banyaknya jumlah data yang diprediksi

Dari hasil yang diberikan pada tahapan *Content-Based Filtering*, 5 dari 5 data film yang direkomendasikan memiliki genre yang sama, dan dilakukan sebanyak 3 kali pada film yang berbeda. Sehingga hal ini dapat disimpulkan bahwa akurasi yang dihasilkan yaitu sebesar 100%.

#### Collaborative Filtering
Berikut metrik evaluasi *Root Mean Squared Error* (RMSE) yang berfungsi untuk mengukur tingkat akurasi perkiraan dari suatu model. Semakin kecil nilai RMSE, semakin dekat nilai yang diprediksi. Berikut rumus dari RMSE:

![rumus rmse](https://media.geeksforgeeks.org/wp-content/uploads/20200622171741/RMSE1.jpg)

Yang dimana:
- Predicted(i) = Nilai prediksi
- Actual(i) = Nilai sebenarnya
- N = jumlah yang diobservasi

Berikut merupakan hasil RMSE dari model dengan teknik *collaborative filtering*.
![rmse](https://i.ibb.co/YQPrtJj/rmse.png)

Dapat dilihat nilai RMSE semakin menurun dan pada epoch ke 25 menyentuh angka 0.1924 untuk train dan 0.2006 untuk test.

### Kesimpulan
Pada proyek sistem rekomendasi yang telah dibuat, dengan menggunakan teknik *Content-Based Filtering*, didapatkan rekomendasi film-film yang memiliki genre yang sama. Ketika menggunakan teknik *Collaborative Filtering*, didapatkan hasil rekomendasi film yang mirip dengan film yang diberi rating tertinggi oleh user. Nilai RMSE yang didapat untuk model *Collaborative Filtering* yaitu berada pada angka 0.1924 untuk data train dan 0.2006 untuk data test.

### Referensi
Mondi, R. H., Wijayanto, A., &#38; Winarno. (2019). Recommendation system with content-based filtering method for culinary tourism in mangan application. *ITSMART: Jurnal Ilmiah Teknologi Dan Informasi, 8*(2). https://doi.org/10.20961/itsmart.v8i2.35008

Mutiasari, H., Purboyo, T. W., &#38; Nugrahaeni, R. A. (2021). Sistem Rekomendasi Film Menggunakan Metode K-means Clustering. *EProceedings of Engineering, 8*(5). https://openlibrarypublications.telkomuniversity.ac.id/index.php/engineering/article/view/16511/16220

Wijaya, A. E., &#38; Alfian, D. (2018). Sistem Rekomendasi Laptop Menggunakan Collaborative Filtering Dan Content-Based Filtering. *Jurnal Computech &#38; Bisnis, 12*(1). http://dx.doi.org/10.55281/jcb.v12i1.167

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [1]: https://openlibrarypublications.telkomuniversity.ac.id/index.php/engineering/article/view/16511/16220
   [dataset]: https://www.kaggle.com/datasets/shubhammehta21/movie-lens-small-latest-dataset

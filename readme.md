[header-dataset]: https://raw.githubusercontent.com/ksmrdn/Vertebrae_Diseases_Predict/master/Image-ReadMe/Header_DataSource.PNG "Data Sumber"
[work-flow]: https://raw.githubusercontent.com/ksmrdn/Vertebrae_Diseases_Predict/master/Image-ReadMe/workflow.PNG "Work Flow"
[home-flask]: https://raw.githubusercontent.com/ksmrdn/Vertebrae_Diseases_Predict/master/Image-ReadMe/home.PNG "Home Flask"
[form-flask]: https://raw.githubusercontent.com/ksmrdn/Vertebrae_Diseases_Predict/master/Image-ReadMe/form.PNG "Form Flask"
[result-flask]: https://raw.githubusercontent.com/ksmrdn/Vertebrae_Diseases_Predict/master/Image-ReadMe/result.PNG "Result Flask"
[spondy-1]: https://raw.githubusercontent.com/ksmrdn/Vertebrae_Diseases_Predict/master/Image-ReadMe/spondy-result1.PNG "Spondy-1"
[spondy-2]: https://raw.githubusercontent.com/ksmrdn/Vertebrae_Diseases_Predict/master/Image-ReadMe/spondy-result2.PNG "Spondy-2"
[spondy-3]: https://raw.githubusercontent.com/ksmrdn/Vertebrae_Diseases_Predict/master/Image-ReadMe/spondy-result4.PNG "Spondy-3"

# **MULTICLASSIFICATION: VERTEBRAE DISEASES PREDICT FROM PELVIS AND LUMBAR SPINE DATASET**
> #### Diagnosis secara otomatis bahwa pasien atau pengguna apakah normal atau terindikasi mengidap diantara dua penyakit mayor dalam kolom vertebrae dengan menggunakan dan membandingkan beberapa metode klasifikasi (Logistic Regression, KNearest Neighbors, Gaussian Naive Bayes, Decision Tree, Random Forest, dan Support Vector Machine) dan representasikan juga berupa produk berupa localhost web-based sebagai interface.

- **Dataset**: Dataset yang digunakan di dalam repository ini adalah dataset yang berasal dari Kumpulan data biomedis yang dibangun oleh Dr. Henrique da Mota selama masa tinggal medis di Kelompok Penelitian Terapan dalam Ortopedi (GARO) dari Pusat MÃ © dico-Chirurgical de RÃ © adaptasi des Massues, Lyon, Prancis.
<br>


!["http://archive.ics.uci.edu/ml/datasets/vertebral+column#"][header-dataset]

- **Sumber Data** : [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/vertebral+column#)

- **Purpose** : Diagnosis secara otomatis bahwa pasien atau pengguna apakah normal atau terindikasi mengidap diantara dua penyakit mayor dalam kolom vertebrae dan dipresentasikan juga berupa produk localhost web-based sebagai interface.

- **Machine Learning**: Logistic Regression, KNearest Neighbors, Gaussian Naive Bayes, Decision Tree, Random Forest, dan Support Vector Machine.

<hr>
<br>
Dalam repository ini, terdapat dokumentasi Notebook dan Folder Flask:

**Sebelum diproses mengaktifkan MySQL pada default port** <br>
> **File (``app_ortho.py``)**: Merupakan file aplikasi Flask dengan main server.
> **File (``Prepare_EDA.ipynb``)**: Merupakan file notebook berisi pengerjaan Exploratory Data Analysis (EDA).
> **File (``Prepare_EDA.ipynb``)**: Merupakan file notebook berisi pengerjaan Classification Modeling.

<hr>
<br>

## Penjelasan Data 

1. Features (Numerik)
    - ``Pelvic Incidence (PI)`` adalah sudut antara garis tegak lurus ke lempeng sakral di titik tengahnya, dan garis menghubungkan titik tesebut ke sumbu kepala femoralis (tulang paha).
    - ``Pelvic Tilt (PT)`` adalah sudut antara garis vertical dari kepala femoralis (tulang paha) dan garis menghubungkan titik tesebut ke sumbu kepala femoralis (tulang paha).
    - ``Sacral Slope (SS)`` adalah sudut dataran tinggi sakral horizontal dengan garis pelurus lempeng sakral.
    - ``Lumbar Lordosis (LL)`` adalah sudut antara T12 vertebrae dan dataran tinggi sakral horizontal 
    - ``Pelvic Radius (PR)`` adalah jari-jari panggul, jarak dari sumbu pinggul ke sudut posterior-superior S1 menunjukkan sumbu pinggul terletak di tengah antara dua titik tengah kepala femoralis.
    - ``Degree Spondylolisthesis (DS)`` dinilai berdasarkan derajat selip dari satu tubuh vertebral pada tubuh vertebral yang berdekatan.

2. TARGET (Categorical)
    - ``Class`` : (Herniated Disk (Hernia), Normal, Spondylolisthesis)

<hr>
<br>

# **WORKFLOW**
Alur pengerjaan project ialah seperti berikut.
![workflow][work-flow]

# **Flask Preview**
Berikut ini adalah preview App yang dibuat menggunakan Flask untuk menampilkan:
> * Tampilkan beranda interaksi
> * Input preferensi pasien/ user
> * Hasil prediksi 

## **Home**
Tampilan awal (``http://127.0.0.1:2070/``)  Laman beranda menjukkan interaksi awal kepada user/ pasien, mereka akan diberitahu bahwa web akan membutuhkan beberapa informasi dari radiologi yang dilakukan.

Web juga memberitahukan prediksi apa yang dapat atau akan dilakukan.

Apabila tombol Form ditekan, maka akan berfungsi untuk beranjak ke laman pengisian form.

Juga terdapat tombol __"Vertebrae Disease Medical Check"__, untuk kembali ke laman __"Home"__.

![alt text][home-flask]<br>

## **Form**
Tampilan selanjutnya (``http://127.0.0.1:2070/form``)  Laman __"form"__ menjukkan bagian yang meminta informasi apa saja yang harus diisi oleh user/ pasien. Hanya features yang sudah dijelaskan sebelumnya yang akan digunakan dalam prediksi.

Web juga menampilkan beberapa slide gambar mengenai pengetahuan akan features yang ada.

Apabila tombol __"Predict"__ ditekan, maka akan berfungsi untuk beranjak ke laman prediksi.


Juga terdapat tombol __"Vertebrae Disease Medical Check"__, untuk kembali ke laman __"Home"__.

![alt text][form-flask]<br>

## **Predict**
Tampilan akhir (``http://127.0.0.1:2070/predict``)  Laman __"predict"__ menjukkan bagian yang menampilkan informasi-informasi yang telah diisikan, lalu mempunyai judgement hasil prediksi apakah pasien __"normal, mengidap hernia disk, atau spondylolisthesis"__.

Ditampilkan juga persentase probabilitas akan masing-masing class, jadi informasi ini dapat memperkirakan sebesar apa prediksi yang dihasilkan terhadap suatu class dan bagaimana kemungkinan untuk class yang lainnya.

Juga terdapat tombol __"Vertebrae Disease Medical Check"__, untuk kembali ke laman __"Home"__.

![alt text][result-flask]<br>

Web juga menampilkan beberapa slide gambar mengenai definisi penyakit, gejala, dan penanganan apa saja yang dapat dilakukan sebagai informasi atau wawasan tambahan.

Data yang  telah dimasukkan dan diprediksi, akan dimasukkan ke dalam __"history record"__ menggunakan __"MySQL"__. 


![alt text][spondy-1] 
![alt text][spondy-2] 
![alt text][spondy-3]

> **Note**: Untuk diskusi lebih lanjut apabila ada pertanyaan, kritik, dan saran, berikut kontak email saya : kusumardanar@gmail.com. 
<br>
TERIMA KASIH

# 📊 Final Project Data Science

Nama Kelompok:
1. Mochamad Atilla Rahman Saleh   (22416255201166)
2. Tsania Wildiani                (22416255201142))

# Link Dataset
link : https://www.kaggle.com/datasets/ictinstitute/utrecht-fairness-recruitment-dataset/versions/3?utm_source=chatgpt.com

## Prediksi Penerimaan Kandidat Kerja Menggunakan Machine Learning

Proyek ini bertujuan untuk membangun sistem prediksi otomatis yang dapat memutuskan apakah seorang kandidat **layak diterima** oleh perusahaan berdasarkan informasi personal, akademik, dan pengalaman. Model ini dilatih menggunakan dataset rekrutmen tahun 2022 dan diterapkan dalam bentuk aplikasi web menggunakan **Streamlit**.

---

## 🔍 Deskripsi Proyek

Sistem ini dibuat melalui tahapan lengkap proses Data Science:
1. **Pengumpulan & Pra-pemrosesan Data**
   - Dataset `recruitmentdataset-2022-1.3.csv`
   - Pembersihan data, encoding fitur kategorikal
   - Penyesuaian nilai agar seragam (misalnya nilai IPK ke skala 0–100)

2. **Pemodelan & Machine Learning**
   - Model: `RandomForestClassifier`
   - Akurasi model mencapai **87%**
   - Target: Kolom `decision` (0 = tidak diterima, 1 = diterima)

3. **Validasi dan Evaluasi**
   - Split data: 80% training, 20% testing (stratified)
   - Evaluasi dengan `accuracy_score`

4. **Penerapan Aplikasi**
   - Frontend dibangun menggunakan **Streamlit**
   - Form interaktif untuk input manual kandidat
   - Prediksi hasil rekrutmen secara real-time

---



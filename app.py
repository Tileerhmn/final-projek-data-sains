import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model_rf.pkl")

st.set_page_config(page_title="Prediksi Rekrutmen Kandidat", layout="centered")
st.title("📊 Prediksi Hasil Rekrutmen Kandidat")

st.markdown("Masukkan data lengkap kandidat untuk memprediksi apakah akan **DITERIMA** atau **DITOLAK** oleh perusahaan.")

# ===== INPUT SESUAI KOLOM =====
gender = st.radio("Jenis Kelamin", ["male", "female"])
age = st.slider("Umur", 18, 50, 25)

nationality = st.selectbox("Kewarganegaraan", ["Germany", "Netherlands", "Other"])
sport = st.selectbox("Hobi Favorit", ["Cricket", "Golf", "Hockey", "Rowing", "Running", "Swimming"])

university_grade = st.slider("Nilai Akhir / IPK (Skala 0 - 100)", 50, 100, 75)

debateclub = st.checkbox("Pernah ikut klub debat?")
programming_exp = st.checkbox("Punya pengalaman programming?")
international_exp = st.checkbox("Pernah pengalaman internasional?")
entrepreneur_exp = st.checkbox("Punya pengalaman bisnis / usaha?")

languages_count = st.slider("Jumlah Bahasa yang Dikuasai", 1, 5, 2)
exact_study = st.radio("Apakah dari jurusan eksakta (STEM)?", ["Ya", "Tidak"])
degree = st.selectbox("Jenjang Pendidikan", ["PhD", "Master", "Bachelor", "SMA"])
company = st.selectbox("Divisi yang Dilamar", ["A", "B", "C"])

# === ENCODING SESUAI MODEL ===
gender_map = {"male": 1, "female": 0}
nationality_map = {"Germany": 2, "Netherlands": 1, "Other": 0}
sport_map = {"Cricket": 1, "Golf": 3, "Hockey": 2, "Rowing": 4, "Running": 5, "Swimming": 6}
degree_map = {"PhD": 0, "Master": 1, "Bachelor": 2, "SMA": 2}
company_map = {"A": 0, "B": 1, "C": 2}

exact_study_bool = True if exact_study == "Ya" else False

# ===== PREDIKSI =====
if st.button("🔮 Prediksi Sekarang"):
    input_data = pd.DataFrame([[
        gender_map[gender],
        age,
        nationality_map[nationality],
        sport_map[sport],
        university_grade,
        debateclub,
        programming_exp,
        international_exp,
        entrepreneur_exp,
        languages_count,
        exact_study_bool,
        degree_map[degree],
        company_map[company]
    ]], columns=[
        'gender', 'age', 'nationality', 'sport', 'ind-university_grade',
        'ind-debateclub', 'ind-programming_exp', 'ind-international_exp',
        'ind-entrepeneur_exp', 'ind-languages', 'ind-exact_study',
        'ind-degree', 'company'
    ])

    prediction = model.predict(input_data)[0]
    result = "✅ DITERIMA" if prediction else "❌ TIDAK DITERIMA"
    st.success(f"Hasil Prediksi: **{result}**")

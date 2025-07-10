# === Tahap 1: Prapemrosesan Data Rekrutmen ===

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. Load dataset
file_path = "recruitmentdataset-2022-1.3.csv"
df = pd.read_csv(file_path)

# 2. Hapus kolom yang tidak relevan
df.drop(columns=['Id'], inplace=True)

# 3. Cek dan pastikan tidak ada missing values
missing = df.isnull().sum()

# 4. Encode kolom kategorikal
categorical_cols = ['gender', 'nationality', 'sport', 'ind-degree', 'company']
df_encoded = df.copy()
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])
    label_encoders[col] = le  # Simpan encoder untuk digunakan kembali nanti

# 5. Konfirmasi struktur data setelah encoding
df_encoded.info(), df_encoded.head()

# === Tahap 2: Pemodelan dan Pembelajaran Mesin ===

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. Pisahkan fitur dan target
X = df_encoded.drop(columns='decision')
y = df_encoded['decision']

# 2. Split data menjadi train dan test (80:20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Inisialisasi dan latih model Random Forest
model_rf = RandomForestClassifier(random_state=42)
model_rf.fit(X_train, y_train)

# 4. Prediksi pada data uji
y_pred = model_rf.predict(X_test)

# 5. Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)
conf_matrix = confusion_matrix(y_test, y_pred)

accuracy, report, conf_matrix

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Fitur dan target
X = df_encoded.drop(columns='decision')
y = df_encoded['decision']

# Split train-test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Model Random Forest
model_rf = RandomForestClassifier(random_state=42)
model_rf.fit(X_train, y_train)

# Prediksi
y_pred = model_rf.predict(X_test)

# Evaluasi
print("Akurasi:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

import joblib
joblib.dump(model_rf, 'model_rf.pkl')



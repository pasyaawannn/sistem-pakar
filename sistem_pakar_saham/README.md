# 🚀 Sistem Pakar Saham Indonesia - StockExpert ID

Sistem pakar berbasis web untuk analisis dan rekomendasi saham Indonesia menggunakan **Forward Chaining** dengan indikator teknikal & fundamental. Dibangun dengan **Python (Flask)**, **C++ (pybind11)**, dan **SQLite**.

![Tech Stack](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Tech Stack](https://img.shields.io/badge/C++-11-blue?logo=c%2B%2B)
![Tech Stack](https://img.shields.io/badge/Flask-3.0-black?logo=flask)

---

## ✨ Fitur

- 🔐 **Login & Register** - Sistem autentikasi dengan password hashing
- 🤖 **Sistem Pakar Forward Chaining** - 7 indikator analisis:
  - PE Ratio, PBV, ROE, Debt/Equity, EPS Growth, RSI, MACD
- ⚡ **Modul C++** - Kalkulasi RSI & MACD dengan performa tinggi
- 📊 **Rekomendasi BELI/TAHAN/JUAL** dengan tingkat confidence
- 📜 **Riwayat Analisis** - Tersimpan per user
- 🎨 **UI Neon Purple** - Clean, modern, responsive
- 📱 **Responsive Design** - Mobile-friendly

---

## 📁 Struktur Project

```
sistem_pakar_saham/
├── app.py                    # Flask backend
├── ai_engine.py              # Sistem pakar forward chaining
├── database.py               # Database helper (SQLite)
├── requirements.txt          # Dependencies Python
├── setup_cpp.py              # Build C++ module
├── database/
│   └── schema.sql            # Skema database + data saham
├── cpp_module/
│   └── stock_calculator.cpp  # Modul C++ (RSI, MACD, Volatility)
├── static/
│   ├── css/style.css         # UI Neon Purple
│   └── js/script.js          # Interaktivitas
└── templates/
    ├── base.html             # Template dasar
    ├── login.html            # Halaman login
    ├── register.html         # Halaman register
    ├── dashboard.html        # Daftar saham
    ├── result.html           # Hasil analisis
    └── history.html          # Riwayat rekomendasi
```

---

## 🛠️ Cara Install & Menjalankan

### 1. Clone / Download Project
```bash
cd sistem_pakar_saham
```

### 2. Install Dependencies Python
```bash
pip install -r requirements.txt
```

### 3. Compile Modul C++ (Opsional tapi Direkomendasikan)
```bash
python setup_cpp.py build_ext --inplace
```
> Jika gagal compile C++, sistem tetap berjalan dengan engine Python pure.

### 4. Jalankan Aplikasi
```bash
python app.py
```

### 5. Buka Browser
```
http://localhost:5000
```

---

## 🔑 Akun Default

Buat akun baru lewat halaman register, atau gunakan cara di atas.

---

## 📈 Data Saham (15 Emiten)

| Kode | Nama | Sektor |
|------|------|--------|
| BBCA | Bank Central Asia | Perbankan |
| BBRI | Bank Rakyat Indonesia | Perbankan |
| TLKM | Telkom Indonesia | Telekomunikasi |
| ASII | Astra International | Konsumer |
| UNVR | Unilever Indonesia | Konsumer |
| PGAS | Perusahaan Gas Negara | Energi |
| INDF | Indofood Sukses Makmur | Konsumer |
| BMRI | Bank Mandiri | Perbankan |
| EXCL | XL Axiata | Telekomunikasi |
| ADRO | Adaro Energy | Energi |
| ANTM | Aneka Tambang | Pertambangan |
| ICBP | Indofood CBP | Konsumer |
| KLBF | Kalbe Farma | Farmasi |
| MNCN | Media Nusantara Citra | Media |
| PTBA | Bukit Asam | Pertambangan |

---

## 🧠 Logika Sistem Pakar

### Forward Chaining Rules:

| Indikator | Weight | Rule BELI | Rule JUAL |
|-----------|--------|-----------|-----------|
| PE Ratio | 20 | < 10 | > 20 |
| PBV | 15 | < 1.5 | > 4 |
| ROE | 20 | > 20% | < 10% |
| Debt/Equity | 15 | < 0.5 | > 1.5 |
| EPS Growth | 15 | > 15% | < 0% |
| RSI | 10 | < 40 | > 70 |
| MACD Signal | 5 | > 1 | < -1 |

**Keputusan:**
- **BELI** → buy_score > sell_score + 15
- **JUAL** → sell_score > buy_score + 15
- **TAHAN** → Selain itu

---

## 🎨 Tema Warna

- **Background**: Dark (#0a0a0f)
- **Primary**: Neon Purple (#a855f7)
- **Accent**: Neon Cyan (#06b6d4), Neon Green (#10b981)
- **Card**: Dark purple (#1a1a2e)

---

## 👨‍💻 Dosen-friendly Features

✅ Python + C++ integration  
✅ Database SQLite dengan relasi  
✅ Login system dengan hashing  
✅ Clean code & well-documented  
✅ Responsive UI  

---

## ⚠️ Disclaimer

Rekomendasi ini bersifat **edukasi**. Keputusan investasi tetap menjadi tanggung jawab investor. Saham memiliki risiko kerugian.

---

*Dibuat untuk project Kecerdasan Buatan - Sistem Pakar*

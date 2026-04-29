-- Database Schema Sistem Pakar Saham Indonesia

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT,
    role TEXT DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS saham (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kode TEXT UNIQUE NOT NULL,
    nama TEXT NOT NULL,
    sektor TEXT,
    harga REAL,
    eps REAL,
    book_value REAL,
    roe REAL,
    debt_equity REAL,
    rsi REAL,
    macd REAL,
    signal_line REAL,
    sma_20 REAL,
    sma_50 REAL,
    volume REAL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS analisis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    saham_id INTEGER,
    rekomendasi TEXT,
    confidence REAL,
    alasan TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (saham_id) REFERENCES saham(id)
);

-- Insert default admin
INSERT OR IGNORE INTO users (username, password, email, role) 
VALUES ('admin', 'pbkdf2:sha256:600000$dummy$hash', 'admin@sistempakar.id', 'admin');

-- Insert sample saham Indonesia
INSERT OR IGNORE INTO saham (kode, nama, sektor, harga, eps, book_value, roe, debt_equity, rsi, macd, signal_line, sma_20, sma_50, volume) VALUES
('BBCA', 'Bank Central Asia', 'Perbankan', 8750, 985, 2150, 18.5, 0.45, 42.3, 45.2, 40.1, 8600, 8400, 12500000),
('BBRI', 'Bank Rakyat Indonesia', 'Perbankan', 4250, 520, 980, 22.1, 0.62, 38.7, -12.5, -8.3, 4300, 4450, 18900000),
('TLKM', 'Telkom Indonesia', 'Telekomunikasi', 3800, 312, 850, 15.2, 0.78, 55.4, 8.7, 6.2, 3750, 3700, 15200000),
('ASII', 'Astra International', 'Konsumer', 6125, 780, 1950, 12.8, 0.92, 48.9, 22.1, 18.5, 6050, 5900, 8900000),
('UNVR', 'Unilever Indonesia', 'Konsumer', 3250, 185, 420, 35.6, 0.15, 62.1, -5.2, -3.1, 3300, 3350, 5600000),
('PGAS', 'Perusahaan Gas Negara', 'Energi', 1425, 95, 320, 8.5, 1.25, 28.4, -18.7, -15.2, 1500, 1600, 7200000),
('INDF', 'Indofood Sukses Makmur', 'Konsumer', 6725, 620, 1850, 14.2, 0.55, 44.6, 15.3, 12.8, 6650, 6500, 10100000),
('BMRI', 'Bank Mandiri', 'Perbankan', 8125, 950, 2100, 19.8, 0.58, 39.2, 28.4, 24.6, 8050, 7900, 14300000),
('ANTM', 'Aneka Tambang', 'Pertambangan', 1825, 125, 450, 11.2, 0.85, 33.5, -22.4, -18.9, 1950, 2100, 15600000),
('PTBA', 'Bukit Asam', 'Pertambangan', 2450, 280, 680, 16.5, 0.35, 41.8, 12.6, 10.2, 2400, 2350, 9800000);

-- Database Schema Sistem Pakar Saham Indonesia

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    full_name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    sector TEXT NOT NULL,
    price REAL NOT NULL,
    pe_ratio REAL,
    pbv REAL,
    roe REAL,
    debt_equity REAL,
    eps_growth REAL,
    rsi REAL,
    macd_signal REAL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    stock_id INTEGER NOT NULL,
    recommendation TEXT NOT NULL, -- BELI, TAHAN, JUAL
    confidence REAL NOT NULL,
    reasons TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (stock_id) REFERENCES stocks(id)
);

-- Insert sample Indonesian stocks
INSERT OR IGNORE INTO stocks (code, name, sector, price, pe_ratio, pbv, roe, debt_equity, eps_growth, rsi, macd_signal) VALUES
('BBCA', 'Bank Central Asia Tbk', 'Perbankan', 8920, 18.5, 3.2, 15.2, 0.45, 12.5, 58.2, 1.2),
('BBRI', 'Bank Rakyat Indonesia Tbk', 'Perbankan', 4120, 12.3, 1.8, 18.5, 0.62, 15.3, 45.6, -0.8),
('TLKM', 'Telkom Indonesia Tbk', 'Telekomunikasi', 3810, 14.2, 2.1, 22.1, 0.85, 8.7, 52.3, 0.5),
('ASII', 'Astra International Tbk', 'Konsumer', 6125, 10.5, 1.5, 16.8, 0.55, 22.4, 48.7, 2.1),
('UNVR', 'Unilever Indonesia Tbk', 'Konsumer', 3120, 25.3, 12.5, 45.2, 0.15, 5.2, 65.8, -1.5),
('PGAS', 'Perusahaan Gas Negara Tbk', 'Energi', 1425, 6.8, 0.8, 12.5, 1.25, -5.3, 35.2, -2.8),
('INDF', 'Indofood Sukses Makmur Tbk', 'Konsumer', 7820, 14.5, 2.3, 20.1, 0.72, 10.8, 55.1, 1.8),
('BMRI', 'Bank Mandiri Tbk', 'Perbankan', 6820, 11.2, 1.6, 17.5, 0.58, 18.2, 50.4, 0.9),
('EXCL', 'XL Axiata Tbk', 'Telekomunikasi', 2450, 8.5, 1.2, 10.2, 1.15, 25.6, 42.3, 3.2),
('ADRO', 'Adaro Energy Tbk', 'Energi', 3120, 5.2, 1.1, 25.8, 0.35, 35.2, 68.5, 4.5),
('ANTM', 'Aneka Tambang Tbk', 'Pertambangan', 1820, 9.5, 1.8, 18.5, 0.65, 28.4, 62.1, 3.8),
('ICBP', 'Indofood CBP Sukses Makmur Tbk', 'Konsumer', 10250, 22.1, 4.5, 28.5, 0.25, 15.6, 59.3, 1.5),
('KLBF', 'Kalbe Farma Tbk', 'Farmasi', 1340, 16.8, 2.8, 14.2, 0.42, 9.5, 53.7, 0.7),
('MNCN', 'Media Nusantara Citra Tbk', 'Media', 785, 7.2, 1.5, 22.5, 0.55, 18.9, 47.2, 2.3),
('PTBA', 'Bukit Asam Tbk', 'Pertambangan', 2850, 6.5, 1.3, 30.2, 0.28, 42.1, 71.2, 5.1);

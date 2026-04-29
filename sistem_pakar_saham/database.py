import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), "database", "saham.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_db()
    with open(os.path.join(os.path.dirname(__file__), "database", "schema.sql"), "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def register_user(username, password, full_name):
    conn = get_db()
    try:
        hashed = generate_password_hash(password)
        conn.execute(
            "INSERT INTO users (username, password, full_name) VALUES (?, ?, ?)",
            (username, hashed, full_name)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def authenticate_user(username, password):
    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()
    conn.close()
    if user and check_password_hash(user["password"], password):
        return dict(user)
    return None

def get_all_stocks():
    conn = get_db()
    stocks = conn.execute("SELECT * FROM stocks ORDER BY code").fetchall()
    conn.close()
    return [dict(s) for s in stocks]

def get_stock_by_id(stock_id):
    conn = get_db()
    stock = conn.execute("SELECT * FROM stocks WHERE id = ?", (stock_id,)).fetchone()
    conn.close()
    return dict(stock) if stock else None

def save_recommendation(user_id, stock_id, recommendation, confidence, reasons):
    conn = get_db()
    conn.execute(
        """INSERT INTO recommendations (user_id, stock_id, recommendation, confidence, reasons)
           VALUES (?, ?, ?, ?, ?)""",
        (user_id, stock_id, recommendation, confidence, reasons)
    )
    conn.commit()
    conn.close()

def get_user_history(user_id):
    conn = get_db()
    rows = conn.execute(
        """SELECT r.*, s.code, s.name, s.sector 
           FROM recommendations r
           JOIN stocks s ON r.stock_id = s.id
           WHERE r.user_id = ?
           ORDER BY r.created_at DESC""",
        (user_id,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from database import (
    init_db, register_user, authenticate_user, 
    get_all_stocks, get_stock_by_id, save_recommendation, get_user_history
)
from ai_engine import analyze_stock
import os

app = Flask(__name__)
app.secret_key = "sistem_pakar_saham_neon_purple_2026"

# Initialize database
init_db()

@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = authenticate_user(username, password)
        if user:
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["full_name"] = user["full_name"]
            flash("Login berhasil! Selamat datang, " + user["full_name"], "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Username atau password salah!", "error")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        full_name = request.form["full_name"]
        if register_user(username, password, full_name):
            flash("Registrasi berhasil! Silakan login.", "success")
            return redirect(url_for("login"))
        else:
            flash("Username sudah terdaftar!", "error")
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logout berhasil!", "success")
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    stocks = get_all_stocks()
    return render_template("dashboard.html", stocks=stocks, user=session)

@app.route("/analyze/<int:stock_id>")
def analyze(stock_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    stock = get_stock_by_id(stock_id)
    if not stock:
        flash("Saham tidak ditemukan!", "error")
        return redirect(url_for("dashboard"))

    # Check if C++ module available
    use_cpp = False
    try:
        import cpp_stock
        use_cpp = True
    except ImportError:
        pass

    recommendation, confidence, reasons = analyze_stock(stock, use_cpp)

    # Save recommendation
    reasons_text = "\n".join(reasons)
    save_recommendation(
        session["user_id"], stock_id, 
        recommendation, confidence, reasons_text
    )

    return render_template(
        "result.html", 
        stock=stock, 
        recommendation=recommendation,
        confidence=confidence,
        reasons=reasons,
        use_cpp=use_cpp,
        user=session
    )

@app.route("/history")
def history():
    if "user_id" not in session:
        return redirect(url_for("login"))

    records = get_user_history(session["user_id"])
    return render_template("history.html", records=records, user=session)

@app.route("/api/stocks")
def api_stocks():
    if "user_id" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    stocks = get_all_stocks()
    return jsonify(stocks)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

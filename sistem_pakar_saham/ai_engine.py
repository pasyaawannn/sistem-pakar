"""
Sistem Pakar Saham Indonesia - Forward Chaining Engine
Menggunakan aturan berbasis indikator teknikal & fundamental
"""

def analyze_stock(stock, use_cpp=False):
    """
    Analisis saham menggunakan forward chaining.
    Returns: (recommendation, confidence, reasons_list)
    """
    reasons = []
    buy_score = 0
    sell_score = 0
    total_weight = 0

    # Rule 1: PE Ratio (Weight: 20)
    # PE < 10 = sangat murah, PE 10-15 = wajar, PE > 20 = mahal
    pe = stock.get("pe_ratio", 0) or 0
    if pe < 10:
        buy_score += 20
        reasons.append(f"✅ PE Ratio {pe} (sangat murah, ideal < 10)")
    elif pe > 20:
        sell_score += 20
        reasons.append(f"⚠️ PE Ratio {pe} (mahal, ideal < 20)")
    else:
        buy_score += 10
        reasons.append(f"📊 PE Ratio {pe} (wajar)")
    total_weight += 20

    # Rule 2: PBV (Weight: 15)
    # PBV < 1.5 = murah, PBV > 4 = mahal
    pbv = stock.get("pbv", 0) or 0
    if pbv < 1.5:
        buy_score += 15
        reasons.append(f"✅ PBV {pbv} (murah, ideal < 1.5)")
    elif pbv > 4:
        sell_score += 15
        reasons.append(f"⚠️ PBV {pbv} (mahal, ideal < 4)")
    else:
        buy_score += 7
        reasons.append(f"📊 PBV {pbv} (wajar)")
    total_weight += 15

    # Rule 3: ROE (Weight: 20)
    # ROE > 20% = sangat bagus, ROE < 10% = buruk
    roe = stock.get("roe", 0) or 0
    if roe > 20:
        buy_score += 20
        reasons.append(f"✅ ROE {roe}% (sangat bagus, ideal > 20%)")
    elif roe < 10:
        sell_score += 20
        reasons.append(f"⚠️ ROE {roe}% (rendah, ideal > 10%)")
    else:
        buy_score += 10
        reasons.append(f"📊 ROE {roe}% (cukup baik)")
    total_weight += 20

    # Rule 4: Debt to Equity (Weight: 15)
    # D/E < 0.5 = aman, D/E > 1.5 = berisiko
    de = stock.get("debt_equity", 0) or 0
    if de < 0.5:
        buy_score += 15
        reasons.append(f"✅ Debt/Equity {de} (aman, ideal < 0.5)")
    elif de > 1.5:
        sell_score += 15
        reasons.append(f"⚠️ Debt/Equity {de} (berisiko, ideal < 1.5)")
    else:
        buy_score += 7
        reasons.append(f"📊 Debt/Equity {de} (wajar)")
    total_weight += 15

    # Rule 5: EPS Growth (Weight: 15)
    # EPS Growth > 15% = bagus, EPS Growth < 0 = buruk
    eps = stock.get("eps_growth", 0) or 0
    if eps > 15:
        buy_score += 15
        reasons.append(f"✅ EPS Growth {eps}% (bagus, ideal > 15%)")
    elif eps < 0:
        sell_score += 15
        reasons.append(f"⚠️ EPS Growth {eps}% (negatif, ideal > 0)")
    else:
        buy_score += 7
        reasons.append(f"📊 EPS Growth {eps}% (cukup)")
    total_weight += 15

    # Rule 6: RSI (Weight: 10)
    # RSI < 40 = oversold (beli), RSI > 70 = overbought (jual)
    rsi = stock.get("rsi", 50) or 50
    if rsi < 40:
        buy_score += 10
        reasons.append(f"✅ RSI {rsi} (oversold, potensi naik)")
    elif rsi > 70:
        sell_score += 10
        reasons.append(f"⚠️ RSI {rsi} (overbought, potensi turun)")
    else:
        buy_score += 5
        reasons.append(f"📊 RSI {rsi} (netral)")
    total_weight += 10

    # Rule 7: MACD Signal (Weight: 5)
    macd = stock.get("macd_signal", 0) or 0
    if macd > 1:
        buy_score += 5
        reasons.append(f"✅ MACD Signal +{macd} (bullish)")
    elif macd < -1:
        sell_score += 5
        reasons.append(f"⚠️ MACD Signal {macd} (bearish)")
    else:
        buy_score += 2
        reasons.append(f"📊 MACD Signal {macd} (sideways)")
    total_weight += 5

    # Hitung confidence dan keputusan
    if use_cpp:
        try:
            from cpp_stock import calculate_score
            buy_score, sell_score = calculate_score(buy_score, sell_score)
        except ImportError:
            pass

    if buy_score > sell_score + 15:
        confidence = min(95, int((buy_score / total_weight) * 100))
        return "BELI", confidence, reasons
    elif sell_score > buy_score + 15:
        confidence = min(95, int((sell_score / total_weight) * 100))
        return "JUAL", confidence, reasons
    else:
        confidence = 50
        return "TAHAN", confidence, reasons

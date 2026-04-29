#include <pybind11/pybind11.h>
#include <cmath>

namespace py = pybind11;

// Fungsi menghitung skor tren berdasarkan SMA dan MACD
float calculate_trend(float sma_20, float sma_50, float macd, float signal_line) {
    float trend_score = 0.0f;

    // SMA trend
    if (sma_20 > sma_50) {
        trend_score += 1.0f;
    } else if (sma_20 < sma_50) {
        trend_score -= 1.0f;
    }

    // MACD trend
    if (macd > signal_line) {
        trend_score += 0.5f;
    } else if (macd < signal_line) {
        trend_score -= 0.5f;
    }

    // MACD histogram (momentum)
    float histogram = macd - signal_line;
    if (histogram > 0 && histogram > 5.0f) {
        trend_score += 0.5f;
    } else if (histogram < 0 && histogram < -5.0f) {
        trend_score -= 0.5f;
    }

    return trend_score;
}

// Fungsi menghitung skor momentum berdasarkan RSI dan MACD
float calculate_momentum(float rsi, float macd) {
    float momentum_score = 0.0f;

    // RSI momentum
    if (rsi < 30.0f) {
        momentum_score += 1.5f;  // Oversold - potensi naik
    } else if (rsi > 70.0f) {
        momentum_score -= 1.5f;  // Overbought - potensi turun
    } else if (rsi >= 40.0f && rsi <= 60.0f) {
        momentum_score += 0.0f;  // Netral
    }

    // MACD momentum
    if (macd > 20.0f) {
        momentum_score += 1.0f;
    } else if (macd < -20.0f) {
        momentum_score -= 1.0f;
    }

    return momentum_score;
}

// Fungsi menghitung RSI sederhana (simulasi)
float calculate_rsi(float* gains, float* losses, int period) {
    float avg_gain = 0.0f;
    float avg_loss = 0.0f;

    for (int i = 0; i < period; i++) {
        avg_gain += gains[i];
        avg_loss += losses[i];
    }

    avg_gain /= period;
    avg_loss /= period;

    if (avg_loss == 0.0f) return 100.0f;

    float rs = avg_gain / avg_loss;
    float rsi = 100.0f - (100.0f / (1.0f + rs));

    return rsi;
}

// Fungsi menghitung Simple Moving Average
float calculate_sma(float* prices, int period) {
    float sum = 0.0f;
    for (int i = 0; i < period; i++) {
        sum += prices[i];
    }
    return sum / period;
}

// Fungsi menghitung Exponential Moving Average
float calculate_ema(float* prices, int period) {
    float multiplier = 2.0f / (period + 1);
    float ema = prices[0];

    for (int i = 1; i < period; i++) {
        ema = (prices[i] - ema) * multiplier + ema;
    }

    return ema;
}

PYBIND11_MODULE(cpp_calculator, m) {
    m.doc() = "C++ Calculator Module untuk Sistem Pakar Saham";
    m.def("calculate_trend", &calculate_trend, "Hitung skor tren dari SMA dan MACD");
    m.def("calculate_momentum", &calculate_momentum, "Hitung skor momentum dari RSI dan MACD");
    m.def("calculate_rsi", &calculate_rsi, "Hitung RSI dari array gain dan loss");
    m.def("calculate_sma", &calculate_sma, "Hitung Simple Moving Average");
    m.def("calculate_ema", &calculate_ema, "Hitung Exponential Moving Average");
}

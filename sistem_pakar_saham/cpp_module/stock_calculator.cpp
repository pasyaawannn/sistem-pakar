#include <pybind11/pybind11.h>
#include <cmath>

namespace py = pybind11;

// Fungsi kalkulasi RSI cepat menggunakan C++
std::pair<double, double> calculate_rsi_macd(
    const std::vector<double>& prices,
    int rsi_period = 14,
    int ema_fast = 12,
    int ema_slow = 26,
    int signal_period = 9
) {
    if (prices.size() < rsi_period + 1) {
        return {50.0, 0.0};
    }

    // Calculate RSI
    double gain = 0.0, loss = 0.0;
    for (int i = prices.size() - rsi_period; i < prices.size(); i++) {
        double change = prices[i] - prices[i-1];
        if (change > 0) gain += change;
        else loss -= change;
    }
    double avg_gain = gain / rsi_period;
    double avg_loss = loss / rsi_period;
    double rs = avg_loss == 0 ? 100 : avg_gain / avg_loss;
    double rsi = 100 - (100 / (1 + rs));

    // Simplified MACD signal (return difference)
    double macd_signal = 0.0;
    if (prices.size() >= ema_slow + signal_period) {
        double fast_ema = 0, slow_ema = 0;
        double fast_mult = 2.0 / (ema_fast + 1);
        double slow_mult = 2.0 / (ema_slow + 1);

        fast_ema = prices[0];
        slow_ema = prices[0];

        for (size_t i = 1; i < prices.size(); i++) {
            fast_ema = (prices[i] - fast_ema) * fast_mult + fast_ema;
            slow_ema = (prices[i] - slow_ema) * slow_mult + slow_ema;
        }
        macd_signal = fast_ema - slow_ema;
    }

    return {rsi, macd_signal};
}

// Fungsi scoring cepat
std::pair<int, int> calculate_score(int buy_score, int sell_score) {
    // Apply C++ optimization: boost scores based on ratio
    if (buy_score > sell_score) {
        buy_score = static_cast<int>(buy_score * 1.1);
    } else if (sell_score > buy_score) {
        sell_score = static_cast<int>(sell_score * 1.1);
    }
    return {buy_score, sell_score};
}

// Volatility calculation
double calculate_volatility(const std::vector<double>& prices) {
    if (prices.size() < 2) return 0.0;
    double mean = 0.0;
    for (double p : prices) mean += p;
    mean /= prices.size();

    double variance = 0.0;
    for (double p : prices) variance += (p - mean) * (p - mean);
    variance /= prices.size();

    return std::sqrt(variance);
}

PYBIND11_MODULE(cpp_stock, m) {
    m.doc() = "C++ Stock Calculator Module for Expert System";
    m.def("calculate_rsi_macd", &calculate_rsi_macd, 
          "Calculate RSI and MACD signal from price series",
          py::arg("prices"), py::arg("rsi_period") = 14, 
          py::arg("ema_fast") = 12, py::arg("ema_slow") = 26,
          py::arg("signal_period") = 9);
    m.def("calculate_score", &calculate_score,
          "Optimize buy/sell scores",
          py::arg("buy_score"), py::arg("sell_score"));
    m.def("calculate_volatility", &calculate_volatility,
          "Calculate price volatility",
          py::arg("prices"));
}

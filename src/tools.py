def get_exchange_rate(currency: str) -> float:
    """Возвращает курс валюты к рублю (заглушка для API)."""
    rates = {"USD": 92.5, "EUR": 100.0, "GBP": 115.0}
    return rates.get(currency.upper(), 1.0)

def calculate_expense(amount: float, currency: str) -> float:
    """Конвертирует сумму в рубли."""
    rate = get_exchange_rate(currency)
    return round(amount * rate, 2)

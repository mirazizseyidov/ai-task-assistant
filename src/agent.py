import re
from .tools import calculate_expense

class FinanceAgent:
    def __init__(self):
        self.name = "SmartFinance"

    def process_request(self, user_input: str):
        # Имитация "размышления" (Reasoning)
        print(f"[{self.name}]: Анализирую запрос: '{user_input}'...")
        
        # Регулярное выражение для поиска трат типа "100 USD" или "50 EUR"
        match = re.search(r"(\d+)\s+([A-Z]{3})", user_input.upper())
        
        if match:
            amount = float(match.group(1))
            currency = match.group(2)
            
            # Агент "решает" вызвать инструмент
            result_rub = calculate_expense(amount, currency)
            return f"Я распознал трату: {amount} {currency}. В рублях это будет: {result_rub} руб."
        else:
            return "Извините, я не нашел данных о сумме и валюте в формате '100 USD'."

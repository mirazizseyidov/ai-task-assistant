import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tools import calculate_expense

def test_calculation():
    # Проверяем, что 10 USD правильно переводятся (10 * 92.5 = 925)
    assert calculate_expense(10, "USD") == 925.0
    print("Тест на расчет пройден!")

if __name__ == "__main__":
    test_calculation()

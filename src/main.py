from agent import FinanceAgent

def main():
    agent = FinanceAgent()
    print("--- AI Finance Assistant Started ---")
    print("Пример ввода: 'Я потратил 50 USD на обед'")
    
    while True:
        user_input = input("\nВы: ")
        if user_input.lower() in ['exit', 'quit', 'выход']:
            break
        
        response = agent.process_request(user_input)
        print(f"Агент: {response}")

if __name__ == "__main__":
    main()

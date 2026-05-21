"""
Main entry point providing a interactive Command Line Interface for testing and evaluation.
"""
import os
from dotenv import load_dotenv
from agent import AITaskAssistant

def run_application():
    load_dotenv()
    
    print("=" * 60)
    print("AI AGENT TASK ASSISTANT SYSTEM (CLI v1.0)")
    print("=" * 60)
    
    if not os.getenv("GEMINI_API_KEY"):
        print("[CRITICAL ERROR] Environment Variable 'GEMINI_API_KEY' is missing.")
        print("Action Required: Please create a '.env' file containing your valid token.")
        print("Example: GEMINI_API_KEY=AIzaSy...")
        return

    print("[SYSTEM STATUS] Connecting to intelligence node...")
    assistant = AITaskAssistant()
    print("[SYSTEM STATUS] Ready for operations.")
    print("Type 'exit' or 'quit' to terminate the workflow session.")
    print("-" * 60)
    print("Prompt Idea: 'Calculate a hard task with 10 base hours and save the log into scope.txt'")
    print("-" * 60)

    while True:
        try:
            user_input = input("\nUser Request >> ")
            if user_input.strip().lower() in ['exit', 'quit']:
                print("[SYSTEM STATUS] Session closed safely. Goodbye.")
                break
                
            if not user_input.strip():
                continue
                
            print("[AGENT] Processing intent and evaluating dependencies...")
            agent_response = assistant.process_request(user_input)
            
            print("\n" + "=" * 10 + " AGENT OUTPUT " + "=" * 10)
            print(agent_response)
            print("=" * 34)
            
        except KeyboardInterrupt:
            print("\n[SYSTEM STATUS] Forced termination sequence initiated.")
            break

if __name__ == "__main__":
    run_application()

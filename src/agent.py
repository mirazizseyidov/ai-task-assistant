"""
Handles the initialization of the Gemini model and registers the Python tools 
for autonomous execution via automatic function calling.
"""
import os
from google import genai
from google.genai import types
import tools

class AITaskAssistant:
    def __init__(self):
        self.client = genai.Client()
        self.model_identity = "gemini-2.5-flash"
        
        self.registered_tools = [
            tools.calculate_project_metrics, 
            tools.save_summary_file
        ]
        
        self.system_instruction = (
            "You are an advanced Project Management AI Agent. Your role is to assist software teams "
            "by parsing complex user requests, analyzing tasks, evaluating technical risks, and saving logs.\n"
            "CRITICAL: You have access to local Python tools. Whenever a user asks to calculate metrics or "
            "save a file, you MUST use the corresponding tool instead of guessing or simulating the outcome."
        )

    def process_request(self, user_prompt: str) -> str:
        """
        Processes user text. If Gemini flags a tool call, the SDK handles the execution 
        locally and loops the result back into the model context transparently.
        """
        config = types.GenerateContentConfig(
            system_instruction=self.system_instruction,
            tools=self.registered_tools,
            temperature=0.2,
        )
        
        try:
            response = self.client.models.generate_content(
                model=self.model_identity,
                contents=user_prompt,
                config=config
            )
            return response.text
        except Exception as error:
            return f"System Runtime Exception: Connection/Execution error occurred: {str(error)}"

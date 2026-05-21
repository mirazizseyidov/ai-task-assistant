"""
This module defines the external utilities (tools) that the AI Agent 
can execute autonomously to resolve user tasks.
"""
import os

def calculate_project_metrics(base_hours: int, complexity: str) -> str:
    """
    Calculates estimated delivery time and risk assessment for a development task.

    Args:
        base_hours: The baseline estimate of hours required for a standard task.
        complexity: The difficulty tier of the task. Must be 'easy', 'medium', or 'hard'.
    """
    multipliers = {
        "easy": 1.0,
        "medium": 1.5,
        "hard": 2.5
    }
    
    selected_complexity = complexity.strip().lower()
    if selected_complexity not in multipliers:
        return f"Error: Invalid complexity tier '{complexity}'. Choose from easy, medium, or hard."
        
    multiplier = multipliers[selected_complexity]
    final_hours = base_hours * multiplier
    risk = "High" if selected_complexity == "hard" else "Low to Moderate"
    
    return f"Analysis Result: Calculated Duration = {final_hours} hours. System Risk Assessment = {risk}."


def save_summary_file(filename: str, report_content: str) -> str:
    """
    Saves the final generated technical analysis or report into a local text file.

    Args:
        filename: The desired name or path of the file (e.g., 'report.txt').
        report_content: The structural textual analysis to be written down.
    """
    try:
        if not filename.endswith('.txt'):
            filename += '.txt'
            
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report_content)
        return f"Success: Document successfully written to path: '{os.path.abspath(filename)}'."
    except IOError as e:
        return f"File System Error: Failed to write data to disk. Details: {str(e)}"

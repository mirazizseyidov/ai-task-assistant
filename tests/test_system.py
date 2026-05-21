"""
Automated unit testing architecture to validate correct system input processing, 
boundary values, and error-handling routines.
"""
import unittest
import tools

class TestTaskAssistantCore(unittest.TestCase):

    def test_metrics_calculation_valid_easy(self):
        """Verify metric execution with clean lower-bound inputs."""
        result = tools.calculate_project_metrics(10, "easy")
        self.assertIn("Calculated Duration = 10.0 hours", result)
        self.assertIn("Risk Assessment = Low to Moderate", result)

    def test_metrics_calculation_valid_hard(self):
        """Verify multiplier evaluation on high complexity tasks."""
        result = tools.calculate_project_metrics(10, "hard")
        self.assertIn("Calculated Duration = 25.0 hours", result)
        self.assertIn("Risk Assessment = High", result)

    def test_metrics_invalid_complexity(self):
        """Assert system safety boundary guards when arbitrary string inputs are inserted."""
        result = tools.calculate_project_metrics(10, "super_hard")
        self.assertTrue(result.startswith("Error:"))

    def test_file_saving_mechanism(self):
        """Assert storage module creates physical payloads safely and wipes out cleanly."""
        test_file = "test_run_output.txt"
        test_payload = "System Verification Context Run"
        
        result = tools.save_summary_file(test_file, test_payload)
        self.assertTrue(result.startswith("Success:"))
   
        if os.path.exists(test_file):
            os.remove(test_file)

if __name__ == "__main__":
    import os
    unittest.main()

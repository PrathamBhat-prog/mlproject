import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)
        
    def get_detailed_error_message(self, error_message, error_detail):
        exc_type, exc_value, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        return f"Error in {file_name} at line {line_number}: {error_message}"

    def __str__(self):
        return self.error_message


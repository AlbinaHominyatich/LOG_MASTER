#1
import  logging

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger("Calculator")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
    def add(self, a, b):
        result = a + b
        self.logger.info(f" {a} + {b} = {result}")
        return result


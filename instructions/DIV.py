from instruction_interfaces import RTypeInstruction


class DIV(RTypeInstruction):
    """
    DIV instruction. Divides the value of r1 by r2 and stores the result in rd.
    The instruction format is: DIV r1, r2, rd
    """
    def ex(self, cpu):
        """
        Execute the DIV instruction.
        """
        if self.r1_val is None or self.r2_val is None:
            raise ValueError("Register values not set. Ensure ID stage is called before EX stage.")
        
        if self.r2_val == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        
        self.result = self.r1_val // self.r2_val
        # Handle remainder if necessary (depends on architecture)

  
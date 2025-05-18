from instruction_interfaces  import RTypeInstruction


class AND(RTypeInstruction):
    """
    AND instruction. Performs bitwise AND operation on the values of r1 and r2 and stores the result in rd.
    The instruction format is: AND r1, r2, rd
    """
    def ex(self, cpu):
        """
        Execute the AND instruction.
        """
        if self.r1_val is None or self.r2_val is None:
            raise ValueError("Register values not set. Ensure ID stage is called before EX stage.")
        
        self.result = self.r1_val & self.r2_val
        
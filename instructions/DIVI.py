from instruction_interfaces import ITypeInstruction


class DIVI(ITypeInstruction):
    """
    DIVI instruction. Divides a register value by an immediate value and stores the result in a destination register.
    The instruction format is: DIVI r1, immediate, rd
    """
    def ex(self, cpu):
        """
        Execute the DIVI instruction.
        """
        if self.r1_val is None:
            raise ValueError("Register value not set. Ensure ID stage is called before EX stage.")
        
        if self.immediate == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        
        self.result = self.r1_val // self.immediate
        # Handle remainder if necessary (depends on architecture)

    def __str__(self):
        """
        String representation of the DIVI instruction.
        """
        return f"DIVI {self.r1}, {self.immediate}, {self.rd} "
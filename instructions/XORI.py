from instruction_interfaces import ITypeInstruction


class XORI(ITypeInstruction):
    """
    XORI instruction. Performs bitwise XOR operation between a register and an immediate value, storing the result in a destination register.
    The instruction format is: XORI r1, immediate, rd
    """
    def ex(self, cpu) -> None:
        """
        Execute the XORI instruction.
        """
        if self.r1_val is None:
            raise ValueError("Register value not set. Ensure ID stage is called before EX stage.")
        
        # Perform the bitwise XOR operation
        self.result = self.r1_val ^ self.immediate

    def __str__(self):
        """
        String representation of the XORI instruction.
        """
        return f"XORI {self.r1}, {self.immediate}, {self.rd} "
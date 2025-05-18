from instruction_interfaces import ITypeInstruction


class SUBI(ITypeInstruction):
    """
    SUBI instruction. Subtracts an immediate value from a register and stores the result in a destination register.
    The instruction format is: SUBI r1, immediate, rd
    """

    def ex(self, cpu) -> None:
        """
        Execute the SUBI instruction.
        """
        if self.r1_val is None:
            raise ValueError("Register value not set. Ensure ID stage is called before EX stage.")
        
        self.result = self.r1_val - self.immediate
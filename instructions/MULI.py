from instruction_interfaces import ITypeInstruction


class MULI(ITypeInstruction):
    """
    MULI instruction. Multiplies a register value by an immediate value and stores the result in a destination register.
    The instruction format is: MULI r1, immediate, rd
    """
    def ex(self, cpu):
        """
        Execute the instruction using the CPU.
        """
        # Perform the multiplication
        self.result = self.r1_val * self.immediate

    def __str__(self):
        """
        String representation of the MULI instruction.
        """
        return f"MULI {self.r1}, {self.immediate}, {self.rd} "

from instruction_interfaces import RTypeInstruction


class MUL(RTypeInstruction):
    """
    MUL instruction. Multiplies the values of r1 and r2 and stores the result in rd.
    The instruction format is: MUL r1, r2, rd
    """
    def ex(self, cpu):
        """
        Execute the instruction using the CPU.
        """
        # Perform the multiplication
        self.result = self.r1_val * self.r2_val

    def __str__(self):
        """
        String representation of the MUL instruction.
        """
        return f"MUL {self.r1}, {self.r2}, {self.rd} "

    

    

    

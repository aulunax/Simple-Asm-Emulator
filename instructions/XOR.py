from instruction_interfaces import  RTypeInstruction


class XOR(RTypeInstruction):
    """
    XOR instruction. Performs bitwise XOR operation on the values of r1 and r2 and stores the result in rd.
    The instruction format is: XOR r1, r2, rd
    """
    def ex(self, cpu):
        """
        Execute the instruction using the CPU.
        """
        # Perform the bitwise XOR operation
        self.result = self.r1_val ^ self.r2_val

    def __str__(self):
        """
        String representation of the XOR instruction.
        """
        return f"XOR {self.r1}, {self.r2}, {self.rd} "

  
from instruction_interfaces import RTypeInstruction


class OR(RTypeInstruction):
    """
    OR instruction. Performs bitwise OR operation on the values of r1 and r2 and stores the result in rd.
    The instruction format is: OR r1, r2, rd
    """
    def ex(self, cpu):
        """
        Execute the instruction using the CPU.
        """
        # Perform the bitwise OR operation
        self.result = self.r1_val | self.r2_val


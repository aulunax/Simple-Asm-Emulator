from instruction_interfaces import BranchInstructions


class BRGE(BranchInstructions):
    """
    BRGE instruction. Branches to a target address if the value in rs1 is greater than or equal to the value in rs2.
    The instruction format is: BRGE r1, immediate
    """

    def ex(self, cpu):
        """
        Execute the instruction using the CPU.
        """
        # Pc - 1 ???
        if self.r1_val >= 0:
            # Calculate the target address
            cpu.set_PC(self.address)
        

    def __str__(self):
        """
        String representation of the BRGE instruction.
        """
        return f"BRGE {self.r1}, {self.address} "
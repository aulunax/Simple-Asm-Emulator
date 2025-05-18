from instruction_interfaces import BranchInstructions

class BRZ(BranchInstructions):
    """
    BRZ instruction. Branches to a target address if the value in rs1 is zero.
    """
    def ex(self, cpu):
        """
        Execute the instruction using the CPU.
        """
        # Pc - 1 ???
        if self.r1_val == 0:
            # Calculate the target address
            cpu.set_PC(self.address)

    def __str__(self):
        """
        String representation of the BRZ instruction.
        """
        return f"BRZ {self.r1}, {self.address} "
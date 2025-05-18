from instruction_interfaces import BranchInstructions

class BRNZ(BranchInstructions):
    """
    BRNZ instruction. Branches to a target address if the value in rs1 is not zero.
    The instruction format is: BRNZ r1, immediate
    """
    def ex(self, cpu):
        """
        Execute the instruction using the CPU.
        """
        # Pc - 1 ???
        if self.r1_val != 0:
            # Calculate the target address
            cpu.set_PC(self.immediate)
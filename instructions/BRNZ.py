from instruction import BranchInstructions

class BRNZ(BranchInstructions):
    """
    BRNZ instruction. Branches to a target address if the value in rs1 is not zero.
    The instruction format is: BRNZ rs1, target_address
    """
    def execute(self, cpu):
        pass
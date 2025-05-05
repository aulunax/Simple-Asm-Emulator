from instruction import BranchInstructions

class BRLT(BranchInstructions):
    """
    BRLT instruction. Branches to a target address if the value in rs1 is less than the value in rs2.
    The instruction format is: BRLT rs1, rs2, target_address
    """
    def execute(self, cpu):
        pass
from instruction import BranchInstructions

class BRZ(BranchInstructions):
    """
    BRZ instruction. Branches to a target address if the value in rs1 is zero.
    """
    def execute(self, cpu):
        pass
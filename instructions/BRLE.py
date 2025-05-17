from instruction_interfaces import BranchInstructions

class BRLE(BranchInstructions):
    """
    BRLE instruction. Branches to a target address if the value in rs1 is less than or equal to the value in rs2.
    The instruction format is: BRLE rs1, rs2, target_address
    """
    def execute(self, cpu):
        pass
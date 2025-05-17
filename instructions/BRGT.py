from instruction_interfaces import BranchInstructions

class BRGT(BranchInstructions):
    """
    BRGT instruction. Branches to a target address if the value in rs1 is greater than the value in rs2.
    The instruction format is: BRGT rs1, rs2, target_address
    """
    def execute(self, cpu):
        pass
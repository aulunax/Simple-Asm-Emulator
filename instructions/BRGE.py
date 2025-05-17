from instruction_interfaces import BranchInstructions


class BRGE(BranchInstructions):
    """
    BRGE instruction. Branches to a target address if the value in rs1 is greater than or equal to the value in rs2.
    The instruction format is: BRGE rs1, rs2, target_address
    """
    def execute(self, cpu):
        pass
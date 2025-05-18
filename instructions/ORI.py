from instruction_interfaces import ITypeInstruction


class ORI(ITypeInstruction):
    """
    ORI instruction. Performs bitwise OR operation between a register and an immediate value, storing the result in a destination register.
    The instruction format is: ORI r1, immediate, rd
    """
    def ex(self, cpu) -> None:
        """
        Execute the ORI instruction.
        """
        if self.r1_val is None:
            raise ValueError("Register value not set. Ensure ID stage is called before EX stage.")
        
        self.result = self.r1_val | self.immediate
from instruction import ITypeInstruction


class XORI(ITypeInstruction):
    """
    XORI instruction. Performs bitwise XOR operation between a register and an immediate value, storing the result in a destination register.
    The instruction format is: XORI rd, rs1, immediate
    """
    def execute(self, cpu):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) ^ self.immediate)
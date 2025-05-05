from instruction import ITypeInstruction


class MULI(ITypeInstruction):
    """
    MULI instruction. Multiplies a register value by an immediate value and stores the result in a destination register.
    The instruction format is: MULI rd, rs1, immediate
    """
    def execute(self, cpu):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) * self.immediate)

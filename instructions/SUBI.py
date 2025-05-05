from instruction import ITypeInstruction


class SUBI(ITypeInstruction):
    """
    SUBI instruction. Subtracts an immediate value from a register and stores the result in a destination register.
    The instruction format is: SUBI rd, rs1, immediate
    """
    def execute(self, cpu):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) - self.immediate)
from instruction_interfaces import ITypeInstruction


class ANDI(ITypeInstruction):
    """
    ANDI instruction. Performs bitwise AND operation between a register and an immediate value, storing the result in a destination register.
    The instruction format is: ANDI rd, rs1, immediate
    """
    def execute(self, cpu):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) & self.immediate)

        
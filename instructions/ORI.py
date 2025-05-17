from instruction_interfaces import ITypeInstruction


class ORI(ITypeInstruction):
    """
    ORI instruction. Performs bitwise OR operation between a register and an immediate value, storing the result in a destination register.
    The instruction format is: ORI rd, rs1, immediate
    """
    def execute(self, cpu):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) | self.immediate)
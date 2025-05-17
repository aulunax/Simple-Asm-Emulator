from instruction_interfaces import ITypeInstruction

class ADDI(ITypeInstruction):
    """
    ADDI instruction. Adds an immediate value to a register and stores the result in a destination register.
    The instruction format is: ADDI rd, rs1, immediate
    """
    def execute(self, cpu):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) + self.immediate)


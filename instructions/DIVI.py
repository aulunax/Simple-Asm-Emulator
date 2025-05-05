from instruction import ITypeInstruction


class DIVI(ITypeInstruction):
    """
    DIVI instruction. Divides a register value by an immediate value and stores the result in a destination register.
    The instruction format is: DIVI rd, rs1, immediate
    """
    def execute(self, cpu):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) // self.immediate)  # Integer division

    @classmethod
    # TODO: Check if not division by zero
    def validate(cls, args: list[str], valid_registers: set[str]):
        pass

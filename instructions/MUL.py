from instruction import RTypeInstruction


class MUL(RTypeInstruction):
    """
    MUL instruction. Multiplies the values of r1 and r2 and stores the result in rd.
    The instruction format is: MUL rd, rs1, rs2
    """
    def execute(self, cpu):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) * cpu.read_register(self.rs2))

    

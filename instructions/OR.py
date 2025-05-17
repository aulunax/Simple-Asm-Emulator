from instruction_interfaces import RTypeInstruction


class OR(RTypeInstruction):
    """
    OR instruction. Performs bitwise OR operation on the values of r1 and r2 and stores the result in rd.
    The instruction format is: OR rd, rs1, rs2
    """
    def execute(self, cpu):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) | cpu.read_register(self.rs2))


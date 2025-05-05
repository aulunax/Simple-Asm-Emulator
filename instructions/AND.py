from instruction  import Instruction, RTypeInstruction


class AND(RTypeInstruction):
    """
    AND instruction. Performs bitwise AND operation on the values of r1 and r2 and stores the result in rd.
    The instruction format is: AND rd, rs1, rs2
    """
    def execute(self, cpu):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) & cpu.read_register(self.rs2))
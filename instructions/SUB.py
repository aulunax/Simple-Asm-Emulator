from instruction_interfaces import  RTypeInstruction
from cpu import CPU

class SUB(RTypeInstruction):
    """
    SUB instruction. Performs operation r1 - r2 and stores it's outcome in rd.
    The instruction format is: SUB rd, rs1, rs2
    """
    def execute(self, cpu: CPU):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) - cpu.read_register(self.rs2))



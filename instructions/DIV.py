from instruction import Instruction, RTypeInstruction


class DIV(RTypeInstruction):
    """
    DIV instruction. Divides the value of r1 by r2 and stores the result in rd.
    The instruction format is: DIV rd, rs1, rs2
    """
    def execute(self, cpu):
        if cpu.read_register(self.rs2) == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        cpu.write_register(self.rd, cpu.read_register(self.rs1) // cpu.read_register(self.rs2))

    @classmethod 
    def validate(cls, args: list[str], valid_registers: set[str]):
        pass
        # TODO check if not division by zero
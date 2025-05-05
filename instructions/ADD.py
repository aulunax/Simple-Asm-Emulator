from instruction import Instruction, RTypeInstruction

class ADD(RTypeInstruction):
    """
    ADD instruction. Adds the values of two registers and stores the result in a third register.
    The instruction format is: ADD rd, rs1, rs2
    """
    def execute(self, cpu):
        cpu.write_register(self.rd, cpu.read_register(self.rs1) + cpu.read_register(self.rs2))

    @classmethod
    def validate(cls, args: list[str], valid_registers: set[str]):
        if len(args) != 3:
            raise ValueError("ADD instruction requires exactly 3 arguments: rd, rs1, rs2.")

        rd, rs1, rs2 = args

        if rd == 'R0':
            raise ValueError("Cannot write to R0, it is always 0.")
        for reg in (rd, rs1, rs2):
            if reg not in valid_registers:
                raise ValueError(f"Register {reg} does not exist.")
            
    


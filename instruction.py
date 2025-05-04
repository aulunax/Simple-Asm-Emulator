class Instruction:
    def execute(self, cpu):
        raise NotImplementedError()

    @classmethod
    def validate(cls, args: list[str]):
        raise NotImplementedError()

class RTypeInstruction(Instruction):
    def __init__(self, rd, rs1, rs2):
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2

class ITypeInstruction(Instruction):
    def __init__(self, rd, imm, rs1):
        self.rd = rd
        self.imm = int(imm, 0)  # auto-detect hex/dec
        self.rs1 = rs1

        

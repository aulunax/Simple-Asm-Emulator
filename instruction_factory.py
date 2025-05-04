from instructions.ADD import ADD
from cpu import CPU

class InstructionFactory :
    def __init__(self, cpu: CPU):
        self._cpu = cpu
        self.instructions = {
            'ADD': ADD
            
        }

    def create_instruction(self, opcode, *args):
        if opcode in self.instructions:
            # Validate the instruction arguments
            self.instructions[opcode].validate(list(args), self._cpu.get_valid_registers())
            return self.instructions[opcode](*args)
        else:
            raise ValueError(f"Unknown opcode: {opcode}")
from instruction_interfaces import MemoryInstructions


class LDW(MemoryInstructions):
    """
    LDW instruction. Loads a word from memory into a register.
    The instruction format is: LDW rd, offset(rs1)
    """
    def execute(self, cpu):
        # TODO : Check if the address is valid, maby do it in cpu 
        # Calculate the effective address
        effective_address = cpu.read_register(self.rs1) + self.offset
        # Load the word from memory into the destination register
        cpu.write_register(self.rd, cpu.memory.load_word(effective_address))

    
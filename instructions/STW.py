from instruction_interfaces import MemoryInstructions


class STW(MemoryInstructions):
    """
    STW instruction. Stores a word from a register into memory.
    The instruction format is: STW rs1, offset(rs2)
    """
    def execute(self, cpu):
        # TODO : Check if the address is valid, maybe do it in cpu
        # Calculate the effective address
        effective_address = cpu.read_register(self.rs2) + self.offset
        # Store the word from the source register into memory
        cpu.memory.store_word(effective_address, cpu.read_register(self.rs1))

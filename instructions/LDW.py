from instruction_interfaces import MemoryInstructions


class LDW(MemoryInstructions):
    """
    LDW instruction. Loads a word from memory into a register.
    The instruction format is: LDW r1, offset(r2)
    """

    def id(self, cpu):
        """
        Fetch the value of the first register from the CPU.
        """
        self.r2_val = cpu.read_register(self.r2)
      
    def ex(self, cpu):
        """
        Execute the instruction using the CPU.
        """
        # Calculate the effective address
        self.effective_address = self.r2_val + self.offset

    def mem(self, cpu):
        """
        Memory stage for LDW instruction.
        Load the word from memory into the destination register.
        """
        if cpu.is_valid_mem_addr(self.effective_address) == False:
            print(f"Invalid memory address: {self.effective_address}")
            raise Exception("Invalid memory address")
        else:
            self.result = cpu.read_dword(self.effective_address)

    def wb(self, cpu):
        """
        Write the result back to the destination register in the CPU.
        """
        if self.r1 != 'R0':
            cpu.write_register(self.r1, self.result)
        # R0 is always 0, so we don't write to it

    def __str__(self):
        """
        String representation of the LDW instruction.
        """
        return f"LDW {self.r1}, {self.offset}({self.r2}) "


    
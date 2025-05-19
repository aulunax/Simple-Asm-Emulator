from instruction_interfaces import MemoryInstructions


class STW(MemoryInstructions):
    """
    STW instruction. Stores a word from a register into memory.
    The instruction format is: STW r1, offset(r2)
    """

    def id(self, cpu):
        """
        Fetch the value of the first register from the CPU.
        """
        self.r2_val = cpu.read_register(self.r2)
        self.r1_val = cpu.read_register(self.r1)

    def ex(self, cpu):
        """
        Execute the instruction using the CPU.
        """
        # Calculate the effective address
        self.effective_address = self.r2_val + self.offset

    def mem(self, cpu):
        """
        Memory stage for STW instruction.
        Store the word from the source register into memory.
        """

        if(cpu.is_valid_mem_addr(self.effective_address) == False):
            print(f"Invalid memory address: {self.effective_address}")
            print(f"Register {self.r1} value: {cpu.read_register(self.r1)}")
            print(f"Register {self.r2} value: {cpu.read_register(self.r2)}")
            print(f"Offset value: {self.offset}")
            print(cpu.registers_to_string())
            raise Exception("Invalid memory address")
        else:
            cpu.write_dword(self.effective_address, self.r1_val)

    def wb(self, cpu):
        """
        Write the result back to the destination register in the CPU.
        """
        # No write-back needed for STW, as it only writes to memory
        pass

    def __str__(self):
        """
        String representation of the STW instruction.
        """
        return f"STW {self.r1}, {self.offset}({self.r2}) "
    

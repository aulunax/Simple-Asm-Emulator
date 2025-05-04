import random

class CPU:
    def __init__(self, number_of_registers:int=32, memory_size_bytes:int=1024):
        #TODO : Initialize memory with values from laboratory file
        """
        Initialize the CPU with a given number of registers and memory size.
        The registers are initialized with random values, and the memory is initialized to zero as of now.
        Args:
            number_of_registers (int): Number of registers to initialize. Default is 8.
            memory_size (int): Size of the memory in bytes. Default is 1024 bytes.
        """

        self._registers = {}
        for i in range(number_of_registers):  # R0 to R7
            name = f'R{i}'
            if name == 'R0':
                self._registers[name] = 0  # Always 0
            else:
                self._registers[name] = random.getrandbits(32)
        self._memory = bytearray(memory_size_bytes)  # Initialize memory with the given size
        self._PC = 0 # Instruction Pointer


    def read_dword(self, addr:int) -> int:
        """
        Read a double word (4 bytes) from memory at the given address.
        Args:
            addr (hex): Address to read from.
        Returns:
            hex: The value read from memory as a hex value.
        """
        return int.from_bytes(self._memory[addr:addr+4], byteorder='little')
    
    def write_dword(self, addr:int, value:int) -> None:
        """
        Write a double word (4 bytes) to memory at the given address.
        Args:
            addr (hex): Address to write to.
            value (hex): Value to write to memory.
        """
        self._memory[addr:addr+4] = value.to_bytes(4, byteorder='little')

    def read_register(self, reg_name:str) -> int:
        """
        Read the value of a register.
        Args:
            reg_name (str): Name of the register to read.
        Returns:
            hex: The value of the register as a hex value.
        """
        return self._registers.get(reg_name, None)   
    

    def write_register(self, reg_name:str, value:int) -> None:
        """
        Write a value to a register.
        Args:
            reg_name (str): Name of the register to write to.
            value (hex): Value to write to the register.
        """

        if reg_name == 'R0':
            raise ValueError("Cannot write to R0, it is always 0.")
        
        
        if reg_name in self._registers:
            value &= 0xFFFFFFFF  # Ensure value is a 32-bit integer
            self._registers[reg_name] = value
        else:
            raise ValueError(f"Register {reg_name} does not exist.")

    def print_memory(self) -> None:
        """
        Print the current state of the memory as hex values.

        """
        for i in range(0, len(self._memory), 32):
            line = " ".join(f"0x{self.read_dword(j):08X}" for j in range(i, min(i + 32, len(self._memory)), 4))
            print(line)

    def registers_to_string(self) -> str:
        """
        Print the current state of the registers as hex values.
        """
        return "\n".join(f"{name}: 0x{value:08X}" for name, value in self._registers.items())
    
    def set_PC(self, value:int) -> None:
        """
        Set the Instruction Pointer (IP) to a given value.
        Args:
            value (int): Value to set the IP to.
        """
        self._PC = value & 0xFFFFFFFF
        # Ensure IP is a 32-bit integer
        #TODO : Add check for valid IP range

    def inc_PC(self) -> None:
        """
        Increment the Instruction Pointer (IP) by 4.
        """
        self._PC += 4
        # Ensure IP is a 32-bit integer
        #TODO : Add check for valid IP range

    def get_valid_registers(self) -> set[str]:
        """
        Get a set of valid register names.
        Returns:
            set: A set of valid register names.
        """
        return set(self._registers.keys())
    
    def get_PC(self) -> int:
        """
        Get the current value of the Instruction Pointer (IP).
        Returns:
            int: The current value of the IP.
        """
        return self._PC & 0xFFFFFFFF
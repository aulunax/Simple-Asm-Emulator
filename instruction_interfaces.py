from cpu import CPU
import re

class Instruction:

    @classmethod
    def validate(cls, args: list[str]):
        raise NotImplementedError()
    
    @classmethod 
    def parse(cls, string:str) -> tuple:
        """
        Parse the instruction string and return a tuple of components.
        """
        raise NotImplementedError()
    
    def id(self, cpu: CPU):
        """
        Fetch the value of the first register from the CPU.
        """
        raise NotImplementedError("ID method not implemented for Instruction")
        

    def ex(self, cpu: CPU):
        """
        Execute the instruction using the CPU.
        """
        raise NotImplementedError("Execute method not implemented for ITypeInstruction")
    
    def mem(self, cpu: CPU):
        """
        Memory stage for I-type instructions.
        This is a placeholder and may not be needed for all I-type instructions.
        """
        raise NotImplementedError("Memory method not implemented for ITypeInstruction")
    
    def wb(self, cpu: CPU):
        """
        Write the result back to the destination register in the CPU.
        """
        if self.rd != 'R0':
            cpu.write_register(self.rd, self.result)
        # R0 is always 0, so we don't write to it   
    

# ------------------------- R-Type Instructions ------------------------- #

class RTypeInstruction(Instruction):
    def __init__(self, r1:str, r2:str, rd:str):
        """
        Initialize the R-type instruction with the given registers.
        The register are strings, the exact value of register is not fetched yet, 
        see the id method in instruction class.
        Args:
            r1 (str): First register.
            r2 (str): Second register.
            rd (str): Destination register.
        """
        self.r1 = r1
        self.r2 = r2
        self.rd = rd

        self.r1_val: int | None = None
        self.r2_val: int | None = None
        self.result : int | None = None

    def id(self, cpu: CPU):
        """
        Fetch the values of the registers from the CPU.
        """
        self.r1_val = cpu.read_register(self.r1)
        self.r2_val = cpu.read_register(self.r2)

    
    def mem(self, cpu: CPU):
        pass
    
    
    @classmethod
    def parse(cls, string:str) -> tuple:
        # Expected format: R1, R2, R3 (no extra spaces, strict commas)
        pattern = r'^\s*(R[0-9]+),\s*(R[0-9]+),\s*(R[0-9]+)\s*$'
        match = re.match(pattern, string)
        if not match:
            raise ValueError(f"Invalid R-type syntax: '{string}' (expected 'R1, R2, R3')")
        return match.groups()
    
    
    @classmethod
    def validate(cls, args: list[str], valid_registers: set[str]):
        if len(args) != 3:
            raise ValueError(str(cls)+"instruction requires exactly 3 arguments: r1, r2, rd.")

        r1, r2, rd = args

        if rd == 'R0':
            raise ValueError("Cannot write to R0, it is always 0.")
        for reg in (r1, r2, rd):
            if reg not in valid_registers:
                raise ValueError(f"Register {reg} does not exist.")
    

# ------------------------- I-Type Instructions ------------------------- #

class ITypeInstruction(Instruction):
    def __init__(self, r1:str, immediate:str,  rd:str):
        """
        Initialize the I-type instruction with the given registers and immediate value.
        The register are strings, the exact value of register is not fetched yet, 
        see the id method in instruction class.
        Args:
            r1 (str): First register.
            immediate (int): Immediate value.
            rd (str): Destination register.
        """
        self.r1:str = r1
        self.immediate: int = int(immediate) & 0xFFFFFFFF  # Ensure it's a 32-bit value
        self.rd:str = rd

        self.r1_val: int | None = None
        self.result : int | None = None
    
    @classmethod
    def parse(cls, string:str) -> tuple:
        # Expected format: R1, immediate (in format 0xFFFFFFFF), R2 (no extra spaces, strict commas)
        pattern = r'^\s*(R[0-9]+)\s*,\s*(0x[0-9A-Fa-f]{8})\s*,\s*(R[0-9]+)\s*$'
        match = re.match(pattern, string)
        if not match:
            raise ValueError(f"Invalid I-type syntax: '{string}' (expected 'R1, immediate (in format 0xFFFFFFFF), R2')")
        return match.groups()
    
    def id(self, cpu: CPU):
        """
        Fetch the value of the first register from the CPU.
        """
        self.r1_val = cpu.read_register(self.r1)
        # The immediate value is already set in the constructor

    def mem(self, cpu: CPU):
        pass
    



# ------------------------- Memory Instructions ------------------------- #

class MemoryInstructions(Instruction):

    def __init__(self, r1:str, immediate:str, r2:str):
        """
        Initialize the Memory instruction with the given registers and immediate value.
        The register are strings, the exact value of register is not fetched yet, 
        see the id method in instruction class.
        Args:
            r1 (str): First register.
            immediate (int): Immediate value.
            r2 (str): Second register.
        """
        self.r1:str = r1
        self.immediate: int = int(immediate) & 0xFFFFFFFF
        self.r2:str = r2

        self.effective_address: int | None = None
        self.r1_val: int | None = None
        self.r2_val: int | None = None

   
    @classmethod
    def parse(cls, string:str) -> tuple:
        # Expected format: R1, immediate (in format 0xFFFFFFFF), R2 (no extra spaces, strict commas)
        pattern = r'^\s*(R[0-9]+)\s*,\s*(0x[0-9A-Fa-f]{8})\((R[0-9]+)\)\s*$'
        match = re.match(pattern, string)
        if not match:
            raise ValueError(f"Invalid Memory instruction syntax: '{string}' (expected 'R1, imm(R2)' imm in format 0xFFFFFFFF)")
        return match.groups()
    


class BranchInstructions(ITypeInstruction):
    @classmethod
    def parse(cls, string:str) -> tuple:
        # Expected format: R1, immediate (in format 0xFFFFFFFF), R2 (no extra spaces, strict commas)
        pattern = r'^\s*(R[0-9]+)\s*,\s*(0x[0-9A-Fa-f]{8}|[a-zA-Z0-9]+)\s*$'
        match = re.match(pattern, string)
        if not match:
            raise ValueError(f"Invalid Branch instruction syntax: '{string}' (expected 'R1, j' j could be a label or immediate in format 0xFFFFFFFF)")
        return match.groups()


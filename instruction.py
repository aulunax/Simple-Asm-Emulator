from cpu import CPU
import re

class Instruction:

    def execute(self, cpu):
        raise NotImplementedError()

    @classmethod
    def validate(cls, args: list[str]):
        raise NotImplementedError()
    
    @classmethod 
    def parse(cls, string:str) -> tuple:
        """
        Parse the instruction string and return a tuple of components.
        """
        raise NotImplementedError()

class RTypeInstruction(Instruction):
    def __init__(self, rd:int, r1:int, r2:int):
        pass

    @classmethod
    def parse(cls, string:str) -> tuple:
        # Expected format: R1, R2, R3 (no extra spaces, strict commas)
        pattern = r'^\s*(R[0-9]+),\s*(R[0-9]+),\s*(R[0-9]+)\s*$'
        match = re.match(pattern, string)
        if not match:
            raise ValueError(f"Invalid R-type syntax: '{string}' (expected 'R1, R2, R3')")
        return match.groups()

class ITypeInstruction(Instruction):
    def __init__(self, rd:int, immediate:int,  r1:int ):
        pass
    
    @classmethod
    def parse(cls, string:str) -> tuple:
        # Expected format: R1, R2, immediate (no extra spaces, strict commas)
        pattern = r'^\s*(R[0-9]+)\s*,\s*(0x[0-9A-Fa-f]{8})\s*,\s*(R[0-9]+)\s*$'
        match = re.match(pattern, string)
        if not match:
            raise ValueError(f"Invalid I-type syntax: '{string}' (expected 'R1, immediate (in format 0xFFFFFFFF), R2')")
        return match.groups()
    

class MemoryInstructions(ITypeInstruction):
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


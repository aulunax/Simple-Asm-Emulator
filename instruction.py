from cpu import CPU
import re

class Instruction:

    _instruction_syntax = None

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
    def __init__(self, rd:int, r1:int, immediate:int):
        pass
    def parse(self, string:str)-> tuple:
        pass
    



from cpu import CPU

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
        string = string.strip()
        string = string.replace(",", "")
        components = string.split()
        
        if len(components) != 3:
            raise ValueError(f"Invalid instruction format: {string}")
        
        return tuple(components)

class ITypeInstruction(Instruction):
    def __init__(self, rd:int, r1:int, immediate:int):
        pass
    def parse(self, string:str)-> tuple:
        pass
    



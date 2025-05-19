from instruction_interfaces import RTypeInstruction


class NOP():

    def __init__(*args, **kwargs):
        pass
    """
    No Operation (NOP) instruction. It does nothing and is used for timing or alignment purposes.
    """

    def id(self, cpu) -> bool:
        """
        ID stage for NOP instruction. It does nothing.
        """
        # NOP does not require any register values
        stall:bool = False
        return stall

    def ex(self, cpu):
        """
        Execute the NOP instruction. It does nothing.
        """
        # NOP does not change any state or registers
        pass

    def mem(self, cpu):
        """
        Memory stage for NOP instruction. It does nothing.
        """
        # NOP does not require any memory access
        pass

    def wb(self, cpu):
        """
        Write-back stage for NOP instruction. It does nothing.
        """
        # NOP does not write back any result
        pass
    


    @classmethod
    def validate(cls, args: list[str], valid_registers: set[str], label_dict: dict[str, int] | None = None, line_number: int | None = None):
        if len(args) != 0:
            raise ValueError("NOP instruction does not require any arguments.")
        
    @classmethod
    def parse(cls, string: str) -> tuple:
        # NOP does not take any arguments
        if string.strip():
            raise ValueError("NOP instruction does not take any arguments.")
        return ()
    
    def __str__(self):
        """
        String representation of the NOP instruction.
        """
        return "NOP"
from instruction import RTypeInstruction


class NOP(RTypeInstruction):
    """
    No Operation (NOP) instruction. It does nothing and is used for timing or alignment purposes.
    """
    def execute(self, cpu):
        # NOP does nothing
        pass

    @classmethod
    def validate(cls, args: list[str], valid_registers: set[str]):
        if len(args) != 0:
            raise ValueError("NOP instruction does not require any arguments.")
        
    @classmethod
    def parse(cls, string: str) -> tuple:
        # NOP does not take any arguments
        if string.strip():
            raise ValueError("NOP instruction does not take any arguments.")
        return ()
from instruction_interfaces import  RTypeInstruction
from cpu import CPU

class SUB(RTypeInstruction):
    """
    SUB instruction. Performs operation r1 - r2 and stores it's outcome in rd.
    The instruction format is: SUB r1, r2, rd
    """

    def ex(self, cpu: CPU) -> None:
        """
        Execute the SUB instruction.
        """
        # Perform the subtraction
        self.result = self.r1_val - self.r2_val
        



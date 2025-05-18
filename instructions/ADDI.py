from instruction_interfaces import ITypeInstruction

class ADDI(ITypeInstruction):
    """
    ADDI instruction. Adds an immediate value to a register and stores the result in a destination register.
    The instruction format is: ADDI r1, immediate, rd
    """

    def ex(self, cpu):
        """
        Execute the ADDI instruction.
        """
        if self.r1_val is None:
            raise ValueError("Register value not set. Ensure ID stage is called before EX stage.")
        
        self.result = self.r1_val + self.immediate
        # Handle overflow if necessary (depends on architecture)

   
        
    


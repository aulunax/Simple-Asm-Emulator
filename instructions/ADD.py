from instruction_interfaces import RTypeInstruction

class ADD(RTypeInstruction):
    """
    ADD instruction. Adds the values of two registers and stores the result in a third register.
    The instruction format is: ADD r1, r2, rd
    """
    
    def ex(self, cpu):
        """
        Execute the ADD instruction.
        """
        if self.r1_val is None or self.r2_val is None:
            raise ValueError("Register values not set. Ensure ID stage is called before EX stage.")
        
        self.result = self.r1_val + self.r2_val
        # Handle overflow if necessary (depends on architecture)


    def __str__(self):
        """
        String representation of the ADD instruction.
        """
        return f"ADD {self.r1}, {self.r2}, {self.rd} "


            
    


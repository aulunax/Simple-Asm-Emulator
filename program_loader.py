from cpu import CPU
from instruction import Instruction
from debugger_gui import DebuggerGUI
from instruction_set import INSTRUCTION_SET



class ProgramLoader:
    def __init__(self, cpu: CPU, gui: DebuggerGUI):
        self.cpu = cpu
        self._labels = {}
        self._parsed_input = [str, tuple] # Stores opcode and tuple of components for future validation
        self._program: list[Instruction] = []
        self.gui = gui
        self._line_number = 0


    def load_program(self, program_path: str):
        """
        Load a program from a file into memory.
        Args:
            program_path (str): Path to the program file.
        """
        with open(program_path, 'r') as file:
            for line_content in file:
                self.parse_lines(line_content.strip())
                self._line_number += 1
            
        
        
    def parse_lines(self, line: str):
        """
        Load the next instruction into memory and execute it.
        Args:
            line (str): The line of assembly code to load.
        """
        # Parse the line to get the label and components
        line = self.strip_label(line)

        # Get the opcode and delete it from the line
        opcode, _, line = line.partition(' ')
        opcode = opcode.strip()
        line = line.strip()


        if opcode not in INSTRUCTION_SET:
            raise ValueError(f"Unknown instruction: {opcode} (line: {line})")
        
        instruction_class = INSTRUCTION_SET[opcode]

        # Parse the instruction line to get the components

        self._parsed_input.append((opcode,instruction_class.parse(line)))

        
        

    def strip_label(self, line:str) -> str:
        """
        Get the label from the line if it exists.
        If label exits than cut it from the original string
        and add it to the label dictionary

        Args:
            line (str) The line of assembly code to check for label
            It is passed through reference 
            

        """
        first, _ , rest = line.partition(' ')
        if first.endswith(':'):
            label = first[:-1]
            self._labels[label] = self._line_number * 4
            return rest.lstrip()
        return line

    def print_state(self):
        """
        Print the current state of the program loader.
        """
        print(f"Current line number: {self._line_number}")
        print(f"Labels: {self._labels}")
        print(f"Parsed input: {self._parsed_input}")
        print(f"Program: {self._program}")


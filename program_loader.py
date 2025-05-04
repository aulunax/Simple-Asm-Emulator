from cpu import CPU
from instruction import Instruction, RTypeInstruction, ITypeInstruction
from debugger_gui import DebuggerGUI
from instruction_factory import InstructionFactory
from parser import parse_line


class ProgramLoader:
    def __init__(self, cpu: CPU, gui: DebuggerGUI):
        self.cpu = cpu
        self.labels = {}
        self.gui = gui


    def load_program(self, program_path: str):
        """
        Load a program from a file into memory.
        Args:
            program_path (str): Path to the program file.
        """
        with open(program_path, 'r') as file:
            for addr, line_content in enumerate(file):
                self.load_next_instruction(line_content.strip(), addr)
            
        
        
    def load_next_instruction(self, line: str, addr: int):
        """
        Load the next instruction into memory and execute it.
        Args:
            line (str): The line of assembly code to load.
        """
        # Parse the line to get the label and components
        label, components = parse_line(line)
        
        # If a label is found, store it in the labels dictionary
        if label:
            self.labels[label] = addr * 4
        
        # Create an instruction from the components
        instruction = InstructionFactory(self.cpu).create_instruction(*components)
        instruction.execute(self.cpu)
        self.gui.update_and_wait()
        self.cpu.inc_PC()
        

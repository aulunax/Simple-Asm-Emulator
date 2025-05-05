from debugger_gui import DebuggerGUI
from cpu import CPU
from program_loader import ProgramLoader

if __name__ == "__main__":
    # Initialize the CPU and GUI
    cpu = CPU()
    gui = DebuggerGUI(cpu)
    gui.update_and_wait()
    # Load the program into memory
    program_loader = ProgramLoader(cpu, gui)
    program_loader.load_program("instructions.txt")
    program_loader.print_state()
    
   

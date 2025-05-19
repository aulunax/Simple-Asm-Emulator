from debugger_gui import DebuggerGUI
from cpu import CPU
from program_loader import ProgramLoader
import time

if __name__ == "__main__":
    # Initialize the CPU and GUI
    cpu = CPU()
    gui = DebuggerGUI(cpu)
    #gui.update_and_wait()
    # Load the program into memory\
    start_time = time.time()
    cpu.load_memory_from_dump("initial_data.txt")
    program_loader = ProgramLoader(cpu, gui)
    program_loader.load_program("instructions.txt")
    #program_loader.print_state()
    program_loader.run_program()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    cpu.print_memory()
    
   

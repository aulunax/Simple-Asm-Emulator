from cpu import CPU
from program_loader import ProgramLoader
import time

if __name__ == "__main__":
    cpu = CPU()
    start_time = time.time()
    cpu.load_memory_from_dump("initial_data.txt")
    program_loader = ProgramLoader(cpu)
 
    program_loader.load_program("instructions2.txt")
    #program_loader.load_program_from_string(instructions)
    program_loader.run_program()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")
    result = program_loader.compare_results()
    print(f"Comparison result: {result}")
    cpu.print_memory()
    
   

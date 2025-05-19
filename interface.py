from cpu import CPU
from program_loader import ProgramLoader
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mem', default="initial_data.txt", help="Path to memory dump file")
    parser.add_argument('--prog', help="Path to program instructions")
    parser.add_argument('--ref', default="correct_result.txt", help="Path to expected results file")
    parser.add_argument('--simple', default=False, help="Simplify output of the program")
    parser.add_argument('--instr', help="Raw instruction string to load instead of file")
    args = parser.parse_args()

    cpu = CPU()
    cpu.load_memory_from_dump(args.mem)
    program_loader = ProgramLoader(cpu)
    

    if args.instr:
        instr_str = args.instr.replace('\\n', '\n')
        try:
            program_loader.load_program_from_string(instr_str)
        except Exception as e:
            print("Invalid")
    elif args.prog:
        try:
            program_loader.load_program(args.prog)
        except Exception as e:
            print("Invalid")
            exit(0)
    else:
        raise ValueError("No program file or instruction string provided.")

    try:
        cycles = program_loader.run_program()
    except Exception as e:
        print("Error")
        exit(0)

    print("Completed")
    print(cycles)
    print(program_loader.compare_results(args.ref))
    
    if not args.simple:
        cpu.print_memory_simple()
from cpu import CPU


if __name__ == "__main__":
    # Initialize the CPU with default values
    cpu = CPU()
    # Print the initial state of the CPU
    print("Initial CPU State:")
    cpu.print_registers()
    print("Memory Size:", len(cpu.memory), "bytes")
    print("Instruction Pointer (IP):", cpu.IP)
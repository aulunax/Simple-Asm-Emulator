from debugger_gui import DebuggerGUI
from cpu import CPU

if __name__ == "__main__":
    cpu = CPU()
    gui = DebuggerGUI(cpu)

    # Simulate execution
    cpu.write_register("R1", 0x11111111)
    gui.update_and_wait()

    cpu.write_register("R2", 0x22222222)
    gui.update_and_wait()

    # Add more steps as needed

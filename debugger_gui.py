import tkinter as tk
from cpu import CPU

class DebuggerGUI:
    def __init__(self, cpu: CPU):
        self.cpu = cpu
        self.root = tk.Tk()
        self.root.title("CPU Registers")

        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        scrollbar = tk.Scrollbar(self.root, command=self.text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=scrollbar.set)

        self.next_pressed = False
        self.button = tk.Button(self.root, text="Next", command=self._on_next)
        self.button.pack()

    def _on_next(self):
        self.next_pressed = True

    def update_and_wait(self):
        self.text_area.delete(1.0, 'end')
        self.text_area.insert('end', self.cpu.registers_to_string())
        self.next_pressed = False
        self.root.update()
        self._wait_for_next()

    def _wait_for_next(self):
        # Wait until user clicks "Next"
        while not self.next_pressed:
            self.root.update()

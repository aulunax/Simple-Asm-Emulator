from instructions import ADD, NOP, SUB, MUL, DIV, AND, OR, XOR

INSTRUCTION_SET: dict[str, type] = {
    "ADD": ADD,
    "NOP": NOP,
    "SUB": SUB,  
    "MUL": MUL,
    "DIV": DIV,
    "AND": AND,
    "OR": OR,
    "XOR": XOR,

    # Add other instructions here
}
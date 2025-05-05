from instructions import ADD, NOP, SUB, MUL, DIV, AND, OR, XOR, ADDI, ANDI, ORI, SUBI, DIVI, MULI, XORI

INSTRUCTION_SET: dict[str, type] = {
    "ADD": ADD,
    "NOP": NOP,
    "SUB": SUB,  
    "MUL": MUL,
    "DIV": DIV,
    "AND": AND,
    "OR": OR,
    "XOR": XOR,
    "ADDI": ADDI,
    "ANDI": ANDI,
    "ORI": ORI,
    "SUBI": SUBI,
    "DIVI": DIVI,
    "MULI": MULI,
    "XORI": XORI

    # Add other instructions here
}
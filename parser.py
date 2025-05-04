from typing import Optional


def parse_line(line: str) -> tuple[Optional[str], list[str]]:
    label:str | None = None
    """
    Parse a line of assembly code into its components.
    Args:
        line (str): A line of assembly code.
    Returns:
        tuple: A tuple containing the label (if any) and a list of components (instruction and arguments).
    """
    # Separate text by whitespace 
    components = line.split()
    
    #Check if first component is a label ( label is in format of "label:")
    if components[0].endswith(':'):
        label = components[0][:-1]  # Remove the colon
        components = components[1:]  # Remove the label from the components
    else:
        label = None
    return label, components
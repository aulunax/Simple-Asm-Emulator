### TODO:

- [x] Parsing of the instruction can be simplified, now it is parsed at once and then chceck if opcode exists it should be as follwing:

1. Read label if exists
2. Read opcode
3. Check if opcode exists, if yes then check the syntax of a given instruction
4. Call the factory, or get rid of factory pattern and just run execute

- [ ] Change structure of all instruction R3 is the destination register not r1

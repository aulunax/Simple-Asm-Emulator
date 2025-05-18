### TODO:

- [x] Parsing of the instruction can be simplified, now it is parsed at once and then chceck if opcode exists it should be as follwing:

1. Read label if exists
2. Read opcode
3. Check if opcode exists, if yes then check the syntax of a given instruction
4. Call the factory, or get rid of factory pattern and just run execute

- [x] Change structure of all instruction R3 is the destination register not r1

- [ ] Parser should ignore empty lines in the file, and treat them as nop

- [ ] Error handling should be improved

- [ ] Validation should run before the execution and it should:

  1. Check if the label is in instruction and replace it with addr
  2. If addr is passed check if it's in code
  3. Check if the registers used are available
  4. Check if instructions have proper number of arguments

- [ ] Validation of the memory and branch classes

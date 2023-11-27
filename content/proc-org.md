+++
title = "Processor Organization Page"
+++

### Short Introduction
The developed architecture is based on the von Neumann model. Its most important components are:
- memory containing both the program code and its data
- arithmetic-logic unit performing arithmetic and logical operations
- control unit that fetches and executes successive instructions
- peripheral devices responsible for processor-user interaction

### Units
- **Arithmetic Logic Unit** - \\( \texttt{ALU} \\): Unit that performs arithmetic calculations in the two's complement system (arithmetic negation, addition, subtraction, multiplication by 2, and division by 2), logical calculations (not, or, and, xor, right shift, and left shift), and generates constants (zero, one, minus one)
- **Memory Unit** - \\( \texttt{MU} \\): Unit that writes words to memory and reads words from memory using \\( \texttt{REG_MBR} \\) and \\( \texttt{REG_MAR} \\); memory word is 8-bit; memory has \\(2^{17}\\) addresses - MSB of address can be set programmatically, further bits are taken from \\(\texttt{REG_MAR} \\); the 8 highest bits of \\( \texttt{MAR} \\) can be easily programmatically cleared to read a word using fewer operations
- **Control Unit** - \\( \texttt{CU} \\): Unit that is responsible for entering the program into memory, fetching and executing successive instructions (sending signals to units), interpreting \\(\texttt{ALU} \\) flags, and processing interrupts; it uses a microcode counter - \\( \texttt{MC} \\) - to perform microinstructions (each instruction consists of a few microinstructions); logic is programmed on EEPROMs
- **Program Counter Unit** - \\( \texttt{PC} \\): Unit that counts and holds the address of the next instruction in memory to perform; the value of \\( \texttt{PC} \\) can also be cleared or set from \\(\texttt{ADDRESS_BUS} \\)
- **Stack Counter Unit** - \\( \texttt{STC} \\): Unit that counts and holds the address of the current stack top; the value of \\( \texttt{STC} \\) can also be cleared or set from \\(\texttt{ADDRESS_BUS}\\)
- **Clock Unit** - \\( \texttt{CLK} \\): Unit that generates a signal with a preset frequency; the signal can also be generated using a button

### Registers
- **Register A** - \\( \texttt{REG_A} \\): 8-bit register, the first of the registers used by the ALU in the process of performing calculations
- **Register B** - \\( \texttt{REG_B} \\): 8-bit register, the second of the registers used by the ALU in the process of performing calculations
- **Temporary Register** - \\( \texttt{REG_TMP} \\): 16-bit register, it is used in the process of splitting a 16-bit address into two 8-bit words to write the address to memory or read the address from memory (memory words are 8-bit). It can also be used to store 8-bit data, then \\( \texttt{REG_TMP} \\) divides into \\( \texttt{REG_TMPH} \\) and \\( \texttt{REG_TMPL} \\)
- **Memory Access Register** - \\( \texttt{REG_MAR} \\): 16-bit register, it is used to store the address of memory to write a word to or read a word from memory
- **Memory Buffer Register** - \\( \texttt{REG_MBR} \\): 8-bit register, it is used to store a word to write a word to or read a word from memory
- **Flags Register** - \\( \texttt{REG_F} \\): 8-bit register, it is used to store flags of the \\( \texttt{ALU} \\)
- **Instruction Register** - \\( \texttt{REG_IR} \\): 8-bit register, it is used to hold the current opcode

### Buses
- **Data Bus** - 8-bit bus, it is used for transferring words between registers: \\(\texttt{REG_A} \\), \\( \texttt{REG_B} \\), \\( \texttt{REG_F} \\), \\( \texttt{REG_TMPH} \\), \\(\texttt{REG_TMPL}\\), \\( \texttt{REG_MBR} \\), \\( \texttt{REG_IR} \\)
- **Address Bus** - 16-bit bus, it is used for transferring addresses between \\(\texttt{REG_TMP} \\), \\( \texttt{REG_MAR} \\), \\( \texttt{PC} \\), \\( \texttt{STC} \\)

### ALU Flags
- **Sign Flag** - \\( \texttt{REG_F[0]} \\): If the bit is set, then the result was negative; otherwise, the result was non-negative
- **Parity Flag** - \\( \texttt{REG_F[1]} \\): If the bit is set, then the result was odd; otherwise, the result was even
- **Zero Flag** - \\( \texttt{REG_F[2]} \\): If the bit is set, then the result was not zero; otherwise, the result was zero
- **Carry Flag** - \\( \texttt{REG_F[3]} \\): If the bit is set, then the result for unsigned numbers operations is out of range; otherwise, the result is correct
- **Overflow Flag** - \\( \texttt{REG_F[4]} \\): If the bit is set, then the result for signed numbers operations is out of range; otherwise, the result is correct
- Bits \\( \texttt{REG_F[5]} \\), \\( \texttt{REG_F[6]} \\), \\( \texttt{REG_F[7]} \\) are not used


### Decoder
- **Decoder** is part of \\( \texttt{CU} \\). It decodes the opcode while taking \\(\texttt{REG_F}\\), interrupts, and operating mode (entering or executing program) into consideration.  
Decoding is a 3-step process:
  1. The input is \\(S_4S_3S_2S_1S_0I_7I_6I_5I_4I_3I_2I_1I_0\\), where \\(S_k\\) is the bit representing the k-th interrupt and \\(I_7I_6I_5I_4I_3I_2I_1I_0\\) is read from the memory opcode. If each \\(S_k\\) is equal to zero, then the result is \\(I_7I_6I_5I_4I_3I_2I_1I_0\\), otherwise, the result is an 8-bit opcode representing a jump to a defined address in memory to handle a specific interrupt. Let's denote the output by \\(I^{'}_7I^{'}_6I^{'}_5I^{'}_4I^{'}_3I^{'}_2I^{'}_1I^{'}_0\\).
  2. The input is \\(F_4F_3F_2F_1F_0I_7I_6I_5I_4I_3I_2I_1I_0\\), where \\(F_k\\) is \\(\texttt{REG_F}[k]\\) and \\(I^{'}_7I^{'}_6I^{'}_5I^{'}_4I^{'}_3I^{'}_2I^{'}_1I^{'}_0\\) is the preprocessed opcode. If the preprocessed opcode depends on flags (e.g., conditional jumps) and the proper flag is set correctly, then the result is the preprocessed opcode. If the proper flag is set incorrectly, then the result is a skip opcode. If the preprocessed opcode doesn't depend on flags, then the result is the preprocessed opcode. Let's denote the output by \\(I^{''}_7I^{''}_6I^{''}_5I^{''}_4I^{''}_3I^{''}_2I^{''}_1I^{''}_0\\).
  3. The input is \\(MI^{''}_7I^{''}_6I^{''}_5I^{''}_4I^{''}_3I^{''}_2I^{''}_1I^{''}_0C_3C_2C_1C_0\\), where \\(M\\) is the operating mode, \\(I^{''}_7I^{''}_6I^{''}_5I^{''}_4I^{''}_3I^{''}_2I^{''}_1I^{''}_0\\) is the proper opcode, and \\(C_3C_2C_1C_0\\) is the microcode counter. The output for each microcode is a set of signals that manage all the components.

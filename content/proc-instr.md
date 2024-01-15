+++
title = "Processor Instructions Page"
+++

### Short Introduction
The processor implements the **CISC** architecture: Complex Instruction Set Computing - each instruction is specialised and consist of few microinstructions. Each instruction has own 8-bit opcode so the maximum number of instructions is 256.

{% button(link="/instructions.json") %}
    Download instructions.json
{% end %}

### Fetch-Decode-Execute Cycle
- **Fetch:** Address of the next instruction is written from \\( \texttt{PC} \\) to \\(\texttt{MAR}\\). Word at this address in memory is written to \\( \texttt{REG_IR} \\).
- **Decode:** Logic programmed in EEPROMs decodes the instruction opcode.
- **Execute:** Successive microcodes produce a sequence of control signals to processor components.

Fetch always takes 2 cycles. Decode + Execute takes a variable number of cycles.

### Instruction Table
Fetching instruction:  
\\( \texttt{REG_MAR} \leftarrow \texttt{PC} \\)  
\\( \texttt{REG_IR} \leftarrow \texttt{MEM[REG_MAR]} \quad \\& \quad \texttt{PC} \leftarrow \texttt{PC + 1} \\)

#### Move Instructions
{{ instructiontable(start=0,end=41) }}

#### ALU Instructions
{{ instructiontable(start=41,end=151) }}


+++
title = "Processor Instructions Page"
+++

<br><br>

### Short Introduction
The processor implements the **CISC** architecture: Complex Instruction Set Computing - each instruction is specialised and consist of few microinstructions. Each instruction has own 8-bit opcode so the maximum number of instructions is 256.

### Fetch-Decode-Execute Cycle
- **Fetch:** Address of the next instruction is written from \\( \texttt{PC} \\) to \\(\texttt{MAR}\\). Word at this address in memory is written to \\( \texttt{REG_IR} \\).
- **Decode:** Logic programmed in EEPROMs decodes the instruction opcode.
- **Execute:** Successive microcodes produce a sequence of control signals to processor components.

Fetch always takes 2 cycles. Decode + Execute takes a variable number of cycles.
Each cycle ends with \\( \texttt{MC} \\) reset.

### General Instruction Table
Fetching instruction:  
\\( \texttt{REG_MAR} \leftarrow \texttt{PC} \\)  
\\( \texttt{REG_IR} \leftarrow \texttt{MEM[REG_MAR]} \quad \\& \quad \texttt{PC} \leftarrow \texttt{PC + 1} \\)

<br>

{{ generalinstructiontable() }}

<br><br><br>

### Detailed Instruction Table
#### Move Instructions
{{ detailedinstructiontable(start=0,end=49) }}

#### ALU Instructions
{{ detailedinstructiontable(start=49,end=162) }}

#### Jump Instructions
{{ detailedinstructiontable(start=162,end=206) }}

#### Stack Instructions
{{ detailedinstructiontable(start=206,end=221) }}

#### Other Instructions
{{ detailedinstructiontable(start=221,end=257) }}
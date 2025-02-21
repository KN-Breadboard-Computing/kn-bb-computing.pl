+++
title = "Processor Instructions Page"
+++

<br><br>

### Short Introduction
The processor implements the **CISC** architecture: Complex Instruction Set Computing - each instruction is specialised and consist of few microinstructions. Each instruction has own 8-bit opcode so the maximum number of instructions is 256.

{% button(link="/all-instructions.json") %}
    Download all-instructions.json
{% end %}

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
{{ detailedinstructiontable(start=0,end=70) }}

#### ALU Instructions
{{ detailedinstructiontable(start=70,end=177) }}

#### Jump Instructions
{{ detailedinstructiontable(start=177,end=221) }}

#### Stack Instructions
{{ detailedinstructiontable(start=221,end=238) }}

#### Other Instructions
{{ detailedinstructiontable(start=238,end=250) }}
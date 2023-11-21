+++
template = "processor-instructions.html"
+++

{{ hello() }}

<h3>Short Introduction</h3>
        <p>The processor implements the <strong>CISC</strong> architecture: Complex Instruction Set Computing - each
            instruction
            is specialised and consist of few microinstructions.
            Each instruction has own 8-bit opcode so the maximum number of instructions is 256.</p>

<h3>Fetch-Decode-Execute Cycle</h3>
<ul>
    <li>
        <strong>Fetch:</strong> Address of the next instruction is written from \( \texttt{PC} \) to \(
        \texttt{MAR}
        \). Word at this address in memory is written to \( \texttt{REG_IR} \).
    </li>
    <li>
        <strong>Decode:</strong> Logic programmed in EEPROMs decodes the instruction opcode.
    </li>
    <li>
        <strong>Execute:</strong> Successive microcodes produce a sequence of control signals to processor
        components.
    </li>
</ul>

<p>Fetch always takes 2 cycles. Decode + Execute takes a variable number of cycles.</p>

<h3>Instruction Table</h3>
<p>Fetching instruction: <br>
    \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br>
    \( \texttt{REG_IR} \leftarrow \texttt{MEM[REG_MAR]} \quad \& \quad \texttt{PC} \leftarrow
    \texttt{PC + 1} \)
</p>

<h4>Move Instructions</h4>
<table class="instruction_table" border="1">
    <thead>
        <tr>
            <th>No.</th>
            <th>Mnemonic</th>
            <th>Opcode</th>
            <th>Total Cycles Number</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1.</td>
            <td>\( \texttt{MOVAB} \)</td>
            <td>0b00000001</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_B} \)</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>\( \texttt{MOVBA} \)</td>
            <td>0b00000010</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_A} \)</td>
        </tr>
        <tr>
            <td>3.</td>
            <td>\( \texttt{MOVAF} \)</td>
            <td>0b00000011</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>4.</td>
            <td>\( \texttt{MOVBF} \)</td>
            <td>0b00000100</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>5.</td>
            <td>\( \texttt{MOVATH} \)</td>
            <td>0b00000101</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_TMPH} \)</td>
        </tr>
        <tr>
            <td>6.</td>
            <td>\( \texttt{MOVBTH} \)</td>
            <td>0b00000110</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_TMPH} \)</td>
        </tr>
        <tr>
            <td>7.</td>
            <td>\( \texttt{MOVATL} \)</td>
            <td>0b00000111</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_TMPL} \)</td>
        </tr>
        <tr>
            <td>8.</td>
            <td>\( \texttt{MOVBTL} \)</td>
            <td>0b00001000</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_TMPL} \)</td>
        </tr>
        <tr>
            <td>9.</td>
            <td>\( \texttt{MOVTHA} \)</td>
            <td>0b00001001</td>
            <td>3</td>
            <td>\( \texttt{REG_TMPH} \leftarrow \texttt{REG_A} \)</td>
        </tr>
        <tr>
            <td>10.</td>
            <td>\( \texttt{MOVTHB} \)</td>
            <td>0b00001010</td>
            <td>3</td>
            <td>\( \texttt{REG_TMPH} \leftarrow \texttt{REG_B} \)</td>
        </tr>
        <tr>
            <td>11.</td>
            <td>\( \texttt{MOVTLA} \)</td>
            <td>0b00001011</td>
            <td>3</td>
            <td>\( \texttt{REG_TMPL} \leftarrow \texttt{REG_A} \)</td>
        </tr>
        <tr>
            <td>12.</td>
            <td>\( \texttt{MOVTLB} \)</td>
            <td>0b00001100</td>
            <td>3</td>
            <td>\( \texttt{REG_TMPL} \leftarrow \texttt{REG_B} \)</td>
        </tr>
        <tr>
            <td>13.</td>
            <td>\( \texttt{MOVAIMM} \)</td>
            <td>0b00001101</td>
            <td>4</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_A} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \)</td>
        </tr>
        <tr>
            <td>14.</td>
            <td>\( \texttt{MOVBIMM} \)</td>
            <td>0b00001110</td>
            <td>4</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_B} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \)</td>
        </tr>
        <tr>
            <td>15.</td>
            <td>\( \texttt{MOVAABS} \)</td>
            <td>0b00001111</td>
            <td>8</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \(
                \texttt{REG_TMPL}
                \leftarrow \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC} \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow
                \texttt{REG_TMP} \)
                <br> \( \texttt{REG_A}
                \leftarrow \texttt{MEM[REG_MAR]} \)
            </td>
        </tr>
        <tr>
            <td>16.</td>
            <td>\( \texttt{MOVBABS} \)</td>
            <td>0b00010000</td>
            <td>8</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \(
                \texttt{REG_TMPL}
                \leftarrow \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC} \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow
                \texttt{REG_TMP} \)
                <br> \( \texttt{REG_B}
                \leftarrow \texttt{MEM[REG_MAR]} \)
            </td>
        </tr>
        <tr>
            <td>17.</td>
            <td>\( \texttt{MOVABSA} \)</td>
            <td>0b00010001</td>
            <td>8</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \(
                \texttt{REG_TMPL}
                \leftarrow \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC} \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow
                \texttt{REG_TMP} \)
                <br> \( \texttt{REG_MBR}
                \leftarrow \texttt{REG_A} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>18.</td>
            <td>\( \texttt{MOVABSB} \)</td>
            <td>0b00010010</td>
            <td>8</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \(
                \texttt{REG_TMPL}
                \leftarrow \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC} \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow
                \texttt{REG_TMP} \)
                <br> \( \texttt{REG_MBR}
                \leftarrow \texttt{REG_B} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>19.</td>
            <td>\( \texttt{MOVABSIMM} \)</td>
            <td>0b00010011</td>
            <td>10</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \(
                \texttt{REG_TMPL}
                \leftarrow \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC} \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow
                \texttt{PC} \)
                <br> \( \texttt{REG_MBR} \leftarrow
                \texttt{MEM[REG_MAR]} \quad \& \quad \texttt{PC} \leftarrow \texttt{PC+1} \) <br> \(
                \texttt{REG_MAR} \leftarrow
                \texttt{REG_TMP} \) <br> \(
                \texttt{MEM[REG_MAR]} \leftarrow \texttt{REG_MBR} \)
            </td>
        </tr>
    </tbody>
</table>


<h4>ALU Instructions</h4>
<table class="instruction_table" border="1">
    <thead>
        <tr>
            <th>No.</th>
            <th>Mnemonic</th>
            <th>Opcode</th>
            <th>Total Cycles Number</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>20.</td>
            <td>\(\texttt{NEGAA}\)</td>
            <td>0b00010100</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow - \texttt{REG_A} \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>21.</td>
            <td>\(\texttt{NEGAB}\)</td>
            <td>0b00010101</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow - \texttt{REG_A} \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>22.</td>
            <td>\(\texttt{NEGAMEM}\)</td>
            <td>0b00010110</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow -
                \texttt{REG_A}
                \quad \&
                \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>23.</td>
            <td>\(\texttt{NEGBA}\)</td>
            <td>0b00010111</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow - \texttt{REG_B} \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>24.</td>
            <td>\(\texttt{NEGBB}\)</td>
            <td>0b00011000</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow - \texttt{REG_B} \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>25.</td>
            <td>\(\texttt{NEGBMEM}\)</td>
            <td>0b00011001</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow -
                \texttt{REG_B}
                \quad \&
                \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>26.</td>
            <td>\(\texttt{ADDA}\)</td>
            <td>0b00011010</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_A} + \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>27.</td>
            <td>\(\texttt{ADDB}\)</td>
            <td>0b00011011</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_A} + \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>28.</td>
            <td>\(\texttt{ADDMEM}\)</td>
            <td>0b00011100</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_A} +
                \texttt{REG_B}
                \quad
                \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow
                \texttt{REG_MBR} \)</td>
        </tr>
        <tr>
            <td>29.</td>
            <td>\(\texttt{SUBABA}\)</td>
            <td>0b00011101</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_A} - \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>30.</td>
            <td>\(\texttt{SUBABB}\)</td>
            <td>0b00011110</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_A} - \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>31.</td>
            <td>\(\texttt{SUBABMEM}\)</td>
            <td>0b00011111</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_A} -
                \texttt{REG_B}
                \quad
                \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow
                \texttt{REG_MBR} \)</td>
        </tr>
        <tr>
            <td>32.</td>
            <td>\(\texttt{SUBBAA}\)</td>
            <td>0b00100000</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_B} - \texttt{REG_A} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>33.</td>
            <td>\(\texttt{SUBBAB}\)</td>
            <td>0b00100001</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_B} - \texttt{REG_A} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>34.</td>
            <td>\(\texttt{SUBBAMEM}\)</td>
            <td>0b00100010</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_B} -
                \texttt{REG_A}
                \quad
                \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow
                \texttt{REG_MBR} \)</td>
        </tr>
        <tr>
            <td>35.</td>
            <td>\(\texttt{MULA2A}\)</td>
            <td>0b00100011</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_A} \cdot 2 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>36.</td>
            <td>\(\texttt{MULA2B}\)</td>
            <td>0b00100100</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_A} \cdot 2 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>37.</td>
            <td>\(\texttt{MULA2MEM}\)</td>
            <td>0b00100101</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_A}
                \cdot 2
                \quad
                \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow
                \texttt{REG_MBR} \)</td>
        </tr>
        <tr>
            <td>38.</td>
            <td>\(\texttt{MULB2A}\)</td>
            <td>0b00100110</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_B} \cdot 2 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>39.</td>
            <td>\(\texttt{MULB2B}\)</td>
            <td>0b00100111</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_B} \cdot 2 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>40.</td>
            <td>\(\texttt{MULB2MEM}\)</td>
            <td>0b00101000</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_B}
                \cdot 2
                \quad
                \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow
                \texttt{REG_MBR} \)</td>
        </tr>
        <tr>
            <td>41.</td>
            <td>\(\texttt{DIVA2A}\)</td>
            <td>0b00101001</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_A} / 2 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>42.</td>
            <td>\(\texttt{DIVA2B}\)</td>
            <td>0b00101010</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_A} / 2 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>43.</td>
            <td>\(\texttt{DIVA2MEM}\)</td>
            <td>0b00101011</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_A} /
                2 \quad
                \&
                \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>44.</td>
            <td>\(\texttt{DIVB2A}\)</td>
            <td>0b00101100</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_B} / 2 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>45.</td>
            <td>\(\texttt{DIVB2B}\)</td>
            <td>0b00101101</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_B} / 2 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>46.</td>
            <td>\(\texttt{DIVB2MEM}\)</td>
            <td>0b00101110</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_B} /
                2 \quad
                \&
                \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>47.</td>
            <td>\(\texttt{INVAA}\)</td>
            <td>0b00101111</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{not } \texttt{REG_A} \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>48.</td>
            <td>\(\texttt{INVAB}\)</td>
            <td>0b00110000</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{not } \texttt{REG_A} \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>49.</td>
            <td>\(\texttt{INVAMEM}\)</td>
            <td>0b00110001</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{not }
                \texttt{REG_A}
                \quad \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]}
                \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>50.</td>
            <td>\(\texttt{INVBA}\)</td>
            <td>0b00110010</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{not } \texttt{REG_B} \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>51.</td>
            <td>\(\texttt{INVBB}\)</td>
            <td>0b00110011</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{not } \texttt{REG_B} \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>52.</td>
            <td>\(\texttt{INVBMEM}\)</td>
            <td>0b00110100</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{not }
                \texttt{REG_B}
                \quad \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]}
                \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>53.</td>
            <td>\(\texttt{ORA}\)</td>
            <td>0b00110101</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_A} \ \texttt{or} \ \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>54.</td>
            <td>\(\texttt{ORB}\)</td>
            <td>0b00110110</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_A} \ \texttt{or} \ \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>55.</td>
            <td>\(\texttt{ORMEM}\)</td>
            <td>0b00110111</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_A} \
                \texttt{or} \
                \texttt{REG_B} \quad \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \(
                \texttt{MEM[REG_MAR]}
                \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>56.</td>
            <td>\(\texttt{ANDA}\)</td>
            <td>0b00111000</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_A} \ \texttt{and} \ \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>57.</td>
            <td>\(\texttt{ANDB}\)</td>
            <td>0b00111001</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_A} \ \texttt{and} \ \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>58.</td>
            <td>\(\texttt{ANDMEM}\)</td>
            <td>0b00111010</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_A} \
                \texttt{and} \
                \texttt{REG_B} \quad \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \(
                \texttt{MEM[REG_MAR]}
                \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>59.</td>
            <td>\(\texttt{XORA}\)</td>
            <td>0b00111011</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_A} \ \texttt{xor} \ \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>60.</td>
            <td>\(\texttt{XORB}\)</td>
            <td>0b00111100</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_A} \ \texttt{xor} \ \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)
            </td>
        </tr>
        <tr>
            <td>61.</td>
            <td>\(\texttt{XORMEM}\)</td>
            <td>0b00111101</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_A} \
                \texttt{xor} \
                \texttt{REG_B} \quad \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \(
                \texttt{MEM[REG_MAR]}
                \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>62.</td>
            <td>\(\texttt{SHRAA}\)</td>
            <td>0b00111110</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_A} \ \gg \ 1 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>63.</td>
            <td>\(\texttt{SHRAB}\)</td>
            <td>0b00111111</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_A} \ \gg \ 1 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>64.</td>
            <td>\(\texttt{SHRAMEM}\)</td>
            <td>0b01000000</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_A} \
                \gg \ 1
                \quad \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]}
                \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>65.</td>
            <td>\(\texttt{SHRBA}\)</td>
            <td>0b01000001</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_B} \ \gg \ 1 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>66.</td>
            <td>\(\texttt{SHRBB}\)</td>
            <td>0b01000010</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_B} \ \gg \ 1 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>67.</td>
            <td>\(\texttt{SHRBMEM}\)</td>
            <td>0b01000011</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_B} \
                \gg \ 1
                \quad \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]}
                \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>68.</td>
            <td>\(\texttt{SHLAA}\)</td>
            <td>0b01000100</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_A} \ \ll \ 1 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>69.</td>
            <td>\(\texttt{SHLAB}\)</td>
            <td>0b01000101</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_A} \ \ll \ 1 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>70.</td>
            <td>\(\texttt{SHLAMEM}\)</td>
            <td>0b01000110</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_A} \
                \ll \ 1
                \quad \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]}
                \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>71.</td>
            <td>\(\texttt{SHLBA}\)</td>
            <td>0b01000111</td>
            <td>3</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_B} \ \ll \ 1 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>72.</td>
            <td>\(\texttt{SHLBB}\)</td>
            <td>0b01001000</td>
            <td>3</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_B} \ \ll \ 1 \quad \& \quad \texttt{save flags to }
                \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>73.</td>
            <td>\(\texttt{SHLBMEM}\)</td>
            <td>0b01001001</td>
            <td>9</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br> \(
                \texttt{REG_MBR}
                \leftarrow
                \texttt{REG_B} \
                \ll \ 1
                \quad \& \quad \texttt{save flags to } \texttt{REG_F} \) <br> \( \texttt{MEM[REG_MAR]}
                \leftarrow
                \texttt{REG_MBR} \)
            </td>
        </tr>
        <tr>
            <td>74.</td>
            <td>\(\texttt{CMPAB}\)</td>
            <td>0b01001010</td>
            <td>3</td>
            <td>\(\texttt{calculate} \quad \texttt{REG_A} - \texttt{REG_B} \quad \& \quad \texttt{save flags to
                } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>75.</td>
            <td>\(\texttt{CMPBA}\)</td>
            <td>0b01001011</td>
            <td>3</td>
            <td>\(\texttt{calculate} \quad \texttt{REG_B} - \texttt{REG_A} \quad \& \quad \texttt{save flags to
                } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>76.</td>
            <td>\(\texttt{CMPTHTL}\)</td>
            <td>0b01001100</td>
            <td>5</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_TMPH} \) <br> \( \texttt{REG_B} \leftarrow
                \texttt{REG_TMPL} \) <br> \(\texttt{calculate} \quad
                \texttt{REG_A} - \texttt{REG_B} \quad \& \quad \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>77.</td>
            <td>\(\texttt{CMPTTLTH}\)</td>
            <td>0b01001101</td>
            <td>5</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_TMPL} \) <br> \( \texttt{REG_B} \leftarrow
                \texttt{REG_TMPH} \) <br> \(\texttt{calculate} \quad
                \texttt{REG_A} - \texttt{REG_B} \quad \& \quad \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>78.</td>
            <td>\(\texttt{CMPATH}\)</td>
            <td>0b01001110</td>
            <td>4</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_TMPH} \) <br> \(\texttt{calculate} \quad \texttt{REG_A}
                - \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>79.</td>
            <td>\(\texttt{CMPTHA}\)</td>
            <td>0b01001111</td>
            <td>4</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_TMPH} \) <br> \(\texttt{calculate} \quad \texttt{REG_B}
                - \texttt{REG_A} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>80.</td>
            <td>\(\texttt{CMPATL}\)</td>
            <td>0b01010000</td>
            <td>4</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_TMPL} \) <br> \(\texttt{calculate} \quad \texttt{REG_A}
                - \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>81.</td>
            <td>\(\texttt{CMPTLA}\)</td>
            <td>0b01010001</td>
            <td>4</td>
            <td>\( \texttt{REG_B} \leftarrow \texttt{REG_TMPL} \) <br> \(\texttt{calculate} \quad \texttt{REG_B}
                - \texttt{REG_A} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>82.</td>
            <td>\(\texttt{CMPBTH}\)</td>
            <td>0b01010010</td>
            <td>4</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_TMPH} \) <br> \(\texttt{calculate} \quad \texttt{REG_B}
                - \texttt{REG_A} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>83.</td>
            <td>\(\texttt{CMPTHB}\)</td>
            <td>0b01010011</td>
            <td>4</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_TMPH} \) <br> \(\texttt{calculate} \quad \texttt{REG_A}
                - \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>84.</td>
            <td>\(\texttt{CMPBTL}\)</td>
            <td>0b01010100</td>
            <td>4</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_TMPL} \) <br> \(\texttt{calculate} \quad \texttt{REG_B}
                - \texttt{REG_A} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)</td>
        </tr>
        <tr>
            <td>85.</td>
            <td>\(\texttt{CMPTLB}\)</td>
            <td>0b01010101</td>
            <td>4</td>
            <td>\( \texttt{REG_A} \leftarrow \texttt{REG_TMPL} \) <br> \( \texttt{calculate } \texttt{REG_A}
                - \texttt{REG_B} \quad \& \quad
                \texttt{save flags to } \texttt{REG_F} \)
            </td>
        </tr>
    </tbody>
</table>

<h4>Jump Instructions</h4>
<table class="instruction_table" border="1">
    <thead>
        <tr>
            <th>No.</th>
            <th>Mnemonic</th>
            <th>Opcode</th>
            <th>Total Cycles Number</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>86.</td>
            <td>\(\texttt{JMPIMM}\)</td>
            <td>0b01010110</td>
            <td>7</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]} \quad \& \quad
                \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPL}
                \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \(\texttt{PC} \leftarrow \texttt{REG_TMP} \)</td>
        </tr>
        <tr>
            <td>87.</td>
            <td>\(\texttt{JMPS}\)</td>
            <td>0b01010111</td>
            <td>7 or 4</td>
            <td>\( \texttt{if REG_F[0]} == 1: \) <br> \( \quad \quad \texttt{JMPIMM} \) <br>
                \( \texttt{else}: \) <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
                <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
            </td>
        </tr>
        <tr>
            <td>88.</td>
            <td>\(\texttt{JMPNS}\)</td>
            <td>0b01011000</td>
            <td>7 or 4</td>
            <td>\( \texttt{if REG_F[0]} == 0: \) <br> \( \quad \quad \texttt{JMPIMM} \) <br>
                \( \texttt{else}: \) <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
                <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
            </td>
        </tr>
        <tr>
            <td>89.</td>
            <td>\(\texttt{JMPP}\)</td>
            <td>0b01011001</td>
            <td>7 or 4</td>
            <td>\( \texttt{if REG_F[1]} == 1: \) <br> \( \quad \quad \texttt{JMPIMM} \) <br>
                \( \texttt{else}: \) <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
                <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
            </td>
        </tr>
        <tr>
            <td>90.</td>
            <td>\(\texttt{JMPNP}\)</td>
            <td>0b01011010</td>
            <td>7 or 4</td>
            <td>\( \texttt{if REG_F[1]} == 0: \) <br> \( \quad \quad \texttt{JMPIMM} \) <br>
                \( \texttt{else}: \) <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
                <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
            </td>
        </tr>
        <tr>
            <td>91.</td>
            <td>\(\texttt{JMPZ}\)</td>
            <td>0b01011011</td>
            <td>7 or 4</td>
            <td>\( \texttt{if REG_F[2]} == 1: \) <br> \( \quad \quad \texttt{JMPIMM} \) <br>
                \( \texttt{else}: \) <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
                <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
            </td>
        </tr>
        <tr>
            <td>92.</td>
            <td>\(\texttt{JMPNZ}\)</td>
            <td>0b01011100</td>
            <td>7 or 4</td>
            <td>\( \texttt{if REG_F[2]} == 0: \) <br> \( \quad \quad \texttt{JMPIMM} \) <br>
                \( \texttt{else}: \) <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
                <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
            </td>
        </tr>
        <tr>
            <td>93.</td>
            <td>\(\texttt{JMPC}\)</td>
            <td>0b01011101</td>
            <td>7 or 4</td>
            <td>\( \texttt{if REG_F[3]} == 1: \) <br> \( \quad \quad \texttt{JMPIMM} \) <br>
                \( \texttt{else}: \) <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
                <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
            </td>
        </tr>
        <tr>
            <td>94.</td>
            <td>\(\texttt{JMPNC}\)</td>
            <td>0b01011110</td>
            <td>7 or 4</td>
            <td>\( \texttt{if REG_F[3]} == 0: \) <br> \( \quad \quad \texttt{JMPIMM} \) <br>
                \( \texttt{else}: \) <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
                <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
            </td>
        </tr>
        <tr>
            <td>95.</td>
            <td>\(\texttt{JMPO}\)</td>
            <td>0b01011111</td>
            <td>7 or 4</td>
            <td>\( \texttt{if REG_F[4]} == 1: \) <br> \( \quad \quad \texttt{JMPIMM} \) <br>
                \( \texttt{else}: \) <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
                <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
            </td>
        </tr>
        <tr>
            <td>96.</td>
            <td>\(\texttt{JMPNO}\)</td>
            <td>0b01100000</td>
            <td>7 or 4</td>
            <td>\( \texttt{if REG_F[4]} == 0: \) <br> \( \quad \quad \texttt{JMPIMM} \) <br>
                \( \texttt{else}: \) <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC}+1 \)
                <br> \( \quad \quad \texttt{PC} \leftarrow \texttt{PC+1} \)
            </td>
        </tr>
        <tr>
            <td>97.</td>
            <td>\(\texttt{JMPFUN}\)</td>
            <td>0b01100001</td>
            <td>12</td>
            <td>\( \texttt{REG_TMP} \leftarrow \texttt{PC} \) <br>
                \( \texttt{REG_MAR} \leftarrow \texttt{STC} \quad \& \quad \texttt{REG_MBR} \leftarrow
                \texttt{REG_TMPH} \) <br>
                \( \texttt{MEM[REG_MAR]} \leftarrow \texttt{REG_MBR} \quad \& \quad \texttt{STC} \leftarrow
                \texttt{STC-1} \) <br>
                \( \texttt{REG_MAR} \leftarrow \texttt{STC} \quad \& \quad \texttt{REG_MBR} \leftarrow
                \texttt{REG_TMPL} \) <br>
                \( \texttt{MEM[REG_MAR]} \leftarrow \texttt{REG_MBR} \quad \& \quad \texttt{STC} \leftarrow
                \texttt{STC-1} \) <br>
                \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br>
                \( \texttt{REG_TMPH} \leftarrow \texttt{MEM[MAR]} \quad \& \quad \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br>
                \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br>
                \( \texttt{REG_TMPL} \leftarrow \texttt{MEM[MAR]} \quad \& \quad \texttt{PC} \leftarrow
                \texttt{PC+1} \) <br>
                \( \texttt{PC} \leftarrow \texttt{TMP} \) <br>
            </td>
        </tr>
        <tr>
            <td>98.</td>
            <td>\(\texttt{JMPRET}\)</td>
            <td>0b01100010</td>
            <td>8</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{STC} \) <br>
                \( \texttt{REG_TMPL} \leftarrow \texttt{MEM[MAR]} \quad \& \quad \texttt{STC} \leftarrow
                \texttt{STC+1} \) <br>
                \( \texttt{REG_MAR} \leftarrow \texttt{STC} \) <br>
                \( \texttt{REG_TMPH} \leftarrow \texttt{MEM[MAR]} \quad \& \quad \texttt{STC} \leftarrow
                \texttt{STC+1} \) <br>
                \( \texttt{PC} \leftarrow \texttt{REG_TMP} \) <br>
                \( \texttt{PC} \leftarrow \texttt{PC+1} \)
            </td>
        </tr>
    </tbody>
</table>

<h4>Stack Instructions</h4>
<table class="instruction_table" border="1">
    <thead>
        <tr>
            <th>No.</th>
            <th>Mnemonic</th>
            <th>Opcode</th>
            <th>Total Cycles Number</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>99.</td>
            <td>\(\texttt{PUSHA}\)</td>
            <td>0b01100011</td>
            <td>4</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{STC} \quad \& \quad \texttt{REG_MBR} \leftarrow
                \texttt{REG_A} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow \texttt{REG_MBR} \quad \& \quad
                \texttt{STC} \leftarrow
                \texttt{STC-1} \)
            </td>
        </tr>
        <tr>
            <td>100.</td>
            <td>\(\texttt{PUSHB}\)</td>
            <td>0b01100100</td>
            <td>4</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{STC} \quad \& \quad \texttt{REG_MBR} \leftarrow
                \texttt{REG_B} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow \texttt{REG_MBR} \quad \& \quad
                \texttt{STC} \leftarrow
                \texttt{STC-1} \)
            </td>
        </tr>
        <tr>
            <td>101.</td>
            <td>\(\texttt{PUSHTH}\)</td>
            <td>0b01100101</td>
            <td>4</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{STC} \quad \& \quad \texttt{REG_MBR} \leftarrow
                \texttt{REG_TMPH} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow \texttt{REG_MBR} \quad \& \quad
                \texttt{STC} \leftarrow
                \texttt{STC-1} \)
            </td>
        </tr>
        <tr>
            <td>102.</td>
            <td>\(\texttt{PUSHTL}\)</td>
            <td>0b01100110</td>
            <td>4</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{STC} \quad \& \quad \texttt{REG_MBR} \leftarrow
                \texttt{REG_TMPL} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow \texttt{REG_MBR} \quad \& \quad
                \texttt{STC} \leftarrow
                \texttt{STC-1} \)
            </td>
        </tr>
        <tr>
            <td>103.</td>
            <td>\(\texttt{PUSHIMM}\)</td>
            <td>0b01100111</td>
            <td>6</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_MBR} \leftarrow
                \texttt{MEM[REG_MAR]} \quad \& \quad \texttt{PC} \leftarrow \texttt{PC+1} \) <br>
                \( \texttt{REG_MAR} \leftarrow \texttt{STC} \) <br> \( \texttt{MEM[REG_MAR]} \leftarrow
                \texttt{REG_MBR} \quad \& \quad
                \texttt{STC} \leftarrow
                \texttt{STC-1} \)</td>
        </tr>
        <tr>
            <td>104.</td>
            <td>\(\texttt{PUSHABS}\)</td>
            <td>0b01101000</td>
            <td>10</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \(
                \texttt{REG_TMPL}
                \leftarrow \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC} \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow
                \texttt{REG_TMP} \)
                <br> \( \texttt{REG_MBR}
                \leftarrow \texttt{MEM[REG_MAR]} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{STC} \) <br>
                \( \texttt{MEM[REG_MAR]} \leftarrow \texttt{REG_MBR} \quad \& \quad
                \texttt{STC} \leftarrow
                \texttt{STC-1} \)
            </td>
        </tr>
        <tr>
            <td>105.</td>
            <td>\(\texttt{POPA}\)</td>
            <td>0b01101001</td>
            <td>4</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{STC} \) <br> \(\texttt{REG_A} \leftarrow
                \texttt{MEM[REG_MAR]} \quad \& \quad
                \texttt{STC} \leftarrow
                \texttt{STC+1} \)
            </td>
        </tr>
        <tr>
            <td>106.</td>
            <td>\(\texttt{POPB}\)</td>
            <td>0b01101010</td>
            <td>4</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{STC} \) <br> \(\texttt{REG_B} \leftarrow
                \texttt{MEM[REG_MAR]} \quad \& \quad
                \texttt{STC} \leftarrow
                \texttt{STC+1} \)
            </td>
        </tr>
        <tr>
            <td>107.</td>
            <td>\(\texttt{POPTH}\)</td>
            <td>0b01101011</td>
            <td>4</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{STC} \) <br> \(\texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]} \quad \& \quad
                \texttt{STC} \leftarrow
                \texttt{STC+1} \)
            </td>
        </tr>
        <tr>
            <td>108.</td>
            <td>\(\texttt{POPTL}\)</td>
            <td>0b01101100</td>
            <td>4</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{STC} \) <br> \(\texttt{REG_TMPL} \leftarrow
                \texttt{MEM[REG_MAR]} \quad \& \quad
                \texttt{STC} \leftarrow
                \texttt{STC+1} \)
            </td>
        </tr>
        <tr>
            <td>109.</td>
            <td>\(\texttt{POPMEM}\)</td>
            <td>0b01101101</td>
            <td>10</td>
            <td>\( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \( \texttt{REG_TMPH} \leftarrow
                \texttt{MEM[REG_MAR]}
                \quad \&
                \quad
                \texttt{PC}
                \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{PC} \) <br> \(
                \texttt{REG_TMPL}
                \leftarrow \texttt{MEM[REG_MAR]}
                \quad \& \quad \texttt{PC} \leftarrow \texttt{PC+1} \) <br> \( \texttt{REG_MAR} \leftarrow
                \texttt{STC} \)
                <br> \( \texttt{REG_MBR}
                \leftarrow \texttt{MEM[REG_MAR]} \) <br> \( \texttt{REG_MAR} \leftarrow \texttt{REG_TMP} \) <br>
                \( \texttt{MEM[REG_MAR]} \leftarrow \texttt{REG_MBR} \quad \& \quad
                \texttt{STC} \leftarrow
                \texttt{STC+1} \)
            </td>
        </tr>
    </tbody>
</table>

<h4>Other Instructions</h4>
<table class="instruction_table" border="1">
    <thead>
        <tr>
            <th>No.</th>
            <th>Mnemonic</th>
            <th>Opcode</th>
            <th>Total Cycles Number</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>110.</td>
            <td>\( \texttt{NOP} \)</td>
            <td>0b00000000</td>
            <td>3</td>
            <td>\(\texttt{do nothing for 1 cycle} \)</td>
        </tr>
        <tr>
            <td>111.</td>
            <td>\( \texttt{SKIP} \)</td>
            <td>0b11111110</td>
            <td>2</td>
            <td>\(\texttt{go to the next instruction} \)</td>
        </tr>
        <tr>
            <td>112.</td>
            <td>\( \texttt{HALT} \)</td>
            <td>0b11111111</td>
            <td>2</td>
            <td>\(\texttt{don't go to the next instruction} \)</td>
        </tr>
    </tbody>
</table>
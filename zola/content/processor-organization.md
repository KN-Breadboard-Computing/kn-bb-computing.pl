+++
template = "processor-organization.html"
+++

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
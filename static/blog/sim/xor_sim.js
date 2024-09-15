import { bitCell, xorGate, connectNodeToNode, processCircuit } from "../sim.js";

const inputA = bitCell(true);
const inputB = bitCell(true);
const output = bitCell(false);
const gate = xorGate();
const netA = connectNodeToNode(inputA, 0, gate, 0);
const netB = connectNodeToNode(inputB, 0, gate, 1);
const netC = connectNodeToNode(gate, 0, output, 0);

/**
 * This functions should take the current state of the circuit and redraw it entirely
 * @param {CanvasRenderingContext2D} ctx
 */
function redrawCircuit(ctx) {
  ctx.save();
  ctx.clearRect(0, 0, 500, 500);

  ctx.strokeStyle = "black";
  ctx.lineWidth = 4;

  ctx.beginWireNet(30, 30, netA.state);
  ctx.lineTo(80, 30);
  ctx.endWireNet();

  ctx.drawGreenDiode(30, 30, inputA.state);

  ctx.beginWireNet(30, 60, netB.state);
  ctx.lineTo(80, 60);
  ctx.endWireNet();

  ctx.drawGreenDiode(30, 60, inputB.state);

  ctx.beginWireNet(140, 45, netC.state);
  ctx.lineTo(180, 45);
  ctx.endWireNet();

  ctx.drawGreenDiode(180, 45, output.state);

  ctx.drawXorGate(70, 15);

  ctx.restore();
}

const circuitWidth = 210;
const circuitHeight = 90;

function resize(container, canvas, ctx) {
  const actualWidth = container.offsetWidth;
  const scale = actualWidth / circuitWidth;

  canvas.width = actualWidth;
  canvas.height = scale * circuitHeight;

  ctx.scale(scale, scale);
}

function draw() {
  const canvas = document.getElementById("xor_example");
  const container = document.getElementById("xor_example_wrapper");
  if (canvas.getContext) {
    /** @type {CanvasRenderingContext2D} */
    const ctx = canvas.getContext("2d");
    
    resize(container, canvas, ctx);
    window.addEventListener('resize', (event) => { resize(container, canvas, ctx); redrawCircuit(ctx); });

    processCircuit([inputA, inputB]);
    redrawCircuit(ctx);

    const buttonInputA = document.getElementById("xor_example_input_a");
    buttonInputA.addEventListener("click", (event) => {
      inputA.state = !inputA.state;
      processCircuit([inputA]);
      redrawCircuit(ctx);
    });

    const buttonInputB = document.getElementById("xor_example_input_b");
    buttonInputB.addEventListener("click", (event) => {
      inputB.state = !inputB.state;
      processCircuit([inputB]);
      redrawCircuit(ctx);
    });
  }
}

window.addEventListener("load", draw);

// Gates have dimensions 70x60

const andGatePath = new Path2D(
  "m 0,60 c 15,0 30,0 45,0 15,0 25,-15 25,-30 C 70,15 60,0 45,0 30,0 15,0 0,0 Z"
);
CanvasRenderingContext2D.prototype.drawAndGate = function (x, y) {
  this.save();
  this.translate(x, y);
  this.fillStyle = 'white';
  this.strokeStyle = 'black';
  this.fill(andGatePath);
  this.stroke(andGatePath);
  this.restore();
};

const orGatePath = new Path2D(
  "M 45,60 C 60,60 70,30 70,30 c 0,0 -10,-30 -25,-30 L 0,0 C 5,10 10,20 10,30 10,40 5,50 0,60 Z"
);
CanvasRenderingContext2D.prototype.drawOrGate = function (x, y) {
  this.save();
  this.translate(x, y);
  this.fillStyle = 'white';
  this.strokeStyle = 'black';
  this.fill(orGatePath)
  this.stroke(orGatePath);
  this.restore();
};

const xorGatePath = new Path2D(
  "m 45,60 c 15,0 25,-30 25,-30 0,0 -10,-30 -25,-30 L 0,0 c 5,10 10,20 10,30 0,10 -5,20 -10,30 z"
);
const xorGatePathLine = new Path2D(
  "M -10,0 C -10,0 0,15 0,30 c 0,15 -10,30 -10,30"
)
CanvasRenderingContext2D.prototype.drawXorGate = function (x, y) {
  this.save();
  this.translate(x, y);
  this.fillStyle = 'white';
  this.strokeStyle = 'black';
  this.fill(xorGatePath)
  this.stroke(xorGatePath);
  this.stroke(xorGatePathLine);
  this.restore();
};

CanvasRenderingContext2D.prototype.drawDiode = function (x, y, color) {
  this.save();
  this.fillStyle = color;
  this.beginPath();
  this.arc(x, y, 10, 0, 180);
  this.fill();
  this.restore();
};

CanvasRenderingContext2D.prototype.drawGreenDiode = function (x, y, state) {
  if (state) {
    this.drawDiode(x, y, "lime");
  } else {
    this.drawDiode(x, y, "darkgreen");
  }
};

CanvasRenderingContext2D.prototype.beginWireNet = function (x, y, state) {
  this.save();
  this.beginPath();
  this.strokeStyle = state ? "green" : "black";
  this.moveTo(x, y);
};

CanvasRenderingContext2D.prototype.endWireNet = function () {
  this.stroke();
  this.restore();
};

export function net() {
  return {
    in: [],
    out: [],
    state: false,
  };
}

export function emptyNode() {
  return {
    in: [],
    out: [],
    simulate: function (input, output) {},
  };
}

export function andGate() {
  const node = emptyNode();
  node.simulate = function (input, output) {
    for (const val of input) {
      if (!val) {
        output.fill(false);
        return;
      }
    }
    output.fill(true);
  };
  return node;
}

export function orGate() {
  const node = emptyNode();
  node.simulate = function (input, output) {
    for (const val of input) {
      if (val) {
        output.fill(true);
        return;
      }
    }
    output.fill(false);
  };
  return node;
}

export function xorGate() {
  const node = emptyNode();
  node.simulate = function (input, output) {
    let count = 0;
    for (const val of input) {
      if (val) {
        count++;
      }
    }
    if (count % 2 == 0) {
      output.fill(false);
    } else {
      output.fill(true);
    }
  };
  return node;
}

export function bitCell(initState) {
  const node = emptyNode();
  node.state = initState;
  node.simulate = function (input, output) {
    if (input[0] === true || input[0] === false) {
      this.state = input[0];
    }
    output.fill(this.state);
  };
  return node;
}

export function connectNetToNode(net, node, inSlot) {
  net.out.push(node);
  node.in[inSlot] = net;
}

export function connectNodeToNet(node, outSlot, net) {
  node.out[outSlot] = net;
  net.in.push(node);
}

export function connectNodeToNode(outNode, outSlot, inNode, inSlot) {
  const intNet = net();
  connectNodeToNet(outNode, outSlot, intNet);
  connectNetToNode(intNet, inNode, inSlot);
  return intNet;
}

export function processCircuit(nodes) {
  const eventQueue = [];
  const nodesSet = new Set(nodes);

  do {
    for (const event of eventQueue) {
      event.net.state = event.value;

      for (const outNode of event.net.out) {
        nodesSet.add(outNode);
      }
    }
    eventQueue.length = 0;

    for (const node of nodesSet) {
      let input = node.in.map((inNet) => inNet.state);
      let output = node.out.map((outNet) => outNet.state);

      node.simulate(input, output);

      for (let i = 0; i < output.length; i++) {
        const outNet = node.out[i];
        if (outNet.state != output[i]) {
          eventQueue.push({ net: outNet, value: output[i] });
        }
      }
    }
    nodesSet.clear();
  } while (eventQueue.length != 0);
}
